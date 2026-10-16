from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopUseEnumeration(StrEnum):
    ACCESS = "access"
    INTERCHANGE_ONLY = "interchangeOnly"
    PASSTHROUGH = "passthrough"
    NO_BOARDING_OR_ALIGHTING = "noBoardingOrAlighting"
