from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_keyword_req import HotelKeywordReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class HotelKeywordsServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | HotelKeywordsServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        hotel_keyword_req: None | HotelKeywordReq = field(
            default=None,
            metadata={
                "name": "HotelKeywordReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            },
        )
