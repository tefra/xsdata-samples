from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CommunicationDirectionTypeSimple(StrEnum):
    """
    :cvar IN: Reception (Input)
    :cvar OUT: Transmission (Output)
    """

    IN = "IN"
    OUT = "OUT"
