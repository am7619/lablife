# LabLife - Biological Age Predictor
Predict your biological age from 29 standard laboratory values using modern machine learning techniques.
ML Zoomcamp 2025

## Problem description
How to assess the age of your patient? Asking is far too easy, right? Don´t look further, you have found the perfect solution. **LabLife** predicts the biological age from 29 common laboratory results. If your predicted age is lower than your chronological one — congratulations, your body might be in excellent shape (according to the all-knowing lab).
Does it make sense? Try it and find out!

### Dataset description
The data is from https://github.com/higgi13425/medicaldata/raw/refs/heads/master/data/thiomon.rda


 'wbc': 'White Blood Cells (10^9/L)',
    'hgb': 'Hemoglobin (g/dL)',
    'hct': 'Hematocrit (%)',
    'plt': 'Platelets (10^9/L)',
    'rbc': 'Red Blood Cells (10^12/L)',
    'mcv': 'MCV (fL)',
    'mch': 'MCH (pg)',
    'mchc': 'MCHC (g/dL)',
    'rdw': 'RDW (%)',
    'mpv': 'Mean Platelet Volume (fL)',
    'neut_percent': 'Neutrophils (%)',
    'lymph_percent': 'Lymphocytes (%)',
    'mono_percent': 'Monocytes (%)',
    'eos_percent': 'Eosinophils (%)',
    'baso_percent': 'Basophils (%)',
    'sod': 'Sodium (mmol/L)',
    'pot': 'Potassium (mmol/L)',
    'chlor': 'Chloride (mmol/L)',
    'co2': 'CO2 (mmHg)',
    'un': 'Urea Nitrogen (mg/dL)',
    'creat': 'Creatinine (mg/dL)',
    'gluc': 'Glucose (mg/dL)',
    'cal': 'Calcium (mg/dL)',
    'prot': 'Total Protein (g/dL)',
    'alb': 'Albumin (g/dL)',
    'ast': 'AST (U/L)',
    'alt': 'ALT (U/L)',
    'alk': 'Alkaline Phosphatase (U/L)',
    'tbil': 'Total Bilirubin (mg/dL)'

## Jupyter Notebook
The notebook leads through the process of creating the model including
- *Data preparation* (loading, cleaning, encoding)
- *Exporatory Data Analysis EDA* (desciptive statistics, histograms, correlation matrix)
- *Comparison of three models* (`LinearRegression`, `RandomForest`, `XGBoost`)
- *Metrics* RMSE comparison and model selection
Calculate RMSE for


## Installation
Clone the repo and install dependencies:
`git clone https://github.com/yourusername/lablife.git
cd lablife
pip install -r requirements.txt`

## Docker container
Build and run the prediction API in a container:
`docker build -t lablife .
docker run -d -p 8080:8080 --name lablife lablife`

Test your container:
`curl -X POST http://localhost/predict -H "Content-Type: application/json" -d "{\"wbc\":4.5,\"hgb\":12.8}"`

Response example:
`{"prediction": 42.7}`


## Cloud Deployment
You can deploy `serve.py` as a microservice to:
AWS ECS or Lambda
Google Cloud Run
Azure Container Apps

Make sure to:
Expose port 8080
Pass model file path via environment variable (if required)
Configure HTTPS using a reverse proxy or managed endpoint

## Acknowledgments
Dataset: medicaldata package by higgi13425
https://github.com/higgi13425/medicaldata
Built for educational purposes in the ML Zoomcamp course 2025.