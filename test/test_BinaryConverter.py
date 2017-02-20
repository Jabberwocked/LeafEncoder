#!/usr/bin/env python
import unittest

from bitarray import bitarray
from LeafNameEncoder.BinaryConverter import BinaryConverter

class BinaryConverterTest(unittest.TestCase):

    def test_convertNumberToBits(self):
        # arrange
        expected = '01111111'
        converter = BinaryConverter()
        # act
        actual = converter.fromUNumber(127, 8)
        # assert
        self.assertEqual(expected, actual)

    def test_convertBitsToAscii(self):
        # arrange
        expected = 'c:rQW@KYW("S:w'
        bits = bitarray('0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100')
        converter = BinaryConverter()
        # act
        actual = converter.toAsciiString(bits)
        # assert
        self.assertEqual(expected, actual)

    def test_convertBitsToInt(self):
        # arrange
        expected = 118
        converter = BinaryConverter()
        # act
        actual = converter.toUNumber('1110110')
        # assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()