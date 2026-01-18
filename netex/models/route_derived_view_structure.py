from __future__ import annotations

from dataclasses import dataclass, field

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .derived_view_structure import DerivedViewStructure
from .direction_view import DirectionView
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .line_view import LineView
from .link_sequence_projection_ref import LinkSequenceProjectionRef
from .multilingual_string import MultilingualString
from .route_ref import RouteRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "Route_DerivedViewStructure"

    route_ref: None | RouteRef = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_mode: None | AllVehicleModesOfTransportEnumeration = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_line_ref_or_line_ref_or_line_view: (
        None | FlexibleLineRef | LineRef | LineView
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
                    "name": "LineView",
                    "type": LineView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_view: None | DirectionView = field(
        default=None,
        metadata={
            "name": "DirectionView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    link_sequence_projection_ref: None | LinkSequenceProjectionRef = field(
        default=None,
        metadata={
            "name": "LinkSequenceProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
