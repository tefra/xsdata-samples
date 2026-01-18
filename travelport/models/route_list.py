from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.route import Route

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class RouteList:
    """
    Identifies the routes and sub-routes that were requested.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    route: list[Route] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
