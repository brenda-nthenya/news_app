from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Oh_four(error):
    '''Renders the error page'''
    return render_template('fourOhfour.html'),404