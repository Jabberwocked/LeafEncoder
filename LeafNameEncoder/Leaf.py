from bitarray import bitarray

from LeafNameEncoder.BinaryConverter import BinaryConverter
from LeafNameEncoder.LeafDecoder import LeafDecoder
from LeafNameEncoder.LeafEncoder import LeafEncoder
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueTypeMap, ValueType


class Leaf():
    def __init__(self):
        self.valueTypeMap = ValueTypeMap().getValueTypes()
        self.BinaryConverter = BinaryConverter()
        self.LeafDecoder = LeafDecoder()
        self.LeafEncoder = LeafEncoder()

    def create(self, values):
        return self.LeafEncoder.encode(values)

    def decode(self, encodedLeaf):
        return self.LeafDecoder.decode(encodedLeaf)

