from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccountStatusTypeEnumeration(StrEnum):
    UNUSED = "unused"
    UNVERIFIED = "unverified"
    ACTIVE = "active"
    DORMANT = "dormant"
    SUSPENDED = "suspended"
    ARCHIVED = "archived"
    CLOSED = "closed"
