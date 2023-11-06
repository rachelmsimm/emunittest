from add_demo_src.add_demo import add
from add_demo_src.add_demo import check_for_duplicates
from add_demo_src.demo import Demo
from exceptions import DuplicateNameOrKeyException
from unittest.mock import patch

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
    def test_add_demo_success(mocker):
        with patch("add_demo_src.add_demo.insert_demo", return_value=None) as mock_insert_entry:
            with patch("add_demo_src.add_demo.get_existing_demos", return_value={}):
                add(mock_demo_obj)
                assert(mock_insert_entry.call_count == 1)

    def test_add_demo_duplicate_name_or_key(mocker):
        with patch("add_demo_src.add_demo.get_existing_demos", return_value=mock_demo_list):
            with pytest.raises(DuplicateNameOrKeyException):
                check_for_duplicates(mock_demo_obj.name, mock_demo_obj.key)        

