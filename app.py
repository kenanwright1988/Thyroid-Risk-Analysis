import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Thyroid Cancer Risk Analysis",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load the thyroid cancer dataset"""
    try:
        # Try to load the cleaned data first
        df = pd.read_csv('thyroid_cancer_risk_data_cleaned.csv')
        st.success("✅ Loaded cleaned dataset successfully!")
        return df
    except FileNotFoundError:
        try:
            # Fallback to original data
            df = pd.read_csv('thyroid_cancer_risk_data.csv')
            st.success("✅ Loaded original dataset successfully!")
            return df
        except FileNotFoundError:
            # If no data files found, show error and create sample data
            st.error("❌ Data files not found. Creating sample data for demonstration.")
            # Create a small sample dataset for demo purposes
            np.random.seed(42)
            sample_data = {
                'Age': np.random.randint(20, 80, 100),
                'Gender': np.random.choice(['Male', 'Female'], 100),
                'Country': np.random.choice(['USA', 'UK', 'Canada', 'Australia'], 100),
                'Thyroid Cancer Risk': np.random.choice(['Low', 'Medium', 'High'], 100),
                'TSH': np.random.uniform(0.5, 5.0, 100),
                'T3': np.random.uniform(80, 200, 100),
                'T4': np.random.uniform(5, 15, 100)
            }
            return pd.DataFrame(sample_data)
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        return None

def main():
    # Add a loading indicator
    with st.spinner("🏥 Loading Thyroid Cancer Risk Analysis Dashboard..."):
        # Header
        st.markdown('<h1 class="main-header">🏥 Thyroid Cancer Risk Analysis Dashboard</h1>', unsafe_allow_html=True)
        
        # Load data
        df = load_data()
        
        if df is None:
            st.stop()
        
        # Show success message
        st.success("✅ Dashboard loaded successfully!")
        
        # Sidebar
        st.sidebar.title("Navigation")
        page = st.sidebar.selectbox("Choose a section:", [
            "Overview",
            "Data Exploration",
            "Risk Factor Analysis",
            "Demographic Analysis",
            "Predictive Modeling",
            "Key Insights"
        ])
        
        if page == "Overview":
            show_overview(df)
        elif page == "Data Exploration":
            show_data_exploration(df)
        elif page == "Risk Factor Analysis":
            show_risk_factor_analysis(df)
        elif page == "Demographic Analysis":
            show_demographic_analysis(df)
        elif page == "Predictive Modeling":
            show_predictive_modeling(df)
        elif page == "Key Insights":
            show_key_insights(df)

def show_overview(df):
    st.header("📊 Project Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", f"{len(df):,}")
    
    with col2:
        st.metric("Features", len(df.columns))
    
    with col3:
        if 'Thyroid Cancer Risk' in df.columns:
            high_risk = len(df[df['Thyroid Cancer Risk'] == 'High'])
            st.metric("High Risk Cases", f"{high_risk:,}")
        else:
            st.metric("Data Columns", len(df.columns))
    
    with col4:
        missing_data = df.isnull().sum().sum()
        st.metric("Missing Values", f"{missing_data:,}")
    
    st.markdown("---")
    
    st.markdown("""
    ### About This Analysis
    
    This dashboard provides a comprehensive analysis of thyroid cancer risk factors using a dataset of over 200,000 records. 
    The analysis focuses on:
    
    - **Demographic Impact**: Age, gender, and ethnicity variations
    - **Geographic Distribution**: Risk patterns across different countries
    - **Medical Indicators**: TSH, T3, T4 levels and their correlation with risk
    - **Environmental Factors**: Radiation exposure, iodine deficiency
    - **Lifestyle Factors**: Smoking, obesity, diabetes impact
    
    Navigate through the sections using the sidebar to explore different aspects of the analysis.
    """)
    
    # Display sample data
    st.subheader("📋 Dataset Sample")
    st.dataframe(df.head(10))

def show_data_exploration(df):
    st.header("🔍 Data Exploration")
    
    # Dataset info
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dataset Information")
        buffer = []
        buffer.append(f"Shape: {df.shape}")
        buffer.append(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")
        st.text("\n".join(buffer))
        
        # Data types
        st.subheader("Data Types")
        st.dataframe(df.dtypes.to_frame("Data Type"))
    
    with col2:
        st.subheader("Missing Values")
        missing_data = df.isnull().sum()
        missing_data = missing_data[missing_data > 0].sort_values(ascending=False)
        
        if len(missing_data) > 0:
            fig = px.bar(x=missing_data.index, y=missing_data.values,
                        title="Missing Values by Column")
            fig.update_layout(xaxis_title="Columns", yaxis_title="Missing Count")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.success("No missing values found!")
    
    # Statistical summary
    st.subheader("📈 Statistical Summary")
    st.dataframe(df.describe())

def show_risk_factor_analysis(df):
    st.header("⚠️ Risk Factor Analysis")
    
    # This is a placeholder - you'll need to customize based on your actual column names
    st.markdown("This section will analyze various risk factors for thyroid cancer.")
    
    if 'Thyroid Cancer Risk' in df.columns:
        # Risk distribution
        risk_counts = df['Thyroid Cancer Risk'].value_counts()
        fig = px.pie(values=risk_counts.values, names=risk_counts.index,
                    title="Distribution of Thyroid Cancer Risk Levels")
        st.plotly_chart(fig, use_container_width=True)
    
    # Add more analysis based on your actual data columns
    st.info("Please customize this section based on your specific dataset columns.")

def show_demographic_analysis(df):
    st.header("👥 Demographic Analysis")
    
    st.markdown("Analysis of thyroid cancer risk across different demographic groups.")
    
    # Placeholder for demographic analysis
    # You'll need to customize this based on your actual column names
    if 'Gender' in df.columns:
        gender_dist = df['Gender'].value_counts()
        fig = px.bar(x=gender_dist.index, y=gender_dist.values,
                    title="Gender Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    st.info("Please customize this section based on your specific dataset columns.")

def show_predictive_modeling(df):
    st.header("🤖 Predictive Modeling")
    
    st.markdown("Machine learning model for thyroid cancer risk prediction.")
    
    # Placeholder for modeling section
    st.info("This section will contain predictive modeling results once the data structure is analyzed.")

def show_key_insights(df):
    st.header("💡 Key Insights")
    
    st.markdown("""
    ### Main Findings
    
    Based on the thyroid cancer risk analysis, here are the key insights:
    
    1. **Demographic Patterns**: [To be filled based on actual analysis]
    2. **Risk Factors**: [To be filled based on actual analysis]
    3. **Geographic Trends**: [To be filled based on actual analysis]
    4. **Medical Indicators**: [To be filled based on actual analysis]
    
    ### Recommendations
    
    - Early screening for high-risk demographics
    - Environmental factor monitoring
    - Lifestyle modification programs
    
    """)

if __name__ == "__main__":
    main()
