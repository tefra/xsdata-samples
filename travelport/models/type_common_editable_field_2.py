from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_field_ref_2 import TypeFieldRef2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeCommonEditableField2(TypeFieldRef2):
    """
    Base type of common attributes that can be edited for a field or field
    group command.

    Parameters
    ----------
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
    label
        Alternate name of the field for display on the UI
    display_order
        The order displayed by an UI
    inheritable
        Denotes that the field/group is inherited in child profiles.
        Defaults to false. The Field/Group for which the Inheritable is set
        to true in parent profile,is inherited in child profiles. The
        Inheritable attribute is not valid in a Template Modify Request if
        the InheritableControlInd is False for that particular Field/Group
    """

    class Meta:
        name = "typeCommonEditableField"

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
    label: None | str = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
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
