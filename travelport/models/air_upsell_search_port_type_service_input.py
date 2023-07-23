from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_upsell_search_req import AirUpsellSearchReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirUpsellSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirUpsellSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_upsell_search_req: None | AirUpsellSearchReq = field(
            default=None,
            metadata={
                "name": "AirUpsellSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
