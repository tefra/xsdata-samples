from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FulfilmentMethodTypeEnumeration(Enum):
    TICKET_OFFICE = "ticketOffice"
    TICKET_MACHINE = "ticketMachine"
    CONDUCTOR = "conductor"
    AGENT = "agent"
    POST = "post"
    COURIER = "courier"
    SELFPRINT = "selfprint"
    SMS = "sms"
    EMAIL = "email"
    TOP_UP_DEVICE = "topUpDevice"
    VALIDATOR = "validator"
    MOBILE_APP = "mobileApp"
    OTHER = "other"
