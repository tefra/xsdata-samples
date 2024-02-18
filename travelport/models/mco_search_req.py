from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.airport_1 import Airport1
from travelport.models.base_req_1 import BaseReq1
from travelport.models.carrier_1 import Carrier1
from travelport.models.mco_create_date import McoCreateDate
from travelport.models.mco_search_modifiers import McoSearchModifiers
from travelport.models.name_1 import Name1
from travelport.models.ticket_number_1 import TicketNumber1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class McoSearchReq(BaseReq1):
    """
    Search for MCOs by certain criteria and return a list.

    Parameters
    ----------
    name
    carrier
    airport
    ticket_number
        The ticket that this MCO was issued in connection with. Could be the
        ticket that caused the fee, a residual from an exchange, or an
        airline service fee.
    mco_create_date
    mco_search_modifiers
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    name: None | Name1 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    carrier: list[Carrier1] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 10,
        },
    )
    airport: list[Airport1] = field(
        default_factory=list,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 10,
        },
    )
    ticket_number: None | TicketNumber1 = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    mco_create_date: None | McoCreateDate = field(
        default=None,
        metadata={
            "name": "McoCreateDate",
            "type": "Element",
        },
    )
    mco_search_modifiers: None | McoSearchModifiers = field(
        default=None,
        metadata={
            "name": "McoSearchModifiers",
            "type": "Element",
        },
    )
