from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class IntervalTypeEnumeration(StrEnum):
    STOP = "stop"
    TARIFF_ZONE = "tariffZone"
    DISTANCE = "distance"
    SECTION = "section"
    COUPON = "coupon"
    OTHER = "other"
