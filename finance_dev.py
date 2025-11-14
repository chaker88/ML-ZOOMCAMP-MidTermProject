import requests

url = "https://loan-prediction-3kej.onrender.com/predict"



customer_data = {'person_education': 'High School',
 'person_home_ownership': 'RENT',
 'loan_intent': 'MEDICAL',
 'previous_loan_defaults_on_file': 0,
 'person_income': 76364.0,
 'loan_amnt': 21000.0,
 'loan_int_rate': 11.36,
 'loan_percent_income': 0.27,
 'cb_person_cred_hist_length': 2.0,
 'credit_score': 645}

response = requests.post(url, json=customer_data)
prediction = response.json()
print(prediction)
if prediction["result"] == 1:
    print(f'The model predicts that the customer will not default on the loan with a probability of {round(prediction["prediction"], 3)}.')
else:
    print(f'The model predicts that the customer will default on the loan with a probability of {round(prediction["prediction"], 3)}.')
