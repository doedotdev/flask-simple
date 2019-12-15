from flask import Blueprint, jsonify, request

from src.services.math import add_sub, mul_div

MATH = Blueprint("math", __name__)


@MATH.route("/add-sub", methods=["GET"])
def get_add_sub():
    a = request.args.get("value_one", default=1, type=float)
    b = request.args.get("value_two", default=1, type=float)

    data = add_sub(a, b)

    return jsonify(data), 200


@MATH.route("/mul-div", methods=["GET"])
def get_mul_div():
    a = request.args.get("value_one", default=1, type=float)
    b = request.args.get("value_two", default=1, type=float)

    data = mul_div(a, b)

    return jsonify(data), 200
