import pandas as pd
import numpy as np

# Define a date range for hourly data (e.g., 48 hours for two days)
date_range = pd.date_range(start="2023-01-01", periods=48, freq="H")

# Generate synthetic data
data = {
    "Timestamp": date_range,
    "GHI": np.random.uniform(150, 300, len(date_range)),  # Global Horizontal Irradiance
    "DNI": np.random.uniform(100, 250, len(date_range)),  # Direct Normal Irradiance
    "DHI": np.random.uniform(50, 100, len(date_range)),   # Diffuse Horizontal Irradiance
    "ModA": np.random.uniform(100, 200, len(date_range)), # Sensor Module A
    "ModB": np.random.uniform(100, 200, len(date_range)), # Sensor Module B
    "Tamb": np.random.uniform(10, 35, len(date_range)),   # Ambient Temperature
    "RH": np.random.uniform(30, 80, len(date_range)),     # Relative Humidity
    "WS": np.random.uniform(1, 8, len(date_range)),       # Wind Speed
    "WSgust": np.random.uniform(2, 12, len(date_range)),  # Maximum Wind Gust Speed
    "WSstdev": np.random.uniform(0.5, 3, len(date_range)), # Wind Speed Std Dev
    "WD": np.random.uniform(0, 360, len(date_range)),     # Wind Direction
    "WDstdev": np.random.uniform(5, 15, len(date_range)), # Wind Direction Std Dev
    "BP": np.random.uniform(950, 1050, len(date_range)),  # Barometric Pressure
    "Cleaning": np.random.choice([0, 1], len(date_range)), # Cleaning Events
    "Precipitation": np.random.uniform(0, 2, len(date_range)), # Precipitation rate
    "TModA": np.random.uniform(10, 30, len(date_range)),  # Module A Temperature
    "TModB": np.random.uniform(10, 30, len(date_range)),  # Module B Temperature
    "Comments": ["No issues"] * len(date_range)           # Placeholder comments
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv("solar_data.csv", index=False)

print("Dataset generated and saved as 'solar_data.csv'.")
