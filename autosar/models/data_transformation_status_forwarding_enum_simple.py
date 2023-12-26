from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DataTransformationStatusForwardingEnumSimple(Enum):
    """
    :cvar NO_TRANSFORMER_STATUS_FORWARDING: The runnable is not able to
        forward a transformer status.
    :cvar TRANSFORMER_STATUS_FORWARDING: The runnable is able to forward
        a transformer status.
    """

    NO_TRANSFORMER_STATUS_FORWARDING = "NO-TRANSFORMER-STATUS-FORWARDING"
    TRANSFORMER_STATUS_FORWARDING = "TRANSFORMER-STATUS-FORWARDING"
