# Data Cleaning Script

This script, `clean_data.py`, is designed to perform data cleaning tasks on the datasets used in the weekly challenge submissions.

## Overview

The script focuses on ensuring data quality by addressing anomalies and missing values in the dataset. Specifically, it targets columns that may contain problematic entries, such as the `Comments` column, which appears entirely null.

### Data Cleaning Tasks

- **Handling Missing Values**: The script identifies and addresses missing values in the dataset to ensure that the analysis is based on complete data.
  
- **Anomaly Detection**: It checks for anomalies in the data, ensuring that the values fall within expected ranges and conform to the dataset's requirements.

- **Comments Column**: Special attention is given to the `Comments` column, which contains entirely null values, to determine how to best handle or remove this data.

## Usage

To run the script, ensure you have the necessary libraries installed and execute the following command in your terminal:

```bash
python scripts/clean_data.py