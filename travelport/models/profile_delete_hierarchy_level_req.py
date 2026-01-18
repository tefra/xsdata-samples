from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.type_delete_hierarchy_lvl_profile_type import (
    TypeDeleteHierarchyLvlProfileType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileDeleteHierarchyLevelReq(BaseReq5):
    """
    Request to delete an existing Group level of an agency or account
    hierarchy.

    Only permitted if no profiles exist for the level.

    Parameters
    ----------
    hierarchy_level_id
        System-assigned, unique hierarchy level ID of the immediate parent
        of this hiearchy level. Leave blank only if profile level is agency
        group.
    profile_type
        The type of profile hierarchy level corresponds which can be deleted
        (e.g., branchgroup and travelergroup).
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level_id: str = field(
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: TypeDeleteHierarchyLvlProfileType = field(
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
