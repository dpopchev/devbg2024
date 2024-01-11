---
topic: Metaprogramming
title: Metaprogramming
subtitle: what I should have known from the start
author: Dimitar Popchev
institute: GlobalFoundries
theme: Frankfurt
date: \today
fontsize: 8pt
fontfamilyoptions: default
section-titles: false
toc: false
aspectratio: 169
header-includes:
  - \AtBeginSection[] { \begin{frame}<beamer>{} \tableofcontents[currentsection] \end{frame} }
---

# Preface

## Metaclasses

###
*Metaclasses are deeper magic than 99% of users should ever worry about.\
If you wonder whether you need them, you don’t.*\
\hfill --Time Peters

### Data model 'uses for'

- *Common uses for sets...*, an entry
- *Uses for metaclasses*, an subsubsection

## Set as datatype

### perlfaq: How can I remove duplicate elements from a list or array?

```perl
my @unique = keys { map { $_, 1 } @data };
```

### perlfaq: How do I sort an array by (anything)?

```perl
# Schwartzian Transform
my @sorted = map  { $_->[0] }
    sort { $a->[1] cmp $b->[1] }
    map  { [ $_, uc( (/\d+\s*(\S+)/)[0]) ] } @data;
```

## Topics

- Software engineering
- Development process
- Programming paradigms
- Refactoring

## Resources

###

- [`dpopchev/devbg2024`](https://github.com/dpopchev/devbg2024) repo at github
- [Gilded Rose Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata)

###

- David Beazley
- Scott Wlaschin
- Kevlin Henney
- Mark Seemann
- Brandon Rhodes
- Martin Fowler
- Dave Farley
- Raymond Hettinger
- ...

# Prologue

## Gilded Rose

- `Gilded Rose` is a small inn ran by Allison
- Trade finest goods on the side
- Inventory system was implemented by a no-nonsense type named Leeroy
\onslide<2->{\item He moved on to new adventures}
\onslide<2->{\item The goblin helped with the implementation}
\onslide<3->{\item The system needs a small update}


## The system

```python
...
if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    if item.quality > 0:
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = item.quality - 1
else:
    if item.quality < 50:
        item.quality = item.quality + 1
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality = item.quality + 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality = item.quality + 1
if item.name != "Sulfuras, Hand of Ragnaros":
    item.sell_in = item.sell_in - 1
if item.sell_in < 0:
    if item.name != "Aged Brie":
        if item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
...
```

## Software Crisis

### Formulation

*The basic problem is that certain classes of systems are placing demands on us
which are beyond our capabilities and our theories and methods of design and
production at this time...\
...We should not expect the production of such systems to be easy.*\
\hfill --Kenneth Kolence, pg 71

## Advices

\onslide<1->{
\begin{block}{NATO Conference 68}
Define a subset of the system which is small enough to bring to an operational
state...then build on that subsystem. This strategy requires that the system be
designed in modules which can be realized, tested, and modified independently.
\end{block}
}

\onslide<2->{
\begin{block}{UNIX Philosophy}
Write programs that do one thing and do it well. Write programs to work
together. Write programs to handle text streams, because that is an universal
interface.
\end{block}
}

\onslide<3->{
\begin{block}{Agile manifesto}
Deliver working software frequently, from a couple of weeks to a couple of
months, with a preference to the shorter timescale.
\end{block}
}

# The What

## System specification

### All Items

- All items have a `SellIn` value which denotes number of days within to sell it
- All items have a `Quality` value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item

### Specific Items

- Once the sell by date has passed, `Quality` degrades twice as fast
- The `Quality` of an item is never negative
- `Aged Brie` actually increases in Quality the older it gets
- The `Quality` of an item is never more than 50
- `Sulfuras`, being a legendary item, never has to be sold or decreases in `Quality`
- `Backstage passes`, increases in `Quality` as its `SellIn` value approaches;

## Requirement test

```python
def test_sell_in(item, inventory):
    """SellIn is lowered"""
    initial_sell_in = item.sell_in
    inventory.update()
    assert item.sell_in < initial_sell_in
```

## Behavior

### Items
- Tracks sell in time measured in number of days
- Measures how valuable it is with `quality`

### System
- Tracks the inventory of items
- Updates inventory everyday according to its type

## Behavior test

```python
# tests/gilded_rose/test_inventory_handling_general_item.py
...
ITEM_ID = 'General Item'
SELL_IN_DECREASE = {normal: 1}
TestcaseFactory = Callable[[str, int, int], Item]
...
def test_sell_in_decrease_rate_is_normal(make_testcase: TestcaseFactory):
    init_sell_in = 10
    item = make_testcase(ITEM_ID, init_sell_in, 10)
    assert item.sell_in == init_sell_in - SELL_IN_DECREASE['normal']
...
```

## New feature

- `Conjured` items should degrade in `Quality` twice as fast as normal items

# The How

## Programming paradigms

### Procedural
```python
# src/devbg2024/gilded_rose.py
...
if item.quality > 0:
    if item.name != "Sulfuras":
        item.quality = item.quality - 1
...
```

### Object oriented
```python
# src/devbg2024/objects_inventory.py
...
item.update_sell_in()
item.update_quality()
...
```

### Functional
```python
# src/devbg2024/objects_inventory.py
...
self._items = [ general_sell_in_strategy(item) for item in self._items]
self._items = [ general_quality_strategy(item) for item in self._items]
...
```

## Item as an object
```python
# src/devbg2024/item_objects.py
...
class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        ...
        self._sell_in_strategy: SellInStrategy = GeneralSellInStrategy()
        self._quality_strategy: QualityStrategy = GeneralQualityStrategy()

    def update_quality(self) -> None:
        self.quality = self._quality_strategy.apply(self.quality, self.sell_in)
        return

    def change_quality_strategy(self, strategy: QualityStrategy) -> None:
        self._quality_strategy = strategy
...
```

## Item as an object
```python
# src/devbg2024/item_objects.py
...
class QualityStrategy(ABC):
    MIN = 0
    MAX = 50
    DEGRADE_RATE = 1

    @abstractmethod
    def apply(self, value: int, sell_in: int) -> int:
        ...

class GeneralQualityStrategy(QualityStrategy):
    def apply(self, value: int, sell_in: int) -> int:
        if value >= self.MAX:
            return self.MAX

        if value <= self.MIN:
            return self.MIN

        return value - self.DEGRADE_RATE if sell_in > 0 else value - 2*self.DEGRADE_RATE
...
```

## Item as a structure
```python
# src/devbg2024/item_structs.py
...
class Item(NamedTuple):
    name: str
    sell_in: int
    quality: int

StrategyPredicate = Callable[[Item], bool]
ItemStrategy = Callable[[Item], Item]
...
```

## Item as a structure
```python
# src/devbg2024/item_structs.py
...
def make_quality_strategy(min: int = 0,
                          max: int = 50,
                          degrade_rate: int = 1,
                          predicate: StrategyPredicate = lambda _: True) -> ItemStrategy:
    def strategy(item: Item) -> Item:
        if not predicate(item):
            return item

        if item.quality >= max:
            return Item(item.name, item.sell_in, max)

        if item.quality <= min:
            return Item(item.name, item.sell_in, min)

        quality = item.quality - degrade_rate if item.sell_in > 0 else item.quality - 2*degrade_rate
        return Item(item.name, item.sell_in, quality)

    return strategy
...
```

# The Why

## Constraints on item

- Should item with negative sell in or quality even exists?
- Item is used as category, should one with arbitrary name exit?

## Validated item
```python
# src/devbg2024/item_validated.py
class NameValidator:
    def __init__(self, *options):
        self.options = set(options)

    def  __get__(self,obj,_):
        return obj._name

    def __set__(self, obj, value):
        if value not in self.options:
            raise ValueError(f'Item name must be one of {self.options}, got {value}')
        obj._name = value
...
class Item:
    name = NameValidator('General Item')
    ...
    def __init__(self, name, sell_in, quality):
        self.name = name
        ...
```

## Angry Shareholder

![Goblin doesn't believe in shared code ownership](data/goblin_not_into_peer_programming.jpg){width=50%}

## Item as a type
```python
# src/devbg2024/item_type.py
FIELDS = {
    'name': NameValidator('General Item'),
    'sell_in': SellInValidator(),
    'quality': QualityValidator(0, 50)
}

class ItemType(type):
    def __new__(cls, name, bases, namespace):
        namespace.update(FIELDS)
        return super().__new__(cls, name, bases, namespace)

class Item(metaclass=ItemType):
    def __init__(self, name, sell_in, quality):
        ...
```

# Epilogue

## Metaclasses

Usefull tool
