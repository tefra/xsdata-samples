from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .version import Version
from .version_ref import VersionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "versions_RelStructure"

    version_ref: List[VersionRef] = field(
        default_factory=list,
        metadata={
            "name": "VersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version: List[Version] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )