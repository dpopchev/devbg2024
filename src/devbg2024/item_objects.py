from abc import ABC, abstractmethod

class ItemStrategy(ABC):
    MIN = 0
    MAX = 50

    @abstractmethod
    def __call__(self, value: int) -> int:
        ...

class GeneralSellInStrategy(ItemStrategy):
    def __call__(self, value: int) -> int:
        if value == 0:
            return 0
        return value - 1

class GeneralQualityStrategy(ItemStrategy):
    def __call__(self, value: int) -> int:
        if value >= self.MAX:
            return self.MAX

        if value <= self.MIN:
            return self.MIN

        return value - 1

class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self._sell_in_strategy: ItemStrategy = GeneralSellInStrategy()
        self._quality_strategy: ItemStrategy = GeneralQualityStrategy()

    def update_sell_in(self) -> None:
        self.sell_in = self._sell_in_strategy(self.sell_in)
        return

    def change_sell_in_strategy(self, strategy: ItemStrategy) -> None:
        self._sell_in_strategy = strategy

    def change_quality_strategy(self, strategy: ItemStrategy) -> None:
        self._quality_strategy = strategy
