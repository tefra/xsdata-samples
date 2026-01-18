from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Arity:
    class Meta:
        name = "arity"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
