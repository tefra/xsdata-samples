from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CheckServiceEnumeration(Enum):
    SELF_SERVICE = "selfService"
    COUNTER_SERVICE = "counterService"
    ANY_SERVICE = "anyService"
    OTHER = "other"
