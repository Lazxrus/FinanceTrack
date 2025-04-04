# routes.py
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from models import db, Transaction

# Create a Blueprint
transactions_bp = Blueprint('transactions', __name__)
api = Api(transactions_bp)

class TransactionsAPI(Resource):
    def get(self):
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
        data = request.json
        new_transaction = Transaction(
            description=data["description"],
            amount=data["amount"],
            category=data["category"]
        )
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({"message": "Transaction added!", "id": new_transaction.id})

# Register the resource with the Blueprint
api.add_resource(TransactionsAPI, "/api/transactions")