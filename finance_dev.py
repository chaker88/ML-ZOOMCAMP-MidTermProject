import requests


url = "http://localhost:9696/predict"

customer_data = {
    "person_education": "Bachelor",
    "person_home_ownership": "MORTGAGE",
    "loan_intent": "EDUCATION",
    "previous_loan_defaults_on_file": 1,
    "person_income": 10000,
    "loan_amnt": 10000,
    "loan_int_rate": 12.0,
    "loan_percent_income": 20,
    "cb_person_cred_hist_length": 5,
    "credit_score": 300
}

response = requests.post(url,json= customer_data)

prediction = response.json()

if prediction[r"result"] == 1:
    print(f"The model predicts that the customer will default on the loan with a probability of {round(prediction["prediction"],3)}.")
else:
    print(f"The model predicts that the customer will NOT default on the loan with a probability of {round(prediction["prediction"],3)}")