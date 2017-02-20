#!/usr/bin/env python
import sys

from LeafNameEncoder.Leaf import Leaf
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueType


def encodeBucketZeroDayZeroHourZero():
    # arrange
    expected = 'kD8!u'
    sut = Leaf()
    values = [(ValueType.DayHour, (0,0)),(ValueType.UShort, 0)]
    # act
    actual = sut.create(values)
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)


def main():
    encodeBucketZeroDayZeroHourZero()

if __name__ == '__main__':
    main()