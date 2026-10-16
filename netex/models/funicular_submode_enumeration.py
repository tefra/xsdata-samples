from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FunicularSubmodeEnumeration(StrEnum):
    UNKNOWN = "unknown"
    FUNICULAR = "funicular"
    STREET_CABLE_CAR = "streetCableCar"
    ALL_FUNICULAR_SERVICES = "allFunicularServices"
    UNDEFINED_FUNICULAR = "undefinedFunicular"
