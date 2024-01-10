from typing import Callable, NamedTuple

class Item(NamedTuple):
    name: str
    sell_in: int
    quality: int

ItemStrategy = Callable[[Item], Item]

def make_quality_strategy(min: int = 0, max: int = 50, degrade_rate: int = 1) -> ItemStrategy:
    def strategy(item: Item) -> Item:
        if item.quality >= max:
            return Item(item.name, item.sell_in, max)

        if item.quality <= min:
            return Item(item.name, item.sell_in, min)

        quality = item.quality - degrade_rate if item.sell_in > 0 else item.quality - 2*degrade_rate
        return Item(item.name, item.sell_in, quality)

    return strategy

def make_sell_in_strategy() -> ItemStrategy:
    def strategy(item: Item) -> Item:
        if item.sell_in == 0:
            return Item(item.name, 0, item.quality)

        return Item(item.name, item.sell_in - 1, item.quality)

    return strategy
