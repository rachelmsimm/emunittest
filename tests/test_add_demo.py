from unittest.mock import patch
from add_demo import add
from demo import Demo
import pytest

mock_demo_list = [
    {"name": "game1",
     "key": "game1",
     "url": "demos/game1/index.html",},
    {"name": "game2",
     "key": "game2",
     "url": "demos/game2/index.html",
     "date": "2020-01-01",}
]

mock_demo_obj = Demo("game1", "game1", "demos/game1/index.html")

class TestAddDemo:
    def test_add_demo_success():
        pass

    def test_add_demo_duplicate_name_or_key(mocker):
        with patch("add_demo.get_existing_demos", return_value=mock_demo_list):
            with pytest.raises(Exception):
                add(mock_demo_obj)

