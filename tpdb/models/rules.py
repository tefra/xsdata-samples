from dataclasses import dataclass, field
from typing import Optional

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
    relrules: Optional[Relrules] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
