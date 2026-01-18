from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TicketValidatorEnumeration(Enum):
    PAPER_STAMP = "paperStamp"
    CONTACT_LESS = "contactLess"
    MAGNETIC = "magnetic"
    OTHER = "other"
