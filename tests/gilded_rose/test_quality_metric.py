import pytest
from devbg2024.gilded_rose import Item, GildedRose
from typing import NamedTuple

class QualityLimits(NamedTuple):
    max: int = 50
    min: int = 0

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
    initial_quality = QUALITY_LIMITS.max
    # Aged Brie degrade quality rate is negative
    item = Item('Aged Brie', sell_in=1, quality=initial_quality)
    inventory.items.append(item)
    inventory.update_quality()
    assert item.quality == QUALITY_LIMITS.max
