from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ModificationSetEnumeration(StrEnum):
    ALL = "all"
    CHANGES_ONLY = "changesOnly"
