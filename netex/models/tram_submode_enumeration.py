from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TramSubmodeEnumeration(StrEnum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    CITY_TRAM = "cityTram"
    LOCAL_TRAM = "localTram"
    REGIONAL_TRAM = "regionalTram"
    SIGHTSEEING_TRAM = "sightseeingTram"
    SHUTTLE_TRAM = "shuttleTram"
    TRAIN_TRAM = "trainTram"
