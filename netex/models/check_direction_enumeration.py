from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CheckDirectionEnumeration(StrEnum):
    FORWARDS = "forwards"
    BACKWARDS = "backwards"
    BOTH_WAYS = "bothWays"
