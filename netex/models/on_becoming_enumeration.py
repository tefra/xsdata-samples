from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OnBecomingEnumeration(Enum):
    AUTOMATIC = "automatic"
    INVITE = "invite"
    NO_ACTION = "noAction"
    OTHER = "other"
