from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SecurityEventReportingModeEnumSimple(Enum):
    """
    :cvar BRIEF: Only the main security event properties such as its ID
        are processed. Any additional context data (if existing) is
        discarded.
    :cvar BRIEF_BYPASSING_FILTERS: The reported security event without
        its context data (if existing) is processed further but the
        filter chain is bypassed.
    :cvar DETAILED: The main properties and the context data (if
        existing) of the reported security event are processed further.
    :cvar DETAILED_BYPASSING_FILTERS: The reported security event
        including its context data (if existing) is processed further
        but the filter chain is bypassed.
    :cvar OFF: The reported security event is not further processed by
        the IdsM and therefore discarded.
    """

    BRIEF = "BRIEF"
    BRIEF_BYPASSING_FILTERS = "BRIEF-BYPASSING-FILTERS"
    DETAILED = "DETAILED"
    DETAILED_BYPASSING_FILTERS = "DETAILED-BYPASSING-FILTERS"
    OFF = "OFF"
