from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_5 import BaseReq5
from travelport.models.type_create_hierarchy_level import (
    TypeCreateHierarchyLevel,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileCreateHierarchyLevelReq(BaseReq5):
    """Request to create a new level within an existing agency or account
    hierarchy.

    The template of the hierarchy level will be auto-generated.

    Parameters
    ----------
    parent_hierarchy_level_id
        System-assigned, unique hierarchy level ID of the immediate parent
        of this hiearchy level. Required unless profile type is AgencyGroup.
    profile_type
        The type of profile this hierarchy level corresponds to. Limited to
        AgencyGroup, BranchGroup and TravelerGroup.
    name
        Name of this level of the hierarchy.
    description
        A brief description of this hierarchy level.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    parent_hierarchy_level_id: None | int = field(
        default=None,
        metadata={
            "name": "ParentHierarchyLevelID",
            "type": "Attribute",
        },
    )
    profile_type: None | TypeCreateHierarchyLevel = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
