from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ProcessingKindEnumSimple(Enum):
    """
    :cvar FILTERED: Indicates that a raw signal has been manipulated by
        some application software components by using filters.
    :cvar NONE: Indicates that none of the other option apply.
    :cvar RAW: Specifies that a signal is taken directly from the basic
        software modules, i.e. from the ECU abstraction layer. It
        indicates to a developer that the control algorithm in the
        software has to provide filters.
    """

    FILTERED = "FILTERED"
    NONE = "NONE"
    RAW = "RAW"
