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

    def decode(self, encodedLeaf):
        result = None
        #decode the full string
        decodedTotal = self.BinaryConverter.from_base_encoded_string_to_bit_array(encodedLeaf)
        while(decodedTotal):
            valueTypeId = self.BinaryConverter.from_bit_array_to_u_number(bitarray(decodedTotal[:4]))
            decodedTotal = decodedTotal[len(decodedTotal)-4:]
            valueType = self.valueTypeMap[valueTypeId]
            valueTypeSize = valueType.getSize()
            value = valueType.decode(decodedTotal[:valueTypeSize])
            result += value
            decodedTotal = decodedTotal[len(decodedTotal)-valueTypeSize:]
        return decodedTotal

    def EncodeValueTypeAndValue(self, value, valueType):
        encodedResult = self.valueTypeMap[valueType].encode(value)
        encodedResult += self.BinaryConverter.from_u_number_to_bit_array(valueType.value, 4)
        return encodedResult

    def _convertEncodedResultToLeaf(self, encodedResult):
        result = BinaryConverter().from_bit_array_to_base_encoded_string(encodedResult)
        if (len(result) > 7):
            raise Exception('The encoded result is bigger than the allowed leaf name:', len(result))
        return result