from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.vehicle_keyword_req import VehicleKeywordReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleKeywordsServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | VehicleKeywordsServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        vehicle_keyword_req: None | VehicleKeywordReq = field(
            default=None,
            metadata={
                "name": "VehicleKeywordReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            }
        )
