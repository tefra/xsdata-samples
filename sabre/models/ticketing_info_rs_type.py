from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.free_text_type import FreeTextType
from sabre.models.ticket_type import TicketType
from sabre.models.valid_interline_type import ValidInterlineType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TicketingInfoRsType:
    """
    Extends TicketingInfoType to provide an eTicketNumber.

    Attributes:
        ticket_advisory: Open text field available for additional ticket
            information.
        tpa_extensions: Place holder for additional elements.
        e_ticket_number: If reservation is electronically ticketed at
            time of booking, this is the field for the eTicket number.
        ticket_time_limit: TicketTimeLimit - Indicates the ticketing
            arrangement, and allows for the requirement that an
            itinerary must be ticketed by a certain date and time.
        ticket_type: TicketType - Indicates the type of ticket (Paper,
            eTicket)
        valid_interline: ValidInterline - Indicates validation of
            interline ticketing aggrement, possible values (Yes, No,
            Unknown), default=unknown
    """

    class Meta:
        name = "TicketingInfoRS_Type"

    ticket_advisory: list[FreeTextType] = field(
        default_factory=list,
        metadata={
            "name": "TicketAdvisory",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 10,
        },
    )
    tpa_extensions: None | str = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    e_ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "eTicketNumber",
            "type": "Attribute",
            "pattern": r"[0-9a-zA-Z]{1,14}",
        },
    )
    ticket_time_limit: None | str = field(
        default=None,
        metadata={
            "name": "TicketTimeLimit",
            "type": "Attribute",
        },
    )
    ticket_type: None | TicketType = field(
        default=None,
        metadata={
            "name": "TicketType",
            "type": "Attribute",
            "required": True,
        },
    )
    valid_interline: ValidInterlineType = field(
        default=ValidInterlineType.UNKNOWN,
        metadata={
            "name": "ValidInterline",
            "type": "Attribute",
        },
    )
