from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopPlaceWeightEnumeration(StrEnum):
    INTERNATIONAL = "international"
    NATIONAL = "national"
    REGIONAL = "regional"
    LOCAL = "local"
