from LeafNameEncoder.Validator import Validator
from LeafNameEncoder.ValueTypes.Base.ValueType import *


class Number(ValueType, metaclass=ABCMeta):
    @abstractmethod
    def getMaxValue(self) -> int:
        pass

    @abstractmethod
    def getMinValue(self) -> int:
        pass

    def encode(self, value) -> bitarray:
        Validator.isNumberType(value)
        Validator.minValue(value, self.getMinValue())
        Validator.maxValue(value, self.getMaxValue())

        return self.binaryConverter.from_u_number_to_bit_array(value, self.getSize())

    def decode(self, value) -> (int, int):
        pass