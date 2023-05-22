from flask import Blueprint, render_template
from server.service import HomeService

home_routes = Blueprint('home', __name__, url_prefix='/home')
about_routes = Blueprint('about', __name__, url_prefix='/about')

@home_routes.route('/')
def home():
    service = HomeService()
    data = service.get_data()
    return render_template('index.html', data=data)

@about_routes.route('/')
def about():
    return render_template('about.html')
