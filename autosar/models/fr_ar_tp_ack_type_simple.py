from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class FrArTpAckTypeSimple(Enum):
    """
    :cvar ACK_WITH_RT: Acknowledgement with retry.
    :cvar ACK_WITHOUT_RT: Acknowledgement without retry.
    :cvar NO_ACK: No acknowledgement.
    """

    ACK_WITH_RT = "ACK-WITH-RT"
    ACK_WITHOUT_RT = "ACK-WITHOUT-RT"
    NO_ACK = "NO-ACK"
