# server/app.py
#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# ----- ADD THIS -----
@app.route('/')
def home():
    return jsonify({"message": "Flask app is running!"})

# Example route to list employees (adjust table/column names if needed)
@app.route('/employees')
def get_employees():
    from models import Employee
    employees = Employee.query.all()
    return jsonify([e.name for e in employees])
# --------------------

if __name__ == '__main__':
    app.run(port=5555, debug=True)
