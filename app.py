# This file is the entry point of your Flask app. It will:
# Initialize Flask
# Configure the database
# Register other parts of the app
from flask import Flask
from models import db
from routes import transactions_bp

# Creates flask
app = Flask(__name__)

# Database config SQLite xOR PostgreSQL?
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# Specifies the database Point of Connection ^?
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database initialization - SQLAlchemy to Flask
db.init_app(app)

# Table creation which are defined/made in models.py
with app.app_context():
    db.create_all()

# Blueprint registration so routes are recognized
app.register_blueprint(transactions_bp)

# Print all registered routes/troubleshoot
"""print("Registered routes:")
print(app.url_map)"""

# Runs app with debug enabled
if __name__ == "__main__":
    app.run(debug=True)