from abc import ABC, abstractmethod

class SellInStrategy(ABC):
    @abstractmethod
    def apply(self, value: int) -> int:
        ...

class QualityStrategy(ABC):
    MIN = 0
    MAX = 50
    DEGRADE_RATE = 1

    @abstractmethod
    def apply(self, value: int, sell_in: int) -> int:
        ...

class GeneralSellInStrategy(SellInStrategy):
    def apply(self, value: int) -> int:
        if value == 0:
            return 0
        return value - 1

class GeneralQualityStrategy(QualityStrategy):
    def apply(self, value: int, sell_in: int) -> int:
        if value >= self.MAX:
            return self.MAX

        if value <= self.MIN:
            return self.MIN

        return value - self.DEGRADE_RATE if sell_in > 0 else value - 2*self.DEGRADE_RATE

class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self._sell_in_strategy: SellInStrategy = GeneralSellInStrategy()
        self._quality_strategy: QualityStrategy = GeneralQualityStrategy()

    def update_sell_in(self) -> None:
        self.sell_in = self._sell_in_strategy.apply(self.sell_in)
        return

    def change_sell_in_strategy(self, strategy: SellInStrategy) -> None:
        self._sell_in_strategy = strategy

    def update_quality(self) -> None:
        self.quality = self._quality_strategy.apply(self.quality, self.sell_in)
        return

    def change_quality_strategy(self, strategy: QualityStrategy) -> None:
        self._quality_strategy = strategy
