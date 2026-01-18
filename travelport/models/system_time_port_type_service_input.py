from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.time_req import TimeReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class SystemTimePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: SystemTimePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        time_req: TimeReq = field(
            metadata={
                "name": "TimeReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/system_v32_0",
            }
        )
