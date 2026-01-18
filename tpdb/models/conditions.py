from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.condition import Condition


@dataclass(kw_only=True)
class Conditions:
    class Meta:
        name = "conditions"

    condition: list[Condition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
