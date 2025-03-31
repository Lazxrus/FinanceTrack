# This file is the entry point of your Flask app. It will:
# Initialize Flask
# Configure the database
# Register other parts of the app
from flask import Flask
from models import db

# Creates flask
app = Flask(__name__)

# Database config SQLite xOR PostgreSQL?
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# Specifies the database Point of Connection ^
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database initialization - SQLAlchemy to Flask
db.init_app(app)

# Table creation which are defined/made in models.py
with app.app_context():
    db.create_all()

import routes

# Print all registered routes
print("Registered routes:")
print(app.url_map)

# Run with debug enabled
if __name__ == "__main__":
    app.run(debug=True)