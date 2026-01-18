from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_otasub_key_1 import TypeOtasubKey1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TypeOtakeyword1:
    """
    A complexType for keyword information.

    Parameters
    ----------
    sub_key
        A further breakdown of a keyword.
    text
        Information for a keyword.
    name
        The keyword name.
    number
        The number for this keyword.
    description
        A brief description of the keyword
    """

    class Meta:
        name = "typeOTAKeyword"

    sub_key: list[TypeOtasubKey1] = field(
        default_factory=list,
        metadata={
            "name": "SubKey",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
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
