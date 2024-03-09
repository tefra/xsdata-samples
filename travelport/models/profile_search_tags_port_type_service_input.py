from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_search_tags_req_1 import ProfileSearchTagsReq1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileSearchTagsPortTypeServiceInput:
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
    body: None | ProfileSearchTagsPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_search_tags_req: None | ProfileSearchTagsReq1 = field(
            default=None,
            metadata={
                "name": "ProfileSearchTagsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            },
        )
