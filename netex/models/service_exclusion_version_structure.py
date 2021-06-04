from dataclasses import dataclass, field
from typing import Optional
from netex.models.assignment_version_structure_2 import AssignmentVersionStructure2
from netex.models.journey_pattern_ref_structure import JourneyPatternRefStructure
from netex.models.journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceExclusionVersionStructure(AssignmentVersionStructure2):
    class Meta:
        name = "ServiceExclusion_VersionStructure"

    excluding_journey_pattern_ref: Optional[JourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "ExcludingJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    excluded_journey_pattern_refs: Optional[JourneyPatternRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "excludedJourneyPatternRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
