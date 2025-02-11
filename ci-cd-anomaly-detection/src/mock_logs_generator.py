import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to create mock logs with anomalies
def generate_mock_logs():
    np.random.seed(42)  # For reproducibility
    timestamp = datetime.now()
    data = []
    
    # Generate 1000 log entries
    for _ in range(1000):
        status_code = np.random.choice([200, 404, 500], p=[0.8, 0.1, 0.1])  # 80% success, 10% error
        response_time = np.random.randint(100, 200) if status_code == 200 else np.random.randint(300, 500)  # Higher response time for errors
        user_agent = np.random.choice(['Chrome', 'Firefox', 'Edge'])
        
        # Inject an anomaly: Randomly set a very high response time
        if np.random.rand() < 0.05:  # 5% chance to create an anomaly
            response_time = np.random.randint(1000, 2000)  # Anomalous high response time
        
        log_entry = {
            'timestamp': (timestamp + timedelta(minutes=_)).strftime('%Y-%m-%d %H:%M:%S'),
            'status_code': status_code,
            'response_time': response_time,
            'user_agent': user_agent
        }
        
        data.append(log_entry)
    
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)
    df.to_csv('../data/mock_logs.csv', index=False)
    print("Mock logs generated and saved to 'data/mock_logs.csv'.")

if __name__ == "__main__":
    generate_mock_logs()
