from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ModeErrorReactionPolicyEnumSimple(Enum):
    """
    :cvar DEFAULT_MODE: This represents the ability to switch to the
        defaultMode in case of a mode error.
    :cvar LAST_MODE: This represents the ability to keep the last mode
        in case of a mode error.
    """
    DEFAULT_MODE = "DEFAULT-MODE"
    LAST_MODE = "LAST-MODE"
