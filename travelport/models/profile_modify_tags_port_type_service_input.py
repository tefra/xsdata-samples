from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_modify_tags_req_1 import ProfileModifyTagsReq1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileModifyTagsPortTypeServiceInput:
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
    body: None | ProfileModifyTagsPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_modify_tags_req: None | ProfileModifyTagsReq1 = field(
            default=None,
            metadata={
                "name": "ProfileModifyTagsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            },
        )
