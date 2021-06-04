from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PassageTypeEnumeration(Enum):
    NONE_VALUE = "none"
    PATHWAY = "pathway"
    CORRIDOR = "corridor"
    OVERPASS = "overpass"
    UNDERPASS = "underpass"
    TUNNEL = "tunnel"
    OTHER = "other"
