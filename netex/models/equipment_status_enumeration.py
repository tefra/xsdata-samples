from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EquipmentStatusEnumeration(Enum):
    UNKNOWN = "unknown"
    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"
