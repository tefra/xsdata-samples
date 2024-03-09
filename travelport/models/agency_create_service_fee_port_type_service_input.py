from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agency_service_fee_create_req import (
    AgencyServiceFeeCreateReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AgencyCreateServiceFeePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AgencyCreateServiceFeePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        agency_service_fee_create_req: None | AgencyServiceFeeCreateReq = (
            field(
                default=None,
                metadata={
                    "name": "AgencyServiceFeeCreateReq",
                    "type": "Element",
                    "namespace": "http://www.travelport.com/schema/util_v52_0",
                },
            )
        )
