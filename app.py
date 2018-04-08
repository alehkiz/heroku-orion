import os
from flask import Flask, render_template, g
import flask
import psycopg2

import folium

app  = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

def connect_db():
	return psycopg2.connect(os.environ.get('DATABASE_URL'), sslmode='require')

@app.before_request
def before_request():
	g.db_conn = connect_db()
	
@app.route('/')
def index():
	cur = g.db_conn.cursor()
	cur.execute("SELECT * FROM country;")
	return render_template('index.html', countries= cur.fetchall())
	
@app.route('/home')
def home():
	m = folium.Map([45, 0], zoom_start=4)
	m.save('teste.html')
	return flask.send_file('teste.html')