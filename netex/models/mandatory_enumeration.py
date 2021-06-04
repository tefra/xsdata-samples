from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MandatoryEnumeration(Enum):
    REQUIRED = "required"
    OPTIONAL_VALUE = "optional"
    NOT_ALLOWED = "notAllowed"
