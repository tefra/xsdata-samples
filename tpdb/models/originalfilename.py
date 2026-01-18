from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Originalfilename:
    class Meta:
        name = "originalfilename"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
