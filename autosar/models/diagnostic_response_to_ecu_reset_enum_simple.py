from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticResponseToEcuResetEnumSimple(Enum):
    """
    :cvar RESPOND_AFTER_RESET: Answer to EcuReset service should come
        after the reset.
    :cvar RESPOND_BEFORE_RESET: Answer to EcuReset service should come
        before the reset.
    """

    RESPOND_AFTER_RESET = "RESPOND-AFTER-RESET"
    RESPOND_BEFORE_RESET = "RESPOND-BEFORE-RESET"
