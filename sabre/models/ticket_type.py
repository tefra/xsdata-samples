from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class TicketType(StrEnum):
    """
    Paper or e-ticket.
    """

    E_TICKET = "eTicket"
    PAPER = "Paper"
