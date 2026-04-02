# FinOps Expense Management API

This project is a FastAPI backend application for managing cloud expenses in a FinOps environment.

## Features
- Create expense
- View all expenses
- View expense by ID
- Update expense
- Delete expense
- Filter expenses by service
- Total cost calculation
- Cost validation (cost > 0)

## Technologies Used
- FastAPI
- SQLAlchemy ORM
- SQLite
- Pydantic
- Uvicorn

## How to Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
