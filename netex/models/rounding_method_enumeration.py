from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoundingMethodEnumeration(StrEnum):
    NONE = "none"
    DOWN = "down"
    UP = "up"
    SPLIT = "split"
    STEP_TABLE = "stepTable"
