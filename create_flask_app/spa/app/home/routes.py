from flask import Blueprint, render_template, request
from random import randint


home = Blueprint('home', __name__)


@home.route('/home')
@home.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        return {'random_num' : str(randint(0,100))}
    return render_template('home.html')
