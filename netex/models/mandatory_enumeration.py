from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MandatoryEnumeration(Enum):
    REQUIRED = "required"
    OPTIONAL = "optional"
    NOT_ALLOWED = "notAllowed"
