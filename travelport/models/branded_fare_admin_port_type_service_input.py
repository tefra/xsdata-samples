from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.branded_fare_admin_req import BrandedFareAdminReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class BrandedFareAdminPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | BrandedFareAdminPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        branded_fare_admin_req: None | BrandedFareAdminReq = field(
            default=None,
            metadata={
                "name": "BrandedFareAdminReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
