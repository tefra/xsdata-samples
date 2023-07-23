from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.branded_fare_search_req import BrandedFareSearchReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class BrandedFareSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | BrandedFareSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        branded_fare_search_req: None | BrandedFareSearchReq = field(
            default=None,
            metadata={
                "name": "BrandedFareSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
