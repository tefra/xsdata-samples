from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Type:
    class Meta:
        name = "type"

    basic: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arrow: None | TypeArrow = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
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
