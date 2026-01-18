from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.ping_req import PingReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class SystemPingPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: SystemPingPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        ping_req: PingReq = field(
            metadata={
                "name": "PingReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/system_v32_0",
            }
        )
