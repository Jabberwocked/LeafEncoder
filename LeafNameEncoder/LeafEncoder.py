from bitarray import bitarray

from LeafNameEncoder.BinaryConverter import BinaryConverter
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueTypeMap


class LeafEncoder():

    def __init__(self):
        self.BinaryConverter = BinaryConverter()
        self.value_types = ValueTypeMap().getValueTypes()

    def encode(self, values):
        return self._convert_encoded_values_to_leaf(self.encode_values(values))

    def encode_values(self, values):
        encodedResult = bitarray()
        for (valueType, value) in values:
            encodedResult += self.encode_value_type_and_value(value, valueType)
        return encodedResult

    def encode_value_type_and_value(self, value, valueType):
        encodedResult = self.value_types[valueType].encode(value)
        encodedResult += self.BinaryConverter.from_u_number_to_bit_array(valueType.value, 4)
        return encodedResult

    def _convert_encoded_values_to_leaf(self, encodedResult):
        result = BinaryConverter().from_bit_array_to_base_encoded_string(encodedResult)
        if (len(result) > 7):
            raise Exception('The encoded result is bigger than the allowed leaf name:', len(result))
        return result