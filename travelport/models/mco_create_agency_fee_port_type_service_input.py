from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.create_agency_fee_mco_req import CreateAgencyFeeMcoReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class McoCreateAgencyFeePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: McoCreateAgencyFeePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        create_agency_fee_mco_req: CreateAgencyFeeMcoReq = field(
            metadata={
                "name": "CreateAgencyFeeMcoReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
