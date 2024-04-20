from dataclasses import dataclass, field
from typing import Optional, Union

from tpdb.models.bound_value import BoundValue


@dataclass
class Yes:
    class Meta:
        name = "yes"

    lowerbound: Optional[Union[str, BoundValue]] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"O\(n\^[0-9]+\)",
        },
    )
    upperbound: Optional[Union[str, BoundValue]] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"O\(n\^[0-9]+\)",
        },
    )
