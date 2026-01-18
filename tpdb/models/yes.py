from dataclasses import dataclass, field

from tpdb.models.bound_value import BoundValue


@dataclass
class Yes:
    class Meta:
        name = "yes"

    lowerbound: str | BoundValue | None = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"O\(n\^[0-9]+\)",
        },
    )
    upperbound: str | BoundValue | None = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"O\(n\^[0-9]+\)",
        },
    )
