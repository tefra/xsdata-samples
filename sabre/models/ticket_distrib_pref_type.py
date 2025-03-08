from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from sabre.models.prefer_level_type import PreferLevelType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TicketDistribPrefType:
    """
    Type of ticket distribution to be used with this collection of preferences.

    Attributes:
        value:
        prefer_level:
        distrib_type: Ticket distribution method; such as Fax, Email,
            Courier, Mail, Airport_Pickup, City_Office, Hotel_Desk,
            WillCall, etc.
        ticket_time: Ticket turnaround time desired, amount of time
            requested to deliver tickets.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 64,
        },
    )
    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        },
    )
    distrib_type: None | str = field(
        default=None,
        metadata={
            "name": "DistribType",
            "type": "Attribute",
        },
    )
    ticket_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "TicketTime",
            "type": "Attribute",
        },
    )
