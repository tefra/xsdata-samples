from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .navigation_path import NavigationPath
from .navigation_path_ref import NavigationPathRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPathsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "navigationPaths_RelStructure"

    navigation_path_ref_or_navigation_path: Iterable[
        NavigationPathRef | NavigationPath
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPath",
                    "type": NavigationPath,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
