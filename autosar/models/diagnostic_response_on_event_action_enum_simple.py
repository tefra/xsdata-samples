from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticResponseOnEventActionEnumSimple(Enum):
    """
    :cvar CLEAR: Clears the configured events.
    :cvar REPORT: Reports the activated events.
    :cvar START: Starts the response on event service.
    :cvar STOP: Stops the response on event service.
    """

    CLEAR = "CLEAR"
    REPORT = "REPORT"
    START = "START"
    STOP = "STOP"
