from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SafetyFacilityEnumeration(StrEnum):
    CC_TV = "ccTv"
    MOBILE_COVERAGE = "mobileCoverage"
    SOS_POINTS = "sosPoints"
    STAFFED = "staffed"
