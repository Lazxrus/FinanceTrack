from flask import Flask
from models import db

# Creates flask
app = Flask(__name__)

# Database config SQLite xOR PostgreSQL 
app.config["SQLACLHEMY_DATABASE_URI"] = "postgresql or sqlite:///database.db"
# Specifies the database Point of Connection ^
app.config["SQLACLHEMY_TRACK_MODIFICATION"] = False

# Database initialization - SQLAlchemy to Flask
db.init_app(app)

# Table creation which are defined/made in models.py
with app.app_context():
    db.create_all()

# Run with debug enabled
if __name__ == "__main__":
    app.run(debug=True)
