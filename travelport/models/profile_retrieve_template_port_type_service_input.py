from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_retrieve_template_req import (
    ProfileRetrieveTemplateReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileRetrieveTemplatePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileRetrieveTemplatePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_retrieve_template_req: None | ProfileRetrieveTemplateReq = field(
            default=None,
            metadata={
                "name": "ProfileRetrieveTemplateReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            },
        )
