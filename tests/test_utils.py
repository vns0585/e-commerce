from unittest.mock import mock_open, patch

from src.utils import load_from_json


def test_load_from_json(utils_json_data: str, utils_load_from_json_result: list) -> None:
    with patch("builtins.open", mock_open(read_data=utils_json_data)) as mock_builtins_open:
        result = load_from_json("test.json")
        assert result == utils_load_from_json_result
        mock_builtins_open.assert_called_once()
