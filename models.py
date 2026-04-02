from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    
    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, index=True)
    category = Column(String)
    cost = Column(Float)
    owner = Column(String)
    status = Column(String)
    usage_date = Column(Date)