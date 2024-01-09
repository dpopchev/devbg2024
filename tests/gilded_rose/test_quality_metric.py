import pytest
from devbg2024.gilded_rose import Item, GildedRose
from typing import NamedTuple

class DegradeRates(NamedTuple):
    normal: int
    expired: int

DEGRADE_RATES = DegradeRates(1, 2)

@pytest.fixture
def inventory():
    return GildedRose([])

def test_degrade_rate_before_sell_in_has_passed_is_normal(inventory: GildedRose):
    initial_quality = 5
    item = Item('item', sell_in=1, quality=initial_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == initial_quality - DEGRADE_RATES.normal

def test_degrade_rate_after_sell_in_has_passed_is_expired(inventory: GildedRose):
    initial_quality = 5
    item = Item('item', sell_in=0, quality=initial_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == initial_quality - DEGRADE_RATES.expired
