import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Custom color schemes
COLOR_SCHEMES = {
    'category_colors': {
        'Modern': '#FF6B6B',  # Coral Red
        'Current': '#4ECDC4', # Turquoise
        'Old': '#45B7D1'      # Sky Blue
    },
    'gradient_colors': px.colors.sequential.Viridis,
    'diverging_colors': px.colors.diverging.RdYlBu,
}

# Page config
st.set_page_config(
    page_title="Plant Breeding YouTube Analytics",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🌱"
)

# Enhanced Custom CSS
st.markdown("""
<style>
.main { padding: 0rem 1rem; }
.stButton>button { 
    width: 100%; 
    background-color: #4ECDC4;
    color: white;
    border-radius: 5px;
}
.reportview-container { background: #f8f9fa }
.sidebar .sidebar-content { background: #f8f9fa }
h1 { 
    color: #21c648;
    font-weight: bold;
    padding-bottom: 20px;
}
h2 { color: #45B7D1; }
h3 { color: #FF6B6B; }
.stAlert { 
    background-color: #4ECDC4 !important;
    color: white !important;
    border: 2px solid #45B7D1 !important;
    border-radius: 10px !important;
    padding: 1rem !important;
    margin: 1rem 0 !important;
    opacity: 0.9 !important;
}
.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("youtube_data/videos_with_relevance.csv")
    df['published_date'] = pd.to_datetime(df['published_date'])
    return df

df = load_data()

# Sidebar
st.sidebar.title("🌱 Navigation")
page = st.sidebar.radio(
    "Choose a section",
    ["Explanation", "Overview", "Trend Analysis", "Category Analysis", 
     "Keyword Analysis", "Opportunity Analysis", "Update Analysis", "Code References"]
)

# Add the Explanation page
if page == "Explanation":
    st.title("🌱 Plant Breeding YouTube Content Analysis Project")
    
    # Project Overview
    st.markdown("""
    This project analyzes **8,971 videos** with **2.1 billion views** for **198 keywords** 
    in **3 categories** of plant breeding concepts (Old, Current, Modern) on YouTube.
    """)
    
    # Problem Statement
    st.header("🎯 Problem Statement")
    with st.expander("Why did we start this project?", expanded=True):
        st.markdown("""
        - We want to start a YouTube channel focusing on plant breeding concepts
        - Existing SEO tools focus only on basic keyword metrics
        - Need for comprehensive analysis of audience interaction across different concept categories
        - YouTube's potential as an educational platform for plant breeding concepts
        """)
    
    # Project Setup
    st.header("⚙️ Project Setup")
    with st.expander("How to set up and run the project"):
        st.markdown("""
        ### 1. Clone the repository:
        ```bash
        git clone git@github.com:nfornadimkhan/data_analysis_youtube.git
        cd data_analysis_youtube
        ```

        ### 2. Install required packages
        ```bash
        pip install -r requirements.txt
        ```   

        ### 3. Run the Application
        ```bash
        streamlit run dashboard.py
        ```
        """)

    # API Configuration
    with st.expander("API Configuration"):
        st.markdown("""
        Get a YouTube Data API key from the [Google Cloud Console](https://console.cloud.google.com/)
        
        Set up environment variables:
        1. Copy `.env.example` to `.env`:
           ```bash
           cp .env.example .env
           ```
        2. Edit `.env` and add your YouTube API key:
           ```
           YOUTUBE_API_KEY=your_actual_api_key_here
           ```
        """)

    # Project Structure
    st.header("📁 Project Structure")
    st.code("""
    project_directory/
    ├── README.md
    ├── requirements.txt
    ├── analysis.ipynb
    ├── .env.example
    ├── .env # (git-ignored)
    ├── .gitignore
    ├── youtube_data_fetcher.py
    ├── dashboard.py
    ├── pre-commit
    ├── youtube_data/
    ├── fetch_state.json
    """)

    # Libraries Used
    st.header("📚 Libraries Used")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - **pandas:** Data manipulation and analysis
        - **numpy:** Numerical operations
        - **matplotlib:** Static visualizations
        - **seaborn:** Statistical visualizations
        - **plotly:** Interactive web visualizations
        - **nltk:** Natural language processing
        """)
    with col2:
        st.markdown("""
        - **sentence-transformers:** BERT encodings
        - **scikit-learn:** Machine learning tools
        - **google-api-python-client:** YouTube API
        - **python-dotenv:** Environment variables
        - **isodate:** Date/time parsing
        - **streamlit:** Web application
        """)

    # Keyword Classification
    st.header("🔑 Keyword Classification")
    
    tab1, tab2, tab3 = st.tabs(["Old (Traditional)", "Current (Established)", "Modern (Cutting-Edge)"])
    
    with tab1:
        st.markdown("""
        **Focus:** Pre-20th century practices
        - Phenotype-based selection
        - Indigenous approaches
        - Field observation methods
        - Community-based breeding
        
        **Example Keywords:**
        1. Traditional selective breeding
        2. Landrace selection
        3. Phenotypic selection
        4. Pedigree breeding
        5. Mass selection
        """)
    
    with tab2:
        st.markdown("""
        **Focus:** Late 20th century methods
        - Molecular biology integration
        - Marker-assisted selection
        - QTL mapping
        - Heterosis exploitation
        
        **Example Keywords:**
        1. Marker-assisted selection
        2. QTL mapping
        3. Hybrid vigor breeding
        4. Backcross breeding
        5. Recurrent selection
        """)
    
    with tab3:
        st.markdown("""
        **Focus:** Emerging technologies
        - CRISPR and gene editing
        - AI/ML applications
        - Computational breeding
        - Precision agriculture
        
        **Example Keywords:**
        1. CRISPR gene editing
        2. Genome sequencing
        3. Precision breeding
        4. Synthetic biology
        5. Gene network analysis
        """)

    # Methodology
    st.header("🔍 Methodology")
    
    # Data Collection
    with st.expander("1️⃣ Data Collection", expanded=True):
        st.markdown("""
        - Collected data using YouTube Data API v3
        - 198 keywords (66 in each category)
        - 50 videos per keyword
        - Total of 8,971 relevant videos analyzed
        
        #### API Quota Management
        - Search request: 100 units
        - Video details: 50 units
        - Total per keyword: 150 units
        - Daily quota: 10,000 units
        - Max keywords per day: 66
        - Days needed: 3
        """)
    
    # Data Cleaning
    with st.expander("2️⃣ Data Cleaning & Preprocessing", expanded=True):
        st.markdown("""
        - Removed duplicate entries
        - Standardized date formats
        - Converted metrics to numeric format
        - Created engagement rate metric
        - Removed irrelevant content
        - Added human-readable duration format
        - Created engagement rate metric: [(likes + comments) / views] * 100
        """)
    
    # Relevance Scoring
    with st.expander("3️⃣ Content Relevance Analysis", expanded=True):
        st.markdown("""
        #### Relevance Scoring Components:
        1. **Base Relevance (60%)**
           - Direct Keyword Match (30%)
           - Word Overlap (40%)
           - Sequence Similarity (30%)
        
        2. **Semantic Similarity (40%)**
           - Using SBERT for semantic analysis
        
        #### Score Categories:
        - High: ≥ 40
        - Medium: 20-40
        - Low: 10-20
        - Not Relevant: < 10
        """)

    # Key Findings
    st.header("🎯 Key Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Top Performing Keywords")
        st.markdown("""
        1. Propagation Techniques
           - Opportunity Score: 10.0/10
           - 330M+ views
        
        2. Quantum Computing
           - Opportunity Score: 5.3/10
           - High engagement rate
        """)
    
    with col2:
        st.markdown("#### Best Publishing Times")
        st.markdown("""
        1. Saturday 22:00
           - 6.86% engagement rate
           - Low competition
        
        2. Sunday 18:00
           - 6.71% engagement rate
           - Moderate competition
        """)

    # Results and Recommendations
    st.header("📊 Results and Recommendations")
    
    st.markdown("""
    Based on our comprehensive analysis of YouTube content related to plant breeding, 
    we have identified several key insights and recommendations:
    """)
    
    # Overall Findings
    with st.expander("Overall Findings", expanded=True):
        st.markdown("""
        1. **Growth Trend**
           - Constant increase in plant breeding related videos on YouTube
           - Rising engagement rates over the years
           - Ideal timing for starting a plant breeding focused channel
        
        2. **Content Impact**
           - Keywords like "Propagation Techniques" show exceptional performance
           - Over 330 million total views for top-performing content
           - High engagement rates indicating strong audience interest
        
        3. **Audience Preferences**
           - Strong interest in practical, actionable content
           - Growing demand for modern technological applications
           - Balance between traditional methods and cutting-edge innovations
        """)
    
    # High-Potential Keywords Analysis
    with st.expander("High-Potential Keywords Analysis", expanded=True):
        st.markdown("""
        | **Keyword** | **Opportunity Score** | **Demand Score** | **Total Views** | **Engagement Per Video** | **Why It's Important** |
        |-------------|----------------------|------------------|-----------------|------------------------|----------------------|
        | Propagation Techniques | 10.0/10 | 6.7/10 | 330M+ | 136,589 | Highly searched and engages users effectively |
        | Quantum Computing | 5.3/10 | 4.8/10 | 131M+ | 91,443 | Modern topic attracting tech-savvy professionals |
        | Indigenous Methods | 5.2/10 | 4.3/10 | 169M+ | 73,288 | Appeals to sustainable practice enthusiasts |
        | Historical Practices | 4.8/10 | 4.0/10 | 163M+ | 63,351 | Niche audience interested in agricultural evolution |
        | CRISPR Gene Editing | 1.5/10 | 3.7/10 | 35M+ | 27,352 | Cutting-edge topic with global relevance |
        """)
    
    # Publishing Strategy
    with st.expander("Optimal Publishing Strategy", expanded=True):
        st.markdown("""
        #### Best Publishing Times
        | **Day** | **Time** | **Engagement Rate** | **Competing Videos** | **Average Views** | **Why This Time Works** |
        |---------|----------|---------------------|---------------------|-------------------|------------------------|
        | Saturday | 22:00 | 6.86% | 10 | - | High engagement, lowest competition |
        | Sunday | 18:00 | 6.71% | 24 | - | Peak weekend engagement |
        | Saturday | 06:00 | 5.58% | 31 | 764,234 | Strong early morning performance |
        | Sunday | 14:00 | 4.18% | - | 3,192,022 | Highest average views |
        
        #### Key Timing Insights
        - Weekend publishing shows consistently higher engagement
        - Early morning and evening slots perform best
        - Lower competition during certain time slots provides opportunities
        - Balance between engagement rate and view potential
        """)
    
    # Engagement Analysis
    with st.expander("Detailed Engagement Analysis", expanded=True):
        st.markdown("""
        #### Category-wise Performance

        **Old Category:**
        - Median Views: 909.50
        - Mean Views: 476,292.65
        - Median Likes: 15
        - Mean Likes: 9,181.28
        - Average Engagement Rate: 1.84%
        - Notable: Highest viral potential with some videos reaching 117M views

        **Modern Category:**
        - Median Views: 487.50
        - Mean Views: 200,511.95
        - Median Likes: 7
        - Average Engagement Rate: 1.73%
        - Notable: Strong performance in niche technical topics

        **Current Category:**
        - Median Views: 791.00
        - Mean Views: 72,754.74
        - Median Likes: 12
        - Mean Likes: 957.30
        - Average Engagement Rate: 1.81%
        - Notable: Steady performance with consistent engagement
        """)
    
    # Content Strategy Recommendations
    with st.expander("Content Strategy Recommendations", expanded=True):
        st.markdown("""
        #### 1. Content Focus
        - Start with practical, hands-on content like propagation techniques
        - Balance traditional methods with modern applications
        - Create content series that bridge old and new concepts
        
        #### 2. Topic Selection Strategy
        - **High-Impact Traditional Topics:**
          - Propagation techniques
          - Indigenous breeding methods
          - Historical agronomic practices
        
        - **Promising Modern Topics:**
          - Quantum computing applications
          - CRISPR gene editing
          - Precision agriculture
        
        #### 3. Engagement Optimization
        - Focus on weekend publishing
        - Utilize optimal time slots (Saturday 22:00, Sunday 18:00)
        - Create content that encourages discussion and interaction
        
        #### 4. Growth Strategy
        - Start with established topics to build audience
        - Gradually introduce modern concepts
        - Maintain consistent publishing schedule
        - Focus on educational value and practical applications
        """)
    
    # Future Opportunities
    with st.expander("Future Opportunities", expanded=True):
        st.markdown("""
        #### Emerging Trends
        1. **Technology Integration**
           - AI/ML applications in breeding
           - Digital phenotyping
           - Automated breeding systems
        
        2. **Sustainable Practices**
           - Climate-resilient breeding
           - Eco-genomics
           - Urban crop development
        
        3. **Educational Content**
           - Interactive tutorials
           - Virtual demonstrations
           - Case studies and success stories
        
        #### Growth Areas
        - **Untapped Niches:** Several modern breeding techniques show high demand but low content supply
        - **Cross-Category Content:** Combining traditional wisdom with modern technology
        - **Practical Applications:** Focus on real-world implementation and results
        """)

    # Team & Acknowledgements
    st.header("👥 Team & Acknowledgements")
    
    st.markdown("""
    **Project Team:**
    - Nadim Khan
    - Samaneh Javidian
    
    **Special Thanks:**
    - Jun. Prof. Christian Krupitzer
    - Maryam Lotfaliani
    
    *Part of Practical Introduction to Programming with Python (1511-501) - Winter term 2024/25*
    
    University of Hohenheim, Stuttgart, Germany
    """)
    
    # License
    st.markdown("---")
    st.markdown("""
    [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
    
    © 2024 Nadim Khan and Samaneh Javidian
    """)

# Overview Page
elif page == "Overview":
    st.title("🎯 Overview")
    
    # Category-wise metrics
    st.subheader("📊 Category Performance")
    cat_metrics = df.groupby('category').agg({
        'view_count': 'sum',
        'like_count': 'sum',
        'comment_count': 'sum'
    }).reset_index()
    
    # Display metrics in columns
    cols = st.columns(3)
    for idx, category in enumerate(cat_metrics['category']):
        with cols[idx]:
            st.markdown(f"### {category}")
            metrics = cat_metrics[cat_metrics['category'] == category].iloc[0]
            st.metric("👀 Views", f"{metrics['view_count']:,.0f}")
            st.metric("👍 Likes", f"{metrics['like_count']:,.0f}")
            st.metric("💬 Comments", f"{metrics['comment_count']:,.0f}")
    
    # Keywords by category
    st.subheader("📝 Keywords by Category")
    
    # Convert categories to list for tabs
    categories = sorted(df['category'].unique().tolist())
    
    # Create tabs for each category
    if len(categories) > 0:
        tabs = st.tabs(categories)
        
        for tab, category in zip(tabs, categories):
            with tab:
                # Get unique keywords for this category
                keywords = sorted(df[df['category'] == category]['keyword'].unique().tolist())
                
                # Create a formatted list of keywords
                st.write(f"**Total Keywords:** {len(keywords)}")
                
                # Display keywords in a grid
                cols = st.columns(3)
                for idx, keyword in enumerate(keywords):
                    cols[idx % 3].write(f"- {keyword}")

# Trend Analysis Page
elif page == "Trend Analysis":
    st.title("📊 Trend Analysis")
    
    # Enhanced time series analysis
    df['year'] = df['published_date'].dt.year
    df['month'] = df['published_date'].dt.to_period('M')
    

        
    # Timeline Analysis (2008-2023)
    st.subheader("📈 Content Evolution (2008-2023)")
    
    # Prepare timeline data
    timeline_data = df.copy()
    timeline_data['year'] = timeline_data['published_date'].dt.year
    yearly_category_data = timeline_data.groupby(['year', 'category']).agg({
        'video_id': 'count',
        'view_count': 'sum',
        'engagement_rate': 'mean'
    }).reset_index()
    
    # Create timeline visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # Video count stack plot
        fig_videos = px.area(yearly_category_data, 
                           x='year', 
                           y='video_id',
                           color='category',
                           color_discrete_map=COLOR_SCHEMES['category_colors'],
                           title="Video Publication Timeline",
                           labels={'video_id': 'Number of Videos', 
                                 'year': 'Year',
                                 'category': 'Category'})
        fig_videos.update_layout(
            xaxis_range=[2008, 2023],
            hovermode='x unified'
        )
        st.plotly_chart(fig_videos, use_container_width=True)
    
    with col2:
        # Views stack plot
        fig_views = px.area(yearly_category_data, 
                          x='year', 
                          y='view_count',
                          color='category',
                          color_discrete_map=COLOR_SCHEMES['category_colors'],
                          title="Cumulative Views Timeline",
                          labels={'view_count': 'Total Views', 
                                'year': 'Year',
                                'category': 'Category'})
        fig_views.update_layout(
            xaxis_range=[2008, 2023],
            hovermode='x unified'
        )
        st.plotly_chart(fig_views, use_container_width=True)
    
    # Engagement trend
    fig_engagement = px.line(yearly_category_data,
                           x='year',
                           y='engagement_rate',
                           color='category',
                           color_discrete_map=COLOR_SCHEMES['category_colors'],
                           title="Engagement Rate Trends",
                           labels={'engagement_rate': 'Engagement Rate (%)',
                                 'year': 'Year',
                                 'category': 'Category'})
    fig_engagement.update_layout(
        xaxis_range=[2008, 2023],
        hovermode='x unified'
    )
    st.plotly_chart(fig_engagement, use_container_width=True)


    
    # Metric selector with custom styling
    metric = st.selectbox(
        "📈 Select Metric",
        ["view_count", "engagement_rate", "like_count", "comment_count"],
        format_func=lambda x: x.replace('_', ' ').title()
    )
    
    # Yearly trends
    yearly_trends = df.groupby(['year', 'category']).agg({
        metric: 'mean'
    }).reset_index()
    
    # Monthly trends
    monthly_trends = df.groupby(['month', 'category']).agg({
        metric: 'mean'
    }).reset_index()
    monthly_trends['month'] = monthly_trends['month'].astype(str)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_yearly = px.line(yearly_trends, x='year', y=metric,
                           color='category',
                           color_discrete_map=COLOR_SCHEMES['category_colors'],
                           title=f"Yearly {metric.replace('_', ' ').title()} Trends")
        fig_yearly.update_layout(hovermode='x unified')
        st.plotly_chart(fig_yearly, use_container_width=True)
    
    with col2:
        fig_monthly = px.area(monthly_trends, x='month', y=metric,
                            color='category',
                            color_discrete_map=COLOR_SCHEMES['category_colors'],
                            title=f"Monthly {metric.replace('_', ' ').title()} Trends")
        fig_monthly.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_monthly, use_container_width=True)

    


# Category Analysis Page
elif page == "Category Analysis":
    st.title("🎯 Category Analysis")
    
    selected_category = st.selectbox("Select Category", df['category'].unique())
    cat_data = df[df['category'] == selected_category]
    
    # Enhanced metrics display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Videos", len(cat_data))
    with col2:
        st.metric("Average Views", f"{cat_data['view_count'].mean():,.0f}")
    with col3:
        st.metric("Average Engagement", f"{cat_data['engagement_rate'].mean():.2f}%")
    
    # Enhanced visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        top_keywords = cat_data.groupby('keyword').agg({
            'view_count': 'sum',
            'engagement_rate': 'mean'
        }).sort_values('view_count', ascending=False).head(10)
        
        fig_keywords = px.bar(top_keywords, y=top_keywords.index, x='view_count',
                            title=f"Top 10 Keywords in {selected_category}",
                            color='engagement_rate',
                            color_continuous_scale=COLOR_SCHEMES['gradient_colors'],
                            orientation='h')
        st.plotly_chart(fig_keywords, use_container_width=True)
    
    with col2:
        fig_engagement = go.Figure()
        fig_engagement.add_trace(go.Histogram(
            x=cat_data['engagement_rate'],
            nbinsx=30,
            marker_color=COLOR_SCHEMES['category_colors'][selected_category]
        ))
        fig_engagement.update_layout(
            title=f"Engagement Distribution in {selected_category}",
            xaxis_title="Engagement Rate",
            yaxis_title="Count"
        )
        st.plotly_chart(fig_engagement, use_container_width=True)

# Keyword Analysis Page
elif page == "Keyword Analysis":
    st.title("🔍 Keyword Analysis & Insights")
    
    # Top-level Insights
    st.header("📊 Key Insights")
    
    # Create three columns for key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Most Viewed Category",
            "Old",
            "476,292 avg views",
            help="Category with highest average views per video"
        )
    with col2:
        st.metric(
            "Highest Engagement",
            "Traditional Methods",
            "+1.84%",
            help="Category with best engagement rate"
        )
    with col3:
        st.metric(
            "Best Time to Publish",
            "Weekend Evenings",
            "+6.86% engagement",
            help="Optimal publishing time for maximum engagement"
        )
    
    # Top Keywords Overview
    st.subheader("🏆 Top Performing Keywords")
    
    tab1, tab2, tab3 = st.tabs(["By Views", "By Engagement", "By Growth Potential"])
    
    with tab1:
        # Top keywords by views
        top_by_views = df.groupby('keyword').agg({
            'view_count': 'sum',
            'category': 'first'
        }).nlargest(10, 'view_count').reset_index()
        
        fig_views = px.bar(
            top_by_views,
            x='keyword',
            y='view_count',
            color='category',
            color_discrete_map=COLOR_SCHEMES['category_colors'],
            title="Top 10 Keywords by Total Views",
            labels={'view_count': 'Total Views', 'keyword': 'Keyword'}
        )
        fig_views.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_views, use_container_width=True)
    
    with tab2:
        # Top keywords by engagement
        top_by_engagement = df.groupby('keyword').agg({
        'engagement_rate': 'mean',
            'category': 'first',
            'view_count': 'sum'
        }).nlargest(10, 'engagement_rate').reset_index()
        
        fig_engagement = px.scatter(
            top_by_engagement,
            x='view_count',
            y='engagement_rate',
            color='category',
            size='view_count',
            text='keyword',
            color_discrete_map=COLOR_SCHEMES['category_colors'],
            title="Top 10 Keywords by Engagement Rate",
            labels={
                'view_count': 'Total Views',
                'engagement_rate': 'Engagement Rate (%)',
                'keyword': 'Keyword'
            }
        )
        fig_engagement.update_traces(textposition='top center')
        st.plotly_chart(fig_engagement, use_container_width=True)
    
    with tab3:
        # Keywords with growth potential
        df['year'] = pd.to_datetime(df['published_date']).dt.year
        yearly_growth = df.groupby(['keyword', 'year']).agg({
            'view_count': 'sum',
            'category': 'first'
    }).reset_index()
        
        # Calculate year-over-year growth
        growth_rate = yearly_growth.pivot(
            index='keyword',
            columns='year',
            values='view_count'
        ).pct_change(axis=1).mean(axis=1)
        
        top_growth = growth_rate.nlargest(10).reset_index()
        top_growth['growth_rate'] = top_growth[0] * 100
        
        fig_growth = px.bar(
            top_growth,
            x='keyword',
            y='growth_rate',
            title="Top 10 Keywords by Growth Rate",
            labels={
                'growth_rate': 'Average YoY Growth Rate (%)',
                'keyword': 'Keyword'
            }
        )
        fig_growth.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_growth, use_container_width=True)
    
    # Advanced Keyword Search and Analysis
    st.header("🔎 Advanced Keyword Analysis")
    
    # Search Interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        search_keyword = st.text_input(
            "Search for a keyword",
            placeholder="Enter a keyword (e.g., 'CRISPR', 'breeding', etc.)"
        )
    
    with col2:
        search_category = st.selectbox(
            "Filter by category",
            ["All Categories"] + sorted(df['category'].unique().tolist())
        )
    
    # Additional filters in expandable section
    with st.expander("Advanced Filters"):
        col1, col2 = st.columns(2)
        with col1:
            min_views = st.number_input(
                "Minimum Views",
                min_value=0,
                value=0
            )
            min_engagement = st.number_input(
                "Minimum Engagement Rate (%)",
                min_value=0.0,
                value=0.0
            )
        with col2:
            date_range = st.date_input(
                "Date Range",
                value=(df['published_date'].min(), df['published_date'].max())
            )
    
    # Apply filters
    if search_keyword or search_category != "All Categories":
        filtered_df = df.copy()
        
        if search_keyword:
            filtered_df = filtered_df[
                filtered_df['keyword'].str.contains(search_keyword, case=False)
            ]
        
        if search_category != "All Categories":
            filtered_df = filtered_df[filtered_df['category'] == search_category]
        
        if min_views > 0:
            filtered_df = filtered_df[filtered_df['view_count'] >= min_views]
        
        if min_engagement > 0:
            filtered_df = filtered_df[
                filtered_df['engagement_rate'] >= min_engagement
            ]
        
        filtered_df = filtered_df[
            (filtered_df['published_date'].dt.date >= date_range[0]) &
            (filtered_df['published_date'].dt.date <= date_range[1])
        ]
        
        if not filtered_df.empty:
            # Keyword Performance Metrics
            st.subheader("📈 Keyword Performance Metrics")
            
            metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
            
            with metric_col1:
                st.metric(
                    "Total Videos",
                    len(filtered_df),
                    help="Number of videos found"
                )
            
            with metric_col2:
                st.metric(
                    "Total Views",
                    f"{filtered_df['view_count'].sum():,.0f}",
                    help="Total views across all videos"
                )
            
            with metric_col3:
                st.metric(
                    "Avg. Engagement Rate",
                    f"{filtered_df['engagement_rate'].mean():.2f}%",
                    help="Average engagement rate"
                )
            
            with metric_col4:
                st.metric(
                    "Avg. Video Duration",
                    f"{filtered_df['duration_seconds'].mean()/60:.1f} min",
                    help="Average video length"
                )
            
            # Temporal Analysis
            st.subheader("📅 Temporal Analysis")
            
            # Views over time
            fig_timeline = px.line(
                filtered_df.groupby('published_date')['view_count'].sum().reset_index(),
                x='published_date',
                y='view_count',
                title="Views Distribution Over Time",
                labels={
                    'published_date': 'Publication Date',
                    'view_count': 'Total Views'
                }
            )
            st.plotly_chart(fig_timeline, use_container_width=True)
            
            # Detailed Results
            st.subheader("📋 Detailed Results")
            
            # Show detailed table with main metrics
            results_df = filtered_df[[
                'keyword', 'category', 'published_date', 'view_count',
                'like_count', 'comment_count', 'engagement_rate'
            ]].sort_values('view_count', ascending=False)
            
            st.dataframe(
                results_df.style.format({
                    'view_count': '{:,.0f}',
                    'like_count': '{:,.0f}',
                    'comment_count': '{:,.0f}',
                    'engagement_rate': '{:.2f}%'
                }),
                use_container_width=True
            )
        else:
            st.markdown("""
            <div style='background-color: #4ECDC4; color: white; padding: 1rem; border-radius: 10px; border: 2px solid #45B7D1; text-align: center;'>
                🔍 Enter a keyword or select a category to see detailed analysis
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background-color: #4ECDC4; color: white; padding: 1rem; border-radius: 10px; border: 2px solid #45B7D1; text-align: center;'>
            🔍 Enter a keyword or select a category to see detailed analysis
        </div>
        """, unsafe_allow_html=True)

# Opportunity Analysis Page
elif page == "Opportunity Analysis":
    st.title("🎯 Content Opportunity Analysis")
    
    st.markdown("""
    This analysis combines demand and supply metrics to identify the most promising content opportunities 
    in plant breeding education on YouTube.
    """)
    
    # Calculate opportunity and demand metrics
    metrics = df.groupby(['category', 'keyword']).agg({
        'view_count': ['sum', 'count', 'mean'],
        'engagement_rate': 'mean',
        'like_count': 'sum',
        'comment_count': 'sum'
    }).reset_index()
    
    # Flatten column names
    metrics.columns = ['category', 'keyword', 'total_views', 'video_count', 'avg_views', 'avg_engagement', 'total_likes', 'total_comments']
    
    # Calculate normalized metrics
    metrics['normalized_views'] = (metrics['total_views'] - metrics['total_views'].min()) / (metrics['total_views'].max() - metrics['total_views'].min())
    metrics['normalized_engagement'] = (metrics['avg_engagement'] - metrics['avg_engagement'].min()) / (metrics['avg_engagement'].max() - metrics['avg_engagement'].min())
    
    # Calculate opportunity and demand scores
    metrics['opportunity_score'] = (
        (0.5 * metrics['normalized_views']) + 
        (0.5 * (metrics['avg_engagement'] / metrics['avg_engagement'].max()))
    ) * 10
    
    metrics['demand_score'] = (
        (0.5 * metrics['normalized_views']) + 
        (0.5 * (metrics['avg_engagement'] / metrics['avg_engagement'].max()))
    ) * 10
    
    # 1. Overall Opportunity Landscape
    st.header("📊 Opportunity Landscape")
    
    # Create opportunity vs demand matrix
    fig_matrix = px.scatter(
        metrics,
        x='opportunity_score',
        y='demand_score',
        size='total_views',
        color='category',
        hover_data={
            'keyword': True,
            'total_views': ':,.0f',
            'avg_engagement': ':.2f%',
            'video_count': True
        },
        color_discrete_map=COLOR_SCHEMES['category_colors'],
        title="Content Opportunity vs Demand Matrix",
        labels={
            'opportunity_score': 'Opportunity Score (0-10)',
            'demand_score': 'Demand Score (0-10)',
            'total_views': 'Total Views'
        }
    )
    
    # Add quadrant lines
    fig_matrix.add_hline(y=metrics['demand_score'].median(), line_dash="dash", line_color="gray", opacity=0.5)
    fig_matrix.add_vline(x=metrics['opportunity_score'].median(), line_dash="dash", line_color="gray", opacity=0.5)
    
    # Add quadrant labels
    fig_matrix.add_annotation(x=8, y=8, text="High Opportunity, High Demand", showarrow=False, font=dict(size=10))
    fig_matrix.add_annotation(x=8, y=2, text="High Opportunity, Low Demand", showarrow=False, font=dict(size=10))
    fig_matrix.add_annotation(x=2, y=8, text="Low Opportunity, High Demand", showarrow=False, font=dict(size=10))
    fig_matrix.add_annotation(x=2, y=2, text="Low Opportunity, Low Demand", showarrow=False, font=dict(size=10))
    
    fig_matrix.update_layout(
        height=600,
        xaxis_title="Opportunity Score (Higher = More Potential)",
        yaxis_title="Demand Score (Higher = More Interest)",
        showlegend=True
    )
    st.plotly_chart(fig_matrix, use_container_width=True)
    
    # Add explanation
    st.markdown("""
    **Matrix Quadrants Explanation:**
    - **Top Right:** High opportunity keywords with strong demand - prime targets for content creation
    - **Top Left:** High demand but lower opportunity - consider ways to differentiate content
    - **Bottom Right:** High opportunity but lower demand - potential for early mover advantage
    - **Bottom Left:** Lower priority keywords for content creation
    """)

    # 2. Category-wise Analysis
    st.header("📈 Category Performance")
    
    # Create tabs for different views
    tab1, tab2 = st.tabs(["Opportunity Scores", "Demand Analysis"])
    
    with tab1:
        # Category-wise opportunity scores
        cat_opportunity = metrics.groupby('category').agg({
            'opportunity_score': ['mean', 'max', 'min'],
            'total_views': 'sum',
            'video_count': 'sum'
        }).round(2)
        
        for category in cat_opportunity.index:
            with st.expander(f"📊 {category} Category Analysis"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric(
                        "Average Opportunity Score",
                        f"{cat_opportunity.loc[category, ('opportunity_score', 'mean')]:.1f}/10",
                        help="Average opportunity score for this category"
                    )
                    st.metric(
                        "Total Views",
                        f"{cat_opportunity.loc[category, ('total_views', 'sum')]:,.0f}",
                        help="Total views in this category"
                    )
                
                with col2:
                    st.metric(
                        "Score Range",
                        f"{cat_opportunity.loc[category, ('opportunity_score', 'min')]:.1f} - {cat_opportunity.loc[category, ('opportunity_score', 'max')]:.1f}",
                        help="Range of opportunity scores in this category"
                    )
                    st.metric(
                        "Total Videos",
                        f"{cat_opportunity.loc[category, ('video_count', 'sum')]:,.0f}",
                        help="Number of videos in this category"
                    )
    
    with tab2:
        # Demand score distribution
        fig_demand = px.box(
            metrics,
            x='category',
            y='demand_score',
            color='category',
            color_discrete_map=COLOR_SCHEMES['category_colors'],
            title="Demand Score Distribution by Category",
            points="all"
        )
        st.plotly_chart(fig_demand, use_container_width=True)
    
    # 3. Top Opportunities
    st.header("🎯 Top Content Opportunities")
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        selected_category = st.selectbox(
            "Select Category",
            ["All Categories"] + sorted(metrics['category'].unique().tolist())
        )
    with col2:
        sort_by = st.selectbox(
            "Sort By",
            ["Opportunity Score", "Demand Score", "Total Views", "Engagement Rate"]
        )
    
    # Filter and sort data
    if selected_category != "All Categories":
        display_metrics = metrics[metrics['category'] == selected_category]
    else:
        display_metrics = metrics
    
    sort_columns = {
        "Opportunity Score": "opportunity_score",
        "Demand Score": "demand_score",
        "Total Views": "total_views",
        "Engagement Rate": "avg_engagement"
    }
    
    display_metrics = display_metrics.nlargest(10, sort_columns[sort_by])
    
    # Display top opportunities
    for idx, row in display_metrics.iterrows():
        with st.expander(f"🎯 {row['keyword']} ({row['category']})"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Opportunity Score",
                    f"{row['opportunity_score']:.1f}/10",
                    help="Combined score of demand and engagement"
                )
            with col2:
                st.metric(
                    "Demand Score",
                    f"{row['demand_score']:.1f}/10",
                    help="Measure of audience interest"
                )
            with col3:
                st.metric(
                    "Engagement Rate",
                    f"{row['avg_engagement']:.2f}%",
                    help="Average engagement rate"
                )
            
            st.markdown(f"""
            **Performance Metrics:**
            - Total Views: {row['total_views']:,.0f}
            - Total Videos: {row['video_count']}
            - Average Views per Video: {row['avg_views']:,.0f}
            - Total Likes: {row['total_likes']:,.0f}
            - Total Comments: {row['total_comments']:,.0f}
            """)
    
    # 4. Strategic Recommendations
    st.header("💡 Strategic Recommendations")
    
    recommendations = {
        "High Opportunity Keywords": {
            "description": "Keywords with high demand but relatively low competition",
            "metrics": metrics[metrics['opportunity_score'] > metrics['opportunity_score'].quantile(0.75)]
        },
        "Emerging Topics": {
            "description": "Topics showing strong growth potential",
            "metrics": metrics[metrics['demand_score'] > metrics['demand_score'].quantile(0.75)]
        },
        "Underserved Categories": {
            "description": "Categories with high demand but limited content",
            "metrics": metrics[metrics['video_count'] < metrics['video_count'].quantile(0.25)]
        }
    }
    
    for rec_type, data in recommendations.items():
        with st.expander(f"📌 {rec_type}"):
            st.write(data["description"])
            st.dataframe(
                data["metrics"][['keyword', 'category', 'opportunity_score', 'demand_score', 'total_views', 'avg_engagement']]
                .sort_values('opportunity_score', ascending=False)
                .head(5)
                .style.format({
                    'opportunity_score': '{:.1f}',
                    'demand_score': '{:.1f}',
                    'total_views': '{:,.0f}',
                    'avg_engagement': '{:.2f}%'
                })
            )

# Update Analysis Page
elif page == "Update Analysis":
    st.title("🔄 Update Analysis with New Data")
    
    st.markdown("""
    Upload a new CSV file to update or compare the analysis. The file should follow the same structure 
    as the original dataset with the following columns:
    - video_id
    - published_date
    - view_count
    - like_count
    - comment_count
    - keyword
    - category
    - duration_seconds
    - engagement_rate
    """)
    
    # File upload section
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            # Load new data
            new_df = pd.read_csv(uploaded_file)
            new_df['published_date'] = pd.to_datetime(new_df['published_date'])
            
            st.success("File successfully loaded! 🎉")
            
            # Display data overview
            st.subheader("📊 New Data Overview")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Videos", len(new_df))
            with col2:
                st.metric("Date Range", f"{new_df['published_date'].min().date()} to {new_df['published_date'].max().date()}")
            with col3:
                st.metric("Total Categories", len(new_df['category'].unique()))
            
            # Compare with original data
            st.subheader("📈 Comparative Analysis")
            
            tab1, tab2, tab3 = st.tabs(["Data Comparison", "Category Distribution", "Engagement Analysis"])
            
            with tab1:
                comparison_df = pd.DataFrame({
                    'Metric': ['Total Videos', 'Total Views', 'Average Engagement Rate'],
                    'Original Data': [
                        len(df),
                        df['view_count'].sum(),
                        df['engagement_rate'].mean()
                    ],
                    'New Data': [
                        len(new_df),
                        new_df['view_count'].sum(),
                        new_df['engagement_rate'].mean()
                    ]
                })
                
                st.dataframe(
                    comparison_df.style.format({
                        'Original Data': lambda x: f'{x:,.0f}' if isinstance(x, (int, float)) else x,
                        'New Data': lambda x: f'{x:,.0f}' if isinstance(x, (int, float)) else x
                    })
                )
            
            with tab2:
                # Category distribution comparison
                fig = go.Figure()
                
                # Original data
                cat_dist_orig = df['category'].value_counts()
                fig.add_trace(go.Bar(
                    name='Original Data',
                    x=cat_dist_orig.index,
                    y=cat_dist_orig.values,
                    marker_color='rgba(78, 205, 196, 0.7)'
                ))
                
                # New data
                cat_dist_new = new_df['category'].value_counts()
                fig.add_trace(go.Bar(
                    name='New Data',
                    x=cat_dist_new.index,
                    y=cat_dist_new.values,
                    marker_color='rgba(255, 107, 107, 0.7)'
                ))
                
                fig.update_layout(
                    title='Category Distribution Comparison',
                    barmode='group',
                    xaxis_title='Category',
                    yaxis_title='Number of Videos'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with tab3:
                # Engagement analysis
                fig = go.Figure()
                
                # Original data engagement
                fig.add_trace(go.Box(
                    y=df['engagement_rate'],
                    name='Original Data',
                    marker_color='rgba(78, 205, 196, 0.7)'
                ))
                
                # New data engagement
                fig.add_trace(go.Box(
                    y=new_df['engagement_rate'],
                    name='New Data',
                    marker_color='rgba(255, 107, 107, 0.7)'
                ))
                
                fig.update_layout(
                    title='Engagement Rate Distribution Comparison',
                    yaxis_title='Engagement Rate (%)'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            # Option to update the analysis
            st.subheader("🔄 Update Analysis")
            update_option = st.radio(
                "Choose how to handle the new data:",
                ["Replace existing data", "Combine with existing data"]
            )
            
            if st.button("Update Analysis"):
                if update_option == "Replace existing data":
                    df = new_df.copy()
                else:  # Combine with existing data
                    df = pd.concat([df, new_df], ignore_index=True)
                    df = df.drop_duplicates(subset=['video_id'])
                
                st.success("Analysis updated successfully! 🎉")
                st.info("Please navigate to other sections to see the updated analysis.")
                
        except Exception as e:
            st.error(f"""
            Error processing the file: {str(e)}
            
            Please ensure your CSV file has the correct structure and column names:
            - video_id
            - published_date
            - view_count
            - like_count
            - comment_count
            - keyword
            - category
            - duration_seconds
            - engagement_rate
            """)
    
    # Add instructions for data preparation
    with st.expander("📋 Data Preparation Guidelines"):
        st.markdown("""
        ### Required Data Format
        
        Your CSV file should contain the following columns:
        
        | Column Name | Data Type | Description |
        |------------|-----------|-------------|
        | video_id | string | Unique identifier for each video |
        | published_date | datetime | Publication date of the video |
        | view_count | integer | Number of views |
        | like_count | integer | Number of likes |
        | comment_count | integer | Number of comments |
        | keyword | string | Associated keyword |
        | category | string | Category (Modern/Current/Old) |
        | duration_seconds | integer | Video duration in seconds |
        | engagement_rate | float | Engagement rate percentage |
        
        ### Data Processing Tips
        1. Ensure all dates are in a consistent format (YYYY-MM-DD)
        2. Remove any duplicate video entries
        3. Clean any missing or invalid values
        4. Verify category names match existing categories
        """)

# Code References Page
elif page == "Code References":
    st.title("📚 Code References & Inspiration")
    
    st.markdown("""
    This dashboard's code was inspired by and adapted from various sources. We believe in giving credit 
    where it's due and encouraging learning from the community.
    """)
    
    # Opportunity Analysis Matrix
    with st.expander("🎯 Opportunity Analysis Matrix", expanded=True):
        st.markdown("""
        ### Matrix Visualization and Analysis
        - [Plotly Quadrant Chart Tutorial](https://plotly.com/python/v3/ipython-notebooks/scoreboard-heatmaps/)
        - [Streamlit Plotly Guide](https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart)
        - [YT MetricsAnalysis](https://keywordseverywhere.com/)
        - [Opportunity Score](https://medium.com/uxr-microsoft/what-is-the-opportunity-score-and-how-to-calculate-it-part-ii-59bbadbdd2ad/)
                    
        """)
    
    # Data Processing & Metrics
    with st.expander("📊 Data Processing & Metrics", expanded=True):
        st.markdown("""
        ### API and Data Handling
        - [YouTube Data API Documentation](https://developers.google.com/youtube/v3/docs)
        - [Pandas Pivot Table Guide](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)
        - [Storyly: Engagement Rate Calculation](https://www.storyly.io/post/how-to-calculate-engagement-rate)
        
        These resources were crucial in developing our data collection and processing pipeline, 
        especially in handling YouTube API data efficiently.
        """)
    
    # Dashboard Design
    with st.expander("🎨 Dashboard Design", expanded=True):
        st.markdown("""
        ### UI/UX Framework
        - [Streamlit Documentation](https://docs.streamlit.io/)
        - [Streamlit Components Gallery](https://streamlit.io/components)
        - [Streamlit Layout Guide](https://docs.streamlit.io/library/api-reference/layout)
        
        The dashboard's user interface was built using Streamlit, with inspiration from these official 
        resources and community examples.
        """)
    
    # Visualization Techniques
    with st.expander("📈 Visualization Techniques", expanded=True):
        st.markdown("""
        ### Interactive Visualizations
        - [Plotly Express Documentation](https://plotly.com/python/plotly-express/)
        - [Plotly Graph Objects](https://plotly.com/python/graph-objects/)
        - [Streamlit Metrics Guide](https://docs.streamlit.io/library/api-reference/data/st.metric)
        
        Our interactive charts and visualizations were created using Plotly, following best practices 
        from these documentation sources.
        """)
    
    # Style & UI/UX
    with st.expander("🎭 Style & UI/UX", expanded=True):
        st.markdown("""
        ### Visual Design
        - [Streamlit Custom Themes](https://docs.streamlit.io/library/advanced-features/theming)
        - [Streamlit CSS Guide](https://docs.streamlit.io/library/api-reference/style)
        - [Material Design Color System](https://material.io/design/color/the-color-system.html)
        
        The dashboard's visual style was influenced by Material Design principles and implemented using 
        Streamlit's theming capabilities.
        """)
    
    # Additional Resources
    with st.expander("📚 Additional Resources", expanded=True):
        st.markdown("""
        ### API and Data Management
        - [Real Python: API Integration](https://realpython.com/api-integration-in-python/)
        - [Python Code: YouTube API Tutorial](https://thepythoncode.com/article/using-youtube-api-in-python)
        - [Peer DH: API Request Quotas](https://peerdh.com/blogs/programming-insights/managing-api-request-quotas-in-python)
        
        These additional resources provided valuable insights into API integration and data management 
        best practices.
        """)
    
    # Acknowledgment Note
    st.markdown("""
    ---
    ### 🙏 Acknowledgments
    
    We extend our gratitude to all the creators and maintainers of these resources. Their work has been 
    instrumental in building this dashboard and making complex data analysis more accessible.
    
    If you're interested in learning more about any specific aspect of this project, we encourage you to 
    explore these references.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Created with ❤️ StreamLit and Plotly by Nadim Khan and Samaneh Javidian</p>
</div>
""", unsafe_allow_html=True)