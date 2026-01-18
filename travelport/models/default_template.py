from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_hierarchy_override_type import (
    TypeHierarchyOverrideType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class DefaultTemplate:
    """
    The information about the default account and traveler templates for
    the agency.

    Only returned for agency hierarchy level.

    Parameters
    ----------
    profile_type
        The profile type that the template is for.
    template_id
        Unique identifier of the template assigned to all profiles of this
        profile type, unless an override template is defined.
    template_version
        The current version number of the template.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_type: TypeHierarchyOverrideType = field(
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    template_id: int = field(
        metadata={
            "name": "TemplateID",
            "type": "Attribute",
            "required": True,
        }
    )
    template_version: int = field(
        metadata={
            "name": "TemplateVersion",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
