from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlDateTime
from travelport.models.type_tcrstatus import TypeTcrstatus

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Tcrinfo:
    """
    Parameters
    ----------
    status
    date
    tcrnumber
        The identifying number for a Ticketless Air Reservation.
    provider_reservation_info_ref
        Provider reservation reference key.
    """

    class Meta:
        name = "TCRInfo"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    status: None | TypeTcrstatus = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
        },
    )
    tcrnumber: None | str = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Attribute",
            "required": True,
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
            "required": True,
        },
    )
