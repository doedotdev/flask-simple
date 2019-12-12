from flask import Blueprint, render_template

from src.configs.config import CONFIG


HOME = Blueprint("home", __name__)


@HOME.route("/", methods=["GET"])
@HOME.route("/home", methods=["GET"])
def get_home():
    return render_template(
        template_name_or_list="home.html",
        version=CONFIG.VERSION,
        name=CONFIG.NAME,
        description=CONFIG.DESCRIPTION,
    )
