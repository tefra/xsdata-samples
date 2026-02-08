from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Duration:
    class Meta:
        name = "duration"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
        }
    )
