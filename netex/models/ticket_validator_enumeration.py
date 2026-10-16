from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TicketValidatorEnumeration(StrEnum):
    PAPER_STAMP = "paperStamp"
    CONTACT_LESS = "contactLess"
    MAGNETIC = "magnetic"
    OTHER = "other"
