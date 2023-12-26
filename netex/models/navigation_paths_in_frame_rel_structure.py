from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .navigation_path import NavigationPath

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPathsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "navigationPathsInFrame_RelStructure"

    navigation_path: List[NavigationPath] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
