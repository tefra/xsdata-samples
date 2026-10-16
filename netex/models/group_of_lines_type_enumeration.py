from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupOfLinesTypeEnumeration(StrEnum):
    MARKETING = "marketing"
    ADMINISTRATIVE = "administrative"
    SCHEDULING = "scheduling"
    CONTROL = "control"
    TARIFF = "tariff"
    OTHER = "other"
