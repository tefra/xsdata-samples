from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ConnectionCertaintyEnumeration(Enum):
    GUARANTEED = "guaranteed"
    NORMALLY_GUARANTEED = "normallyGuaranteed"
    NOT_GUARANTEED = "notGuaranteed"
    NEVER_GUARANTEED = "neverGuaranteed"
