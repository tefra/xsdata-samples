from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class TypeKeyBasedReference4:
    """
    Generic type to be used for Key based reference.
    """

    class Meta:
        name = "typeKeyBasedReference"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
