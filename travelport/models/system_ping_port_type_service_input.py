from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.ping_req import PingReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class SystemPingPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | SystemPingPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ping_req: None | PingReq = field(
            default=None,
            metadata={
                "name": "PingReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/system_v32_0",
            },
        )
