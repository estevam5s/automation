from flask import Flask
from route.routes import home_routes, about_routes

app = Flask(__name__)

# Registro das rotas
app.register_blueprint(home_routes)
app.register_blueprint(about_routes)

if __name__ == '__main__':
    app.run()
