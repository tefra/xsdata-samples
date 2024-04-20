from dataclasses import dataclass, field
from typing import List

from tpdb.models.condition import Condition


@dataclass
class Conditions:
    class Meta:
        name = "conditions"

    condition: List[Condition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
