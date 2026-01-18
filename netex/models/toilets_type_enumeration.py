from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ToiletsTypeEnumeration(Enum):
    SEATED = "seated"
    URINAL = "urinal"
    SQUAT = "squat"
    SEATED_AND_URINAL = "seatedAndUrinal"
