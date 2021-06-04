from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.point_of_interest_space import PointOfInterestSpace
from netex.models.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestSpacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pointOfInterestSpaces_RelStructure"

    point_of_interest_space_ref: List[SiteComponentRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_space: List[PointOfInterestSpace] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
