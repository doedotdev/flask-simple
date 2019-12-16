from pytest import fixture

from src.servers.web import WEB
from src.configs.config import CONFIG


@fixture
def test_app():
    WEB.register_blueprints()
    return WEB.flask_app.test_client()


def test_info(test_app):
    info_response = test_app.get("/info")

    assert info_response.status == "200 OK"
    assert info_response.status_code == 200
    assert info_response.json["name"] == CONFIG.NAME
    assert info_response.json["version"] == CONFIG.VERSION
    assert info_response.json["description"] == CONFIG.DESCRIPTION
