from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.conditions import Conditions
from tpdb.models.lhs import Lhs
from tpdb.models.rhs import Rhs


@dataclass(kw_only=True)
class Rule:
    class Meta:
        name = "rule"

    lhs: Lhs = field(
        metadata={
            "type": "Element",
        }
    )
    rhs: Rhs = field(
        metadata={
            "type": "Element",
        }
    )
    conditions: None | Conditions = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
