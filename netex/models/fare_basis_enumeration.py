from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FareBasisEnumeration(StrEnum):
    ROUTE = "route"
    DISTANCE = "distance"
