from flask import render_template
from server.service import HomeService

def home_controller():
    service = HomeService()
    data = service.get_data()
    return render_template('index.html', data=data)
