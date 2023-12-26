from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CouplingElementEnumSimple(Enum):
    """
    :cvar HUB: A device that is used to connect segments of a LAN. In
        Hubs frames are "broadcasted" to every one of its ports.
    :cvar ROUTER: A device that routes frames between different
        networks.
    :cvar SWITCH: A device that filters and forwards frames between
        different LAN segments.
    """

    HUB = "HUB"
    ROUTER = "ROUTER"
    SWITCH = "SWITCH"
