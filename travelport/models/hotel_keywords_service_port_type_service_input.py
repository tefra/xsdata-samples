from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.hotel_keyword_req import HotelKeywordReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class HotelKeywordsServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: HotelKeywordsServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        hotel_keyword_req: HotelKeywordReq = field(
            metadata={
                "name": "HotelKeywordReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            }
        )
