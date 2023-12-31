from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CouplingTypeEnumeration(Enum):
    UNDEFINED = "undefined"
    PLUG = "plug"
    PANTOGRAPH_ABOVE = "pantographAbove"
    PANTOGRAPH = "pantograph"
    INDUCTION = "induction"
    OTHER = "other"
