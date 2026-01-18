from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Var:
    class Meta:
        name = "var"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
