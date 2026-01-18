from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_create_req_1 import ProfileCreateReq1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProfileCreatePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: object = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: ProfileCreatePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        profile_create_req: ProfileCreateReq1 = field(
            metadata={
                "name": "ProfileCreateReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            }
        )
