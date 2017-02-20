#!/usr/bin/env python
import sys

from LeafNameEncoder.ValueTypes.DayHour import DayHour

def encodeFirstHourOfWeek():
    # arrange
    expected = '00000000'
    dayHour = DayHour()
    # act
    actual = dayHour.encode((0, 0))
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def decodeFirstHourOfWeek():
    # arrange
    expected = 0, 0
    dayHour = DayHour()
    # act
    actual = dayHour.decode('00000000')
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def encodeLastHourOfWeek():
    # arrange
    expected = '10100111'
    dayHour = DayHour()
    # act
    actual = dayHour.encode((6, 23))
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def decodeLastHourOfWeek():
    # arrange
    expected = 6, 23
    dayHour = DayHour()
    # act
    actual = dayHour.decode('10100111')
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def encodeFirstHourOfSecondDay():
    expected = '00011000'
    dayHour = DayHour()
    # act
    actual = dayHour.encode((1, 0))
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def decodeFirstHourOfSecondDay():
    expected = 1 , 0
    dayHour = DayHour()
    # act
    actual = dayHour.decode('00011000')
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def decodeHourZero():
    # arrange
    expected = 1
    dayHour = DayHour()
    # act
    actual = dayHour._decodeHour(1)
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def decodeHourTwentyFour():
    # arrange
    expected = 0
    dayHour = DayHour()
    # act
    actual = dayHour._decodeHour(24)
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def decodeHourTwentyFive():
    # arrange
    expected = 1
    dayHour = DayHour()
    # act
    actual = dayHour._decodeHour(25)
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def withOneArgShouldRaiseException():
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

def withThreeArgsShouldRaiseException():
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


def decodeDayFromZero():
    # arrange
    expected = 0
    dayHour = DayHour()
    # act
    actual = dayHour._decodeDay(0)
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)


def decodeDayFromTwentyThree():
    # arrange
    expected = 0
    dayHour = DayHour()
    # act
    actual = dayHour._decodeDay(23)
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)


def decodeDayFromTwentyFour():
    # arrange
    expected = 1
    dayHour = DayHour()
    # act
    actual = dayHour._decodeDay(24)
    # assert
    if expected != actual:
        print(sys._getframe().f_code.co_name)
        print('Convert failed: expected:', expected, ' actual:', actual)

def runTest():
    encodeFirstHourOfWeek()
    decodeFirstHourOfWeek()
    decodeFirstHourOfSecondDay()
    encodeFirstHourOfSecondDay()
    encodeLastHourOfWeek()
    decodeLastHourOfWeek()

    decodeHourZero()
    decodeHourTwentyFour()
    decodeHourTwentyFive()

    decodeDayFromZero()
    decodeDayFromTwentyThree()
    decodeDayFromTwentyFour()

    withOneArgShouldRaiseException()
    withThreeArgsShouldRaiseException()

def main():
    runTest()

if __name__ == '__main__':
    main()