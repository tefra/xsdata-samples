from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_search_field_req_1 import ProfileSearchFieldReq1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileSearchFieldPortTypeServiceInput:
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
    body: None | ProfileSearchFieldPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_search_field_req: None | ProfileSearchFieldReq1 = field(
            default=None,
            metadata={
                "name": "ProfileSearchFieldReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            },
        )
