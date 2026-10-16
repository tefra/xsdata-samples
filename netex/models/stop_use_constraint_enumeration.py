from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopUseConstraintEnumeration(StrEnum):
    ARRIVING = "arriving"
    DEPARTING = "departing"
    PASSING_THROUGH = "passingThrough"
