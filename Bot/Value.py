from enum import Enum


class Value:
    class Type(Enum):
        ABS = 0
        REL = 1

    def __init__(self, obj: str):
        if obj.endswith('%'):
            self.type = Value.Type.REL
        else:
            self.type = Value.Type.ABS

        self.v = float(obj.replace('%', ''))

    def __str__(self):
        return '{}{}'.format(self.v, '%' if self.type == Value.Type.REL else '')

    def __repr__(self):
        return self.__str__()