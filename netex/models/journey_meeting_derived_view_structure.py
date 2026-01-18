from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

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
from .line_derived_view_structure import LineDerivedViewStructure
from .line_ref import LineRef
from .multilingual_string import MultilingualString
from .reason_for_meeting_enumeration import ReasonForMeetingEnumeration
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_journey_ref import ServiceJourneyRef
from .single_journey_ref import SingleJourneyRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .transfer_duration_structure import TransferDurationStructure
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyMeetingDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "JourneyMeeting_DerivedViewStructure"

    journey_meeting_ref: None | JourneyMeetingRef = field(
        default=None,
        metadata={
            "name": "JourneyMeetingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time_day_offset: None | int = field(
        default=None,
        metadata={
            "name": "EarliestTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    latest_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "LatestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    latest_time_day_offset: None | int = field(
        default=None,
        metadata={
            "name": "LatestTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reason: None | ReasonForMeetingEnumeration = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_wait_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connection_ref: None | ConnectionRefStructure = field(
        default=None,
        metadata={
            "name": "ConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connecting_stop_point_ref: Iterable[ScheduledStopPointRefStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "ConnectingStopPointRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    connecting_stop_point_name: Iterable[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingStopPointName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: (
        None
        | SingleJourneyRef
        | DatedVehicleJourneyRef
        | DatedSpecialServiceRef
        | SpecialServiceRef
        | TemplateServiceJourneyRef
        | ServiceJourneyRef
        | DeadRunRef
        | VehicleJourneyRef
        | ConnectingJourneyView
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SingleJourneyRef",
                    "type": SingleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                    "name": "ConnectingJourneyView",
                    "type": ConnectingJourneyView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    flexible_line_ref_or_line_ref_or_connecting_line_view: (
        None | FlexibleLineRef | LineRef | LineDerivedViewStructure
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    stay_seated: None | bool = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cross_border: None | bool = field(
        default=None,
        metadata={
            "name": "CrossBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    planned: None | bool = field(
        default=None,
        metadata={
            "name": "Planned",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    guaranteed: None | bool = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    advertised: None | bool = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    controlled: None | bool = field(
        default=None,
        metadata={
            "name": "Controlled",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connection_certainty: None | ConnectionCertaintyEnumeration = field(
        default=None,
        metadata={
            "name": "ConnectionCertainty",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_duration: None | TransferDurationStructure = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
