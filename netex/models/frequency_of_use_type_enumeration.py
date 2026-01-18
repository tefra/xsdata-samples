from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FrequencyOfUseTypeEnumeration(Enum):
    NONE = "none"
    UNLIMITED = "unlimited"
    LIMITED = "limited"
    TWICE_ADAY = "twiceADay"
    SINGLE = "single"
