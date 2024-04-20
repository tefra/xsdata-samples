from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.conditions import Conditions
from tpdb.models.lhs import Lhs
from tpdb.models.rhs import Rhs


@dataclass
class Rule:
    class Meta:
        name = "rule"

    lhs: Optional[Lhs] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rhs: Optional[Rhs] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    conditions: Optional[Conditions] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
