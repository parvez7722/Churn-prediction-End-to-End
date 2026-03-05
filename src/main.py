from fastapi import FastAPI
from src.schemas.UserVariables import UserVariables
from src.loader import save_data,load_data
from src.pipeline import predict_churn

app = FastAPI()

@app.get('/')
def root():
    return {'message':'Hello World'}

@app.get('/users')
def get_user():
    data =  load_data()
    return data

@app.post('/predict')
def predict(user: UserVariables):
    data = user.model_dump()
    save_data(data)

    a =  predict_churn(user)
    if a[0] == 0:
        return {'churn': 'No'}
    else:
        return {'churn': 'Yes'}



