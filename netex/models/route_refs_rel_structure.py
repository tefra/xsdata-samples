from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.route_ref import RouteRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "routeRefs_RelStructure"

    route_ref: List[RouteRef] = field(
        default_factory=list,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
