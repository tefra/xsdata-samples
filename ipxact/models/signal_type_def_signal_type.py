from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class SignalTypeDefSignalType(StrEnum):
    CONTINUOUS_CONSERVATIVE = "continuous-conservative"
    CONTINUOUS_NON_CONSERVATIVE = "continuous-non-conservative"
    DISCRETE = "discrete"
    DIGITAL = "digital"
