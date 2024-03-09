from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_delete_req_1 import ProfileDeleteReq1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileDeletePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | object = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: None | ProfileDeletePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_delete_req: None | ProfileDeleteReq1 = field(
            default=None,
            metadata={
                "name": "ProfileDeleteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            },
        )
