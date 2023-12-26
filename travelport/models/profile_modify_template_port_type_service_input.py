from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_modify_template_req import (
    ProfileModifyTemplateReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileModifyTemplatePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileModifyTemplatePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_modify_template_req: None | ProfileModifyTemplateReq = field(
            default=None,
            metadata={
                "name": "ProfileModifyTemplateReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            },
        )
