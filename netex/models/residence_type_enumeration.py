from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ResidenceTypeEnumeration(StrEnum):
    LIVE = "live"
    WORK = "work"
    STUDY = "study"
    EXCHANGE = "exchange"
    BORN = "born"
    NON_RESIDENT = "nonResident"
