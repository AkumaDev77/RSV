from flask import Blueprint,render_template,jsonify,request
from supabase import create_client
from database.supabase_client import supabase
from datetime import datetime
import locale
import yfinance as yf
import uuid

home_route = Blueprint('home', __name__)

#ROTAS DE TRANSIÇÃO WEB
@home_route.route('/')
def home():
    return render_template('index.html')