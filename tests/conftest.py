import pytest
from item import Item


@pytest.fixture
def test_data():
     item3 = Item("Смартфон", 20, 10000)
