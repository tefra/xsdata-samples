from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyHierarchyLevelReq(BaseReq5):
    """
    Request to modify an existing level within an agency or account hierarchy.

    Parameters
    ----------
    hierarchy_level_id
        System-assigned, unique hierarchy level ID of the immediate parent
        of this hiearchy level. Leave blank only if profile level is agency
        group.
    profile_type
        The type of profile this hierarchy level corresponds to (e.g.,
        branch, account, traveler, group).
    name
        Name of this level of the hierarchy.
    description
        A brief description of this hierarchy level.
    parent_hierarchy_level_id
        To swap the order of two Group levels, specify the new parent of
        this level. Only Group levels can be reassigned, and can only move
        up or down one location in the overall hierarchy.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level_id: None | str = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
            "required": True,
        },
    )
    profile_type: None | TypeProfileType7 = field(
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
    parent_hierarchy_level_id: None | str = field(
        default=None,
        metadata={
            "name": "ParentHierarchyLevelID",
            "type": "Attribute",
        },
    )
