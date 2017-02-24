#!/usr/bin/env python
import unittest

from bitarray import bitarray

from LeafNameEncoder.ValueTypes.UInt import UInt

class UIntTest(unittest.TestCase):
    
    def test_encode(self):
        # arrange
        expected = bitarray('00000000000000001101010100100100')
        sut = UInt()
        # act
        actual = sut.encode(54564)
        # assert
        self.assertEqual(expected, actual)
    
    def test_decode(self):
        # arrange
        expected = 54564
        sut = UInt()
        # act
        actual = sut.decode(bitarray('00000000000000001101010100100100'))
        # assert
        self.assertEqual(expected, actual)
    
    def test_withSignedValueShouldRaiseException(self):
        # arrange
        raised = False
        sut = UInt()
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
        sut = UInt()
        # act
        try:
            sut.encode(4294967296)
        except:
            raised = True
        # assert
        if not raised:
            print('Expected exception was not raised')
    
    def test_withTwoArgsShouldRaiseException(self):
        # arrange
        raised = False
        sut = UInt()
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