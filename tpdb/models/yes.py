from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.bound_value import BoundValue


@dataclass(kw_only=True)
class Yes:
    class Meta:
        name = "yes"

    lowerbound: None | str | BoundValue = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"O\(n\^[0-9]+\)",
        },
    )
    upperbound: None | str | BoundValue = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"O\(n\^[0-9]+\)",
        },
    )
