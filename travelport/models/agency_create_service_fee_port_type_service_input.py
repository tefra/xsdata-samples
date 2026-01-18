from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agency_service_fee_create_req import (
    AgencyServiceFeeCreateReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class AgencyCreateServiceFeePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: AgencyCreateServiceFeePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        agency_service_fee_create_req: AgencyServiceFeeCreateReq = field(
            metadata={
                "name": "AgencyServiceFeeCreateReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
