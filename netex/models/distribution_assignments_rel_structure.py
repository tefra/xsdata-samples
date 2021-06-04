from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.distribution_assignment import DistributionAssignment
from netex.models.distribution_assignment_ref import DistributionAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "distributionAssignments_RelStructure"

    distribution_assignment_ref: List[DistributionAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DistributionAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_assignment: List[DistributionAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DistributionAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
