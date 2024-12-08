How to Use
Open analysis.ipynb in Jupyter Notebook.
Execute the cells in order.
The notebook includes steps for:
Data loading
Data preprocessing
Visualization
Correlation analysis
Visualize insights such as:
Time-series analysis patterns over GHI, DNI, DHI, and temperature.
Influence of wind and cleaning on solar readings.
Correlation heatmaps between temperature, humidity, and solar radiation data.
🏆 Key Features
Time-Series Analysis:

Analyze solar radiation patterns over time.
Plot trends of GHI, DNI, DHI, and ambient temperature (Tamb) across time.
Correlation Analysis:

Compute correlations between GHI, DNI, DHI, temperature, and wind measurements.
Visualize correlations with heatmaps and scatter plots.
Wind Conditions' Influence:

Analyze how wind patterns (e.g., WS gusts, wind direction) affect solar irradiance.
Cleaning Impact:

Investigate the effect of cleaning cycles on solar panel measurements using environmental data.
💡 How It Works
Loading & Preprocessing:

Normalize column names.
Handle missing or incomplete data with placeholders where necessary.
Time-Series Visualizations:

Using Seaborn and Matplotlib to visualize patterns in solar radiation over time.
Correlation Heatmaps & Scatter Analysis:

Statistical computations using pandas.DataFrame.corr() and visualizations using seaborn.heatmap() and seaborn.scatterplot().
Interactive Visualization:

Visualization outputs are generated in cells after computations.