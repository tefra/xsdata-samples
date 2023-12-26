from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IPduSignalProcessingEnumSimple(Enum):
    """
    :cvar DEFERRED: The signal indications / confirmations are deferred.
    :cvar IMMEDIATE: The signal indications / confirmations are
        performed.
    """

    DEFERRED = "DEFERRED"
    IMMEDIATE = "IMMEDIATE"
