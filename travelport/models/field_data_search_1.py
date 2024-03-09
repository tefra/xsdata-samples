from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class FieldDataSearch1:
    """
    Specifies a search term and value (wildcards permitted), to search profiles by
    data in custom profile fields.

    Parameters
    ----------
    field_id
        The reference to the custom field that this FieldData refers.Provide
        either FieldID or Name, not both.
    name
        Name of the custom field that this FieldData refers.Provide either
        Name or FieldID, not both.
    value
        The value to search for in the relevant profiles. Wildcards
        permitted. All searches are case-insensitive.
    field_group_id
        Used to limit the search to multiple fields of the same field group
        instance.
    """

    class Meta:
        name = "FieldDataSearch"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        },
    )
    field_group_id: None | str = field(
        default=None,
        metadata={
            "name": "FieldGroupID",
            "type": "Attribute",
        },
    )
