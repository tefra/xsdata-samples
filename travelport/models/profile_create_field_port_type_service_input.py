from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_create_field_req_1 import ProfileCreateFieldReq1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileCreateFieldPortTypeServiceInput:
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
    body: None | ProfileCreateFieldPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        profile_create_field_req: None | ProfileCreateFieldReq1 = field(
            default=None,
            metadata={
                "name": "ProfileCreateFieldReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            }
        )
