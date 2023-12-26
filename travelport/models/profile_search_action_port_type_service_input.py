from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_search_action_req import ProfileSearchActionReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileSearchActionPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileSearchActionPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_search_action_req: None | ProfileSearchActionReq = field(
            default=None,
            metadata={
                "name": "ProfileSearchActionReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            },
        )
