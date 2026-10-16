from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DeadRunTypeEnumeration(StrEnum):
    GARAGE_RUN_OUT = "garageRunOut"
    GARAGE_RUN_IN = "garageRunIn"
    TURNING_MANOEUVRE = "turningManoeuvre"
    OTHER = "other"
