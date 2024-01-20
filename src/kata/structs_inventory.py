from typing import Iterable
from typing import Protocol
from kata.item_structs import general_quality_strategy, general_sell_in_strategy

class Item(Protocol):
    name: str
    sell_in: str
    quality: str

class GildedRose:
    def __init__(self, items: Iterable[Item]):
        self._items: list = [ item for item in items ]

    def update_quality(self):
        self._items = [ general_sell_in_strategy(item) for item in self._items]
        self._items = [ general_quality_strategy(item) for item in self._items]

    def tail(self):
        return self._items[-1]
