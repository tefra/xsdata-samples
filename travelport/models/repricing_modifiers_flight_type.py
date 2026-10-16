from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class RepricingModifiersFlightType(StrEnum):
    DIRECT = "Direct"
    NON_STOP = "NonStop"
    SINGLE_CONNECTION = "SingleConnection"
    NO_RESTRICTIONS = "NoRestrictions"
