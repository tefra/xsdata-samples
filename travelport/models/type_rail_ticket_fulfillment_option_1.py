from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeRailTicketFulfillmentOption1(Enum):
    """
    The type of Rail Ticket Fulfillment Type.
    """

    AGENCY = "Agency"
    COURIER = "Courier"
    KIOSK = "Kiosk"
    MAIL = "Mail"
    TICKETLESS = "Ticketless"
    OTHER = "Other"
