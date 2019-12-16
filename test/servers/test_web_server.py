from mock import patch

from src.servers.web import WEB
from src.configs.config import CONFIG


@patch("src.servers.web.WEB.flask_app.run")
def test_start_app_is_called_with_configs_once(mock_run):

    mock_run.return_value = None
    WEB.start_app()

    mock_run.assert_called_with(debug=CONFIG.DEBUG, host=CONFIG.HOST, port=CONFIG.PORT)
    assert mock_run.call_count == 1
