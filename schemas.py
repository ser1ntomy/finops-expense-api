from pydantic import BaseModel, Field
from datetime import date

class ExpenseCreate(BaseModel):
    service_name: str
    category: str
    cost: float = Field(..., gt=0)   # cost must be greater than 0
    owner: str
    status: str
    usage_date: date

class ExpenseResponse(ExpenseCreate):
    id: int

    class Config:
        from_attributes = True