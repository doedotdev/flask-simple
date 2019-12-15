from pytest import fixture

from src.servers.web import WEB


@fixture
def test_app():
    WEB.register_blueprints()
    return WEB.flask_app.test_client()


def test_math_mul_div(test_app):

    value_one = 3
    value_two = 4

    math_response = test_app.get("/mul-div?value_one={}&value_two={}".format(value_one, value_two))

    assert math_response.status == "200 OK"
    assert math_response.status_code == 200
    assert math_response.json["value_one"] == value_one
    assert math_response.json["value_two"] == value_two
    assert math_response.json["multiplication"] == value_one * value_two
    assert math_response.json["division"] == value_one / value_two


def test_math_add_sub(test_app):

    value_one = 3
    value_two = 4

    math_response = test_app.get("/add-sub?value_one={}&value_two={}".format(value_one, value_two))

    assert math_response.status == "200 OK"
    assert math_response.status_code == 200
    assert math_response.json["value_one"] == value_one
    assert math_response.json["value_two"] == value_two
    assert math_response.json["subtraction"] == value_one - value_two
    assert math_response.json["addition"] == value_one + value_two
