from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RelativeDirectionEnumeration(StrEnum):
    BOTH = "both"
    FORWARDS = "forwards"
    BACKWARDS = "backwards"
