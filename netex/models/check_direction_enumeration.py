from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CheckDirectionEnumeration(Enum):
    FORWARDS = "forwards"
    BACKWARDS = "backwards"
    BOTH_WAYS = "bothWays"
