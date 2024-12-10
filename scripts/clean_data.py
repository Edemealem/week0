import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

def load_data(file_path):
    return pd.read_csv(file_path)

def missing_values(df, action='report', fill_value=None):
    """
    Check for missing values in the DataFrame.
    
    Parameters:
    - df: pandas DataFrame
    - action: 'report', 'drop', or 'fill' (default is 'report')
    - fill_value: value to fill missing data if action is 'fill'
    
    Returns:
    - DataFrame with missing values handled according to the specified action
    """
    if action == 'report':
        return df.isnull().sum()
    
    elif action == 'drop':
        return df.dropna()
    
    elif action == 'fill':
        if fill_value is not None:
            return df.fillna(fill_value)
        else:
            raise ValueError("fill_value must be provided when action is 'fill'")
    
    else:
        raise ValueError("Invalid action. Choose 'report', 'drop', or 'fill'.")

def clean_data(df):
    """Clean the dataset by handling missing values and anomalies."""
    
    # Report missing values
    missing_report = missing_values(df, action='drop')
    print("Missing values report:\n", missing_report)
    

    df = missing_values(df, action='fill', fill_value='No comments') 
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        df = df[(df[col] >= (q1 - 1.5 * iqr)) & (df[col] <= (q3 + 1.5 * iqr))]
    
    return df

def save_data(df, file_path):
    """Save the cleaned dataset to a CSV file."""
    df.to_csv(file_path, index=False)

def main():
    # Paths to the datasets
    paths = {
        'benin': '/content/drive/MyDrive/10Academy/benin-malanville.csv', 
        'sierra_leone': '/content/drive/MyDrive/10Academy/sierraleone-bumbuna.csv',  
        'togo': '/content/drive/MyDrive/10Academy/togo-dapaong_qc.csv'
    }
    
    for name, file_path in paths.items():
        print(f"Processing {name} dataset...")
        df = load_data(file_path)
        cleaned_df = clean_data(df)
        save_data(cleaned_df, f'cleaned_{name}_data.csv')

if __name__ == '__main__':
    main()
