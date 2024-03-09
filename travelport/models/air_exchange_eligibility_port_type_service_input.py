from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_eligibility_req import (
    AirExchangeEligibilityReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirExchangeEligibilityPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirExchangeEligibilityPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        air_exchange_eligibility_req: None | AirExchangeEligibilityReq = field(
            default=None,
            metadata={
                "name": "AirExchangeEligibilityReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
