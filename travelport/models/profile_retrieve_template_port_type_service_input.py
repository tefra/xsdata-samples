from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_retrieve_template_req import (
    ProfileRetrieveTemplateReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProfileRetrieveTemplatePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ProfileRetrieveTemplatePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        profile_retrieve_template_req: ProfileRetrieveTemplateReq = field(
            metadata={
                "name": "ProfileRetrieveTemplateReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            }
        )
