from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class JourneyAccountingEnumeration(StrEnum):
    CONTRACT = "contract"
    SUBSIDY = "subsidy"
    OTHER = "other"
