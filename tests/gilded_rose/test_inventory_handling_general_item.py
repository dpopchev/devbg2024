import pytest
import devbg2024.gilded_rose as original
import devbg2024.item_objects as oop_items
import devbg2024.objects_inventory as oop_inventory
import devbg2024.item_structs as struct_items
import devbg2024.structs_inventory as struct_inventory
import devbg2024.item_validated as validated_items
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

@pytest.fixture(params=[
    (original.Item, original.GildedRose),
    (oop_items.Item, oop_inventory.GildedRose),
    (struct_items.Item, struct_inventory.GildedRose),
    (validated_items.Item, struct_inventory.GildedRose)
    ],
    ids=['original', 'oop', 'fp', 'validators'])
def make_testcase(request):
    def factory(name, sell_in, quality):
        item = request.param[0](name, sell_in, quality)
        inventory = request.param[1]([item])
        inventory.update_quality()
        return inventory.tail()
    return factory

def test_sell_in_decrease_rate(make_testcase):
    init_sell_in = 10
    item = make_testcase(ITEM_ID, init_sell_in, 10)
    assert item.sell_in == init_sell_in - SELL_IN_DECREASE.normal

def test_quality_degrade_rate_within_sell_in(make_testcase):
    init_quality = 10
    item = make_testcase(ITEM_ID, 10, init_quality)
    assert item.quality == init_quality - QUALITY_DEGRADE.normal

def test_quality_degrade_rate_after_sell_in(make_testcase):
    init_quality = 10
    item = make_testcase(ITEM_ID, 0, init_quality)
    assert item.quality == init_quality - QUALITY_DEGRADE.expired

def test_quality_is_never_negative(make_testcase):
    init_quality = 0
    item = make_testcase(ITEM_ID, 0, init_quality)
    assert item.quality >= 0
