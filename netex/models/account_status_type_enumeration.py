from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccountStatusTypeEnumeration(Enum):
    UNUSED = "unused"
    UNVERIFIED = "unverified"
    ACTIVE = "active"
    DORMANT = "dormant"
    SUSPENDED = "suspended"
    ARCHIVED = "archived"
    CLOSED = "closed"
