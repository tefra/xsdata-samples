from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.system_info_req import SystemInfoReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class SystemInfoPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | SystemInfoPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        system_info_req: None | SystemInfoReq = field(
            default=None,
            metadata={
                "name": "SystemInfoReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/system_v32_0",
            },
        )
