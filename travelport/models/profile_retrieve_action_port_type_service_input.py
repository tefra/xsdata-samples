from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_retrieve_action_req import ProfileRetrieveActionReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileRetrieveActionPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileRetrieveActionPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        profile_retrieve_action_req: None | ProfileRetrieveActionReq = field(
            default=None,
            metadata={
                "name": "ProfileRetrieveActionReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            }
        )
