import os


class Config:
    VERSION = "0.0.1"
    NAME = "flask-simple"
    DESCRIPTION = "Flask Simple Example | Structure + Simplicity"
    PORT = int(os.environ.get("PORT", 8080))
    HOST = "0.0.0.0"
    DEBUG = True
    TEMPLATES = os.path.abspath("./src/templates")


CONFIG = Config()
