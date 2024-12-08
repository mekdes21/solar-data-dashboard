import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Set the page configuration
st.set_page_config(
    page_title="Solar Data Insights Dashboard",
    layout="wide",
    initial_sidebar_state="auto"
)

# Title and description
st.title("🌞 Solar Data Insights Dashboard")
st.write("""
Visualizing solar radiation, weather trends, and insights with interactive features.
Use sliders, date range selectors, and filters to dynamically view insights into solar radiation and weather patterns.
""")


# Load the data safely with caching
@st.cache_data
def load_data():
    """Load data from CSV and preprocess."""
    try:
        # Define file path
        file_path = os.path.join("src", "solar_data.csv")
        
        # Check if file exists
        if not os.path.exists(file_path):
            st.error(f"Data file not found at: {file_path}")
            return pd.DataFrame()
        
        # Load the CSV
        data = pd.read_csv(file_path)

        # Preprocess the data
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])  # Ensure Timestamp is datetime
        data.columns = data.columns.str.strip()  # Remove spaces from column names
        st.success("Data loaded and preprocessed successfully!")
        return data
    except Exception as e:
        st.error(f"An error occurred while loading data: {e}")
        return pd.DataFrame()


# Load the data
data = load_data()

# Debugging section: Display the columns and first rows of data
st.sidebar.header("📊 Data Information")
if not data.empty:
    st.sidebar.write("### Available Columns in Data")
    st.sidebar.write(data.columns)
else:
    st.sidebar.warning("No data loaded. Please check the data source.")

# Ensure the data has loaded before proceeding
if data.empty:
    st.warning("Data could not be loaded. Please fix data source issues and refresh the page.")
else:
    # Date range selector - Dynamic filtering by user input
    st.sidebar.header("🔎 Select Date Range")
    min_date, max_date = data['Timestamp'].min(), data['Timestamp'].max()
    selected_range = st.sidebar.date_input(
        "Select Date Range",
        [min_date.date(), max_date.date()],
        min_value=min_date.date(),
        max_value=max_date.date(),
    )

    # Filter data by date range
    filtered_data = data[
        (data['Timestamp'].dt.date >= selected_range[0]) &
        (data['Timestamp'].dt.date <= selected_range[1])
    ]

    st.write("### 🗓️ Filtered Data Preview")
    st.dataframe(filtered_data)

    # Dynamic sliders for Solar Radiation Threshold
    st.sidebar.header("🌡️ Customize Insights")
    if 'Solar_Radiation' in filtered_data.columns:
        min_threshold, max_threshold = float(filtered_data['Solar_Radiation'].min()), float(filtered_data['Solar_Radiation'].max())
        user_min_solar_threshold = st.sidebar.slider(
            "Set Minimum Solar Radiation Threshold",
            min_value=int(min_threshold),
            max_value=int(max_threshold),
            value=int(min_threshold),
            step=1,
        )

        # Filter data based on user-defined threshold
        custom_filtered_data = filtered_data[
            filtered_data['Solar_Radiation'] >= user_min_solar_threshold
        ]
    else:
        st.error("Column `Solar_Radiation` not found in data.")
        custom_filtered_data = pd.DataFrame()

    # Visualizations Section
    st.write("## 📈 Insights & Visualizations")

    # Solar Radiation Visualization
    if not custom_filtered_data.empty and 'Solar_Radiation' in custom_filtered_data.columns:
        st.write("### 🌞 Solar Radiation Insights")
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.lineplot(x="Timestamp", y="Solar_Radiation", data=custom_filtered_data)
        plt.xlabel("Timestamp")
        plt.ylabel("Solar Radiation (units)")
        plt.title("Filtered Solar Radiation Over Time")
        st.pyplot(plt)
    else:
        st.info("No solar radiation data matches the current threshold settings.")

    # Temperature Insights
    if 'Temperature' in filtered_data.columns:
        st.write("### 🌡️ Temperature Trends")
        plt.figure(figsize=(12, 6))
        sns.lineplot(x="Timestamp", y="Temperature", data=filtered_data)
        plt.xlabel("Timestamp")
        plt.ylabel("Temperature (°C)")
        plt.title("Temperature Trends Over Time")
        st.pyplot(plt)
    else:
        st.warning("Temperature data is unavailable or missing.")

    # Additional Insights Section
    st.write("""
    Explore other trends and predictions with this visualization dashboard. 
    You can integrate machine learning models in the future to make this even more insightful.
    """)

# Add a footer for the dashboard
st.markdown(
    """
    <hr>
    <div style="text-align: center; font-size: 14px;">
    🛠️ Built with Streamlit | 🚀 Data Visualization | 📊 Dashboard Deployment
    </div>
    """,
    unsafe_allow_html=True
)
