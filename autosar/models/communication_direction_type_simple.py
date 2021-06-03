from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CommunicationDirectionTypeSimple(Enum):
    """
    :cvar IN_VALUE: Reception (Input)
    :cvar OUT: Transmission (Output)
    """
    IN_VALUE = "IN"
    OUT = "OUT"
