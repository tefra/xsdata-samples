from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EventAcceptanceStatusEnumSimple(Enum):
    """
    :cvar EVENT_ACCEPTANCE_DISABLED: Acceptance of a diagnostic event is
        disabled.
    :cvar EVENT_ACCEPTANCE_ENABLED: Acceptance of a diagnostic event is
        enabled.
    """
    EVENT_ACCEPTANCE_DISABLED = "EVENT-ACCEPTANCE-DISABLED"
    EVENT_ACCEPTANCE_ENABLED = "EVENT-ACCEPTANCE-ENABLED"
