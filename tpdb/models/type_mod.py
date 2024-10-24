from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TypeType:
    class Meta:
        name = "type"

    basic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arrow: Optional["TypeArrow"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TypeArrow:
    class Meta:
        global_type = False

    type_value: List[TypeType] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
