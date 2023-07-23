from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_retrieve_req import HotelRetrieveReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class HotelRetrieveServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | HotelRetrieveServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        hotel_retrieve_req: None | HotelRetrieveReq = field(
            default=None,
            metadata={
                "name": "HotelRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            }
        )
