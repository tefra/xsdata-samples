from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RxAcceptContainedIPduEnumSimple(Enum):
    """
    :cvar ACCEPT_ALL: No fixed set of containedIPdus is defined for
        reception, any known containedIPdu (based on headerId) shall be
        expected within this ContainerIPdu.
    :cvar ACCEPT_CONFIGURED: A fixed set of containedIPdus is defined
        for reception. Only these assigned containedIPdus (based on
        headerId) are expected in this ContainerIPdu. If a not assigned
        containedIPdu is received within this ContainerIPdu this
        containedIPdu is discarded.
    """
    ACCEPT_ALL = "ACCEPT-ALL"
    ACCEPT_CONFIGURED = "ACCEPT-CONFIGURED"
