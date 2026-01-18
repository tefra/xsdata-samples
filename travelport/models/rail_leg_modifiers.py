from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.connection_point_1 import ConnectionPoint1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailLegModifiers:
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    permitted_connection_points: (
        None | RailLegModifiers.PermittedConnectionPoints
    ) = field(
        default=None,
        metadata={
            "name": "PermittedConnectionPoints",
            "type": "Element",
        },
    )
    prohibited_connection_points: (
        None | RailLegModifiers.ProhibitedConnectionPoints
    ) = field(
        default=None,
        metadata={
            "name": "ProhibitedConnectionPoints",
            "type": "Element",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class PermittedConnectionPoints:
        connection_point: list[ConnectionPoint1] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass(kw_only=True)
    class ProhibitedConnectionPoints:
        connection_point: list[ConnectionPoint1] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
