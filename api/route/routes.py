from flask import Blueprint, render_template
from server.service import HomeService
from server.interface import RenderTemplateInterface

class HomeRoutes:
    def __init__(self, home_service: HomeService, template_interface: RenderTemplateInterface):
        self.home_service = home_service
        self.template_interface = template_interface

    def home(self):
        data = self.home_service.get_data()
        return self.template_interface.render_template('index.html', data=data)


class AboutRoutes:
    def __init__(self, template_interface: RenderTemplateInterface):
        self.template_interface = template_interface

    def about(self):
        return self.template_interface.render_template('about.html')


home_routes = Blueprint('home', __name__, url_prefix='/home')
about_routes = Blueprint('about', __name__, url_prefix='/about')

home_handler = HomeRoutes(HomeService(), RenderTemplateInterface())
about_handler = AboutRoutes(RenderTemplateInterface())

home_routes.add_url_rule('/', 'home', home_handler.home)
about_routes.add_url_rule('/', 'about', about_handler.about)
