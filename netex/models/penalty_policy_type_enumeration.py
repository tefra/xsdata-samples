from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PenaltyPolicyTypeEnumeration(Enum):
    NO_TICKET = "noTicket"
    NO_CHECK_IN = "noCheckIn"
    NO_CHECK_OUT = "noCheckOut"
    NO_VALIDATION = "noValidation"
    OTHER = "other"
