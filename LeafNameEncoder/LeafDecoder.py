from bitarray import bitarray

from LeafNameEncoder.BinaryConverter import BinaryConverter
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueType, ValueTypeMap


class LeafDecoder():
    def __init__(self):
        self.value_type_map = ValueTypeMap().getValueTypes()
        self.binary_converter = BinaryConverter()
        self.decoded_total = None
        self.result = None

    def decode(self, encodedLeaf):
        self.initialize(encodedLeaf)

        while (self.decoded_total):
            self.decode_next_value()
        return self.result

    def initialize(self, encodedLeaf):
        self.result = []
        self.decoded_total = self.binary_converter.from_base_encoded_string_to_bit_array(encodedLeaf)

    def decode_next_value(self):
        valueType = self.decode_value_type()
        value = self.decode_value(valueType)
        self.result.insert(0, (valueType, value))

    def decode_value(self, valueType):
        value_type_obj = self.value_type_map[ValueType(valueType)]
        value_type_size = value_type_obj.getSize()
        value = value_type_obj.decode(self.decoded_total[-value_type_size:])
        self.decoded_total = self.decoded_total[:-value_type_size]
        return value

    def decode_value_type(self):
        valueTypeId = self.binary_converter.from_bit_array_to_u_number(bitarray(self.decoded_total[-4:]))
        self.decoded_total = self.decoded_total[:-4]
        value_type = ValueType(valueTypeId)
        return value_type