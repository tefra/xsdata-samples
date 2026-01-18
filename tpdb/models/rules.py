from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.relrules import Relrules
from tpdb.models.rule import Rule


@dataclass
class Rules:
    class Meta:
        name = "rules"

    rule: list[Rule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    relrules: Relrules | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
