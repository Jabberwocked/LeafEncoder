#!/usr/bin/env python
from LeafNameEncoder.ValueTypes.UShort import UShort


def encode():
    # arrange
    expected = '0011101110000100'
    sut = UShort()
    # act
    actual = sut.encode(15236)
    # assert
    if expected != actual:
        print('Convert failed: expected:', expected, ' actual:', actual)

def decode():
    # arrange
    expected = 15236
    sut = UShort()
    # act
    actual = sut.decode('0011101110000100')
    # assert
    if expected != actual:
        print('Convert failed: expected:', expected, ' actual:', actual)

def withSignedValueShouldRaiseException():
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

def withValueTooBigShouldRaiseException():
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

def withTwoArgsShouldRaiseException():
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

def runTest():
    encode()
    decode()
    withSignedValueShouldRaiseException()
    withValueTooBigShouldRaiseException()
    withTwoArgsShouldRaiseException()

def main():
    runTest()

if __name__ == '__main__':
    main()