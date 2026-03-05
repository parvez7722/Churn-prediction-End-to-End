import joblib
import pandas as pd
from src.schemas.UserVariables import UserVariables

model = joblib.load('src/model/model.pkl')

def predict_churn(user: UserVariables):
    
    data = pd.DataFrame([user.model_dump()])

    prediction = model.predict(data)

    return prediction