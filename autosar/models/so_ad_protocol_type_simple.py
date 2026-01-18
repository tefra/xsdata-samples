from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoAdProtocolTypeSimple(Enum):
    """
    :cvar TCP: Transmission Control Protocol (TCP) enables two hosts to
        establish a connection and exchange streams of data.
    :cvar UDP: User Datagram Protocol (UDP) offers a connectionless way
        to send and receive datagrams over an IP network. It's used
        primarily for broadcasting messages over a network.
    """

    TCP = "TCP"
    UDP = "UDP"
