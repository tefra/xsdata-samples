from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BooleanOperatorEnumeration(Enum):
    AND_VALUE = "AND"
    OR_VALUE = "OR"
    NOT_VALUE = "NOT"
    XOR = "XOR"
