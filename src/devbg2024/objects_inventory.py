from typing import Iterable
from typing import Protocol

class Item(Protocol):
    name: str
    sell_in: str
    quality: str

    def update_sell_in(self) -> None:
        ...

    def update_quality(self) -> None:
        ...

class GildedRose:
    def __init__(self, items: Iterable[Item]):
        self._items = [ item for item in items ]

    def update_quality(self):
        for item in self._items:
            item.update_sell_in()
            item.update_quality()
