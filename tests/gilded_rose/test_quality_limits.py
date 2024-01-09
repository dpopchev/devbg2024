import pytest
from devbg2024.gilded_rose import Item, GildedRose
from typing import NamedTuple

class QualityLimits(NamedTuple):
    max: int = 50
    min: int = 0
    sulfuras: int = 80

QUALITY_LIMITS = QualityLimits()

@pytest.fixture
def inventory():
    return GildedRose([])

def test_when_quality_reaches_min_remains_the_same(inventory: GildedRose):
    initial_quality = QUALITY_LIMITS.min
    item = Item('item', sell_in=1, quality=initial_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == QUALITY_LIMITS.min

def test_when_quality_reaches_max_remains_the_same(inventory: GildedRose):
    """Aged Brie quality rate is negative"""
    initial_quality = QUALITY_LIMITS.max
    item = Item('Aged Brie', sell_in=1, quality=initial_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == QUALITY_LIMITS.max

def test_sulfuras_quality_remains_same_at_its_limit(inventory: GildedRose):
    initial_quality = QUALITY_LIMITS.sulfuras
    item = Item('Sulfuras', sell_in=1, quality=initial_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == QUALITY_LIMITS.sulfuras
