from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.type_ticket_status import TypeTicketStatus

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ConjunctedTicketInfo:
    """
    Parameters
    ----------
    number
    iatanumber
    ticket_issue_date
    ticketing_agent_sign_on
    country_code
        Contains Ticketed PCC’s Country code.
    status
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

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
