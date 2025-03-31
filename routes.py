# routes.py functions to fetch all transactions (GET /api/transactions)
# adds new transactions (POST /apt/transactions)
from flask import request, jsonify
from flask_restful import Resource, Api
from models import db, Transaction
from app import app

# API initialize
api = Api(app) # Attaches Flask-RESTful to app

# Checks to see if routes is working
print("Routes module is being imported and executed")

# Defines an API resource
# La clase no cierra preguntar
class TransactionsAPI(Resource):
    def get(self):
        """Gets all transactions from db"""
        transactions = Transaction.query.all()
        return jsonify([
            {
                "id": t.id,
                "description": t.description,
                "amount": t.amount,
                "category": t.category,
                "date": t.date.strftime("%Y-%m-%d %H:%M:%S")
            } 
            for t in transactions
        ])
    
    def post(self):
        """Adds new transactions"""
        data = request.json #Gets JSON data from request
        new_transaction = Transaction(
            description=data["description"],
            amount=data["amount"],
            category=data["category"]
        )
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({"message": "Transaction added!", "id": new_transaction.id})
    
# API endpoint registration
api.add_resource(TransactionsAPI, "/api/transactions")