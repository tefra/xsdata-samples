from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .path_link import PathLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pathLinksInFrame_RelStructure"

    path_link: Iterable[PathLink] = field(
        default_factory=list,
        metadata={
            "name": "PathLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
