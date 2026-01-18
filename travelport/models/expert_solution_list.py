from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.expert_solution import ExpertSolution

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class ExpertSolutionList:
    """
    Identifies the Expert Solutions retrieved from the Knowledge Base.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    expert_solution: list[ExpertSolution] = field(
        default_factory=list,
        metadata={
            "name": "ExpertSolution",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
