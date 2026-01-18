from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.back_office_hand_off import BackOfficeHandOff
from travelport.models.itinerary import Itinerary

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class DocumentSelect:
    """
    Allows an agency to select the documents to produce for the itinerary.

    Parameters
    ----------
    back_office_hand_off
    itinerary
    issue_ticket_only
        Set to true to alter system default of itinerary,ticket and back
        office.
    issue_electronic_ticket
        Set to true for electronic tickets.
    fax_indicator
        Set to true for providing fax details.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    back_office_hand_off: None | BackOfficeHandOff = field(
        default=None,
        metadata={
            "name": "BackOfficeHandOff",
            "type": "Element",
        },
    )
    itinerary: None | Itinerary = field(
        default=None,
        metadata={
            "name": "Itinerary",
            "type": "Element",
        },
    )
    issue_ticket_only: None | bool = field(
        default=None,
        metadata={
            "name": "IssueTicketOnly",
            "type": "Attribute",
        },
    )
    issue_electronic_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "IssueElectronicTicket",
            "type": "Attribute",
        },
    )
    fax_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "FaxIndicator",
            "type": "Attribute",
        },
    )
