from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.activation_point_ref import ActivationPointRef
from netex.models.beacon_point_ref import BeaconPointRef
from netex.models.border_point_ref import BorderPointRef
from netex.models.complex_feature_ref_structure import ComplexFeatureRefStructure
from netex.models.complex_feature_refs_rel_structure import ComplexFeatureRefsRelStructure
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.garage_point_ref import GaragePointRef
from netex.models.infrastructure_point_ref import InfrastructurePointRef
from netex.models.parking_point_ref import ParkingPointRef
from netex.models.point_on_link_ref import PointOnLinkRef
from netex.models.point_ref import PointRef
from netex.models.projection_version_structure import ProjectionVersionStructure
from netex.models.railway_point_ref import RailwayPointRef
from netex.models.relief_point_ref import ReliefPointRef
from netex.models.road_point_ref import RoadPointRef
from netex.models.route_point_ref import RoutePointRef
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.timing_point_ref import TimingPointRef
from netex.models.traffic_control_point_ref import TrafficControlPointRef
from netex.models.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplexFeatureProjectionVersionStructure(ProjectionVersionStructure):
    class Meta:
        name = "ComplexFeatureProjection_VersionStructure"

    projected_fearture_ref: Optional[ComplexFeatureRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedFeartureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onto_feature_ref: Optional[ComplexFeatureRefStructure] = field(
        default=None,
        metadata={
            "name": "OntoFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_point_ref: List[BorderPointRef] = field(
        default_factory=list,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: List[ScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage_point_ref: List[GaragePointRef] = field(
        default_factory=list,
        metadata={
            "name": "GaragePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_point_ref: List[ParkingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_point_ref: List[ReliefPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_ref: List[TimingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_point_ref: List[RoutePointRef] = field(
        default_factory=list,
        metadata={
            "name": "RoutePointRef",
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
        }
    )
    road_point_ref: List[RoadPointRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_point_ref: List[RailwayPointRef] = field(
        default_factory=list,
        metadata={
            "name": "RailwayPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_point_ref: List[InfrastructurePointRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructurePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    traffic_control_point_ref: List[TrafficControlPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TrafficControlPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    beacon_point_ref: List[BeaconPointRef] = field(
        default_factory=list,
        metadata={
            "name": "BeaconPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_point_ref: List[ActivationPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_on_link_ref: List[PointOnLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_ref: List[PointRef] = field(
        default_factory=list,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    features: Optional[ComplexFeatureRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
