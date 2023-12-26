from dataclasses import dataclass, field
from typing import Optional
from .assignment_version_structure_1 import AssignmentVersionStructure1
from .group_of_timing_links_ref import GroupOfTimingLinksRef
from .time_demand_type_ref import TimeDemandTypeRef
from .timeband_ref import TimebandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandTypeAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "TimeDemandTypeAssignment_VersionStructure"

    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timeband_ref: Optional[TimebandRef] = field(
        default=None,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_timing_links_ref: Optional[GroupOfTimingLinksRef] = field(
        default=None,
        metadata={
            "name": "GroupOfTimingLinksRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
