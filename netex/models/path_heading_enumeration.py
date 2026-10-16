from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PathHeadingEnumeration(StrEnum):
    LEFT = "left"
    RIGHT = "right"
    FORWARD = "forward"
    BACK = "back"
