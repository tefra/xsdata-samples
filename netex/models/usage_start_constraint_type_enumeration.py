from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageStartConstraintTypeEnumeration(Enum):
    VARIABLE = "variable"
    FIXED = "fixed"
    FIXED_WINDOW = "fixedWindow"
