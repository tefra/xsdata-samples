from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupCheckInEnumeration(Enum):
    NONE_VALUE = "none"
    REQUIRED = "required"
    ALLOWED = "allowed"