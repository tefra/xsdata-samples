from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeatAllocationMethodEnumeration(Enum):
    AUTO_ASSIGNED = "autoAssigned"
    SEAT_MAP = "seatMap"
    OPEN_SEATING = "openSeating"
