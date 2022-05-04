from flask import render_template

from app import app

@app.errorhandler(404)
def four_Oh_four(error):
    '''Renders the error page'''
    return render_template('fourOhfour.html'),404