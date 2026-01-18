from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_custom_field_or_group_type import (
    TypeCustomFieldOrGroupType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class OverrideDefinition:
    """
    Element to override setting of fields defined in default template .Can
    be used to override custom filed,custom group , fixed field group and
    fixed field.

    Parameters
    ----------
    template_field_id
        Unique identifier of the base template field or group id .
    hide
        A flag that determines if the UI should show this field.  Default to
        false.
    label
        Alternate name of the field for display on the UI
    min_occurs_override
        Agency-defined override defining the minimum number of values
        permitted for this field on profiles using this template. Value
        cannot be less than the boundary MinOccurs defined on the field or
        field group itself.
    read_only
        Defines if field as editable or not.
    template_field_type
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    template_field_id: str = field(
        metadata={
            "name": "TemplateFieldID",
            "type": "Attribute",
            "required": True,
        }
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        },
    )
    label: None | str = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    min_occurs_override: None | int = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
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
    template_field_type: None | TypeCustomFieldOrGroupType = field(
        default=None,
        metadata={
            "name": "TemplateFieldType",
            "type": "Attribute",
        },
    )
