import pandas as pd

try:
    # Load the dataset
    print("Loading data...")
    data = pd.read_csv('solar_data.csv')  # Ensure this is in the same directory or adjust path

    # Output key inspection results
    print("Data loaded successfully!")
    print("\nFirst 5 rows of the data:")
    print(data.head())

    print("\nInformation about the dataset:")
    print(data.info())

    print("\nChecking for missing values:")
    print(data.isnull().sum())

    print("\nSummary statistics:")
    print(data.describe())
except Exception as e:
    print("An error occurred:", e)
