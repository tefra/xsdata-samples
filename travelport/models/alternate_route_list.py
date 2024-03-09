from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.alternate_route import AlternateRoute

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AlternateRouteList:
    """
    Identifies the alternate routes for the request.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    alternate_route: list[AlternateRoute] = field(
        default_factory=list,
        metadata={
            "name": "AlternateRoute",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
