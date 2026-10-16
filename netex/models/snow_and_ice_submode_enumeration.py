from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SnowAndIceSubmodeEnumeration(StrEnum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    SNOW_MOBILE = "snowMobile"
    SNOW_CAT = "snowCat"
    SNOW_COACH = "snowCoach"
    TERRA_BUS = "terraBus"
    WIND_SLED = "windSled"
