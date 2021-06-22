from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from .connecting_journey_view import ConnectingJourneyView
from .connection_certainty_enumeration import ConnectionCertaintyEnumeration
from .connection_ref_structure import ConnectionRefStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .derived_view_structure import DerivedViewStructure
from .flexible_line_ref import FlexibleLineRef
from .journey_meeting_ref import JourneyMeetingRef
from .journey_ref import JourneyRef
from .line_derived_view_structure import LineDerivedViewStructure
from .line_ref import LineRef
from .multilingual_string import MultilingualString
from .reason_for_meeting_enumeration import ReasonForMeetingEnumeration
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_journey_ref import ServiceJourneyRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .transfer_duration_structure import TransferDurationStructure
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyMeetingDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "JourneyMeeting_DerivedViewStructure"

    journey_meeting_ref: Optional[JourneyMeetingRef] = field(
        default=None,
        metadata={
            "name": "JourneyMeetingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    earliest_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EarliestTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    latest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    latest_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "LatestTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reason: Optional[ReasonForMeetingEnumeration] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connection_ref: Optional[ConnectionRefStructure] = field(
        default=None,
        metadata={
            "name": "ConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connecting_stop_point_ref: List[ScheduledStopPointRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connecting_stop_point_name: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingStopPointName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyRef",
                    "type": JourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectingJourneyView",
                    "type": ConnectingJourneyView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectingLineView",
                    "type": LineDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaySeated",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossBorder",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Planned",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Guaranteed",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Advertised",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Controlled",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectionCertainty",
                    "type": ConnectionCertaintyEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransferDuration",
                    "type": TransferDurationStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 31,
        }
    )
