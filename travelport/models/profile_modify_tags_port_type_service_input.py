from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_modify_tags_req_1 import ProfileModifyTagsReq1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProfileModifyTagsPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: object = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: ProfileModifyTagsPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        profile_modify_tags_req: ProfileModifyTagsReq1 = field(
            metadata={
                "name": "ProfileModifyTagsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            }
        )
