from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TriggerModeSimple(Enum):
    """
    :cvar DYNAMIC_PART_TRIGGER: IPduM sends a transmission request to
        the PduR if a dynamic part is received.
    :cvar NONE: IPduM does not trigger transmission because of receiving
        anything of this IPdu in case of TriggerTransmit.
    :cvar STATIC_OR_DYNAMIC_PART_TRIGGER: IPduM sends a transmission
        request to the PduR if a static or dynamic part is received.
    :cvar STATIC_PART_TRIGGER: IPduM sends a transmission request to the
        PduR if a static part is received.
    """
    DYNAMIC_PART_TRIGGER = "DYNAMIC-PART-TRIGGER"
    NONE = "NONE"
    STATIC_OR_DYNAMIC_PART_TRIGGER = "STATIC-OR-DYNAMIC-PART-TRIGGER"
    STATIC_PART_TRIGGER = "STATIC-PART-TRIGGER"
