import pytest
from devbg2024.gilded_rose import Item, GildedRose
from typing import NamedTuple

ITEM_ID = 'Conjured'

class SellInDecreaseRates(NamedTuple):
    normal: int = 1

class QualityDegradeRates(NamedTuple):
    normal: int = 2

class QualityLimits(NamedTuple):
    min: int = 0
    max: int = 50

SELL_IN_DECREASE = SellInDecreaseRates()
QUALITY_DEGRADE = QualityDegradeRates()
QUALITY_LIMITS = QualityLimits()

@pytest.fixture
def inventory():
    return GildedRose([])

@pytest,mark.xfail(reason='TBD')
def test_quality_degrade_rate_within_sell_in(inventory: GildedRose):
    init_quality = 10
    item = Item(ITEM_ID, sell_in=10, quality=init_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == init_quality - QUALITY_DEGRADE.normal
