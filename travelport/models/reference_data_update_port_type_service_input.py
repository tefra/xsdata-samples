from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.reference_data_update_req import ReferenceDataUpdateReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ReferenceDataUpdatePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ReferenceDataUpdatePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        reference_data_update_req: ReferenceDataUpdateReq = field(
            metadata={
                "name": "ReferenceDataUpdateReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
