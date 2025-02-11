from joblib import load

def detect_anomalies(data):
    model = load("models/anomaly_model.joblib")
    return model.predict(data)

print("BEJI")