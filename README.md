# Customer Churn Prediction – End to End ML Project

## Overview

This project builds a **machine learning system to predict customer churn** using telecom customer data.
The goal is to identify customers who are likely to leave a service so companies can take preventive actions.

The project demonstrates a **complete ML pipeline**, including model training, API development, UI integration, and containerized deployment.

---

## Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* FastAPI
* Streamlit
* Docker
* Joblib

---

## Features

* Data preprocessing and feature engineering
* Machine learning model training
* REST API for predictions
* Interactive Streamlit UI
* Docker containerization
* End-to-End deployment ready

---

## Project Architecture

Streamlit UI
⬇
FastAPI Backend
⬇
Machine Learning Model (Pickle)

---

## Project Structure

```
Churn-Prediction-End-To-End/
│
├── src/
│   ├── main.py
│   ├── app.py
│   ├── model/
│   │   └── model.pkl
│   └── utils.py
│
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/<your-username>/Churn-Prediction-End-To-End.git
```

Move to project directory

```
cd Churn-Prediction-End-To-End
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Run FastAPI Server

```
uvicorn src.main:app --reload
```

API docs available at

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit UI

```
streamlit run src/app.py
```

Streamlit app will open at

```
http://localhost:8501
```

---

## Docker Setup

Build Docker image

```
docker build -t churn-predict .
```

Run container

```
docker run -p 8000:8000 -p 8501:8501 churn-predict
```

---

## Model Details

Algorithm used:

* Random Forest Classifier

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

---

## Future Improvements

* CI/CD pipeline
* Model monitoring
* Cloud deployment
* Real-time prediction pipeline

---

## Author

Mohammed Parvez
