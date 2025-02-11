from fastapi import FastAPI
from pydantic import BaseModel
from anomaly_detector import detect_anomalies
import pandas as pd 
import numpy as np
import io

app = FastAPI()

class LogEntry(BaseModel):
    timestamp: str
    status_code: int
    response_time: int
    user_agent: str

@app.post("/detect-anomaly/")
async def detect_anomaly(log_entry: LogEntry):
    # Convert the input data into a DataFrame
    data = pd.DataFrame([log_entry.dict() for log_entry in log_entry])
    
    # Detect anomalies
    anomalies = detect_anomalies(data)
    
    return {"anomalies": anomalies.tolist()}

@app.get("/")
def read_root():
    return {"message": "Anomaly Detection API is running!"} 



#print("BEJI")