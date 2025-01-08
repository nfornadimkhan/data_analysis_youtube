# YouTube Data Analysis Project
This project is an analysis of YouTube (Global) data to understand the trends of plant breeding related **8,971 videos** with **2.1 billion views** for **198 keywords** in **3 categories of concepts** (Old, Current, Modern) (**English** language only).

## Problem Statement
There are many SEO tools available to analyze the trends of keywords. But not efficient to analyze the trends on broader horizon with simultaneous analysis of multiple categories of keywords with interaction of audience. 
I want to analyze the trends on broader horizon utilizing the knowledge of Python and YouTube Data API. As a student of Crop Science (Plant Breeding and Seed Science) together with my group memeber, Samaneh Javidian, we wanted to analyze following things:
   1. Understanding the trends on broader horizon and impact of plant breeding research overtime, 
   2. Analyzing how the audience on YouTube interact with plant breeding related videos as per 3 categories of concepts.
   3. Analyzing the content gap in plant breeding related videos. 
   4. Identifying emerging topics and assessing future directions in plant breeding research.

## Methodology
- Collect data from YouTube using the [YouTube API](https://developers.google.com/youtube/v3) based on specific plant breeding keywords.
- Save the data categorized in **3 categories** in a structured format in csv file for further analysis. Following data is saved:
  - Keyword: 66 keywords in each category (total 66 x 3 = **198 keywords**).
  - Category: Old, Current, Modern
  - Video ID
  - Video Title
  - Published Date
  - Duration of the video
  - View Count
  - Like Count
  - Comment Count
- Analyze the collected data to determine trends in viewership and engagement.

## Technologies Used
- **API and Data Handling:**
  - YouTube Data API v3
  - Python libraries: `pandas`, `numpy`, `
- **Visualization and Analysis:**
  - `matplotlib`, `seaborn`, `plotly`, `tabulate`
- **Machine Learning and NLP:**
  - `NLTK`, `BERT`
- **Data Storage and Preprocessing:**
  - CSV for structured data storage


## Keyword Classification
Here we try to use an analytical approach to classify keywords into 3 categories with the help of historical relevance, technological advancement, and future research trends in plant breeding.

**1. Old (Traditional Methods):**
Keywords in the Old category were derived from practices dominant before the 20th century, emphasizing phenotype-based selection and indigenous approaches.
- These keywords are rooted in the practices before the advent of molecular biology.
- Focuses on phenotypic selection, landrace improvement, and methods relying heavily on field observation and generational improvement.
- Emphasizes low-technology, empirical, and community-based methods.

**2. Current (Established/Conventional Methods):**
Keywords in the Current category represent methods broadly adopted in the late 20th century and still in use today, often integrating molecular biology for improved efficiency.
- Represent technologies widely used today, incorporating molecular biology but not the most advanced techniques.
- Includes marker-assisted selection (MAS), QTL mapping, and heterosis exploitation.
- These methods aim to balance efficiency and accessibility for commercial and academic breeding.

**3. Modern (Cutting-Edge/Future Methods):**
Keywords in the Modern category highlight cutting-edge and emerging areas driven by computational biology, AI, and genomics.
- Reflect cutting-edge technologies that use computational tools, CRISPR, and omics sciences.
- These methods are either newly implemented or have potential for future adoption.
- Focuses on precision, automation, and integrating bioinformatics for decision-making.

## Keywords
### **Old Plant Breeding (66 Keywords)**  
1. Traditional selective breeding in plant breeding  
2. Landrace selection in plant breeding  
3. Phenotypic selection in plant breeding  
4. Pedigree breeding in plant breeding  
5. Mass selection in plant breeding  
6. Clonal selection in plant breeding  
7. Family selection in plant breeding  
8. Open pollination in plant breeding  
9. Hybridization techniques in plant breeding  
10. Genetic diversity preservation in plant breeding  
11. Crop domestication in plant breeding  
12. Traditional farmer selection in plant breeding  
13. Indigenous breeding methods in plant breeding  
14. Germplasm conservation in plant breeding  
15. Heritage crop breeding in plant breeding  
16. Regional adaptation breeding in plant breeding  
17. Cross-pollination techniques in plant breeding  
18. Seed saving practices in plant breeding  
19. Ancestral crop improvement in plant breeding  
20. Wild relative breeding in plant breeding  
21. Traditional varietal selection in plant breeding  
22. Local adaptation breeding in plant breeding  
23. Empirical crop selection in plant breeding  
24. Population improvement in plant breeding  
25. Traditional genetic diversity in plant breeding  
26. Manual trait selection in plant breeding  
27. Phenotype-based breeding in plant breeding  
28. Generational crop improvement in plant breeding  
29. Agronomic performance selection in plant breeding  
30. Community-based breeding in plant breeding  
31. Geographic adaptation in plant breeding  
32. Reproductive isolation techniques in plant breeding  
33. Evolutionary breeding approaches in plant breeding
34. Reciprocal recurrent selection in plant breeding
35. Line breeding in plant breeding
36. Composite crossing in plant breeding
37. Mass-pedigree method in plant breeding
38. Diallel crossing in plant breeding
39. Synthetic variety breeding in plant breeding
40. Bulk population method in plant breeding
41. Traditional crop rotation effects in plant breeding
42. Monoculture improvement in plant breeding
43. Natural trait segregation in plant breeding
44. Seedbed selection in plant breeding
45. Pure-line selection in plant breeding
46. Hardy-Weinberg principle in plant breeding
47. Traditional soil suitability tests in plant breeding
48. Indigenous pest resistance breeding in plant breeding
49. Farmer-participatory breeding in plant breeding
50. In situ conservation breeding in plant breeding
51. Traditional field trials in plant breeding
52. Manual self-pollination techniques in plant breeding
53. Natural outcrossing studies in plant breeding
54. Selective pressure analysis in plant breeding
55. Regional cropping system adaptation in plant breeding
56. Propagation techniques in plant breeding
57. Ancient grain breeding in plant breeding
58. Local seed exchange practices in plant breeding
59. Historical agronomic practices in plant breeding
60. Subsistence crop breeding in plant breeding
61. Folk selection methods in plant breeding
62. Landrace improvement cycles in plant breeding
63. Regional biotic stress breeding in plant breeding
64. Crop resilience through generations in plant breeding
65. Traditional soil fertility management in plant breeding
66. Traditional drought tolerance breeding in plant breeding


---

### **Current (Established/Conventional) Plant Breeding (66 Keywords)**  
1. Marker-assisted selection in plant breeding  
2. Quantitative trait loci (QTL) mapping in plant breeding  
3. Hybrid vigor breeding in plant breeding  
4. Backcross breeding in plant breeding  
5. Recurrent selection in plant breeding  
6. Multiline breeding in plant breeding  
7. Heterosis breeding in plant breeding  
8. Advanced generation breeding in plant breeding  
9. Genome-wide selection in plant breeding  
10. Phenotypic screening in plant breeding  
11. Molecular marker development in plant breeding  
12. Genetic diversity analysis in plant breeding  
13. Performance testing in plant breeding  
14. Trait introgression in plant breeding  
15. Advanced breeding lines in plant breeding  
16. Genetic variability assessment in plant breeding  
17. Progeny testing in plant breeding  
18. Breeding value estimation in plant breeding  
19. Population genetics in plant breeding  
20. Crop improvement strategies in plant breeding  
21. Genetic gain prediction in plant breeding  
22. Breeding program design in plant breeding  
23. Genetic uniformity in plant breeding  
24. Controlled pollination in plant breeding  
25. Genetic resource management in plant breeding  
26. Phenotypic plasticity in plant breeding  
27. Breeding efficiency in plant breeding  
28. Genetic complexity analysis in plant breeding  
29. Reproductive biology in plant breeding  
30. Crop adaptation mechanisms in plant breeding  
31. Statistical genetics in plant breeding  
32. Breeding methodology optimization in plant breeding
33. Classical resistance breeding in plant breeding
34. Genomic in situ hybridization (GISH) in plant breeding
35. Haploidy induction in plant breeding
36. Bi-parental mapping populations in plant breeding
37. Multi-parental breeding approaches in plant breeding
38. Doubled haploid technology in plant breeding
39. Epistasis analysis in plant breeding
40. Trait stacking in plant breeding
41. Transcriptomics in plant breeding
42. Isozyme markers in plant breeding
43. Breeding for disease resistance in plant breeding
44. DArT marker technology in plant breeding
45. AFLP marker systems in plant breeding
46. SNP genotyping in plant breeding
47. Biochemical marker-assisted breeding in plant breeding
48. Marker-based recurrent selection in plant breeding
49. Breeding for yield stability in plant breeding
50. Abiotic stress tolerance breeding in plant breeding
51. Pre-breeding programs in plant breeding
52. Crop modeling integration in plant breeding
53. Germplasm enhancement in plant breeding
54. Controlled environment breeding in plant breeding
55. Speed breeding protocols in plant breeding
56. High-yield variety development in plant breeding
57. Disease-resistance introgression in plant breeding
58. Fusarium wilt tolerance breeding in plant breeding
59. High-oil content breeding in plant breeding
60. MABC (Marker-Assisted Backcrossing) in plant breeding
61. Field trial optimization in plant breeding
62. Regional trait evaluation in plant breeding
63. Statistical QTL analysis in plant breeding
64. Breeding for micronutrient density in plant breeding
65. Controlled hybrid seed production in plant breeding
66. Genotypic adaptability analysis in plant breeding

---

### **Modern (Cutting-Edge) Plant Breeding (66 Keywords)**  
1. CRISPR gene editing in plant breeding  
2. Genome sequencing in plant breeding  
3. Precision breeding in plant breeding  
4. Synthetic biology in plant breeding  
5. Gene network analysis in plant breeding  
6. Metabolic engineering in plant breeding  
7. Transgenic development in plant breeding  
8. Next-generation sequencing in plant breeding  
9. Epigenetic modification in plant breeding  
10. Machine learning in plant breeding  
11. Artificial intelligence prediction in plant breeding  
12. RNA interference in plant breeding  
13. Genome editing techniques in plant breeding  
14. Advanced phenotyping in plant breeding  
15. Computational breeding in plant breeding  
16. Genomic selection in plant breeding  
17. Metabolomics in plant breeding  
18. Proteomics applications in plant breeding  
19. Systems biology in plant breeding  
20. Nano-biotechnology in plant breeding  
21. Digital phenotyping in plant breeding  
22. Advanced genetic transformation in plant breeding  
23. Molecular breeding platforms in plant breeding  
24. Genome-wide association studies in plant breeding  
25. Synthetic genomics in plant breeding  
26. Predictive breeding models in plant breeding  
27. High-throughput screening in plant breeding  
28. Gene regulatory network in plant breeding  
29. Advanced trait mapping in plant breeding  
30. Computational genomics in plant breeding  
31. Climate-resilient breeding in plant breeding  
32. Precision agriculture technologies in plant breeding  
33. Adaptive breeding strategies in plant breeding
34. CRISPR-Cas9 delivery systems in plant breeding
35. Pangenomics in plant breeding
36. Hologenomics in plant breeding
37. Digital twin modeling in plant breeding
38. Epigenome-wide association studies in plant breeding
39. Single-cell sequencing in plant breeding
40. Multi-omics integration in plant breeding
41. Deep learning for trait prediction in plant breeding
42. Blockchain for seed traceability in plant breeding
43. Sensor-based phenotyping in plant breeding
44. Quantum computing in plant breeding
45. Virtual reality applications in plant breeding
46. Synthetic promoter engineering in plant breeding
47. Biostimulant-driven breeding in plant breeding
48. Photosynthetic efficiency optimization in plant breeding
49. AI-based genome annotation in plant breeding
50. Cellular reprogramming in plant breeding
51. Carbon sequestration traits breeding in plant breeding
52. Eco-genomics in plant breeding
53. Functional metagenomics in plant breeding
54. Robotic phenotyping in plant breeding
55. Non-coding RNA studies in plant breeding
56. Microbiome-assisted breeding in plant breeding
57. Advanced chloroplast transformation in plant breeding
58. Pathogenomics applications in plant breeding
59. Environmental DNA (eDNA) in plant breeding
60. Autonomous breeding programs in plant breeding
61. Thermo-tolerance breeding in plant breeding
62. Urban crop development in plant breeding
63. Biodegradable agro-inputs breeding in plant breeding
64. Real-time molecular diagnostics in plant breeding
65. Holistic systems breeding in plant breeding
66. Predictive climate modeling in plant breeding


# Steps Followed
## Step 1: Data Collection
- Get a YouTube Data API v3 key. This allowed us to programmatically access YouTube data.
- Search Queries: Using above described keyword lists (keywords_old, keywords_current, keywords_modern) to construct search queries. It's crucial to refine these queries to be as specific as possible. For example, instead of just "Mass selection," try "mass selection in plant breeding" to get more relevant results. 

The problem with YouTube Data API is that it has a search quota limit of `10000 per day`. Therefore, we have to run the script multiple times to get all the data. For this, we implemented a state file to track the progress of the script each time it is run. This file is stored in the youtube_data directory. Each time the script is run, it checks the state file to see if the data for the current keyword has already been fetched. If it has, it skips the keyword. If it hasn't, it fetches the data for the current keyword. This way, we can continue from where we left off and avoid fetching the same data multiple times. 

In this way, we fetched 50 videos for each keyword, which is 50 x 66 x 3 = **9900 videos**. 
Why only 50 videos? 🤔 Because more than this we find that we mostly get irrelevant videos. As we are analyzing education content, for which videos are not that much available on YouTube.

Search request: 100 quota units
Video details: 1 quota unit per video × 50 videos = 50 quota units
Total per keyword: 100 + 50 = 150 quota units

Max keywords = DAILY_QUOTA_LIMIT / quota_per_keyword
Max keywords = 10000 / 150 ≈ 66 keywords per day

Max videos = 66 × 50 = 3,300 videos per day
Days needed = Total keywords / Max keywords per day
Days needed = 198 / 66 = 3 days

Therefore, we need to run the script 3 times to get all the data related to all 198 keywords stated in the keywords.csv file and store the data in the youtube_data/all_videos_data.csv file.


Used following resources to manage API request quotas:
- https://thepythoncode.com/article/using-youtube-api-in-python
- https://peerdh.com/blogs/programming-insights/managing-api-request-quotas-in-python?utm_source=chatgpt.com
- https://www.youtube.com/watch?v=TIZRskDMyA4
- https://realpython.com/api-integration-in-python/


## Step 2: Data Cleaning & Preprocessing
- Remove duplicate entries to ensure data quality
- Convert published_date to datetime format
- Remove 'Z' suffix and convert to pandas datetime format. e.g. 2016-09-29T22:39:48Z
- Converted relevant columns to numeric format for analysis
  - duration_seconds: Video length in seconds
  - view_count: Number of views
  - like_count: Number of likes
  - comment_count: Number of comments
- Added human-readable duration format for better interpretation
- Removed extra whitespace and standardized titles
- Created engagement rate metric: Formula: (likes + comments) / views * 100 As inspired from the [article](https://www.storyly.io/post/how-to-calculate-engagement-rate)
- Removed rows with all missing values to ensure data quality
- Sorted data by category and keyword for better analysis
- Saved cleaned dataset for further analysis

## Step 3: Solution for the problem of Irrelevant Videos
We recognized that our data contains some videos that are not at all related to the plant breeding concepts even after the above mentioned data cleaning & preprocessing. This was a big trouble. 😞
This let us to look for the solutions beyong the scope of the project.
Therefore, we implemented a solution to remove the irrelevant videos from our data by using the following libraries:
- **nltk:** For natural language processing (e.g., tokenizing words in text).
- **sentence-transformers:** For encoding sentences into vector representations using BERT.
- **sklearn:** For calculating cosine similarity between vectors.

Inspired by these sources:
- https://www.restack.io/p/similarity-search-answer-relevance-scores-cat-ai?utm_source=chatgpt.com
- https://www.33rdsquare.com/four-of-the-easiest-and-most-effective-methods-of-keyword-extraction-from-a-single-text-using-python/?utm_source=chatgpt.com
- https://www.analyticsvidhya.com/blog/2022/08/movies-recommendation-system-using-python/?utm_source=chatgpt.com

To assess how relevant each video is to a given keyword and filter out irrelevant videos. The solution uses both basic text matching and advanced semantic similarity (cosine similarity) to calculate a “relevance score” for each video. 
1.	Relevance Scoring:
	-	Each video title is compared to its corresponding search keyword using:
	   -	Direct Keyword Match: Checks if the keyword is present in the title.
	   -	Word Overlap: Measures how many words in the title overlap with the keyword.
	   -	Sequence Similarity: Checks how similar the sequence of words in the title is to the keyword.
	   -	These scores are combined with weights to calculate a **base relevance score**.
         - Direct keyword match (30% weight).
         - Word overlap (40% weight).
         - Sequence similarity (30% weight).
2.	Semantic Similarity:
	-	Uses Sentence BERT (SBERT) to compute the similarity between the title and keyword on a semantic level.
   -	The final relevance score combines the **base relevance score (60%)** and **semantic similarity score (40%)**.
3.	Categorization:
	-	Videos are categorized based on their relevance scores:
	-	High: Scores ≥ 40 (as average relevance score of the data was near 40)
	-	Medium: Scores between 20 and 40 (half of average relevance score)
	-	Low: Scores between 10 and 20 (quarter of average relevance score)
	-	Not Relevant: Scores < 10 (This was found from the data that any video below this score was not relevant to the keyword at all)
4.	Filter and Save:
	-	Videos with relevance scores > 10 are considered relevant and saved to a new file.

## Step 4: Exploratory Data Analysis
Following libraries are used for data analysis:
- **pandas:** For data manipulation and analysis
- **numpy:** For numerical operations
- **matplotlib:** For creating static, interactive, and animated visualizations
- **seaborn:** For creating statistical data visualizations
- **plotly:** For creating interactive web-based visualizations

### Discussion on Results
**Trend Analysis:**
- Identified increasing interest in modern plant breeding techniques like CRISPR and AI-based genomic selection.
- Observed consistent engagement with traditional topics, suggesting continued relevance.

## Calculation of Demand Metrics
The demand score is a measure of how much interest (or demand) there is for a keyword. It combines two metrics: average views and average engagement rate. These metrics are weighted to prioritize their relative importance.

```python
keyword_metrics['demand_score'] = (
    (keyword_metrics['avg_views'] / keyword_metrics['avg_views'].mean()) * 0.6 +
    (keyword_metrics['avg_engagement'] / keyword_metrics['avg_engagement'].mean()) * 0.4
)
```

### Components:

- avg_views: The mean number of views for videos associated with the keyword.
Indicates how popular the keyword is among viewers.
- Weight: 60%
- avg_engagement: The mean engagement rate (likes, comments, etc.) for the keyword.
Indicates how actively viewers engage with videos containing this keyword.
Weight: 40%
Normalization:

Both metrics (avg_views and avg_engagement) are divided by their respective means.
This ensures the scores are relative and comparable across different scales.
Weighted Combination:

The two normalized metrics are multiplied by their respective weights (0.6 for views, 0.4 for engagement) and summed.

### Supply Score
The supply score measures the availability of content (videos) related to a keyword. A higher supply score means there are many videos available for the keyword, making it more competitive.
```python
keyword_metrics['supply_score'] = keyword_metrics['video_count'] / keyword_metrics['video_count'].mean()
```

Components:
- video_count: The total number of videos associated with the keyword.
- Indicates how much content is already available for the keyword.

### Normalization:

video_count is divided by its mean to make the score relative to the overall supply of videos.

### Opportunity Score
The opportunity score identifies keywords with a high demand-to-supply ratio, indicating the best opportunities for creating new content.
```python
keyword_metrics['opportunity_score'] = keyword_metrics['demand_score'] / keyword_metrics['supply_score']
```

Components:
- demand_score: Captures the interest in the keyword. 
- supply_score: Captures the competition for the keyword.
- Ratio:
The opportunity score is calculated as the ratio of demand to supply.
A higher ratio means high demand with low competition, making it a good opportunity for content creation.


### Interpretation
- Demand Score:
High demand scores indicate popular keywords that attract a lot of interest and engagement.
- Supply Score:
High supply scores indicate highly competitive keywords with many videos already created.
- Opportunity Score:
High opportunity scores identify keywords with unmet demand (low competition relative to high interest).

## Key Findings

1. **Demand Indicators**:
   - **Top Keywords**:
     - Keywords like `Modern Breeding Techniques`, `Hybrid Varieties`, and `CRISPR in Plants` have the highest **Opportunity Scores**, indicating high demand and strong engagement potential.
   - **Engagement Metrics**:
     - Keywords under the `Modern` category show the highest average **Engagement Rate** (5.6%), while `Old` technologies demonstrate steady, albeit lower, audience interest.

2. **Category-Level Insights**:
   - **Modern**:
     - This category has the **highest Opportunity Score** due to topics like genetic editing and sustainable practices gaining popularity.
     - Total Views: **3.2M**; Engagement Rate: **5.6%**
   - **Current**:
     - Focused on trending topics like genome sequencing, offering moderate engagement and competitive opportunities.
     - Total Views: **2.8M**; Engagement Rate: **4.3%**
   - **Old**:
     - Historical breeding methods still attract niche audiences, but lower engagement suggests less dynamic interest.
     - Total Views: **1.9M**; Engagement Rate: **3.2%**

3. **Visualization Insights**:
   - **Treemap Analysis**:
     - Keywords under the `Modern` category dominate with higher Opportunity Scores.
   - **Bubble Chart**:
     - Keywords with high views and engagement (e.g., `CRISPR`, `Sustainable Practices`) present ideal starting points for content creation.


## Relevance of Such Analysis

1. **Identifying Content Gaps**:
   - The analysis reveals specific keywords with high demand but relatively low supply in terms of detailed content. Targeting these gaps can attract substantial viewership.

2. **Strategic Content Focus**:
   - Keywords with high **Engagement Rates** and **Opportunity Scores** (e.g., `Modern Technologies`) indicate topics where audiences are actively interested and engaged.
   - Avoid oversaturated or underperforming keywords.

3. **Audience Preferences**:
   - Insights on engagement trends guide the style and depth of content creation (e.g., informative, visual-heavy, or interview formats).

## Actionable Recommendations

1. **Focus Areas**:
   - Begin with `Modern` topics like CRISPR and Hybrid Breeding, as they combine high audience interest and engagement.

2. **Content Strategy**:
   - Use engaging visuals and simplified explanations for complex topics to increase accessibility.
   - Consider a series format to explore different aspects of modern plant breeding technologies.

3. **Niche Selection**:
   - Target subdomains like `Genetic Editing`, `Genome Sequencing`, and `Sustainable Breeding Practices`, which show consistent demand.

4. **Content Frequency**:
   - Publish frequently on trending topics to maintain relevance, especially under the `Current` category.

5. **SEO Optimization**:
   - Optimize video titles and descriptions with high-ranking keywords like `CRISPR`, `Hybrid Plants`, and `Genome Editing`.

## Future Work

1. **Trend Monitoring**:
   - Continuously analyze evolving audience interests using new data over time to stay ahead of trends.

2. **Deep Dive into Audience Segmentation**:
   - Identify demographic and regional preferences for specific keywords to tailor content.

3. **Performance Tracking**:
   - Regularly monitor engagement metrics (views, likes, comments) to refine the content strategy.

4. **Collaborative Content**:
   - Collaborate with experts or influencers in the plant breeding domain to leverage their audience and add credibility.

5. **Advanced Analytics**:
   - Utilize predictive modeling to forecast future trends in plant breeding content on YouTube.


## Project Setup
### 1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install required packages:
```bash
pip install -r requirements.txt
```   

### 3. Run the Application
- Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
- Run the application:
   ```bash
   streamlit run dashboard.py
   ```


## To run a fresh analysis setup the API Configuration
Get a YouTube Data API key from the [Google Cloud Console](https://console.cloud.google.com/)
Set up environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your YouTube API key:
     ```
     YOUTUBE_API_KEY=your_actual_api_key_here
     ```

## Project Structure
├── README.md
├── requirements.txt
├── .env.example
├── .env # (git-ignored)
├── .gitignore
├── youtube_data_fetcher.py
├── dashboard.py
└── youtube_data/
└── all_videos_data.csv

## License
The project was developed by **Nadim Khan** and **Samaneh Javidian** as a part of the **Practical Introduction to Programming with Python (1511-501) - Winter term 2024/25** course at the University of Hohenheim, Stuttgart, Germany.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Security Notice
⚠️ If you're forking this repository, make sure to:
1. Never commit API keys or sensitive data
2. Use environment variables for sensitive data
3. Check git history for sensitive data before making public.