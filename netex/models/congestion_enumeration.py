from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CongestionEnumeration(StrEnum):
    NO_WAITING = "noWaiting"
    QUEUE = "queue"
    CROWDING = "crowding"
    FULL = "full"
