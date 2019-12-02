from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/doorprize', methods=['POST'])
def doorprize():
     kode_provider = request.form['kode_provider']
     return render_template('rollresult.html')

@app.route('/')
def index():
     return render_template('index.html')
