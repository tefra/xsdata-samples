from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.conditions import Conditions
from tpdb.models.lhs import Lhs
from tpdb.models.rhs import Rhs


@dataclass
class Rule:
    class Meta:
        name = "rule"

    lhs: Lhs | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rhs: Rhs | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    conditions: Conditions | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
