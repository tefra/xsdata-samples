from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.ack_schedule_change_req import AckScheduleChangeReq
from travelport.models.supported_versions import SupportedVersions

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AckScheduleChangeServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | AckScheduleChangeServicePortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: None | AckScheduleChangeServicePortTypeServiceInput.Body = field(
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
        ack_schedule_change_req: None | AckScheduleChangeReq = field(
            default=None,
            metadata={
                "name": "AckScheduleChangeReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
