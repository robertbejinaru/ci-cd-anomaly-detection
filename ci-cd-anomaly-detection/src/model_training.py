from joblib import dump
from sklearn.ensemble import IsolationForest

def train_model(data):
    """Train an anomaly detection model."""
    model = IsolationForest()
    model.fit(data)
    dump(model, "models/anomaly_model.joblib")
    print("Model saved successfully!")

#print("BEJI")