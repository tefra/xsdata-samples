from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CongestionEnumeration(Enum):
    NO_WAITING = "noWaiting"
    QUEUE = "queue"
    CROWDING = "crowding"
    FULL = "full"
