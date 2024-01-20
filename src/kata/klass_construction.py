class Klass:
    """demonstrate object creation steps trough stdout messages"""

    def __new__(cls, *args, **kwargs):
        print('Object of type Klass is being created')
        obj = super().__new__(cls)
        return obj

    def __init__(self, attr):
        print('Klass object attributes are initialized')
        self.attr = attr

    def mthd(self, value):
        print('Public method is called')
        return self.attr + value

def inline_klass_factory(name):
    """demonstrate runtime class creation, duplicating Klass"""
    return type(f'InlineKlass{name}', (), {'mthd': lambda self, value: value+42})

class KlassType(type):
    """demonstrate steps for creating costume class creating process"""
    @classmethod
    def __prepare__(metaclass, cls, bases):
        print('Preparing class namespace')
        return {'injected_attr': 42}

    def __new__(metacls, cls, bases, clsdict):
        print('Object of type class is being created')
        return super().__new__(metacls, cls, bases, clsdict)

class KlassTypeInstance(metaclass=KlassType):
    """demonstrate object creation steps trough stdout messages"""
    def __new__(cls, *args, **kwargs):
        print('Object of type Klass is being created')
        obj = super().__new__(cls)
        return obj

    def __init__(self, attr):
        print('Klass object attributes are initialized')
        self.attr = attr

    def mthd(self, value):
        print('Public method is called')
        return self.attr + value
