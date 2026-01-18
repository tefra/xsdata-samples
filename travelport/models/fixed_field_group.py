from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.fixed_field import FixedField

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class FixedFieldGroup:
    """
    Defines the structure of a fixed group, which can be based on existing
    fixed fields and groups.

    Parameters
    ----------
    fixed_field
        Specify fixed fields that belong to this group.
    fixed_field_group
        Specify fixed fields that belong to this group.
    id
        Unique identifier of the fixed group.
    name
        Name of the field group.
    description
        Description of the field group as a whole.
    component
        The corresponding name of the element that this field refers to in
        the profile message. This is a read only attribute.
    correlation_element
        The name of an attribute on the profile element that defines a
        "type".  This is a read-only attribute.
    correlation_value
        The value that should be put in the attribute that the
        CorrelationElement defines.  This is a read-only attribute.
    display_order
        The order displayed by an UI
    hide
        A flag the determines if the UI should show this field.  Default to
        false.
    inheritable
        A flag to indicate if the group can be inherited. Default to false.
    min_occurs
        Minimum number of instances permitted (e.g., 0, 1).
    max_occurs
        Maximum number of instances permitted. Leave blank to indicate
        unlimited (i.e., ..*).
    label
        Alternate name of the field group for display on the UI
    min_occurs_override
        Minimum Agency-defined override defining the minimum number of
        instances permitted by the agency.
    max_occurs_override
        Maximum Agency-defined override defining the maximum number of
        instances permitted by the agency.
    inheritable_control_ind
        A flag to indicate whether agency can control inheritance. Default
        to false.
    read_only
        Defines if field as editable or not.
    overriden
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    fixed_field: list[FixedField] = field(
        default_factory=list,
        metadata={
            "name": "FixedField",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fixed_field_group: list[FixedFieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "FixedFieldGroup",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    id: str = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
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
        },
    )
    component: None | str = field(
        default=None,
        metadata={
            "name": "Component",
            "type": "Attribute",
            "max_length": 50,
        },
    )
    correlation_element: None | str = field(
        default=None,
        metadata={
            "name": "CorrelationElement",
            "type": "Attribute",
            "max_length": 50,
        },
    )
    correlation_value: None | str = field(
        default=None,
        metadata={
            "name": "CorrelationValue",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
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
    label: None | str = field(
        default=None,
        metadata={
            "name": "Label",
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
