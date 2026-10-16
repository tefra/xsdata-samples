from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupTicketingEnumeration(StrEnum):
    ALL_ON_ONE_TICKET = "allOnOneTicket"
    SEPARATE_TICKETS = "separateTickets"
    TICKET_WITH_COUPONS = "ticketWithCoupons"
    OTHER = "other"
