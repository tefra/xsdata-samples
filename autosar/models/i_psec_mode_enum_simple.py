from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IPsecModeEnumSimple(Enum):
    """
    :cvar TRANSPORT: Signifying that the IPSec transport mode is used.
        With the transport mode the original IP header is retained and
        only the IP payload and ESP trailer is encrypted.
    :cvar TUNNEL: Signifying that the IPSec tunnel mode is used. With
        tunnel mode, the entire original IP packet is protected by
        IPSec. This means IPSec wraps the original packet, encrypts it,
        adds a new IP header and sends it to the other side.
    """

    TRANSPORT = "TRANSPORT"
    TUNNEL = "TUNNEL"
