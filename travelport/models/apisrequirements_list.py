from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.apisrequirements import Apisrequirements

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class ApisrequirementsList:
    """
    The shared object list of APISRequirements.
    """

    class Meta:
        name = "APISRequirementsList"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    apisrequirements: list[Apisrequirements] = field(
        default_factory=list,
        metadata={
            "name": "APISRequirements",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
