from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GradientEnumeration(StrEnum):
    VERY_STEEP = "verySteep"
    STEEP = "steep"
    MEDIUM = "medium"
    GENTLE = "gentle"
    LEVEL = "level"
