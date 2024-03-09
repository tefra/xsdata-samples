from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.field_2 import Field2
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class FieldGroup2:
    """
    Defines the structure of a new field group, which can be based on existing
    fields and groups (referred to by Id) and/or new fields and groups (referred to
    by FieldGroupRef or FieldRef and defined in FieldList or FieldGroupList).

    Parameters
    ----------
    field_value
        Specify fields that belong to this group.
    id
        Unique identifier of the field group.
    name
        Name of the field group.
    description
        Description of the field group as a whole.
    protected
        If true, then special authorization is required for a user to create
        or modify this field or group.
    inheritable
        Denotes that the custom field group is inherited in child profiles.
        Defaults to false.
    min_occurs
        Minimum number of instances permitted (e.g., 0, 1).
    max_occurs
        Maximum number of instances permitted. Leave blank to indicate
        unlimited (i.e., ..*).
    profile_id
        The profile ID of the agency or account that the field belongs to.
    profile_type
        The type of the Profile to be created.
    is_used
        True if the custom field group has been added to a template.
    """

    class Meta:
        name = "FieldGroup"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    field_value: list[Field2] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    id: None | str = field(
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
            "max_length": 255,
        },
    )
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
            "type": "Attribute",
        },
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        },
    )
    min_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        },
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
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
    is_used: None | bool = field(
        default=None,
        metadata={
            "name": "IsUsed",
            "type": "Attribute",
            "required": True,
        },
    )
