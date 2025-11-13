import requests

url = "http://localhost:9696/predict"

customer_data = {
    "person_education": "Master",
    "person_home_ownership": "RENT",
    "loan_intent": "PERSONAL",
    "previous_loan_defaults_on_file": 1,
    "person_income": 71948.0,
    "loan_amnt": 35000,
    "loan_int_rate": 16.2,
    "loan_percent_income": 0.49,
    "cb_person_cred_hist_length": 3,
    "credit_score": 561
}

customer_data = {'person_education': 'Master',
    'person_home_ownership': 'RENT',
    'loan_intent': 'PERSONAL',
    'previous_loan_defaults_on_file': 0,
    'person_income': 71948.0,
    'loan_amnt': 35000.0,
    'loan_int_rate': 16.02,
    'loan_percent_income': 0.49,
    'cb_person_cred_hist_length': 3.0,
    'credit_score': 561}

response = requests.post(url, json=customer_data)
prediction = response.json()
print(prediction)
if prediction["result"] == 1:
    print(f'The model predicts that the customer will not default on the loan with a probability of {round(prediction["prediction"], 3)}.')
else:
    print(f'The model predicts that the customer will default on the loan with a probability of {round(prediction["prediction"], 3)}.')
