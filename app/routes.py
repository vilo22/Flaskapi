from app import app 

from flask import render_template
@app.route('/')
def home():
    greeting = 'Welcome to flask week foxes!'
    print(greeting)
    return render_template ('index.html', g = greeting) 

@app.route('/about')
def about():
    return render_template('about.html')

from .services import poke_guetter
from flask_login import login_required
@app.route('/pokemon_api')
@login_required
def pokemon_api():

    context = poke_guetter()

    return render_template('pokemon_api.html', **context)