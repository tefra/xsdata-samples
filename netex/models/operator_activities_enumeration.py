from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OperatorActivitiesEnumeration(StrEnum):
    PASSENGER = "passenger"
    FREIGHT = "freight"
    INFRASTRUCTURE = "infrastructure"
    OTHER = "other"
