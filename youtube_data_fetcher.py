# Step 1: Data Collection
# This code is for Step 1 of the project as described in the README.md

import os # required in this script for the file and directory operations
from dotenv import load_dotenv # required for loading environment variables
import pandas as pd # required for reading data from keywords.csv
from googleapiclient.discovery import build # it provides a build function to create a service object for interacting with the YouTube Data API v3.
import json # required for JSON data handling
from datetime import datetime # required for storing the date and time of the data fetching
import time # required for waiting between requests
import isodate # required for parsing ISO 8601 formatted dates
import logging # required for logging messages

"""
YouTube Data Fetcher

This script fetches video data from YouTube using the YouTube Data API v3.
It processes keywords from a CSV file.
"""

# Load environment variables from .env file in which store the API key as:
# YOUTUBE_API_KEY=YOUR_API_KEY
load_dotenv()

# Set up logging to track script execution and debug issues
logging.basicConfig(
    level=logging.INFO, # set logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s' # format log messages
)

# API configuration
API_KEY = os.getenv('YOUTUBE_API_KEY') # get API key from environment variables
if not API_KEY:
    raise ValueError("YouTube API key not found in environment variables") # raise an error if API key is not found

# Define budget quota for YouTube API
QUOTA = {
    'search': 100,    # 100 search requests per day
    'videos': 1       # Get details for 1 video
}
DAILY_QUOTA_LIMIT = 10000  # Maximum daily budget
VIDEOS_PER_KEYWORD = 50    # Number of videos to fetch per keyword
DATA_DIR = 'youtube_data'  # Directory to store results
STATE_FILE = 'fetch_state.json'  # File to track progress as the script has to be run multiple times

class YouTubeDataFetcher:
    """
    Class to handle YouTube data fetching operations.
    With a state file to track progress as the script has to be run multiple times

    """

    def __init__(self):
        """
        Initializes the YouTube API client, sets up necessary directories, and 
        loads the script’s state from a JSON file to track progress across multiple runs.

        """
        try:
            self.youtube = build('youtube', 'v3', developerKey=API_KEY)
            self.quota_used = 0
            self.ensure_directories()
            self.state = self.load_state()
            logging.info("YouTubeDataFetcher initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing YouTubeDataFetcher: {str(e)}")
            raise

    def can_make_request(self, cost):
        """
        Check if we have enough quota to make a request.
        Like checking if you have enough money in your account before making a purchase:
        current_balance = 100
        purchase_cost = 50
        can_buy = current_balance >= purchase_cost  # True
        """
        return (self.quota_used + cost) <= DAILY_QUOTA_LIMIT

    def ensure_directories(self):
        """
        Create necessary directories if they don't exist to store the fetched data.
        """
        try:
            os.makedirs(DATA_DIR, exist_ok=True)
            logging.info(f"Created/verified directory: {DATA_DIR}")
        except Exception as e:
            logging.error(f"Error creating directory: {str(e)}")
            raise

    def load_state(self):
        """
        Loads the current state from fetch_state.json, allowing the script to resume progress in subsequent runs.
        """
        try:
            if os.path.exists(STATE_FILE):
                with open(STATE_FILE, 'r') as f:
                    state = json.load(f)
                logging.info("State file loaded successfully")
                return state
            logging.info("No existing state file found, creating new state")
            return {
                'last_update': None,
                'processed_keywords': {}
            }
        except Exception as e:
            logging.error(f"Error loading state: {str(e)}")
            raise

    def save_state(self):
        """
        Saves the current state to fetch_state.json to track progress across multiple runs.
        """
        try:
            with open(STATE_FILE, 'w') as f:
                json.dump(self.state, f, indent=2)
            logging.info("State saved successfully")
        except Exception as e:
            logging.error(f"Error saving state: {str(e)}")
            raise

    def fetch_videos_for_keyword(self, keyword, category):
        """
        Fetches video data for a given keyword and category. 
        It performs a search request to obtain video IDs and then retrieves detailed information for each video, 
        such as title, publication date, duration, view count, like count, and comment count.
        """
        if not self.can_make_request(QUOTA['search']):
            logging.warning("Daily quota limit reached")
            return None
        
        try:
            # Search for videos
            logging.info(f"Searching videos for keyword: {keyword}")
            search_response = self.youtube.search().list(
                q=keyword,
                part='id',
                type='video',
                maxResults=VIDEOS_PER_KEYWORD,
                order='relevance'
            ).execute()
            
            self.quota_used += QUOTA['search']
            
            # Extract video IDs 
            video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]
            
            if not video_ids:
                logging.warning(f"No videos found for keyword: {keyword}")
                return None
            
            # Get detailed information about each video
            videos_response = self.youtube.videos().list(
                id=','.join(video_ids),
                part='snippet,statistics,contentDetails'
            ).execute()
            
            self.quota_used += len(video_ids) * QUOTA['videos']
            
            # Process each video's data
            videos_data = []
            for video in videos_response.get('items', []):
                try:
                    duration = isodate.parse_duration(video['contentDetails']['duration']).total_seconds()
                    
                    video_data = {
                        'keyword': keyword,
                        'category': category,
                        'video_id': video['id'],
                        'title': video['snippet']['title'],
                        'published_date': video['snippet']['publishedAt'],
                        'duration_seconds': duration,
                        'view_count': int(video['statistics'].get('viewCount', 0)),
                        'like_count': int(video['statistics'].get('likeCount', 0)),
                        'comment_count': int(video['statistics'].get('commentCount', 0))
                    }
                    videos_data.append(video_data)
                except Exception as e:
                    logging.error(f"Error processing video {video.get('id', 'unknown')}: {str(e)}")
                    continue
            
            return videos_data
            
        except Exception as e:
            logging.error(f"Error fetching videos for keyword '{keyword}': {str(e)}")
            return None

    def process_keywords(self):
        """
        Reads keywords from keywords.csv, processes each keyword to fetch corresponding video data, and 
        saves the data to a CSV file in the specified data directory. 
        It also updates the state to keep track of processed keywords and ensures the script operates within the API quota limits.
        """
        try:
            keywords_df = pd.read_csv('keywords.csv')
            
            # Set up or load existing data file
            main_data_file = os.path.join(DATA_DIR, 'all_videos_data.csv')
            all_data = pd.DataFrame()
            if os.path.exists(main_data_file):
                all_data = pd.read_csv(main_data_file)
            
            # Process each keyword
            for _, row in keywords_df.iterrows():
                keyword = row['keyword']
                category = row['group']
                
                # Skip if already processed 
                if keyword in self.state['processed_keywords']:
                    continue
                
                # Check quota before proceeding
                if not self.can_make_request(QUOTA['search']):
                    break
                
                # Fetch and save data
                videos_data = self.fetch_videos_for_keyword(keyword, category)
                if videos_data:
                    new_data = pd.DataFrame(videos_data)
                    all_data = pd.concat([all_data, new_data], ignore_index=True)
                    all_data.to_csv(main_data_file, index=False)
                    
                    # Update progress
                    self.state['processed_keywords'][keyword] = {
                        'processed_date': datetime.now().isoformat(),
                        'videos_count': len(videos_data)
                    }
                    self.save_state()
                
                # Wait between requests
                time.sleep(1)
            
            return all_data
            
        except Exception as e:
            logging.error(f"Error in process_keywords: {str(e)}")
            raise

def main():
    """
    Main execution function.
    - Logging the start of the process.
    - Creating an instance of YouTubeDataFetcher.
    - Calling process_keywords() to fetch and save video data.
    - Logging the completion of data collection and the total number of videos collected.
    """
    try:
        logging.info("Starting YouTube data fetching process")
        fetcher = YouTubeDataFetcher()
        data = fetcher.process_keywords()
        logging.info("Data collection complete!")
        logging.info(f"Total videos collected: {len(data) if data is not None else 0}")
    except Exception as e:
        logging.error(f"Error in main: {str(e)}")
        raise

if __name__ == "__main__":
    main() 