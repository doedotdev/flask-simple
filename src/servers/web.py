from flask import Flask

from src.configs.config import CONFIG
from src.controllers.info import INFO
from src.controllers.math import MATH
from src.pages.home import HOME


class Web:
    flask_app = None

    def __init__(self):
        self.flask_app = Flask(CONFIG.NAME, template_folder=CONFIG.TEMPLATES)

    def register_blueprints(self):
        self.flask_app.register_blueprint(blueprint=INFO, url_prefix="")
        self.flask_app.register_blueprint(blueprint=HOME, url_prefix="")
        self.flask_app.register_blueprint(blueprint=MATH, url_prefix="")

    def start_app(self):
        self.flask_app.run(debug=CONFIG.DEBUG, host=CONFIG.HOST, port=CONFIG.PORT)


WEB = Web()
