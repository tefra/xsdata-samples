from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.custom_field import CustomField
from travelport.models.custom_field_group import CustomFieldGroup
from travelport.models.fixed_field_group import FixedFieldGroup
from travelport.models.override_definition import OverrideDefinition

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileTemplate:
    """
    Template for a profile.

    Parameters
    ----------
    fixed_field_group
    custom_field
    custom_field_group
    override_definition
    id
        Unique identifier of the template, defined by the system.
    name
        Name for the template.
    description
        Description of the template and its use.
    version
        Version of the template.
    base_template_id
        Presence of base template id  indicate that current templat e is a
        override template and is created based on "BaseTemplateID".
    owner_profile_id
        Presence of owner profile id indicates by which profile this
        template is been owned
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    fixed_field_group: list[FixedFieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "FixedFieldGroup",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    custom_field: list[CustomField] = field(
        default_factory=list,
        metadata={
            "name": "CustomField",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    custom_field_group: list[CustomFieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "CustomFieldGroup",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    override_definition: list[OverrideDefinition] = field(
        default_factory=list,
        metadata={
            "name": "OverrideDefinition",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    id: None | int = field(
        default=None,
        metadata={
            "name": "ID",
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
            "max_length": 128,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 225,
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    base_template_id: None | int = field(
        default=None,
        metadata={
            "name": "BaseTemplateID",
            "type": "Attribute",
        },
    )
    owner_profile_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerProfileID",
            "type": "Attribute",
        },
    )
