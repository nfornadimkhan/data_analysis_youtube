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
    color: #2E4057;
    font-weight: bold;
    padding-bottom: 20px;
}
h2 { color: #45B7D1; }
h3 { color: #FF6B6B; }
.stAlert { 
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
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

# Sidebar with enhanced styling
st.sidebar.title("🌱 Navigation")
page = st.sidebar.radio(
    "Choose a section",
    ["Overview", "Trend Analysis", "Category Analysis", "Keyword Analysis", "Opportunity Analysis", "Results"]
)

# Overview Page
if page == "Overview":
    st.title("🎯 Plant Breeding YouTube Content Analysis")
    
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
    st.title("Keyword Analysis")
    
    # Keyword search and filtering
    search_term = st.text_input("Search Keywords")
    if search_term:
        filtered_df = df[df['keyword'].str.contains(search_term, case=False)]
    else:
        filtered_df = df
    
    # Keyword metrics
    keyword_metrics = filtered_df.groupby('keyword').agg({
        'view_count': 'mean',
        'engagement_rate': 'mean',
        'video_id': 'count'
    }).reset_index()
    
    fig = px.scatter(keyword_metrics, x='view_count', y='engagement_rate',
                     size='video_id', hover_data=['keyword'],
                     title="Keyword Performance Matrix")
    st.plotly_chart(fig)

# Opportunity Analysis Page
elif page == "Opportunity Analysis":
    st.title("🌱 Content Opportunity Analysis")
    
    def calculate_metrics(df):
        """Calculate comprehensive content metrics"""
        metrics = df.groupby(['category', 'keyword']).agg({
            'view_count': ['sum', 'mean'],
            'like_count': 'sum',
            'comment_count': 'sum',
            'engagement_rate': 'mean',
            'published_date': 'max'
        }).reset_index()
        
        metrics.columns = ['category', 'keyword', 'total_views', 'avg_views', 
                          'total_likes', 'total_comments', 'avg_engagement', 'latest_date']
        
        # Calculate engagement impact
        metrics['engagement_impact'] = (
            metrics['total_likes'] + metrics['total_comments']
        ) / metrics['total_views']
        
        # Calculate scores
        metrics['demand_score'] = (
            0.4 * (metrics['total_views'] / metrics['total_views'].max()) +
            0.4 * (metrics['avg_engagement'] / metrics['avg_engagement'].max()) +
            0.2 * (metrics['engagement_impact'] / metrics['engagement_impact'].max())
        ) * 10
        
        metrics['opportunity_score'] = (
            0.5 * (metrics['avg_engagement'] / metrics['avg_engagement'].max()) +
            0.3 * (metrics['total_views'] / metrics['total_views'].max()) +
            0.2 * (metrics['engagement_impact'] / metrics['engagement_impact'].max())
        ) * 10
        
        return metrics
    
    # Calculate metrics
    metrics = calculate_metrics(df)
    
    # 1. Overview Metrics
    st.header("📊 Market Overview")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Average Demand Score",
            f"{metrics['demand_score'].mean():.1f}/10",
            delta=f"{metrics['demand_score'].std():.1f} σ"
        )
    
    with col2:
        st.metric(
            "Average Opportunity Score",
            f"{metrics['opportunity_score'].mean():.1f}/10",
            delta=f"{metrics['opportunity_score'].std():.1f} σ"
        )
    
    with col3:
        high_potential = metrics[
            (metrics['demand_score'] > metrics['demand_score'].median()) &
            (metrics['opportunity_score'] > metrics['opportunity_score'].median())
        ]
        st.metric(
            "High Potential Keywords",
            len(high_potential),
            delta=f"{len(high_potential)/len(metrics)*100:.1f}%"
        )
    
    
    # 2. Opportunity Distribution
    st.header("📈 Opportunity Distribution")
    
    tab1, tab2 = st.tabs(["Heatmap", "Top Keywords"])
    
    with tab1:
        # Create demand level bins
        metrics['demand_level'] = pd.qcut(
            metrics['demand_score'], 
            q=5, 
            labels=['Very Low', 'Low', 'Medium', 'High', 'Very High']
        )
        
        # Create heatmap
        heatmap_data = metrics.pivot_table(
            index='category',
            columns='demand_level',
            values='opportunity_score',
            aggfunc='mean'
        )
        
        fig_heatmap = go.Figure(go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            colorscale='RdYlGn',
            text=np.round(heatmap_data.values, 1),
            texttemplate='%{text}',
            textfont={"size": 14}
        ))
        
        fig_heatmap.update_layout(
            title="Opportunity Score Distribution",
            height=400
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    with tab2:
        # Top keywords bar chart
        for category in metrics['category'].unique():
            st.subheader(f"📌 {category} Category")
            cat_data = metrics[metrics['category'] == category]
            top_10 = cat_data.nlargest(10, 'opportunity_score')
            
            fig_bar = go.Figure(go.Bar(
                x=top_10['keyword'],
                y=top_10['opportunity_score'],
                marker_color=COLOR_SCHEMES['category_colors'][category],
                hovertemplate=(
                    "<b>%{x}</b><br>" +
                    "Opportunity Score: %{y:.1f}<br>" +
                    "<extra></extra>"
                )
            ))
            
            fig_bar.update_layout(
                height=400,
                xaxis_tickangle=-45
            )
            st.plotly_chart(fig_bar, use_container_width=True)
            
            # Display metrics in a table
            st.write("Detailed Metrics:")
            metrics_df = top_10[['keyword', 'opportunity_score', 'demand_score', 
                               'total_views', 'avg_engagement']].round(2)
            metrics_df.columns = ['Keyword', 'Opportunity Score', 'Demand Score', 
                                'Total Views', 'Avg Engagement (%)']
            st.dataframe(metrics_df, hide_index=True)
    
    # 3. Strategic Insights
    st.header("💡 Strategic Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top Opportunities")
        top_overall = metrics.nlargest(5, 'opportunity_score')
        for _, row in top_overall.iterrows():
            with st.expander(f"🎯 {row['keyword']}"):
                st.write(f"**Category:** {row['category']}")
                st.write(f"**Opportunity Score:** {row['opportunity_score']:.1f}/10")
                st.write(f"**Demand Score:** {row['demand_score']:.1f}/10")
                st.write(f"**Total Views:** {row['total_views']:,.0f}")
                st.write(f"**Engagement Rate:** {row['avg_engagement']:.2f}%")
    
    with col2:
        st.subheader("Category Performance")
        cat_metrics = metrics.groupby('category').agg({
            'opportunity_score': ['mean', 'std'],
            'demand_score': 'mean',
            'total_views': 'sum'
        }).round(2)
        
        for category in cat_metrics.index:
            with st.expander(f"📊 {category}"):
                st.write(f"**Avg Opportunity Score:** {cat_metrics.loc[category, ('opportunity_score', 'mean')]:.1f}/10")
                st.write(f"**Score Variation:** ±{cat_metrics.loc[category, ('opportunity_score', 'std')]:.1f}")
                st.write(f"**Avg Demand Score:** {cat_metrics.loc[category, ('demand_score', 'mean')]:.1f}/10")
                st.write(f"**Total Views:** {cat_metrics.loc[category, ('total_views', 'sum')]:,.0f}")

# Results Analysis Page
elif page == "Results":
    st.title("📊 Key Findings and Results")
    
    # 1. Category Performance Overview
    st.header("1. Category Performance Overview")
    
    # Create metrics data
    category_metrics = {
        'Modern': {'views': '3.2M', 'engagement': '5.6%'},
        'Current': {'views': '2.8M', 'engagement': '4.3%'},
        'Old': {'views': '1.9M', 'engagement': '3.2%'}
    }
    
    # Display metrics in columns
    cols = st.columns(3)
    for idx, (category, metrics) in enumerate(category_metrics.items()):
        with cols[idx]:
            st.markdown(f"### {category}")
            st.metric("Total Views", metrics['views'])
            st.metric("Engagement Rate", metrics['engagement'])
    
    # 2. Demand Score Analysis
    st.header("2. Demand Score Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Calculate demand scores
        demand_metrics = df.groupby('category').agg({
            'view_count': 'mean',
            'engagement_rate': 'mean'
        }).reset_index()
        
        # Normalize and calculate demand score
        demand_metrics['normalized_views'] = demand_metrics['view_count'] / demand_metrics['view_count'].mean()
        demand_metrics['normalized_engagement'] = demand_metrics['engagement_rate'] / demand_metrics['engagement_rate'].mean()
        demand_metrics['demand_score'] = (
            demand_metrics['normalized_views'] * 0.6 + 
            demand_metrics['normalized_engagement'] * 0.4
        )
        
        fig_demand = px.bar(demand_metrics, 
                          x='category', 
                          y='demand_score',
                          color='category',
                          color_discrete_map=COLOR_SCHEMES['category_colors'],
                          title="Demand Score by Category")
        st.plotly_chart(fig_demand, use_container_width=True)
    
    with col2:
        # Top keywords by engagement
        top_keywords = df.groupby('keyword').agg({
            'view_count': 'sum',
            'engagement_rate': 'mean'
        }).nlargest(10, 'engagement_rate').reset_index()
        
        fig_keywords = px.scatter(top_keywords,
                                x='view_count',
                                y='engagement_rate',
                                text='keyword',
                                title="Top Keywords by Engagement",
                                labels={'view_count': 'Total Views',
                                       'engagement_rate': 'Engagement Rate (%)'},
                                size='view_count')
        fig_keywords.update_traces(textposition='top center')
        st.plotly_chart(fig_keywords, use_container_width=True)
    
    # 3. Content Opportunity Analysis
    st.header("3. Content Opportunity Analysis")
    
    # Calculate opportunity scores
    opportunity_metrics = df.groupby(['category', 'keyword']).agg({
        'view_count': ['sum', 'count'],
        'engagement_rate': 'mean'
    }).reset_index()
    
    opportunity_metrics.columns = ['category', 'keyword', 'total_views', 'video_count', 'avg_engagement']
    
    # Calculate demand and supply scores
    opportunity_metrics['demand_score'] = (
        (opportunity_metrics['total_views'] / opportunity_metrics['total_views'].mean()) * 0.6 +
        (opportunity_metrics['avg_engagement'] / opportunity_metrics['avg_engagement'].mean()) * 0.4
    )
    
    opportunity_metrics['supply_score'] = opportunity_metrics['video_count'] / opportunity_metrics['video_count'].mean()
    opportunity_metrics['opportunity_score'] = opportunity_metrics['demand_score'] / opportunity_metrics['supply_score']
    
    # Display top opportunities
    st.subheader("Top Content Opportunities")
    top_opportunities = opportunity_metrics.nlargest(10, 'opportunity_score')
    
    fig_opportunities = px.scatter(top_opportunities,
                                 x='demand_score',
                                 y='supply_score',
                                 color='category',
                                 size='opportunity_score',
                                 text='keyword',
                                 color_discrete_map=COLOR_SCHEMES['category_colors'],
                                 title="Top 10 Content Opportunities",
                                 labels={'demand_score': 'Demand Score',
                                       'supply_score': 'Supply Score'})
    
    fig_opportunities.update_traces(textposition='top center')
    st.plotly_chart(fig_opportunities, use_container_width=True)
    
    # 4. Key Recommendations
    st.header("4. Key Recommendations")
    
    recommendations = [
        {
            "title": "Focus on Modern Topics",
            "description": "Prioritize content creation for modern topics like CRISPR and AI-based genomic selection, which show highest engagement rates."
        },
        {
            "title": "Balance Content Distribution",
            "description": "While modern topics lead in engagement, maintain coverage of traditional methods which show steady interest."
        },
        {
            "title": "Target High-Opportunity Keywords",
            "description": "Focus on keywords with high demand but low competition for maximum impact."
        },
        {
            "title": "Optimize Content Strategy",
            "description": "Use engaging visuals and simplified explanations for complex topics to increase accessibility."
        }
    ]
    
    cols = st.columns(2)
    for idx, rec in enumerate(recommendations):
        with cols[idx % 2]:
            st.markdown(f"""
            #### {rec['title']}
            {rec['description']}
            """)

# Footer with enhanced styling
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Created with ❤️ StreamLit and Plotly by Nadim Khan and Samaneh Javidian</p>
</div>
""", unsafe_allow_html=True)