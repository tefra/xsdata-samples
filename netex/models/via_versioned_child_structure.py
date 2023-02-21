from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_texts_rel_structure import VersionedChildStructure
from .border_point_ref import BorderPointRef
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
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


@dataclass
class ViaVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "Via_VersionedChildStructure"

    destination_display_ref_or_destination_display_view_or_name: List[object] = field(
        default_factory=list,
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
            "max_occurs": 3,
        }
    )
    border_point_ref: Optional[BorderPointRef] = field(
        default=None,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref: Optional[FareScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage_point_ref: Optional[GaragePointRef] = field(
        default=None,
        metadata={
            "name": "GaragePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_point_ref: Optional[ParkingPointRef] = field(
        default=None,
        metadata={
            "name": "ParkingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_point_ref: Optional[ReliefPointRef] = field(
        default=None,
        metadata={
            "name": "ReliefPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_ref: Optional[TimingPointRef] = field(
        default=None,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_point_ref: Optional[RoutePointRef] = field(
        default=None,
        metadata={
            "name": "RoutePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    via_type: Optional[ViaTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ViaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
