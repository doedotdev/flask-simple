from pytest import fixture

from src.servers.web import WEB
from src.configs.config import CONFIG


@fixture
def test_app():
    WEB.register_blueprints()
    return WEB.flask_app.test_client()


def test_home_from_home_path(test_app):
    home_response = test_app.get("/home")

    assert home_response.status == "200 OK"
    assert home_response.status_code == 200

    html_reponse = str(home_response.data)

    assert "n<h1>Welcome</h1>" in html_reponse
    assert "<p>NAME: flask-simple</p>" in html_reponse
    assert "<p>VERSION: 0.0.1</p>" in html_reponse
    assert (
        "<p>DESCRIPTION: Flask Simple Example | Structure + Simplicity</p>"
        in html_reponse
    )


def test_home_from_root_path(test_app):
    home_response = test_app.get("/")

    assert home_response.status == "200 OK"
    assert home_response.status_code == 200

    html_reponse = str(home_response.data)

    assert "n<h1>Welcome</h1>" in html_reponse
    assert "<p>NAME: flask-simple</p>" in html_reponse
    assert "<p>VERSION: 0.0.1</p>" in html_reponse
    assert (
        "<p>DESCRIPTION: Flask Simple Example | Structure + Simplicity</p>"
        in html_reponse
    )
