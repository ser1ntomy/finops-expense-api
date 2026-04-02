from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
import schemas
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FinOps Expense Management API",
    description="API for managing cloud expense records",
    version="1.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "FinOps Expense CRUD API is running"}

@app.post("/expenses", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)

@app.get("/expenses", response_model=list[schemas.ExpenseResponse])
def read_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)

@app.get("/expenses/total")
def get_total_cost(db: Session = Depends(get_db)):
    expenses = crud.get_expenses(db)
    total = sum(exp.cost for exp in expenses)
    return {"total_cost": total}

@app.get("/expenses/service/{service_name}", response_model=list[schemas.ExpenseResponse])
def read_expenses_by_service(service_name: str, db: Session = Depends(get_db)):
    return crud.get_expenses_by_service(db, service_name)

@app.get("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = crud.get_expense(db, expense_id)
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return db_expense

@app.put("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def update_expense(expense_id: int, expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = crud.update_expense(db, expense_id, expense)
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return db_expense

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = crud.delete_expense(db, expense_id)
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted successfully"}