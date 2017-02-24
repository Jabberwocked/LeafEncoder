#!/usr/bin/env python
import sys
import unittest

from bitarray import bitarray

from LeafNameEncoder.ValueTypes.DayHour import DayHour

class DayHourTest(unittest.TestCase):

    def test_encodeFirstHourOfWeek(self):
        # arrange
        expected = bitarray('00000000')
        dayHour = DayHour()
        # act
        actual = dayHour.encode((0, 0))
        # assert
        self.assertEqual(expected, actual)

    def test_decodeFirstHourOfWeek(self):
        # arrange
        expected = 0, 0
        dayHour = DayHour()
        # act
        actual = dayHour.decode(bitarray('00000000'))
        # assert
        self.assertEqual(expected, actual)

    def test_encodeLastHourOfWeek(self):
        # arrange
        expected = bitarray('10100111')
        dayHour = DayHour()
        # act
        actual = dayHour.encode((6, 23))
        # assert
        self.assertEqual(expected, actual)

    def test_decodeLastHourOfWeek(self):
        # arrange
        expected = 6, 23
        dayHour = DayHour()
        # act
        actual = dayHour.decode(bitarray('10100111'))
        # assert
        self.assertEqual(expected, actual)

    def test_encodeFirstHourOfSecondDay(self):
        expected = bitarray('00011000')
        dayHour = DayHour()
        # act
        actual = dayHour.encode((1, 0))
        # assert
        self.assertEqual(expected, actual)

    def test_decodeFirstHourOfSecondDay(self):
        expected = 1 , 0
        dayHour = DayHour()
        # act
        actual = dayHour.decode(bitarray('00011000'))
        # assert
        self.assertEqual(expected, actual)

    def test_decodeHourZero(self):
        # arrange
        expected = 1
        dayHour = DayHour()
        # act
        actual = dayHour._decodeHour(1)
        # assert
        self.assertEqual(expected, actual)

    def test_decodeHourTwentyFour(self):
        # arrange
        expected = 0
        dayHour = DayHour()
        # act
        actual = dayHour._decodeHour(24)
        # assert
        self.assertEqual(expected, actual)

    def test_decodeHourTwentyFive(self):
        # arrange
        expected = 1
        dayHour = DayHour()
        # act
        actual = dayHour._decodeHour(25)
        # assert
        self.assertEqual(expected, actual)

    def test_withOneArgShouldRaiseException(self):
        # arrange
        raised = False
        dayHour = DayHour()
        # act
        try:
            dayHour.encode(1)
        except:
            raised = True
        # assert
        if not raised:
            print(sys._getframe().f_code.co_name)
            print('Expected exception was not raised')

    def test_withThreeArgsShouldRaiseException(self):
        # arrange
        raised = False
        dayHour = DayHour()
        # act
        try:
            dayHour.encode(1 ,2 ,3)
        except:
            raised = True
        # assert
        if not raised:
            print(sys._getframe().f_code.co_name)
            print('Expected exception was not raised')


    def test_decodeDayFromZero(self):
        # arrange
        expected = 0
        dayHour = DayHour()
        # act
        actual = dayHour._decodeDay(0)
        # assert
        self.assertEqual(expected, actual)

    def test_decodeDayFromTwentyThree(self):
        # arrange
        expected = 0
        dayHour = DayHour()
        # act
        actual = dayHour._decodeDay(23)
        # assert
        self.assertEqual(expected, actual)

    def test_decodeDayFromTwentyFour(self):
        # arrange
        expected = 1
        dayHour = DayHour()
        # act
        actual = dayHour._decodeDay(24)
        # assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()