#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
from bitarray import bitarray

from LeafNameEncoder.BinaryConverter import BinaryConverter


class ValueType(metaclass=ABCMeta):
    def __init__(self):
        self.binaryConverter = BinaryConverter()

    @abstractmethod
    def encode(self, value)-> bitarray:
        pass
    @abstractmethod
    def decode(self, value):
        pass
    @abstractmethod
    def getSize(self) -> int:
        pass
