#!/usr/bin/env python
import unittest

from bitarray import bitarray

from LeafNameEncoder.ValueTypes.UShort import UShort

class UShortTest(unittest.TestCase):

    def test_encode(self):
        # arrange
        expected = bitarray('0011101110000100')
        sut = UShort()
        # act
        actual = sut.encode(15236)
        # assert
        self.assertEqual(expected, actual)
    
    def test_decode(self):
        # arrange
        expected = 15236
        sut = UShort()
        # act
        actual = sut.decode(bitarray('0011101110000100'))
        # assert
        self.assertEqual(expected, actual)
    
    def test_withSignedValueShouldRaiseException(self):
        # arrange
        raised = False
        sut = UShort()
        # act
        try:
            sut.encode(-1)
        except:
            raised = True
        # assert
        if not raised:
            print('Expected exception was not raised')
    
    def test_withValueTooBigShouldRaiseException(self):
        # arrange
        raised = False
        sut = UShort()
        # act
        try:
            sut.encode(65536)
        except:
            raised = True
        # assert
        if not raised:
            print('Expected exception was not raised')
    
    def test_withTwoArgsShouldRaiseException(self):
        # arrange
        raised = False
        sut = UShort()
        # act
        try:
            sut.encode(1, 2)
        except:
            raised = True
        # assert
        if not raised:
            print('Expected exception was not raised')

if __name__ == '__main__':
    unittest.main()