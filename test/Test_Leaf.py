#!/usr/bin/env python
import unittest

from LeafNameEncoder.Leaf import Leaf
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueType


class LeafTest(unittest.TestCase):


    def test_encode_decode(self):
        # arrange
        sut = Leaf()
        expected = [(ValueType.DayHour, (0, 0)), (ValueType.UShort, 0)]
        encodedValues = sut.create(expected)
        # act
        actual = sut.decode(encodedValues)
        # assert
        self.assertEqual(expected, actual)


    def test_encodeBucketZeroDayZeroHourZero(self):
        # arrange
        expected = 'kD8!u'
        sut = Leaf()
        values = [(ValueType.DayHour, (0, 0)), (ValueType.UShort, 0)]
        # act
        actual = sut.create(values)
        # assert
        self.assertEqual(expected, actual)

    def test_decodeLeafName(self):
        # arrange
        expected = [(ValueType.DayHour, (0, 0)), (ValueType.UShort, 0)]
        sut = Leaf()
        #act
        actual = sut.decode('kD8!u')
        #assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
