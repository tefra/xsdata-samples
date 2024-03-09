from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.default_template import DefaultTemplate
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class HierarchyLevel:
    """
    Information about a level within an agency/account hierarchy.

    Parameters
    ----------
    default_template
    hierarchy_level_id
        System-assigned, unique hierarchy level ID of the immediate parent
        of this hiearchy level. Leave blank only if profile level is agency
        group.
    profile_type
        The type of profile this hierarchy level corresponds to (e.g.,
        branch, account, traveler, group).
    name
        Name of this level of the hierarchy.
    level_number
        Number of this level of the hierarchy, vis-a-vis other levels.
    description
        A brief description of this hierarchy level.
    template_id
        Unique identifier of the template assigned to all profiles at this
        level of the hierarchy. Not relevant for account and traveler
        levels.
    template_version
        The current version number of the template.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    default_template: list[DefaultTemplate] = field(
        default_factory=list,
        metadata={
            "name": "DefaultTemplate",
            "type": "Element",
            "max_occurs": 2,
        },
    )
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
            "required": True,
            "min_length": 1,
            "max_length": 64,
        },
    )
    level_number: None | int = field(
        default=None,
        metadata={
            "name": "LevelNumber",
            "type": "Attribute",
            "required": True,
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
    template_id: None | int = field(
        default=None,
        metadata={
            "name": "TemplateID",
            "type": "Attribute",
        },
    )
    template_version: None | int = field(
        default=None,
        metadata={
            "name": "TemplateVersion",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
