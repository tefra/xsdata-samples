from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ModificationEnumeration(Enum):
    NEW = "new"
    REVISE = "revise"
    DELETE = "delete"
    UNCHANGED = "unchanged"
    DELTA = "delta"
