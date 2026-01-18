from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ScopeOfTicketEnumeration(Enum):
    UNKNOWN = "unknown"
    LOCAL_TICKET = "localTicket"
    NATIONAL_TICKET = "nationalTicket"
    INTERNATIONAL_TICKET = "internationalTicket"
