import pytest
from devbg2024.gilded_rose import Item, GildedRose
from typing import NamedTuple

ITEM_ID = 'General Item'

class SellInDecreaseRates(NamedTuple):
    normal: int = 1

class QualityDegradeRates(NamedTuple):
    normal: int = 1
    expired: int = 2

class QualityLimits(NamedTuple):
    min: int = 0
    max: int = 50

SELL_IN_DECREASE = SellInDecreaseRates()
QUALITY_DEGRADE = QualityDegradeRates()
QUALITY_LIMITS = QualityLimits()

@pytest.fixture
def inventory():
    return GildedRose([])

def test_sell_in_decrease_rate(inventory: GildedRose):
    init_sell_in = 10
    item = Item(ITEM_ID, sell_in=init_sell_in, quality=10)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.sell_in == init_sell_in - SELL_IN_DECREASE.normal

def test_quality_degrade_rate_within_sell_in(inventory: GildedRose):
    init_quality = 10
    item = Item(ITEM_ID, sell_in=10, quality=init_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == init_quality - QUALITY_DEGRADE.normal

def test_quality_degrade_rate_after_sell_in(inventory: GildedRose):
    init_quality = 10
    item = Item(ITEM_ID, sell_in=0, quality=init_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == init_quality - QUALITY_DEGRADE.expired

def test_quality_is_never_negative(inventory: GildedRose):
    init_quality = 0
    item = Item(ITEM_ID, sell_in=0, quality=init_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality >= 0
