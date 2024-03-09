from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class VoidDocumentInfoDocumentType(Enum):
    SERVICE_FEE = "Service Fee"
    PAPER_TICKET = "Paper Ticket"
    MCO = "MCO"
    E_TICKET = "E-Ticket"
