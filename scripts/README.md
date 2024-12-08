1. Load the data
The script loads data from the file path ../src/solar_data.csv. The function load_data() takes care of:

Reading the CSV file.
Catching exceptions in case the file doesn't exist or is unreadable.

2. Process data
The function process_data() is responsible for computing statistical summaries. The data.describe() method generates statistics across all numeric columns in the loaded dataset.


3. Main execution

Data loading by calling load_data.
If data is successfully loaded, the script processes it and prints the statistical summaries.

🏆 Key Features
Robust data loading:

The script uses exception handling to ensure invalid paths or non-existent files are handled gracefully.
Data statistics via pandas.describe():

Computes statistical summaries like mean, standard deviation, min, max, and percentiles for each numerical column in the dataset.
Ease of use:

Simply run the script to compute statistical summaries and visualize key insights into the dataset.
