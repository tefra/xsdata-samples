from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class MetaData6:
    """Extra data to elaborate the parent element.

    This data is primarily informative and is not persisted.
    """
    class Meta:
        name = "MetaData"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        }
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )
