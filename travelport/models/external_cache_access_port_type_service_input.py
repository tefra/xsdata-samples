from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.external_cache_access_req import ExternalCacheAccessReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ExternalCacheAccessPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ExternalCacheAccessPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        external_cache_access_req: ExternalCacheAccessReq = field(
            metadata={
                "name": "ExternalCacheAccessReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/system_v32_0",
            }
        )
