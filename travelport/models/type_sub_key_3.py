from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class TypeSubKey3:
    """
    The attributes and elements in a SubKey.

    Parameters
    ----------
    text
        Information for a sub key.
    name
        A subkey to identify the specific information within this keyword
    description
        A brief description of a subkey.
    """

    class Meta:
        name = "typeSubKey"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        },
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
