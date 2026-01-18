from __future__ import annotations

from dataclasses import dataclass, field

from .border_point_ref import BorderPointRef
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .entity_in_version_structure import VersionedChildStructure
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .garage_point_ref import GaragePointRef
from .multilingual_string import MultilingualString
from .parking_point_ref import ParkingPointRef
from .relief_point_ref import ReliefPointRef
from .route_point_ref import RoutePointRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .timing_point_ref import TimingPointRef
from .via_type_enumeration import ViaTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ViaVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "Via_VersionedChildStructure"

    destination_display_ref_or_destination_display_view_or_name: (
        None
        | DestinationDisplayRef
        | DestinationDisplayView
        | MultilingualString
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayView",
                    "type": DestinationDisplayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Name",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice: (
        None
        | BorderPointRef
        | FareScheduledStopPointRef
        | ScheduledStopPointRef
        | GaragePointRef
        | ParkingPointRef
        | ReliefPointRef
        | TimingPointRef
        | RoutePointRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BorderPointRef",
                    "type": BorderPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointRef",
                    "type": TimingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePointRef",
                    "type": RoutePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    via_type: None | ViaTypeEnumeration = field(
        default=None,
        metadata={
            "name": "ViaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
