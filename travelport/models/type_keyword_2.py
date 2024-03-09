from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_sub_key_2 import TypeSubKey2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TypeKeyword2:
    """
    A complexType for keyword information.

    Parameters
    ----------
    sub_key
        A further breakdown of a keyword.
    name
        The keyword name.
    number
        The number for this keyword.
    description
        A brief description of the keyword
    """

    class Meta:
        name = "typeKeyword"

    sub_key: list[TypeSubKey2] = field(
        default_factory=list,
        metadata={
            "name": "SubKey",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "max_occurs": 99,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        },
    )
    number: None | object = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        },
    )
    description: None | object = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
