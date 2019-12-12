from flask import Blueprint, jsonify

from src.configs.config import CONFIG

INFO = Blueprint("info", __name__)


@INFO.route("/info", methods=["GET"])
def get_info():
    info = {
        "version": CONFIG.VERSION,
        "name": CONFIG.NAME,
        "description": CONFIG.DESCRIPTION,
    }

    return jsonify(info), 200
