from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.rule import Rule


@dataclass(kw_only=True)
class Relrules:
    class Meta:
        name = "relrules"

    rule: list[Rule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
