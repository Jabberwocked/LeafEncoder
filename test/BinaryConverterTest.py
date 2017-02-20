#!/usr/bin/env python
from bitarray import bitarray

from LeafNameEncoder.BinaryConverter import BinaryConverter

def convertNumberToBits():
    # arrange
    expected = '01111111'
    converter = BinaryConverter()
    # act
    actual = converter.fromUNumber(127, 8)
    # assert
    if expected != actual:
        print('Convert failed: expected:', expected, ' actual:', actual)


def convertBitsToAscii():
    # arrange
    expected = 'aaWF93RVY4AwqvW'
    bits = bitarray('0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100')
    converter = BinaryConverter()
    # act
    actual = converter.toAsciiString(bits)
    # assert
    if expected != actual:
        print('Convert failed: expected:', expected, ' actual:', actual)

def convertBitsToInt():
    # arrange
    expected = 118
    converter = BinaryConverter()
    # act
    actual = converter.toUNumber('1110110')
    # assert
    if expected != actual:
        print('Convert failed: expected:', expected, ' actual:', actual)

def runTest():
    convertNumberToBits()
    convertBitsToAscii()
    convertBitsToInt()

def main():
    runTest()

if __name__ == '__main__':
    main()