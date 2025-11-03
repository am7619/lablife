from fastapi import FastAPI
import pickle
import numpy as np
import xgboost as xgb
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("model.pkl", "rb") as f_in:
    dv, model = pickle.load(f_in)

app = FastAPI(title="LabLife API", version="1.0")

@app.get("/")
def root():
    return {"message": "API is running. Access from http://localhost/predict"}


@app.post("/predict")
def predict(data: dict):
    X = dv.transform([data])
    prediction = model.predict(X)
    return {"prediction": float(np.round(prediction[0], 3))}
