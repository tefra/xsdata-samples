from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GenderLimitationEnumeration(StrEnum):
    BOTH = "both"
    FEMALE_ONLY = "femaleOnly"
    MALE_ONLY = "maleOnly"
    SAME_SEX_ONLY = "sameSexOnly"
