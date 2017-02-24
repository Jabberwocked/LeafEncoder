#!/usr/bin/env python
import unittest

from bitarray import bitarray
from LeafNameEncoder.BinaryConverter import BinaryConverter

class BinaryConverterTest(unittest.TestCase):

    def test_convertNumberToBits(self):
        # arrange
        expected = bitarray('01111111')
        converter = BinaryConverter()
        # act
        actual = converter.from_u_number_to_bit_array(127, 8)
        # assert
        self.assertEqual(expected, actual)

    def test_convertBitsToAscii(self):
        # arrange
        expected = 'c:rQW@KYW("S:w'
        bits = bitarray('0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100')
        converter = BinaryConverter()
        # act
        actual = converter.from_bit_array_to_base_encoded_string(bits)
        # assert
        self.assertEqual(expected, actual)

    def test_convert_to_from_base_encoded_string_round_trip(self):
        # arrange
        converter = BinaryConverter()
        expected = bitarray('1001')
        # act
        encoded = converter.from_bit_array_to_base_encoded_string(expected)
        actual = converter.from_base_encoded_string_to_bit_array(encoded)
        # assert
        self.assertEqual(expected, actual)

    def test_convertBitsToInt(self):
        # arrange
        expected = 118
        converter = BinaryConverter()
        # act
        actual = converter.from_bit_array_to_u_number(bitarray('1110110'))
        # assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()