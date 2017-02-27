from bitarray import bitarray

from LeafNameEncoder.BinaryConverter import BinaryConverter
from LeafNameEncoder.LeafDecoder import LeafDecoder
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueTypeMap, ValueType


class Leaf():
    def __init__(self):
        self.valueTypeMap = ValueTypeMap().getValueTypes()
        self.BinaryConverter = BinaryConverter()
        self.LeafDecoder = LeafDecoder()

    def create(self, values):
        return self._convertEncodedResultToLeaf(self._encode(values))

    def decode(self, encodedLeaf):
        return self.LeafDecoder.decode(encodedLeaf)

    def _encode(self, values):
        encodedResult = bitarray()
        for (valueType, value) in values:
            encodedResult += self.EncodeValueTypeAndValue(value, valueType)
        return encodedResult

    def EncodeValueTypeAndValue(self, value, valueType):
        encodedResult = self.valueTypeMap[valueType].encode(value)
        encodedResult += self.BinaryConverter.from_u_number_to_bit_array(valueType.value, 4)
        return encodedResult

    def _convertEncodedResultToLeaf(self, encodedResult):
        result = BinaryConverter().from_bit_array_to_base_encoded_string(encodedResult)
        if (len(result) > 7):
            raise Exception('The encoded result is bigger than the allowed leaf name:', len(result))
        return result