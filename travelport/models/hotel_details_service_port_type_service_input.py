from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_details_req import HotelDetailsReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class HotelDetailsServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | HotelDetailsServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        hotel_details_req: None | HotelDetailsReq = field(
            default=None,
            metadata={
                "name": "HotelDetailsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            },
        )
