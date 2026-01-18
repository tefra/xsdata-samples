from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.calculate_tax_req import CalculateTaxReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class CalculateTaxPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CalculateTaxPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        calculate_tax_req: CalculateTaxReq = field(
            metadata={
                "name": "CalculateTaxReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
