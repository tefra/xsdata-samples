from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .distribution_assignment import DistributionAssignment
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionAssignmentsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "distributionAssignmentsInFrame_RelStructure"

    distribution_assignment: Iterable[DistributionAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DistributionAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
