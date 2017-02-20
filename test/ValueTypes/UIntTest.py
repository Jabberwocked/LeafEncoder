#!/usr/bin/env python
from LeafNameEncoder.ValueTypes.UInt import UInt


def encode():
    # arrange
    expected = '00000000000000001101010100100100'
    sut = UInt()
    # act
    actual = sut.encode(54564)
    # assert
    if expected != actual:
        print('Convert failed: expected:', expected, ' actual:', actual)

def decode():
    # arrange
    expected = 54564
    sut = UInt()
    # act
    actual = sut.decode('00000000000000001101010100100100')
    # assert
    if expected != actual:
        print('Convert failed: expected:', expected, ' actual:', actual)

def withSignedValueShouldRaiseException():
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

def withValueTooBigShouldRaiseException():
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

def withTwoArgsShouldRaiseException():
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