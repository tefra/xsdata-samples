from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.hotel_super_shopper_req import HotelSuperShopperReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class HotelSuperShopperServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: HotelSuperShopperServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        hotel_super_shopper_req: HotelSuperShopperReq = field(
            metadata={
                "name": "HotelSuperShopperReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            }
        )
