from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CheckServiceEnumeration(StrEnum):
    SELF_SERVICE = "selfService"
    COUNTER_SERVICE = "counterService"
    ANY_SERVICE = "anyService"
    OTHER = "other"
