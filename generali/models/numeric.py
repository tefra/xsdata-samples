from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Numeric:
    class Meta:
        name = "numeric"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
