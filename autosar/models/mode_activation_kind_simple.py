from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ModeActivationKindSimple(Enum):
    """
    :cvar ON_ENTRY: On entering the referred mode.
    :cvar ON_EXIT: On exiting the referred mode.
    :cvar ON_TRANSITION: On transition of the 1st referred mode to the
        2nd referred mode.
    """
    ON_ENTRY = "ON-ENTRY"
    ON_EXIT = "ON-EXIT"
    ON_TRANSITION = "ON-TRANSITION"
