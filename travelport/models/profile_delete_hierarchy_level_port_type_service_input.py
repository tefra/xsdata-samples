from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_delete_hierarchy_level_req import (
    ProfileDeleteHierarchyLevelReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileDeleteHierarchyLevelPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileDeleteHierarchyLevelPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_delete_hierarchy_level_req: (
            None | ProfileDeleteHierarchyLevelReq
        ) = field(
            default=None,
            metadata={
                "name": "ProfileDeleteHierarchyLevelReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            },
        )
