from LeafNameEncoder.ValueTypes.Base.UNumber import *

class UShort(UNumber):

    def getSize(self) -> int:
        return 16

    def getMaxValue(self) -> int:
        return 65535