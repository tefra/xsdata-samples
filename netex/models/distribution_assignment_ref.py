from __future__ import annotations

from dataclasses import dataclass

from .distribution_assignment_ref_structure import (
    DistributionAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionAssignmentRef(DistributionAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
