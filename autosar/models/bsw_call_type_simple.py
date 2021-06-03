from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class BswCallTypeSimple(Enum):
    """
    :cvar CALLBACK: Callback (i.e. the caller specifies the signature)
    :cvar CALLOUT: Callout - provide defined means to extend the
        functionality of an existing module.  In this case caller
        specifies the signature.
    :cvar INTERRUPT: Interrupt routine
    :cvar REGULAR: Regular API call
    :cvar SCHEDULED: Called by the scheduler
    """
    CALLBACK = "CALLBACK"
    CALLOUT = "CALLOUT"
    INTERRUPT = "INTERRUPT"
    REGULAR = "REGULAR"
    SCHEDULED = "SCHEDULED"
