from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlTime

from .connecting_journey_view import ConnectingJourneyView
from .connection_ref_structure import ConnectionRefStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .entity_in_version_structure import DataManagedObjectStructure
from .flexible_line_ref import FlexibleLineRef
from .line_derived_view_structure import LineDerivedViewStructure
from .line_ref import LineRef
from .multilingual_string import MultilingualString
from .point_in_journey_pattern_ref_structure import (
    PointInJourneyPatternRefStructure,
)
from .reason_for_meeting_enumeration import ReasonForMeetingEnumeration
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_journey_ref import ServiceJourneyRef
from .single_journey_ref import SingleJourneyRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyMeetingVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "JourneyMeeting_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    at_stop_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "AtStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_journey_ref: VehicleJourneyRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_journey_ref: VehicleJourneyRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    from_point_in_journey_pattern_ref: PointInJourneyPatternRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromPointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_point_in_journey_pattern_ref: PointInJourneyPatternRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToPointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "EarliestTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    latest_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "LatestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    latest_time_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "LatestTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reason: ReasonForMeetingEnumeration | None = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connection_ref: ConnectionRefStructure | None = field(
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
    choice: SingleJourneyRef | DatedVehicleJourneyRef | DatedSpecialServiceRef | SpecialServiceRef | TemplateServiceJourneyRef | ServiceJourneyRef | DeadRunRef | VehicleJourneyRef | ConnectingJourneyView | None = field(
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
    flexible_line_ref_or_line_ref_or_connecting_line_view: FlexibleLineRef | LineRef | LineDerivedViewStructure | None = field(
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
