from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Type:
    class Meta:
        name = "type"

    basic: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arrow: TypeArrow | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TypeArrow:
    class Meta:
        global_type = False

    type_value: list[Type] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
