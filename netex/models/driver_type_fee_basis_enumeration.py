from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DriverTypeFeeBasisEnumeration(StrEnum):
    FREE = "free"
    PER_ADDTIONAL_DRIVER = "perAddtionalDriver"
    OTHER = "other"
