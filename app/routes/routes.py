from app import app
from flask import render_template

print("--- 4. Entramos em app/routes.py para definir as URLs ---")

@app.route('/')
def index():
    return render_template('index.html')