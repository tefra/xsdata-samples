from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_modify_hierarchy_level_req import (
    ProfileModifyHierarchyLevelReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileModifyHierarchyLevelPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileModifyHierarchyLevelPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_modify_hierarchy_level_req: (
            None | ProfileModifyHierarchyLevelReq
        ) = field(
            default=None,
            metadata={
                "name": "ProfileModifyHierarchyLevelReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            },
        )
