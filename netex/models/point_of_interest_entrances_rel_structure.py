from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .point_of_interest_entrance import PointOfInterestEntrance
from .site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestEntrancesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pointOfInterestEntrances_RelStructure"

    point_of_interest_entrance_ref_or_point_of_interest_entrance: List[Union[SiteComponentRefStructure, PointOfInterestEntrance]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOfInterestEntranceRef",
                    "type": SiteComponentRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntrance",
                    "type": PointOfInterestEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
