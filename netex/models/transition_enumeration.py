from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransitionEnumeration(StrEnum):
    UP = "up"
    DOWN = "down"
    LEVEL = "level"
    UP_AND_DOWN = "upAndDown"
    DOWN_AND_UP = "downAndUp"
