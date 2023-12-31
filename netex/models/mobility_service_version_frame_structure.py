from dataclasses import dataclass, field
from typing import Optional
from .common_version_frame_structure import CommonVersionFrameStructure
from .fleets_rel_structure import FleetsRelStructure
from .mobility_service_constraint_zones_in_frame_rel_structure import (
    MobilityServiceConstraintZonesInFrameRelStructure,
)
from .mobility_services_rel_structure import MobilityServicesRelStructure
from .modes_of_operation_rel_structure import ModesOfOperationRelStructure
from .online_services_rel_structure import OnlineServicesRelStructure
from .pool_of_vehicles_rel_structure import PoolOfVehiclesRelStructure
from .vehicle_meeting_links_in_frame_rel_structure import (
    VehicleMeetingLinksInFrameRelStructure,
)
from .vehicle_meeting_places_rel_structure import (
    VehicleMeetingPlacesRelStructure,
)
from .vehicle_meeting_point_assignments_in_frame_rel_structure import (
    VehicleMeetingPointAssignmentsInFrameRelStructure,
)
from .vehicle_meeting_points_in_frame_rel_structure import (
    VehicleMeetingPointsInFrameRelStructure,
)
from .vehicle_service_place_assignments_rel_structure import (
    VehicleServicePlaceAssignmentsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityServiceVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "MobilityService_VersionFrameStructure"

    fleets: Optional[FleetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pools_of_vehicles: Optional[PoolOfVehiclesRelStructure] = field(
        default=None,
        metadata={
            "name": "poolsOfVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    modes_of_operation: Optional[ModesOfOperationRelStructure] = field(
        default=None,
        metadata={
            "name": "modesOfOperation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mobility_services: Optional[MobilityServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "mobilityServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    online_services: Optional[OnlineServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "onlineServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_meeting_points: Optional[
        VehicleMeetingPointsInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_meeting_links: Optional[
        VehicleMeetingLinksInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_meeting_point_assignments: Optional[
        VehicleMeetingPointAssignmentsInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingPointAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_meeting_places: Optional[VehicleMeetingPlacesRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_meeting_place_assignments: Optional[
        VehicleServicePlaceAssignmentsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingPlaceAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mobility_service_constraint_zones: Optional[
        MobilityServiceConstraintZonesInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "mobilityServiceConstraintZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
