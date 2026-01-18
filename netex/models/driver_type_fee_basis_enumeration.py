from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DriverTypeFeeBasisEnumeration(Enum):
    FREE = "free"
    PER_ADDTIONAL_DRIVER = "perAddtionalDriver"
    OTHER = "other"
