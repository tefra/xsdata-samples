from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_common_editable_field_1 import (
    TypeCommonEditableField1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeCommonEditableGroup1(TypeCommonEditableField1):
    """
    Base type of common attributes that can be edited for a field group command.

    Parameters
    ----------
    hide
        A flag the determines if the UI should show this field.  Default to
        false.
    """

    class Meta:
        name = "typeCommonEditableGroup"

    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        },
    )
