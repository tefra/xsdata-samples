from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ContainedIPduCollectionSemanticsEnumSimple(Enum):
    """
    :cvar LAST_IS_BEST: The ContainedIPdu data will be fetched via
        TriggerTransmit just before the transmission executes.
    :cvar QUEUED: The ContainedIPdu data will instantly be stored to the
        ContainerIPdu in the context of the Transmit API.
    """

    LAST_IS_BEST = "LAST-IS-BEST"
    QUEUED = "QUEUED"
