from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MediaTypeEnumeration(StrEnum):
    NONE = "none"
    PAPER_TICKET = "paperTicket"
    PAPER_TICKET_WITH_COUPONS = "paperTicketWithCoupons"
    COUPON = "coupon"
    SELF_PRINT_PAPER_TICKET = "selfPrintPaperTicket"
    SMART_CARD = "smartCard"
    MOBILE_APP = "mobileApp"
    LICENCE_PLATE = "licencePlate"
    CARD = "card"
    MMS = "mms"
    SMS = "sms"
    OTHER = "other"
