from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_search_action_req import ProfileSearchActionReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProfileSearchActionPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ProfileSearchActionPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        profile_search_action_req: ProfileSearchActionReq = field(
            metadata={
                "name": "ProfileSearchActionReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            }
        )
