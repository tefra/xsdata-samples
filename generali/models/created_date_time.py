from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CreatedDateTime:
    class Meta:
        name = "created-date-time"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    format: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
