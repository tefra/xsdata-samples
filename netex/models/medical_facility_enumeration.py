from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MedicalFacilityEnumeration(StrEnum):
    UNKNOWN = "unknown"
    DEFIBRILLATOR = "defibrillator"
    ALCOHOL_TEST = "alcoholTest"
