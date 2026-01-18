from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.hotel_rules_req import HotelRulesReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class HotelRulesServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: HotelRulesServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        hotel_rules_req: HotelRulesReq = field(
            metadata={
                "name": "HotelRulesReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            }
        )
