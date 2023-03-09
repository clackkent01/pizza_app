from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
db = SQLAlchemy(app)
