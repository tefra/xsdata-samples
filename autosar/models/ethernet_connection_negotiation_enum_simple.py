from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EthernetConnectionNegotiationEnumSimple(Enum):
    """
    :cvar AUTO: Automatic Negotiation
    :cvar MASTER: Master
    :cvar SLAVE: Slave
    """

    AUTO = "AUTO"
    MASTER = "MASTER"
    SLAVE = "SLAVE"
