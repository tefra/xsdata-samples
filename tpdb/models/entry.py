from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Entry:
    class Meta:
        name = "entry"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
