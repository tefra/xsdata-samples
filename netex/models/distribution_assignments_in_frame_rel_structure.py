from dataclasses import dataclass, field
from typing import List
from netex.models.distribution_assignment import DistributionAssignment
from netex.models.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionAssignmentsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "distributionAssignmentsInFrame_RelStructure"

    distribution_assignment: List[DistributionAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DistributionAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
