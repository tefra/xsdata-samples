from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.solution_group import SolutionGroup

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Enumeration:
    """
    Provides the capability to group the results into differnt trip type
    and diversification strategies.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    solution_group: list[SolutionGroup] = field(
        default_factory=list,
        metadata={
            "name": "SolutionGroup",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
