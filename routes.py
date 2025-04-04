# routes.py functions to fetch all transactions (GET /api/transactions)
# adds new transactions (POST /apt/transactions)
from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from models import db, Transaction

# Creates a blueprint which is easier to maintain and call
transactions_bp = Blueprint('transactions', __name__)

# Attaches Flask-RESTful to app
api = Api(transactions_bp)

# Defines an API resource
class TransactionsAPI(Resource):
    def get(self):
        """Gets all transactions from db"""
        # makes a query to the db
        query = Transaction.query

        # Applies filter conditionals if parameters are provided
        category = request.args.get("category") #get category from URL
        if category:
            query = query.filter_by(category=category) # add a WHERE category to SQL query

        # Sort by amount or date (default is date)
        sort_by = request.args.get("sort_by", "date") # check URL for sort_by and defaults to date
        if sort_by == "amount":
            query = query.order_by(Transaction.amount.desc()) # desc is descending
        else:
            query = query.order_by(Transaction.date.desc())

        # executes the query
        transactions = query.all()

        # JSON conversion
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
    
# API endpoint registration
api.add_resource(TransactionsAPI, "/api/transactions")