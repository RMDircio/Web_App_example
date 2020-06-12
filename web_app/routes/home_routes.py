from flask import Blueprint, render_template

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    return render_template('books.html')

@home_routes.route('/about')
def about():
    print('Here is the About page')
    return 'About me'
