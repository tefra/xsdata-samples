from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.calculate_tax_req import CalculateTaxReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class CalculateTaxPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | CalculateTaxPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        calculate_tax_req: None | CalculateTaxReq = field(
            default=None,
            metadata={
                "name": "CalculateTaxReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
