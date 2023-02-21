from dataclasses import dataclass, field
from typing import List, Optional
from .all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from .derived_view_structure import DerivedViewStructure
from .direction_view import DirectionView
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .line_view import LineView
from .link_sequence_projection_ref import LinkSequenceProjectionRef
from .multilingual_string import MultilingualString
from .route_ref import RouteRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "Route_DerivedViewStructure"

    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_line_ref_or_line_ref_or_line_view: List[object] = field(
        default_factory=list,
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
                    "name": "LineView",
                    "type": LineView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 3,
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
    link_sequence_projection_ref: Optional[LinkSequenceProjectionRef] = field(
        default=None,
        metadata={
            "name": "LinkSequenceProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
