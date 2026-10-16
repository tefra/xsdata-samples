from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OnBecomingEnumeration(StrEnum):
    AUTOMATIC = "automatic"
    INVITE = "invite"
    NO_ACTION = "noAction"
    OTHER = "other"
