# models.py defines database structure
from flask_sqlalchemy import SQLAlchemy

# var name change?
db = SQLAlchemy()

# var name change, class exp, extracto
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Unique Identifier(Primary Key)
    description = db.Column(db.String(100), nullable=False) #Short text(mutable)
    amount = db.Column(db.Float, nullable=False) #Transaction value (+for income, -for expense)
    category = db.Column(db.String(50), nullable=False) #Category of transaction (food, bills, expenses)
    date = db.Column(db.DateTime, default=db.func.current_timestamp()) #Saves transaction date