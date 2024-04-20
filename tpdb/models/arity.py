from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Arity:
    class Meta:
        name = "arity"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
