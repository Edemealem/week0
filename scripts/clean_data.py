import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def missing_values(df):
    return df.dropna()

def clean_data(df):
    missing_report = df.isnull().sum()
    print("Missing values report:\n", missing_report)
    
    df = missing_values(df)
    
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        df = df[(df[col] >= (q1 - 1.5 * iqr)) & (df[col] <= (q3 + 1.5 * iqr))]
    
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def main():
    paths = {
        'benin': "F:\\10 ACadamy data\\Dataset\\data\\benin-malanville.csv", 
        'sierra_leone': "F:\\10 ACadamy data\\Dataset\\data\\sierraleone-bumbuna.csv",  
        'togo': "F:\\10 ACadamy data\\Dataset\\data\\togo-dapaong_qc.csv"
    }
    
    for name, file_path in paths.items():
        print(f"Processing {name} dataset...")
        df = load_data(file_path)
        cleaned_df = clean_data(df)
        save_data(cleaned_df, f'cleaned_{name}_data.csv')
        print(f"Cleaned data saved as cleaned_{name}_data.csv")

if __name__ == '__main__':
    main()