from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeatAllocationMethodEnumeration(StrEnum):
    AUTO_ASSIGNED = "autoAssigned"
    SEAT_MAP = "seatMap"
    OPEN_SEATING = "openSeating"
