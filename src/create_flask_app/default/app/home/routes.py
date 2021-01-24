from flask import Blueprint, render_template, request
from random import randint


home = Blueprint('home', __name__)


@home.route('/home')
@home.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('home.html', title='Home')


@home.route('/about')
def about():
    return render_template('about.html', title='About')
