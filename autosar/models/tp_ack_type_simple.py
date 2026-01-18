from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TpAckTypeSimple(Enum):
    """
    :cvar ACK_WITH_RT: Acknowledgement with retry.
    :cvar NO_ACK: No acknowledgement.
    """

    ACK_WITH_RT = "ACK-WITH-RT"
    NO_ACK = "NO-ACK"
