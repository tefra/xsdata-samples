from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.lhs import Lhs
from tpdb.models.rhs import Rhs


@dataclass
class Condition:
    class Meta:
        name = "condition"

    lhs: None | Lhs = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rhs: None | Rhs = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
