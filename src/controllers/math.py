from flask import Blueprint, jsonify, request

from src.configs.config import CONFIG

MATH = Blueprint("math", __name__)


@MATH.route("/add-sub", methods=["POST"])
def post_add_sub():
    a = request.args.get("a", default=1, type=float)
    b = request.args.get("b", default=1, type=float)

    data = {
        "a": a,
        "b": b,
        "add": a + b,
        "aub": a - b,
    }

    return jsonify(data), 200


# @MATH.route("/mul-div", methods=["POST"])
# def post_mul_div():
#     info = {
#         "version": CONFIG.VERSION,
#         "name": CONFIG.NAME,
#         "description": CONFIG.DESCRIPTION,
#     }
#
#     return jsonify(info), 200
