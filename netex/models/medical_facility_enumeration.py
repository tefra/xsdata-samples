from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MedicalFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    DEFIBRILLATOR = "defibrillator"
    ALCOHOL_TEST = "alcoholTest"
