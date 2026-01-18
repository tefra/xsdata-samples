from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.content_provider_retrieve_req import (
    ContentProviderRetrieveReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ContentProviderRetrievePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ContentProviderRetrievePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        content_provider_retrieve_req: ContentProviderRetrieveReq = field(
            metadata={
                "name": "ContentProviderRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
