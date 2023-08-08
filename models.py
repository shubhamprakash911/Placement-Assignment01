from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)

class Company(db.Model):
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    founded_year = db.Column(db.Integer, nullable=False)

