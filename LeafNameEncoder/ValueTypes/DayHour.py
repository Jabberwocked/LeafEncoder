from LeafNameEncoder.Validator import Validator
from LeafNameEncoder.ValueTypes.Base.ValueType import *


class DayHour(ValueType):

    def encode(self, value) -> bitarray:
        """
        transforms day of week and hour into an array of bits.
        :param args[0]: zero-based day of week, starting on Monday = 0.
        :param args[1]: zero-based hour of day (24h representation, where hour 0 goes from 0:00 to 0:59).
        """
        Validator.lenOfTuple(value, 2)

        dayOfWeek = value[0]
        hour = value[1]
        product = (dayOfWeek * 24) + hour
        return self.binaryConverter.from_u_number_to_bit_array(product, self.getSize())

    def decode(self, value) -> (int, int):
        decodedvalue = self.binaryConverter.from_bit_array_to_u_number(value)
        return self._decodeDay(decodedvalue), self._decodeHour(decodedvalue)

    def getSize(self):
        return 8

    def _decodeHour(self,  value) -> int:
        return ( value % 24 )

    def _decodeDay(self, value) -> int:
        return ( value // 24 )