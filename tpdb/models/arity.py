from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Arity:
    class Meta:
        name = "arity"

    value: int = field(
        metadata={
            "required": True,
        }
    )
