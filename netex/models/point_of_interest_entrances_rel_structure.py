from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.point_of_interest_entrance import PointOfInterestEntrance
from netex.models.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestEntrancesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pointOfInterestEntrances_RelStructure"

    point_of_interest_entrance_ref: List[SiteComponentRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_entrance: List[PointOfInterestEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
