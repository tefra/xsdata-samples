from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.navigation_path import NavigationPath
from netex.models.navigation_path_ref import NavigationPathRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPathsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "navigationPaths_RelStructure"

    navigation_path_ref: List[NavigationPathRef] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_path: List[NavigationPath] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
