from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class TypeKeyBasedReference4:
    """
    Generic type to be used for Key based reference.
    """

    class Meta:
        name = "typeKeyBasedReference"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
