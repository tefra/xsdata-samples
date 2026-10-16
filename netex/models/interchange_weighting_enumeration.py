from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class InterchangeWeightingEnumeration(StrEnum):
    NO_INTERCHANGE = "noInterchange"
    INTERCHANGE_ALLOWED = "interchangeAllowed"
    RECOMMENDED_INTERCHANGE = "recommendedInterchange"
    PREFERRED_INTERCHANGE = "preferredInterchange"
