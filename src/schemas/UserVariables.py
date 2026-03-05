from pydantic import BaseModel,Field,field_validator
from typing import Literal

class UserVariables(BaseModel):
    id: int = Field(..., description="Unique identifier for the user")
    gender: Literal["Male", "Female"] = Field(..., description="Gender of the user")
    SeniorCitizen: Literal['Yes', 'No'] = Field(..., description="Whether the user is a senior citizen")
    Partner: Literal['Yes', 'No'] = Field(..., description="Whether the user has a partner")
    Dependents: Literal['Yes', 'No'] = Field(..., description="Whether the user has dependents")
    tenure: int = Field(..., description="Number of months the user has been with the company")
    PhoneService: Literal['Yes', 'No'] = Field(..., description="Whether the user has phone service")
    MultipleLines: Literal['Yes', 'No', 'No phone service'] = Field(..., description="Whether the user has multiple lines")
    InternetService: Literal['DSL', 'Fiber optic', 'No'] = Field(..., description="Type of internet service the user has")
    OnlineSecurity: Literal['Yes', 'No', 'No internet service'] = Field(..., description="Whether the user has online security")
    OnlineBackup: Literal['Yes', 'No', 'No internet service'] = Field(..., description="Whether the user has online backup")
    DeviceProtection: Literal['Yes', 'No', 'No internet service'] = Field(..., description="Whether the user has device protection")
    TechSupport: Literal['Yes', 'No', 'No internet service'] = Field(description="Whether the user has tech support", default='No')
    StreamingTV: Literal['Yes', 'No', 'No internet service'] = Field(description="Whether the user has streaming TV", default='No')
    StreamingMovies: Literal['Yes', 'No', 'No internet service'] = Field(description="Whether the user has streaming movies", default='No')
    Contract: Literal['Month-to-month', 'One year', 'Two year'] = Field(..., description="Type of contract the user has")
    PaperlessBilling: Literal['Yes', 'No'] = Field(..., description="Whether the user has paperless billing")
    PaymentMethod: Literal['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'] = Field(..., description="Payment method used by the user")
    MonthlyCharges: float = Field(..., description="Monthly charges for the user")
    TotalCharges: float = Field(..., description="Total charges for the user")

    @field_validator('SeniorCitizen','Partner','Dependents','PhoneService','PaperlessBilling')
    def binary_conversion(cls, value):
        if value == 'Yes':
            return 1
        else:
            return 0
        
    @field_validator('gender')
    def gender_conversion(cls, value):
        if value == 'Male':
            return 0
        else:
            return 1 
        