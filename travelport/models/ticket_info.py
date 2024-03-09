from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from travelport.models.conjuncted_ticket_info import ConjunctedTicketInfo
from travelport.models.exchanged_ticket_info import ExchangedTicketInfo
from travelport.models.name_1 import Name1
from travelport.models.type_ticket_status import TypeTicketStatus

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TicketInfo:
    """
    Parameters
    ----------
    name
    conjuncted_ticket_info
    exchanged_ticket_info
    number
    iatanumber
    ticket_issue_date
    ticketing_agent_sign_on
    country_code
        Contains Ticketed PCC’s Country code.
    status
    bulk_ticket
        Whether the ticket was issued as bulk.
    booking_traveler_ref
        A reference to a passenger.
    air_pricing_info_ref
        A reference to a AirPricing.Applicable Providers 1G and 1V.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    name: None | Name1 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        },
    )
    conjuncted_ticket_info: list[ConjunctedTicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "ConjunctedTicketInfo",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    exchanged_ticket_info: list[ExchangedTicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "ExchangedTicketInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        },
    )
    iatanumber: None | str = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "max_length": 8,
        },
    )
    ticket_issue_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "TicketIssueDate",
            "type": "Attribute",
        },
    )
    ticketing_agent_sign_on: None | str = field(
        default=None,
        metadata={
            "name": "TicketingAgentSignOn",
            "type": "Attribute",
            "max_length": 9,
        },
    )
    country_code: None | str = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "length": 2,
        },
    )
    status: None | TypeTicketStatus = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    bulk_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        },
    )
    air_pricing_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Attribute",
        },
    )
