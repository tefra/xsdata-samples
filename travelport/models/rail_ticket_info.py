from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.rail_journey_ref import RailJourneyRef
from travelport.models.ticket_advisory import TicketAdvisory

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailTicketInfo:
    """
    Parameters
    ----------
    rail_journey_ref
    ticket_advisory
    number
        Ticket number.
    issue_location
        Issue location is internal distributor code associated with the PCC.
    ticket_status
        Status of Ticket.
    ticket_form_type
        FormType of Ticket.
    traffic_type
        Type of traffic.
    issued_date
        Ticket issue date.
    ticket_type
        Type of ticket. Paper, eTicket etc.
    booking_traveler_ref
        Reference to a BookingTraveler.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_journey_ref: list[RailJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "RailJourneyRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    ticket_advisory: list[TicketAdvisory] = field(
        default_factory=list,
        metadata={
            "name": "TicketAdvisory",
            "type": "Element",
            "max_occurs": 10,
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 19,
        },
    )
    issue_location: None | str = field(
        default=None,
        metadata={
            "name": "IssueLocation",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 128,
        },
    )
    ticket_status: None | str = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    ticket_form_type: None | str = field(
        default=None,
        metadata={
            "name": "TicketFormType",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        },
    )
    traffic_type: None | str = field(
        default=None,
        metadata={
            "name": "TrafficType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    issued_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "IssuedDate",
            "type": "Attribute",
        },
    )
    ticket_type: None | str = field(
        default=None,
        metadata={
            "name": "TicketType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
