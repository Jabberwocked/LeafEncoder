#!/usr/bin/env python
from LeafTest import runTest as leafRun
from ValueTypes.DayHourTest import runTest as dayHourRun
from ValueTypes.UTinyIntTest import runTest as uTinyIntRun
from ValueTypes.UShortTest import runTest as uShortIntRun
from ValueTypes.UIntTest import runTest as uIntRun
from BinaryConverterTest import runTest as binConvRun

def main():
    leafRun()
    dayHourRun()
    uTinyIntRun()
    uShortIntRun()
    uIntRun()

    binConvRun()

if __name__ == '__main__':
    main()