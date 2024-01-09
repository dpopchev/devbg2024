import pytest
from devbg2024.gilded_rose import Item, GildedRose
from typing import NamedTuple

class DecreaseRates(NamedTuple):
    normal: int = 1
    sulfuras: int = 0

DEGRADE_RATES = DecreaseRates()

@pytest.fixture
def inventory():
    return GildedRose([])

def test_sell_in_decrease_rate_default_is_normal(inventory: GildedRose):
    initial_sell_in = 5
    item = Item('item', sell_in=initial_sell_in, quality=10)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.sell_in == initial_sell_in - DEGRADE_RATES.normal

def test_sell_in_decrease_rate_for_sulfuras_is_applied(inventory: GildedRose):
    initial_sell_in = 5
    item = Item('Sulfuras', sell_in=initial_sell_in, quality=10)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.sell_in == initial_sell_in - DEGRADE_RATES.sulfuras
