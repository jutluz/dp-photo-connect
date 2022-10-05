from flask import Flask, jsonify, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'pessoas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

app.secret_key = '$#EWFGHJUI*&DEGBHYJU&Y%T#RYJHG%##RU&U'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
