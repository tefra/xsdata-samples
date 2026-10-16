from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ToiletsTypeEnumeration(StrEnum):
    SEATED = "seated"
    URINAL = "urinal"
    SQUAT = "squat"
    SEATED_AND_URINAL = "seatedAndUrinal"
