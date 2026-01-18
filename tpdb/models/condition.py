from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.lhs import Lhs
from tpdb.models.rhs import Rhs


@dataclass
class Condition:
    class Meta:
        name = "condition"

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
