from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.direction_info_direction import DirectionInfoDirection

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class RoutingRules:
    """
    Rules related to routing.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    routing: list[RoutingRules.Routing] = field(
        default_factory=list,
        metadata={
            "name": "Routing",
            "type": "Element",
            "max_occurs": 999,
        },
    )

    @dataclass(kw_only=True)
    class Routing:
        direction_info: list[RoutingRules.Routing.DirectionInfo] = field(
            default_factory=list,
            metadata={
                "name": "DirectionInfo",
                "type": "Element",
                "max_occurs": 999,
            },
        )
        routing_constructed_ind: None | bool = field(
            default=None,
            metadata={
                "name": "RoutingConstructedInd",
                "type": "Attribute",
            },
        )
        number: None | str = field(
            default=None,
            metadata={
                "name": "Number",
                "type": "Attribute",
            },
        )
        routing_restriction: None | str = field(
            default=None,
            metadata={
                "name": "RoutingRestriction",
                "type": "Attribute",
            },
        )

        @dataclass(kw_only=True)
        class DirectionInfo:
            location_code: None | str = field(
                default=None,
                metadata={
                    "name": "LocationCode",
                    "type": "Attribute",
                    "length": 3,
                    "white_space": "collapse",
                },
            )
            direction: None | DirectionInfoDirection = field(
                default=None,
                metadata={
                    "name": "Direction",
                    "type": "Attribute",
                },
            )
