from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.lhs import Lhs
from tpdb.models.rhs import Rhs


@dataclass(kw_only=True)
class Condition:
    class Meta:
        name = "condition"

    lhs: Lhs = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    rhs: Rhs = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
