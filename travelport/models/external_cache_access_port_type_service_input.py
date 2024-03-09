from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.external_cache_access_req import ExternalCacheAccessReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ExternalCacheAccessPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ExternalCacheAccessPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        external_cache_access_req: None | ExternalCacheAccessReq = field(
            default=None,
            metadata={
                "name": "ExternalCacheAccessReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/system_v32_0",
            },
        )
