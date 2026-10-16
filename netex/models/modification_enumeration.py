from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ModificationEnumeration(StrEnum):
    NEW = "new"
    REVISE = "revise"
    DELETE = "delete"
    UNCHANGED = "unchanged"
    DELTA = "delta"
