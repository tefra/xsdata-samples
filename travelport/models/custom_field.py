from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.action_ref import ActionRef
from travelport.models.type_custom_field_2 import TypeCustomField2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CustomField(TypeCustomField2):
    """
    Specify any existing fields that belong to this group.

    Parameters
    ----------
    action_ref
    label
        Alternate name of the field for display on the UI.  Labels are only
        valid for custom fields at the root level
    searchable
        All custom fields are searchable.  This will always be true.
    search_option
        If true, then this field is identified as one that is allowed to be
        searched on.  It is user defined.
    search_option_display_order
        The display order for search option.
    hide
        A flag the determines if the UI should show this field.  Default to
        false.
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

    action_ref: list[ActionRef] = field(
        default_factory=list,
        metadata={
            "name": "ActionRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    label: None | str = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        },
    )
    searchable: None | object = field(
        default=None,
        metadata={
            "name": "Searchable",
            "type": "Attribute",
            "required": True,
        },
    )
    search_option: bool = field(
        default=False,
        metadata={
            "name": "SearchOption",
            "type": "Attribute",
        },
    )
    search_option_display_order: None | int = field(
        default=None,
        metadata={
            "name": "SearchOptionDisplayOrder",
            "type": "Attribute",
        },
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        },
    )
    min_occurs_override: None | int = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        },
    )
    max_occurs_override: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        },
    )
    inheritable_control_ind: bool = field(
        default=False,
        metadata={
            "name": "InheritableControlInd",
            "type": "Attribute",
        },
    )
    read_only: None | bool = field(
        default=None,
        metadata={
            "name": "ReadOnly",
            "type": "Attribute",
        },
    )
    overriden: bool = field(
        default=False,
        metadata={
            "name": "Overriden",
            "type": "Attribute",
        },
    )
