#!/usr/bin/env python
import unittest

from LeafNameEncoder.ValueTypes.UTinyInt import UTinyInt

class UTinyTest(unittest.TestCase):
    
    def test_encode(self):
        # arrange
        expected = '01110011'
        sut = UTinyInt()
        # act
        actual = sut.encode(115)
        # assert
        self.assertEqual(expected, actual)
    
    
    def test_decode(self):
        # arrange
        expected = 115
        sut = UTinyInt()
        # act
        actual = sut.decode('01110011')
        # assert
        self.assertEqual(expected, actual)
    
    def test_withSignedValueShouldRaiseException(self):
        # arrange
        raised = False
        sut = UTinyInt()
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
        sut = UTinyInt()
        # act
        try:
            sut.encode(256)
        except:
            raised = True
        # assert
        if not raised:
            print('Expected exception was not raised')
    
    def test_withTwoArgsShouldRaiseException(self):
        # arrange
        raised = False
        sut = UTinyInt()
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