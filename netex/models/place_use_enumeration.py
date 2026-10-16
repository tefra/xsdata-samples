from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PlaceUseEnumeration(StrEnum):
    START_AT = "startAt"
    END_AT = "endAt"
    VIA = "via"
    RESTRICT_TO = "restrictTo"
    OTHER = "other"
