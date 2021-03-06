from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # CReating app configurations
    app.config.from_object(config_options[config_name])

    # INitializing file extensions
    bootstrap.init_app(app)

    # Add views and forms 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)


    return app