import pandas as pd

def load_data(file_path):
    """Load data from CSV."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def process_data(data):
    """Perform data processing."""
    print("Processing data...")
    # You can process or clean data here if needed
    return data.describe()


if __name__ == "__main__":
    # Load the data
    file_path = '../src/solar_data.csv'
    data = load_data(file_path)
    
    # Process data
    if data is not None:
        stats = process_data(data)
        print(stats)
