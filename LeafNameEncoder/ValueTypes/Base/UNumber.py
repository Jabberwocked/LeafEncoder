from LeafNameEncoder.ValueTypes.Base.Number import Number
from LeafNameEncoder.ValueTypes.Base.ValueType import *


class UNumber(Number, metaclass=ABCMeta):
    def getMinValue(self) -> int:
        return 0

    def decode(self, value):
        return self.binaryConverter.toUNumber(value)