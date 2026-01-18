from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class HeadwayUseEnumeration(Enum):
    DISPLAY_PASSING_TIMES_ONLY = "DisplayPassingTimesOnly"
    DISPLAY_AS_WELL_AS_PASSING_TIMES = "DisplayAsWellAsPassingTimes"
    DISPLAY_INSTEAD_OF_PASSING_TIMES = "DisplayInsteadOfPassingTimes"
