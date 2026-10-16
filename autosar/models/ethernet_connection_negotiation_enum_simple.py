from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EthernetConnectionNegotiationEnumSimple(StrEnum):
    """
    :cvar AUTO: Automatic Negotiation
    :cvar MASTER: Master
    :cvar SLAVE: Slave
    """

    AUTO = "AUTO"
    MASTER = "MASTER"
    SLAVE = "SLAVE"
