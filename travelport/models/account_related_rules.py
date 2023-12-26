from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_rules import BookingRules
from travelport.models.routing_rules import RoutingRules

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AccountRelatedRules:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    booking_rules: list[BookingRules] = field(
        default_factory=list,
        metadata={
            "name": "BookingRules",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    routing_rules: None | RoutingRules = field(
        default=None,
        metadata={
            "name": "RoutingRules",
            "type": "Element",
        },
    )
