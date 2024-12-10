# Weekly Challenge Submissions

This repository contains separate Jupyter Notebook files addressing the Week 0 challenges in data analysis. The following notebooks are included:

- `eda_correlation_analysis.ipynb`
- `eda_bubble_charts.ipynb`
- `eda_data_quality_check.ipynb`
- `eda_histograms.ipynb`
- `eda_summary_statistics.ipynb`
- `eda_temperature_analysis.ipynb`
- `eda_time_series_analysis.ipynb`
- `eda_wind_analysis.ipynb`
- `eda_z_score_analysis.ipynb`

## Challenge Tasks Overview

Each notebook addresses specific tasks outlined in the challenge objectives:

### Summary Statistics
- Calculate the mean, median, standard deviation, and other statistical measures for each numeric column to understand data distribution.

### Data Quality Check
- Look for missing values, outliers, or incorrect entries (e.g., negative values in GHI, DNI, DHI).
- Check for outliers, especially in sensor readings (ModA, ModB) and wind speed data (WS, WSgust).

### Time Series Analysis
- Plot bar charts or line charts of GHI, DNI, DHI, and Tamb over time.
- Analyze patterns by month, trends throughout the day, or anomalies in solar irradiance or temperature fluctuations.
- Evaluate the impact of cleaning (using the 'Cleaning' column) on sensor readings (ModA, ModB) over time.

### Correlation Analysis
- Use correlation matrices or pair plots to visualize correlations between solar radiation components (GHI, DNI, DHI) and temperature measures (TModA, TModB).
- Investigate relationships between wind conditions (WS, WSgust, WD) and solar irradiance using scatter matrices.

### Wind Analysis
- Use radial bar plots or wind roses to identify trends and significant wind events.
- Show the distribution of wind speed and direction, along with variability in wind direction.

### Temperature Analysis
- Examine how relative humidity (RH) influences temperature readings and solar radiation.

### Histograms
- Create histograms for GHI, DNI, DHI, WS, and temperature variables to visualize frequency distributions.

### Z-Score Analysis
- Calculate Z-scores to flag data points significantly different from the mean.

### Bubble Charts
- Explore relationships between GHI, Tamb, and WS, with bubble size representing an additional variable like RH or BP (Barometric Pressure).


All tasks listed above are completed under each file separately.