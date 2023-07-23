from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.create_field_2 import CreateField2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CreateFieldGroup2:
    """
    Defines the structure of a new field group, which can be based on existing
    fields and groups (referred to by Id) and/or new fields and groups (referred to
    by FieldGroupRef or FieldRef and defined in FieldList or FieldGroupList).

    Parameters
    ----------
    create_field
        Specify fields that belong to this group.
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
    """
    class Meta:
        name = "CreateFieldGroup"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    create_field: list[CreateField2] = field(
        default_factory=list,
        metadata={
            "name": "CreateField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    min_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
