from flask import Flask
from models import db
from route_test import transactions_bp  # Import the Blueprint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Register the Blueprint
app.register_blueprint(transactions_bp)

print("Registered routes:")
print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)