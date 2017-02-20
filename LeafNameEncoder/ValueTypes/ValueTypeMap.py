from enum import Enum

from LeafNameEncoder.ValueTypes.DayHour import DayHour
from LeafNameEncoder.ValueTypes.UInt import UInt
from LeafNameEncoder.ValueTypes.UShort import UShort
from LeafNameEncoder.ValueTypes.UTinyInt import UTinyInt

class ValueType(Enum):
    UTinyInt = 0
    UShort = 1
    UInt = 2
    DayHour = 3

class ValueTypeMap():
    def getValueTypes(self):
        return {ValueType.UTinyInt:UTinyInt(),
                ValueType.UShort: UShort(),
                ValueType.UInt: UInt(),
                ValueType.DayHour: DayHour()}