from LeafNameEncoder.ValueTypes.Base.UNumber import *

class UInt(UNumber):

    def getSize(self) -> int:
        return 32

    def getMaxValue(self) -> int:
        return  4294967295