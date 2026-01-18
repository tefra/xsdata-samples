from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Arity:
    class Meta:
        name = "arity"

    value: None | int = field(
        default=None,
        metadata={
            "required": True,
        },
    )
