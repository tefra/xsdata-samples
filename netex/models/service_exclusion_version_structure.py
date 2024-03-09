from dataclasses import dataclass, field
from typing import Optional

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceExclusionVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "ServiceExclusion_VersionStructure"

    excluding_journey_pattern_ref: Optional[JourneyPatternRefStructure] = (
        field(
            default=None,
            metadata={
                "name": "ExcludingJourneyPatternRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    start_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    excluded_journey_pattern_refs: Optional[JourneyPatternRefsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "excludedJourneyPatternRefs",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
