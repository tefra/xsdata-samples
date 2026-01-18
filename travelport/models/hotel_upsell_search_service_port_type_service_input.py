from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.hotel_upsell_details_req import HotelUpsellDetailsReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class HotelUpsellSearchServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: HotelUpsellSearchServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        hotel_upsell_details_req: HotelUpsellDetailsReq = field(
            metadata={
                "name": "HotelUpsellDetailsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            }
        )
