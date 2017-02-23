from bitarray import bitarray

from LeafNameEncoder.BinaryConverter import BinaryConverter
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueTypeMap


class Leaf():
    def __init__(self):
        self.valueTypeMap = ValueTypeMap().getValueTypes()
        self.BinaryConverter = BinaryConverter()

    def create(self, values):
        return self._convertEncodedResultToLeaf(self._encode(values))

    def _encode(self, values):
        encodedResult = bitarray()
        for (valueType, value) in values:
            encodedResult += self.EncodeValueTypeAndValue(value, valueType)
        return encodedResult

    def EncodeValueTypeAndValue(self, value, valueType):
        encodedResult = self.BinaryConverter.fromUNumber(valueType.value, 4)
        encodedResult += self.valueTypeMap[valueType].encode(value)
        return encodedResult

    def _convertEncodedResultToLeaf(self, encodedResult):
        result = BinaryConverter().toAsciiString(encodedResult)
        if (len(result) > 7):
            raise Exception('The encoded result is bigger than the allowed leaf name:', len(result))
        return result