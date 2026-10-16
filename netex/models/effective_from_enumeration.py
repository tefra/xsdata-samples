from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EffectiveFromEnumeration(StrEnum):
    NEVER = "never"
    NEXT_INTERVAL = "nextInterval"
    NEXT_INSTALLMENT = "nextInstallment"
    ANY_TIME = "anyTime"
    OTHER = "other"
