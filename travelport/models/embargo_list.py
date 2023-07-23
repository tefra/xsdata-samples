from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.embargo import Embargo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class EmbargoList:
    """List of embargoes.

    Provider: 1G, 1V, 1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    embargo: list[Embargo] = field(
        default_factory=list,
        metadata={
            "name": "Embargo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        }
    )
