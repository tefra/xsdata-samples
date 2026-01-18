from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class MetaData7:
    """
    Extra data to elaborate the parent element.

    This data is primarily informative and is not persisted.
    """

    class Meta:
        name = "MetaData"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        }
    )
    value: str = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )
