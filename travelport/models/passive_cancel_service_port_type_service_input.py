from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.passive_cancel_req import PassiveCancelReq
from travelport.models.supported_versions import SupportedVersions

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class PassiveCancelServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | PassiveCancelServicePortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: None | PassiveCancelServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        supported_versions: None | SupportedVersions = field(
            default=None,
            metadata={
                "name": "SupportedVersions",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )

    @dataclass
    class Body:
        passive_cancel_req: None | PassiveCancelReq = field(
            default=None,
            metadata={
                "name": "PassiveCancelReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
