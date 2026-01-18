from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_create_hierarchy_level_req import (
    ProfileCreateHierarchyLevelReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProfileCreateHierarchyLevelPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ProfileCreateHierarchyLevelPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        profile_create_hierarchy_level_req: ProfileCreateHierarchyLevelReq = field(
            metadata={
                "name": "ProfileCreateHierarchyLevelReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            }
        )
