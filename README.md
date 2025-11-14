# ML-ZOOMCAMP-MidTermProject
This repo is dedicated for the end-to-end midterm project as part of the ML bootcamp delivered by Data Talks taught by Mr Alexey Grigorev

## 📊 About the Dataset

### 1. Data Source
This dataset is a **synthetic version** inspired by the original *Credit Risk* dataset on Kaggle.  
It has been **enriched with additional variables** derived from *Financial Risk for Loan Approval* data.  
To increase data diversity, **SMOTENC** (Synthetic Minority Over-sampling Technique for Nominal and Continuous data) was used to simulate new data points, expanding the dataset size.  

The dataset includes both **categorical** and **continuous** features, structured for credit risk and loan approval analysis.

---

### 2. Metadata
The dataset contains **45,000 records** and **14 variables**.  
Below is the description of each column:

| **Column** | **Description** | **Type** |
|-------------|-----------------|-----------|
| `person_age` | Age of the person | Float |
| `person_gender` | Gender of the person | Categorical |
| `person_education` | Highest education level | Categorical |
| `person_income` | Annual income | Float |
| `person_emp_exp` | Years of employment experience | Integer |
| `person_home_ownership` | Home ownership status (e.g., rent, own, mortgage) | Categorical |
| `loan_amnt` | Loan amount requested | Float |
| `loan_intent` | Purpose of the loan | Categorical |
| `loan_int_rate` | Loan interest rate | Float |
| `loan_percent_income` | Loan amount as a percentage of annual income | Float |
| `cb_person_cred_hist_length` | Length of credit history in years | Float |
| `credit_score` | Credit score of the person | Integer |
| `previous_loan_defaults_on_file` | Indicator of previous loan defaults | Categorical |
| `loan_status` *(target variable)* | Loan approval status: `1 = approved`, `0 = rejected` | Integer |


### MileStones

- I chose the data from Kaggle (Binary Classification Problem)
- Started by exploaring and wrangling the data 
- Data visualization and EDA to get a better idea
- I used chatgpt to understand the finance part of the data since I'm not a specialist and I kept a markdown file in the repo for anyone willing to understand the dataset further
- I tried multiple models (Logistic Regression,RandomForest...) and noticed that the Xgboost is the best
- I created the train.py file to train and save the model in a json format and the Dictvictorizer
- I created the predict.py file that contains the app the financial team will call to get results
- I created a finance_dev.py file tried it locally through port .
- I created a Dockerfile and containerize my app in the docker image loan-api
- I created an account in Render and with the help of chatgpt I deployed my app with the following url : 'https://loan-prediction-3kej.onrender.com'
- I tested the url in the finance.py and got the reuslts so it worked 