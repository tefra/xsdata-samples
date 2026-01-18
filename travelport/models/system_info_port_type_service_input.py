from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.system_info_req import SystemInfoReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class SystemInfoPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: SystemInfoPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        system_info_req: SystemInfoReq = field(
            metadata={
                "name": "SystemInfoReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/system_v32_0",
            }
        )
