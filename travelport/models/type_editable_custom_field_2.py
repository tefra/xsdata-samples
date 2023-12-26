from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_common_editable_field_2 import (
    TypeCommonEditableField2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeEditableCustomField2(TypeCommonEditableField2):
    """
    Base type of an editable custom field or field group command.

    Parameters
    ----------
    hide
        A flag the determines if the UI should show this field.  Default to
        false.
    search_option
        If true, then this field is identified as one that is allowed to be
        searched on.  It is user defined.
    search_option_display_order
        The display order for search option.
    """

    class Meta:
        name = "typeEditableCustomField"

    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
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
