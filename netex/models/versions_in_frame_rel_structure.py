from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .version import Version

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "versionsInFrame_RelStructure"

    version: List[Version] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
