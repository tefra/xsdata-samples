from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.relrules import Relrules
from tpdb.models.rule import Rule


@dataclass(kw_only=True)
class Rules:
    class Meta:
        name = "rules"

    rule: list[Rule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    relrules: None | Relrules = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
