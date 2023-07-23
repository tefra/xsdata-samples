from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.custom_field import CustomField

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CustomFieldGroup:
    """
    Defines the structure of a new field group, which can be based on existing
    fields and groups (referred to by Id) and/or new fields and groups (referred to
    by FieldGroupRef or FieldRef and defined in FieldList or FieldGroupList).

    Parameters
    ----------
    custom_field
        Specify fields that belong to this group.
    id
        Unique identifier of the field group.
    name
        Name of the field group.
    display_order
        The order displayed by an UI
    description
        Description of the field group as a whole.
    label
        Alternate name of the field for display on the UI
    inheritable
        If true, thern this custom field can be inherited in children
        profiles.
    hide
        A flag the determines if the UI should show this field.  Default to
        false.
    min_occurs
        Minimum number of instances permitted (e.g., 0, 1).
    max_occurs
        Maximum number of instances permitted. Leave blank to indicate
        unlimited (i.e., ..*).
    min_occurs_override
        Agency-defined override defining the minimum number of values
        permitted for this field on profiles using this template. Value
        cannot be less than the boundary MinOccurs defined on the field or
        field group itself.
    max_occurs_override
        Agency-defined override defining the maximum number of values
        permitted for this field on profiles using this template. Value
        cannot be greater than the boundary MaxOccurs defined on the field
        or field group itself.
    inheritable_control_ind
        A flag to indicate whether agency can control inheritance. Default
        to false.
    read_only
        Defines if field as editable or not.
    overriden
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    custom_field: list[CustomField] = field(
        default_factory=list,
        metadata={
            "name": "CustomField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
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
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
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
    label: None | str = field(
        default=None,
        metadata={
            "name": "Label",
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
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
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
    min_occurs_override: None | int = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs_override: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        }
    )
    inheritable_control_ind: bool = field(
        default=False,
        metadata={
            "name": "InheritableControlInd",
            "type": "Attribute",
        }
    )
    read_only: None | bool = field(
        default=None,
        metadata={
            "name": "ReadOnly",
            "type": "Attribute",
        }
    )
    overriden: bool = field(
        default=False,
        metadata={
            "name": "Overriden",
            "type": "Attribute",
        }
    )
