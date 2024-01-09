import pytest
from devbg2024.gilded_rose import Item, GildedRose
from typing import NamedTuple

ITEM_ID = 'Backstage passes'

class SellInDecreaseRates(NamedTuple):
    normal: int = 1

class QualityDegradeRates(NamedTuple):
    normal: int = -1
    ten_days_mark: int = -2
    five_days_mark: int = -3

class QualityLimits(NamedTuple):
    min: int = 0
    max: int = 50

SELL_IN_DECREASE = SellInDecreaseRates()
QUALITY_DEGRADE = QualityDegradeRates()
QUALITY_LIMITS = QualityLimits()

@pytest.fixture
def inventory():
    return GildedRose([])

def test_quality_degrade_rate_before_10_day_sell_in_mark(inventory: GildedRose):
    init_quality = 10
    item = Item(ITEM_ID, sell_in=11, quality=init_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == init_quality - QUALITY_DEGRADE.normal

def test_quality_degrade_rate_in_10_to_5_days_sell_in_range(inventory: GildedRose):
    init_quality = 10
    item = Item(ITEM_ID, sell_in=8, quality=init_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == init_quality - QUALITY_DEGRADE.ten_days_mark

def test_quality_degrade_rate_after_5_days_sell_in_mark(inventory: GildedRose):
    init_quality = 10
    item = Item(ITEM_ID, sell_in=4, quality=init_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == init_quality - QUALITY_DEGRADE.five_days_mark

def test_quality_is_min_after_the_concert(inventory: GildedRose):
    init_quality = 10
    item = Item(ITEM_ID, sell_in=0, quality=init_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == QUALITY_LIMITS.min
