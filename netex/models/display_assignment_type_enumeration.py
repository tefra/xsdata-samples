from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DisplayAssignmentTypeEnumeration(StrEnum):
    ARRIVALS = "arrivals"
    DEPARTURES = "departures"
    ALL = "all"
