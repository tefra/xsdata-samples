from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeriesTypeEnumeration(Enum):
    STATION_TO_STATION = "stationToStation"
    ORIGIN_TO_BORDER = "originToBorder"
    BORDER_TO_DESTINATION = "borderToDestination"
    BORDER = "border"
    TRANSIT = "transit"
