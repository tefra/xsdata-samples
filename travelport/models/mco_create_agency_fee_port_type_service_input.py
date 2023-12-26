from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.create_agency_fee_mco_req import CreateAgencyFeeMcoReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class McoCreateAgencyFeePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | McoCreateAgencyFeePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        create_agency_fee_mco_req: None | CreateAgencyFeeMcoReq = field(
            default=None,
            metadata={
                "name": "CreateAgencyFeeMcoReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
