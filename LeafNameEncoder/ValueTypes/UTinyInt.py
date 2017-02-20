from LeafNameEncoder.ValueTypes.Base.UNumber import *

class UTinyInt(UNumber):

    def getSize(self) -> int:
        return 8

    def getMaxValue(self) -> int:
        return 255