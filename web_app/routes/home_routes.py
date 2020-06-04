from flask import Blueprint

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    print('Visiting the home page')
    x = 2 + 3
    return f'Hello World! {x}'

@home_routes.route('/about')
def about():
    print('Here is the About page')
    return 'About me'
