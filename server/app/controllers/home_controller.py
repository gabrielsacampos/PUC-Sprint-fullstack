from flask import Flask, request, render_template
from app import app

@app.route('/')
def index():
    headers = request.headers
    return render_template('home.html')