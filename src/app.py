from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'Home'
    

@app.route('/categories')
def categories():
    return 'Categories'

@app.route('/establishment')
def establishment():
    return 'Establishment'

@app.route('/users')
def users():
    return 'Users'

if __name__ == '__main__':
    app.run(debug=True, host='')


