import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# Set the page configuration
st.set_page_config(page_title="Solar Data Insights Dashboard", layout="wide")

# Title and description
st.title("Solar Data Insights Dashboard")
st.write("""
Visualizing solar radiation data and weather patterns with interactive features.
Use sliders and date range selectors to customize insights dynamically.
""")


# Load data with caching
@st.cache_data
def load_data():
    """Load data from CSV and preprocess it."""
    try:
        data = pd.read_csv("src/solar_data.csv")
        # Ensure Timestamp is converted to datetime
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
        # Normalize column names
        data.columns = data.columns.str.strip()  # Remove unwanted spaces
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()


# Load the data
data = load_data()

# Debugging: Display column names for user inspection
st.write("### Available Columns in Data")
st.write(data.columns)

# If data didn't load, stop execution
if data.empty:
    st.warning("No data available to process. Please check the provided CSV data.")
else:
    # Allow users to select date range dynamically
    min_date, max_date = data['Timestamp'].min(), data['Timestamp'].max()
    selected_date_range = st.date_input(
        "Select Date Range",
        [min_date.date(), max_date.date()],
        min_value=min_date.date(),
        max_value=max_date.date(),
    )

    # Filter the data based on selected date range
    filtered_data = data[
        (data['Timestamp'].dt.date >= selected_date_range[0]) &
        (data['Timestamp'].dt.date <= selected_date_range[1])
    ]

    # Debugging: Visualize the filtered data table
    st.write("### Filtered Data Preview")
    st.write(filtered_data)

    # Create dynamic sliders for thresholds
    st.write("### Customize Insights")
    if 'Solar_Radiation' in filtered_data.columns:
        min_solar = float(filtered_data['Solar_Radiation'].min())
        max_solar = float(filtered_data['Solar_Radiation'].max())
        
        user_min_threshold = st.slider(
            "Set Minimum Solar Radiation Threshold",
            min_value=int(min_solar),
            max_value=int(max_solar),
            value=int(min_solar),
        )

        # Filter data based on slider threshold
        custom_filtered_data = filtered_data[filtered_data['Solar_Radiation'] >= user_min_threshold]
    else:
        st.error("Column `Solar_Radiation` is missing from the filtered data.")
        custom_filtered_data = pd.DataFrame()

    # Visualization Section: Solar Radiation Insights
    if not custom_filtered_data.empty:
        st.write("### Solar Radiation Insights")
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.lineplot(x="Timestamp", y="Solar_Radiation", data=custom_filtered_data)
        plt.xlabel("Timestamp")
        plt.ylabel("Solar Radiation (units)")
        plt.title("Solar Radiation Over Time (Filtered)")
        st.pyplot(plt)
    else:
        st.write("No solar radiation data to visualize with current filters.")

    # Visualization Section: Temperature Insights
    if 'Temperature' in filtered_data.columns:
        st.write("### Temperature Insights")
        plt.figure(figsize=(12, 6))
        sns.lineplot(x="Timestamp", y="Temperature", data=filtered_data)
        plt.xlabel("Timestamp")
        plt.ylabel("Temperature (°C)")
        plt.title("Temperature Trends Over Time")
        st.pyplot(plt)
    else:
        st.warning("Temperature data is missing in the selected range.")

    # Additional Insights (Optional)
    st.write("""
    Explore further visualizations or integrate machine learning models in the future.
    Dynamic simulation with prediction models can be built using these visualizations.
    """)

