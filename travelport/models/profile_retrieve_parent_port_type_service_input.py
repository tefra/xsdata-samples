from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_retrieve_parent_req import ProfileRetrieveParentReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileRetrieveParentPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | object = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | ProfileRetrieveParentPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        profile_retrieve_parent_req: None | ProfileRetrieveParentReq = field(
            default=None,
            metadata={
                "name": "ProfileRetrieveParentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            }
        )
