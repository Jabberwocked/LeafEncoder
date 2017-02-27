#!/usr/bin/env python
import unittest

from LeafNameEncoder.Leaf import Leaf
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueType


class LeafTest(unittest.TestCase):


    def test_encode_decode_zeroes(self):
        # arrange
        sut = Leaf()
        expected = [(ValueType.DayHour, (0, 0)), (ValueType.UShort, 0)]
        encodedValues = sut.create(expected)
        # act
        actual = sut.decode(encodedValues)
        # assert
        self.assertEqual(expected, actual)

    def test_encode_decode_values(self):
        # arrange
        sut = Leaf()
        expected = [(ValueType.DayHour, (2, 11)), (ValueType.UShort, 23124)]
        encodedValues = sut.create(expected)
        # act
        actual = sut.decode(encodedValues)
        # assert
        self.assertEqual(expected, actual)

    def test_encode_decode_four_day_hours(self):
        # arrange
        sut = Leaf()
        expected = [(ValueType.DayHour, (1, 10)),
                    (ValueType.DayHour, (2, 11)),
                    (ValueType.DayHour, (3, 14)),
                    (ValueType.DayHour, (5, 15))]
        encodedValues = sut.create(expected)
        # act
        actual = sut.decode(encodedValues)
        # assert
        self.assertEqual(expected, actual)

    def test_encodeBucketZeroDayZeroHourZero(self):
        # arrange
        expected = 'd-bt'
        sut = Leaf()
        values = [(ValueType.DayHour, (0, 0)), (ValueType.UShort, 0)]
        # act
        actual = sut.create(values)
        # assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
