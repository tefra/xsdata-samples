from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StatusEnumeration(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    OTHER = "other"
