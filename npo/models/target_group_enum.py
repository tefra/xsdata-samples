from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class TargetGroupEnum(Enum):
    KIDS_6 = "KIDS_6"
    KIDS_12 = "KIDS_12"
    YOUNG_ADULTS = "YOUNG_ADULTS"
    ADULTS = "ADULTS"
    ADULTS_WITH_KIDS_6 = "ADULTS_WITH_KIDS_6"
    ADULTS_WITH_KIDS_12 = "ADULTS_WITH_KIDS_12"
    EVERYONE = "EVERYONE"
