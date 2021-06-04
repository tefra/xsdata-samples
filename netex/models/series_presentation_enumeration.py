from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeriesPresentationEnumeration(Enum):
    NONE_VALUE = "none"
    REQUIRED = "required"
    OPTIONAL_LEFT = "optionalLeft"
    OPTIONAL_RIGHT = "optionalRight"
