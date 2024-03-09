from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_retrieve_req_1 import ProfileRetrieveReq1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileRetrievePortTypeServiceInput:
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
    body: None | ProfileRetrievePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_retrieve_req: None | ProfileRetrieveReq1 = field(
            default=None,
            metadata={
                "name": "ProfileRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            },
        )
