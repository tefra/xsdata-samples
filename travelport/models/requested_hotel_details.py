from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_type import HotelType
from travelport.models.type_hotel_details import TypeHotelDetails

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class RequestedHotelDetails(TypeHotelDetails):
    """
    Parameters
    ----------
    hotel_type
        Supported Providers:1G/1V/1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_type: None | HotelType = field(
        default=None,
        metadata={
            "name": "HotelType",
            "type": "Element",
        },
    )
