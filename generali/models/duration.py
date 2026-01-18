from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Duration:
    class Meta:
        name = "duration"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
