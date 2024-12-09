from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class SignalTypeDefSignalType(Enum):
    CONTINUOUS_CONSERVATIVE = "continuous-conservative"
    CONTINUOUS_NON_CONSERVATIVE = "continuous-non-conservative"
    DISCRETE = "discrete"
    DIGITAL = "digital"
