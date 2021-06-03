from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DataExchangePointKindSimple(Enum):
    """
    :cvar AGREED: the data exchange point description represents the
        agreed data exchange point that should be used during data
        exchange
    :cvar CONSUMER: the data exchange point description represents the
        input of a consuming tool.
    :cvar PRODUCER: the data exchange point description represents the
        output of a producing tool.
    """
    AGREED = "AGREED"
    CONSUMER = "CONSUMER"
    PRODUCER = "PRODUCER"
