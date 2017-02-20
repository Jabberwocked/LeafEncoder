#!/usr/bin/env python
from LeafNameEncoder.ValueTypes.UTinyInt import UTinyInt


def encode():
    # arrange
    expected = '01110011'
    sut = UTinyInt()
    # act
    actual = sut.encode(115)
    # assert
    if expected != actual:
        print('Convert failed: expected:', expected, ' actual:', actual)


def decode():
    # arrange
    expected = 115
    sut = UTinyInt()
    # act
    actual = sut.decode('01110011')
    # assert
    if expected != actual:
        print('Convert failed: expected:', expected, ' actual:', actual)

def withSignedValueShouldRaiseException():
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

def withValueTooBigShouldRaiseException():
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

def withTwoArgsShouldRaiseException():
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