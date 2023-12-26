from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_media_links_req import HotelMediaLinksReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class HotelMediaLinksServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | HotelMediaLinksServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        hotel_media_links_req: None | HotelMediaLinksReq = field(
            default=None,
            metadata={
                "name": "HotelMediaLinksReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            },
        )
