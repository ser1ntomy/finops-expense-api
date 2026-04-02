from sqlalchemy.orm import Session
import models
import schemas

def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session):
    return db.query(models.Expense).all()

def get_expense(db: Session, expense_id: int):
    return db.query(models.Expense).filter(models.Expense.id == expense_id).first()

def get_expenses_by_service(db: Session, service_name: str):
    return db.query(models.Expense).filter(models.Expense.service_name == service_name).all()

def update_expense(db: Session, expense_id: int, expense: schemas.ExpenseCreate):
    db_expense = get_expense(db, expense_id)
    if db_expense:
        for key, value in expense.model_dump().items():
            setattr(db_expense, key, value)
        db.commit()
        db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int):
    db_expense = get_expense(db, expense_id)
    if db_expense:
        db.delete(db_expense)
        db.commit()
    return db_expense