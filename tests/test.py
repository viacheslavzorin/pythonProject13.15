import pytest
from item import Item


# item = Item("Смартфон", 20, 10000)
def test_calculate_total_prise(test_data):
    assert test_data.calculate_total_price() == 200000


def test_apply_discount(test_data):
    assert test_data.apply_discount == 8500.0


def test_instantiate_from_csv():
    assert len(Item.instantiate_from_csv()) == 5
    item4 = Item.instantiate_from_csv()[2]
    assert item4._Item__product == 'Кабель'


def test_is_integer():
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.8) is False


def test_long_name():
    item7 = Item('eee', 1000, 10)
    assert item7.long_name == 'eee'

    with pytest.raises(Exception):
        assert item7.long_name("aaaaaaaaaaa")
