from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopUseConstraintEnumeration(Enum):
    ARRIVING = "arriving"
    DEPARTING = "departing"
    PASSING_THROUGH = "passingThrough"
