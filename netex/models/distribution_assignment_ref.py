from dataclasses import dataclass
from netex.models.distribution_assignment_ref_structure import DistributionAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionAssignmentRef(DistributionAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
