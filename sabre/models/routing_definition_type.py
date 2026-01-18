from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.routing_leg_type import RoutingLegType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class RoutingDefinitionType:
    """
    Definition of a routing.

    Attributes:
        routing_leg:
        add_wildcards: If true, wildcards will be automatically inserted
            between each two leg (RoutingLeg) elements. Will be set to
            'false' if not present.
    """

    routing_leg: list[RoutingLegType] = field(
        default_factory=list,
        metadata={
            "name": "RoutingLeg",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )
    add_wildcards: None | bool = field(
        default=None,
        metadata={
            "name": "AddWildcards",
            "type": "Attribute",
        },
    )
