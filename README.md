# FinOps Expense Management API

This project is a FastAPI backend application for managing and tracking cloud expenses in a FinOps environment.

## Features
- Add new expense
- View all expenses
- View expense by ID
- Update expense
- Delete expense
- Filter expenses by service
- Calculate total expense cost
- Cost validation (cost must be greater than 0)

## Technologies Used
- FastAPI
- SQLAlchemy (ORM)
- SQLite (Database)
- Pydantic (Data validation)
- Uvicorn (Server)

## How to Run the Project
Step 1: Install required libraries
pip install -r requirements.txt

Step 2: Run the FastAPI server
uvicorn main:app --reload

Step 3: Open in browser
http://127.0.0.1:8000/docs

## Database
This project uses SQLite database stored as a file: finops.db
You can open and view the database using **DB Browser for SQLite**.

## Author
Serin Tomy
