class NameValidator:
    def __init__(self, *options):
        self.options = set(options)

    def  __get__(self,obj,_):
        return obj._name

    def __set__(self, obj, value):
        if value not in self.options:
            raise ValueError(f'Item name must be one of {self.options}, got {value}')
        obj._name = value

class SellInValidator:
    def  __get__(self,obj,_):
        return obj._sell_in

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f'Cannot have negative sell in time')
        obj._sell_in = value

class QualityValidator:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def  __get__(self,obj,_):
        return obj._quality

    def __set__(self, obj, value):
        if not self.min <= value <= self.max:
            raise ValueError(f'Item quality value out of boundaries [{self.min}, {self.max}]')
        obj._quality = value

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
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
