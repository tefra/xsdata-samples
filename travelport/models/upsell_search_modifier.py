from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class UpsellSearchModifier:
    """
    Upsell search modifier to hold values for start and max results.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        },
    )
    start_from_result: int = field(
        default=1,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
