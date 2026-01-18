from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ResidenceTypeEnumeration(Enum):
    LIVE = "live"
    WORK = "work"
    STUDY = "study"
    EXCHANGE = "exchange"
    BORN = "born"
    NON_RESIDENT = "nonResident"
