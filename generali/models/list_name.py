from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ListName:
    class Meta:
        name = "@list-name"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
