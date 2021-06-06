from dataclasses import dataclass, field
from typing import Optional
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .derived_view_structure import DerivedViewStructure
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .direction_ref import DirectionRef
from .direction_type_enumeration import DirectionTypeEnumeration
from .direction_view import DirectionView
from .journey_pattern_ref import JourneyPatternRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operational_context_ref import OperationalContextRef
from .route_ref import RouteRef
from .route_view import RouteView
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .timing_pattern_ref import TimingPatternRef
from .type_of_journey_pattern_ref import TypeOfJourneyPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "JourneyPattern_DerivedViewStructure"

    service_journey_pattern_ref: Optional[ServiceJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_pattern_ref: Optional[ServicePatternRef] = field(
        default=None,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_journey_pattern_ref: Optional[DeadRunJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_ref: Optional[JourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_view: Optional[RouteView] = field(
        default=None,
        metadata={
            "name": "RouteView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_view: Optional[DirectionView] = field(
        default=None,
        metadata={
            "name": "DirectionView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_view: Optional[DestinationDisplayView] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_journey_pattern_ref: Optional[TypeOfJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_pattern_ref: Optional[TimingPatternRef] = field(
        default=None,
        metadata={
            "name": "TimingPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
