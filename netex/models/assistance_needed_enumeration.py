from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistanceNeededEnumeration(StrEnum):
    LEVEL_ACCESS = "levelAccess"
    STEP_NEGOTIATION = "stepNegotiation"
    RAMP_REQUIRED = "rampRequired"
    HOIST_REQUIRED = "hoistRequired"
    UNKNOWN = "unknown"
