import pandas as pd

def preprocess_logs(file_path):
    """Load and preprocess logs for anomaly detection."""
    df = pd.read_csv(file_path)
    print(df.head())
    # Feature extraction & transformation logic
    return df

#print ("beji")

logs = preprocess_logs('../data/mock_logs.csv')