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

def test_quality_is_never_negative(inventory: GildedRose):
    initial_quality = 0
    item = Item('item', sell_in=1, quality=initial_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == 0
