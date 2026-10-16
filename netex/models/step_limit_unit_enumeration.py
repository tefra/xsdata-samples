from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StepLimitUnitEnumeration(StrEnum):
    STOPS = "stops"
    STOPS_INCLUDING_PASS_THROUGH_STOPS = "stopsIncludingPassThroughStops"
    SECTIONS = "sections"
    ZONES = "zones"
    NETWORKS = "networks"
    OPERATORS = "operators"
    COUNTRIES = "countries"
