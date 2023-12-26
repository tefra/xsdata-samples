from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_create_hierarchy_level_req import (
    ProfileCreateHierarchyLevelReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileCreateHierarchyLevelPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileCreateHierarchyLevelPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_create_hierarchy_level_req: None | ProfileCreateHierarchyLevelReq = field(
            default=None,
            metadata={
                "name": "ProfileCreateHierarchyLevelReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            },
        )
