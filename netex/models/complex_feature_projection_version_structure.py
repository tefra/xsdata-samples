from dataclasses import dataclass, field
from typing import List, Optional, Union
from .activation_point_ref import ActivationPointRef
from .beacon_point_ref import BeaconPointRef
from .border_point_ref import BorderPointRef
from .complex_feature_ref_structure import ComplexFeatureRefStructure
from .complex_feature_refs_rel_structure import ComplexFeatureRefsRelStructure
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .garage_point_ref import GaragePointRef
from .parking_point_ref import ParkingPointRef
from .point_ref import PointRef
from .projection_version_structure import ProjectionVersionStructure
from .railway_point_ref import RailwayPointRef
from .relief_point_ref import ReliefPointRef
from .road_point_ref import RoadPointRef
from .route_point_ref import RoutePointRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .timing_point_ref import TimingPointRef
from .traffic_control_point_ref import TrafficControlPointRef
from .wire_point_ref import WirePointRef

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
        },
    )
    onto_feature_ref: Optional[ComplexFeatureRefStructure] = field(
        default=None,
        metadata={
            "name": "OntoFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: List[
        Union[
            BorderPointRef,
            FareScheduledStopPointRef,
            ScheduledStopPointRef,
            GaragePointRef,
            ParkingPointRef,
            ReliefPointRef,
            TimingPointRef,
            RoutePointRef,
            WirePointRef,
            RoadPointRef,
            RailwayPointRef,
            TrafficControlPointRef,
            BeaconPointRef,
            ActivationPointRef,
            PointRef,
        ]
    ] = field(
        default_factory=list,
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
                {
                    "name": "WirePointRef",
                    "type": WirePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadPointRef",
                    "type": RoadPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayPointRef",
                    "type": RailwayPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPointRef",
                    "type": TrafficControlPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPointRef",
                    "type": BeaconPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPointRef",
                    "type": ActivationPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointRef",
                    "type": PointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    features: Optional[ComplexFeatureRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
