from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeRailTicketFulfillmentOption2(Enum):
    """
    The type of Rail Ticket Fulfillment Type.
    """
    AGENCY = "Agency"
    COURIER = "Courier"
    KIOSK = "Kiosk"
    MAIL = "Mail"
    TICKETLESS = "Ticketless"
    OTHER = "Other"
