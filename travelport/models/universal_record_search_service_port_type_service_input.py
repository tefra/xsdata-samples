from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.universal_record_search_req import (
    UniversalRecordSearchReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class UniversalRecordSearchServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: UniversalRecordSearchServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        universal_record_search_req: UniversalRecordSearchReq = field(
            metadata={
                "name": "UniversalRecordSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
