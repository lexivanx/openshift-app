import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app_name = os.getenv('APP_NAME', 'default')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return f'Hello, from {app_name}!'


@app.route('/healthz')
def healthz():
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
