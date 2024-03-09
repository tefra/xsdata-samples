from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PolicyCodesList:
    """
    Parameters
    ----------
    policy_code
        A code that indicates why an item was determined to be ‘out of
        policy’.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    policy_code: list[int] = field(
        default_factory=list,
        metadata={
            "name": "PolicyCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
            "min_inclusive": 1,
            "max_inclusive": 9999,
        },
    )
