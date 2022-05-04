from flask import render_template, request, redirect, url_for
from app import app
from .request import get_source, article_source, get_category, get_headlines


@app.route('/')
def index():
    '''Returns the home page'''
    source = get_source()
    headlines = get_headlines()
    return render_template('index.html',sources=source, headlines = headlines)

@app.route('/article/<id>')
def article(id):
    '''VIew article page function that return various article details page'''

    article = article_source(id)
    return render_template('article.html', article=article, id = id)

@app.route('/categories/<cat_name>')
def category(cat_name):
    '''Function to return categories page and its content'''
    category - get_category
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html', title = title, category=category, cat = cat_name)