from dataclasses import dataclass, field
from typing import Optional
from .railway_link_ref import RailwayLinkRef
from .railway_point_ref import RailwayPointRef
from .road_link_ref import RoadLinkRef
from .road_point_ref import RoadPointRef
from .stop_place_space_version_structure import StopPlaceSpaceVersionStructure
from .vehicle_quay_alignments_rel_structure import VehicleQuayAlignmentsRelStructure
from .vehicle_stopping_positions_rel_structure import VehicleStoppingPositionsRelStructure
from .wire_link_ref import WireLinkRef
from .wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPlaceVersionStructure(StopPlaceSpaceVersionStructure):
    class Meta:
        name = "VehicleStoppingPlace_VersionStructure"

    wire_link_ref: Optional[WireLinkRef] = field(
        default=None,
        metadata={
            "name": "WireLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_link_ref: Optional[RoadLinkRef] = field(
        default=None,
        metadata={
            "name": "RoadLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_link_ref: Optional[RailwayLinkRef] = field(
        default=None,
        metadata={
            "name": "RailwayLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_point_ref: Optional[WirePointRef] = field(
        default=None,
        metadata={
            "name": "WirePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_point_ref: Optional[RoadPointRef] = field(
        default=None,
        metadata={
            "name": "RoadPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_point_ref: Optional[RailwayPointRef] = field(
        default=None,
        metadata={
            "name": "RailwayPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_positions: Optional[VehicleStoppingPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleStoppingPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_alignments: Optional[VehicleQuayAlignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "quayAlignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
