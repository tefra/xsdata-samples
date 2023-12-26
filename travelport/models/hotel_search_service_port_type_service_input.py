from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_search_availability_req import (
    HotelSearchAvailabilityReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class HotelSearchServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | HotelSearchServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        hotel_search_availability_req: None | HotelSearchAvailabilityReq = field(
            default=None,
            metadata={
                "name": "HotelSearchAvailabilityReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            },
        )
