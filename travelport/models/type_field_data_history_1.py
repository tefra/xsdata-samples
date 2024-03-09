from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeFieldDataHistory1(TypeKeyElement1):
    """
    History Element for Field Data.

    Parameters
    ----------
    display_order
        The order the UI should display the field.
    value
        The value of this instance of the field.
    field_id
        The unique ID of the template field (instance of a field on a
        template) that this value is applied to.
    name
        Name of the custom field that this value is applied to.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "typeFieldDataHistory"

    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    field_id: None | str = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        },
    )
