from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CommunicationDirectionTypeSimple(Enum):
    """
    :cvar IN: Reception (Input)
    :cvar OUT: Transmission (Output)
    """
    IN = "IN"
    OUT = "OUT"
