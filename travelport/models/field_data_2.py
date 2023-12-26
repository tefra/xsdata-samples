from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_tagged_element_2 import TypeKeyTaggedElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class FieldData2(TypeKeyTaggedElement2):
    """
    Parameters
    ----------
    value
        The value of this instance of the field.
    field_id
        The unique ID of the template field (instance of a field on a
        template) that this value is applied to.Provide either FieldID or
        Name, not both.
    name
        Name of the custom field that this value is applied to.Provide
        either Name or FieldID, not both.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "FieldData"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
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
