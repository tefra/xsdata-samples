from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.coupon import Coupon
from travelport.models.exchanged_ticket_info import ExchangedTicketInfo
from travelport.models.ticket_endorsement import TicketEndorsement
from travelport.models.tour_code import TourCode
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_ticket_status import TypeTicketStatus

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Ticket:
    """
    The ticket that resulted from an air booking.

    Parameters
    ----------
    coupon
    ticket_endorsement
    tour_code
    exchanged_ticket_info
    key
    ticket_number
    ticket_status
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    coupon: list[Coupon] = field(
        default_factory=list,
        metadata={
            "name": "Coupon",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 4,
        },
    )
    ticket_endorsement: list[TicketEndorsement] = field(
        default_factory=list,
        metadata={
            "name": "TicketEndorsement",
            "type": "Element",
            "max_occurs": 6,
        },
    )
    tour_code: list[TourCode] = field(
        default_factory=list,
        metadata={
            "name": "TourCode",
            "type": "Element",
            "max_occurs": 999,
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
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    ticket_number: str = field(
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
            "required": True,
            "length": 13,
        }
    )
    ticket_status: None | TypeTicketStatus = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
