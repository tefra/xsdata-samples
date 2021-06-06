from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_timebands_ref import GroupOfTimebandsRef
from .group_of_timebands_versioned_child_structure import GroupOfTimebandsVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTimebandsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupOfTimebands_RelStructure"

    group_of_timebands_ref: List[GroupOfTimebandsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimebandsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_timebands: List[GroupOfTimebandsVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimebands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
