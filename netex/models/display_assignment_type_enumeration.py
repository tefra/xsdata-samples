from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DisplayAssignmentTypeEnumeration(Enum):
    ARRIVALS = "arrivals"
    DEPARTURES = "departures"
    ALL = "all"
