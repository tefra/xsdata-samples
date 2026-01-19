from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .distribution_assignment import DistributionAssignment
from .distribution_assignment_ref import DistributionAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "distributionAssignments_RelStructure"

    distribution_assignment_ref_or_distribution_assignment: Sequence[
        DistributionAssignmentRef | DistributionAssignment
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistributionAssignmentRef",
                    "type": DistributionAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionAssignment",
                    "type": DistributionAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
