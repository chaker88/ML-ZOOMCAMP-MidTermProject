import pickle
import pandas as pd
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

def load_data():
    path = "https://raw.githubusercontent.com/chaker88/ML-ZOOMCAMP-MidTermProject/main/loan_data.csv"
    df = pd.read_csv(path)
    df["person_age"] = df["person_age"].astype(int)
    df = df[
        (df["person_income"] <= 100000.0) &
        (df["person_age"] <= 100) &
        (df["person_emp_exp"] <= 70)
    ]
    return df

def train_model(df):
    features = ['person_education', 'person_home_ownership', 'loan_intent',
                'previous_loan_defaults_on_file', 'person_income', 'loan_amnt',
                'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length',
                'credit_score', 'loan_status']

    df = df[features]

    temp, test = train_test_split(df, test_size=0.20, stratify=df["loan_status"], random_state=42)
    train, val = train_test_split(temp, test_size=0.25, stratify=temp["loan_status"], random_state=42)

    # Separate X and y
    X_train = train.drop(columns="loan_status")
    y_train = train["loan_status"].values
    X_val = val.drop(columns="loan_status")
    y_val = val["loan_status"].values

    # Transform categorical features
    dv = DictVectorizer(sparse=False)
    X_train_transformed = dv.fit_transform(X_train.to_dict(orient='records'))
    X_val_transformed = dv.transform(X_val.to_dict(orient='records'))
    feature_names = list(dv.get_feature_names_out())

    # Create DMatrix
    dtrain = xgb.DMatrix(X_train_transformed, label=y_train, feature_names=feature_names)
    dval = xgb.DMatrix(X_val_transformed, label=y_val, feature_names=feature_names)

    # XGBoost parameters
    xgb_params = {
        'eta': 0.3,
        'max_depth': 10,
        'objective': 'binary:logistic',
        'scale_pos_weight': 2.86,
        'eval_metric': 'auc',
        'random_state': 42,
        'verbosity': 1
    }

    # Train model
    model = xgb.train(xgb_params,dtrain,num_boost_round=100)


    # Evaluate
    y_pred_proba = model.predict(dval)
    y_pred = (y_pred_proba > 0.5).astype(int)

    print("Validation Accuracy:", accuracy_score(y_val, y_pred))
    print("Validation F1 Score:", f1_score(y_val, y_pred))
    print("Validation AUC:", roc_auc_score(y_val, y_pred_proba))

    return model, dv

def save_model(model, dv, model_file='xgb_model.json', dv_file='dv.pkl'):
    model.save_model(model_file)
    with open(dv_file, 'wb') as f_out:
        pickle.dump(dv, f_out)

df = load_data()
model, dv = train_model(df)
save_model(model, dv)
print("Model and DictVectorizer saved.")