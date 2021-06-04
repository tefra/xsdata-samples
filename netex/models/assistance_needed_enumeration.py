from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistanceNeededEnumeration(Enum):
    LEVEL_ACCESS = "levelAccess"
    STEP_NEGOTIATION = "stepNegotiation"
    RAMP_REQUIRED = "rampRequired"
    HOIST_REQUIRED = "hoistRequired"
    UNKNOWN = "unknown"
