from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRuleFailureInfo:
    """
    Returns fare rule failure reason codes when fare basis code is forced.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    reason: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
