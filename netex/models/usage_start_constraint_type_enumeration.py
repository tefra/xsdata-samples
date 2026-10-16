from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageStartConstraintTypeEnumeration(StrEnum):
    VARIABLE = "variable"
    FIXED = "fixed"
    FIXED_WINDOW = "fixedWindow"
