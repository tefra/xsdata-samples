from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.infrastructure_link_ref import InfrastructureLinkRef
from netex.models.infrastructure_point_ref import InfrastructurePointRef
from netex.models.railway_link_ref import RailwayLinkRef
from netex.models.railway_point_ref import RailwayPointRef
from netex.models.road_link_ref import RoadLinkRef
from netex.models.road_point_ref import RoadPointRef
from netex.models.stop_place_space_version_structure import StopPlaceSpaceVersionStructure
from netex.models.vehicle_quay_alignments_rel_structure import VehicleQuayAlignmentsRelStructure
from netex.models.vehicle_stopping_positions_rel_structure import VehicleStoppingPositionsRelStructure
from netex.models.wire_link_ref import WireLinkRef
from netex.models.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPlaceVersionStructure(StopPlaceSpaceVersionStructure):
    class Meta:
        name = "VehicleStoppingPlace_VersionStructure"

    wire_link_ref: List[WireLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "WireLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    road_link_ref: List[RoadLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    railway_link_ref: List[RailwayLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RailwayLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    infrastructure_link_ref: Optional[InfrastructureLinkRef] = field(
        default=None,
        metadata={
            "name": "InfrastructureLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_point_ref: List[WirePointRef] = field(
        default_factory=list,
        metadata={
            "name": "WirePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    road_point_ref: List[RoadPointRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    railway_point_ref: List[RailwayPointRef] = field(
        default_factory=list,
        metadata={
            "name": "RailwayPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    infrastructure_point_ref: Optional[InfrastructurePointRef] = field(
        default=None,
        metadata={
            "name": "InfrastructurePointRef",
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
