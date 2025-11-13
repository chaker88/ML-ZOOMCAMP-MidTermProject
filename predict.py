import pickle
from fastapi import FastAPI
import uvicorn
import xgboost as xgb
from pydantic import BaseModel, Field
from typing import Literal
import numpy as np

class LoanInputModel(BaseModel):
    person_education: Literal['Bachelor', 'High School', 'Associate', 'Master', 'Doctorate']
    person_home_ownership: Literal['RENT', 'MORTGAGE', 'OWN', 'OTHER']
    loan_intent: Literal['EDUCATION', 'MEDICAL', 'VENTURE', 'PERSONAL', 'DEBTCONSOLIDATION', 'HOMEIMPROVEMENT']
    previous_loan_defaults_on_file: int = Field(..., ge=0, le=1)
    person_income: float = Field(..., ge=0, le=100000)
    loan_amnt: float = Field(..., ge=100, le=100000)
    loan_int_rate: float = Field(..., ge=0, le=100)
    loan_percent_income: float = Field(..., ge=0, le=100)
    cb_person_cred_hist_length: float = Field(..., ge=0, le=100)
    credit_score: float = Field(..., ge=300, le=850)

class PredictionResponseModel(BaseModel):
    prediction: float  # probability
    result: int        # class label

app = FastAPI(title="Loan Default API")

# Load vectorizer
with open('dv.pkl', 'rb') as f_in:
    dv = pickle.load(f_in)

# Load XGBoost model
model = xgb.Booster()
model.load_model('xgb_model.json')

def predict_loan_single(customer_data: list):
    """
    customer_data: list of dicts
    Returns:
        y_pred_proba: predicted probability
        y_pred_class: predicted class (0 or 1)
    """
    X_transformed = dv.transform(customer_data)
    dmatrix = xgb.DMatrix(X_transformed, feature_names=list(dv.get_feature_names_out()))
    y_pred_proba = model.predict(dmatrix)      # probability
    y_pred_class = (y_pred_proba > 0.5).astype(int)
    return y_pred_proba, y_pred_class

@app.post("/predict", response_model=PredictionResponseModel)
def predict_loan(input_data: LoanInputModel):
    customer_data = [input_data.dict()]
    y_pred_proba, y_pred_class = predict_loan_single(customer_data)
    return {
        "prediction": float(y_pred_proba[0]),
        "result": int(y_pred_class[0])
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
