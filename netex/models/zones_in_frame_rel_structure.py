from dataclasses import dataclass, field
from typing import List
from .access_space import AccessSpace
from .access_zone import AccessZone
from .addressable_place import AddressablePlace
from .administrative_zone_version_structure import (
    AdministrativeZone1,
    TransportAdministrativeZone,
)
from .boarding_position import BoardingPosition
from .containment_aggregation_structure import ContainmentAggregationStructure
from .country import Country
from .entrance import Entrance
from .equipment_place import EquipmentPlace
from .fare_zone import FareZone
from .flexible_area import FlexibleArea
from .flexible_quay import FlexibleQuay
from .flexible_stop_place import FlexibleStopPlace
from .garage import Garage
from .general_zone import GeneralZone
from .hail_and_ride_area import HailAndRideArea
from .parking import Parking
from .parking_area import ParkingArea
from .parking_bay import ParkingBay
from .parking_component import ParkingComponent
from .parking_entrance_for_vehicles import ParkingEntranceForVehicles
from .parking_passenger_entrance import ParkingPassengerEntrance
from .point_of_interest import PointOfInterest
from .point_of_interest_entrance import PointOfInterestEntrance
from .point_of_interest_space import PointOfInterestSpace
from .point_of_interest_vehicle_entrance import PointOfInterestVehicleEntrance
from .postal_address import PostalAddress
from .quay import Quay
from .road_address import RoadAddress
from .routing_constraint_zone import RoutingConstraintZone
from .service_site import ServiceSite
from .stop_area import StopArea
from .stop_place import StopPlace
from .stop_place_entrance import StopPlaceEntrance
from .stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from .tariff_zone_1 import TariffZone1
from .topographic_place import TopographicPlace
from .vehicle_stopping_place import VehicleStoppingPlace
from .vehicle_stopping_position import VehicleStoppingPosition
from .zone import Zone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZonesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "zonesInFrame_RelStructure"

    routing_constraint_zone: List[RoutingConstraintZone] = field(
        default_factory=list,
        metadata={
            "name": "RoutingConstraintZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_area: List[StopArea] = field(
        default_factory=list,
        metadata={
            "name": "StopArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_zone: List[AccessZone] = field(
        default_factory=list,
        metadata={
            "name": "AccessZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hail_and_ride_area: List[HailAndRideArea] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_area: List[FlexibleArea] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_quay: List[FlexibleQuay] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleQuay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_stop_place: List[FlexibleStopPlace] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_place: List[VehicleStoppingPlace] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position: List[BoardingPosition] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_space: List[AccessSpace] = field(
        default_factory=list,
        metadata={
            "name": "AccessSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay: List[Quay] = field(
        default_factory=list,
        metadata={
            "name": "Quay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_space: List[PointOfInterestSpace] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_bay: List[ParkingBay] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_area: List[ParkingArea] = field(
        default_factory=list,
        metadata={
            "name": "ParkingArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_component: List[ParkingComponent] = field(
        default_factory=list,
        metadata={
            "name": "ParkingComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_position: List[VehicleStoppingPosition] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_vehicle_entrance: List[PointOfInterestVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_entrance: List[PointOfInterestEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_passenger_entrance: List[ParkingPassengerEntrance] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPassengerEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_for_vehicles: List[ParkingEntranceForVehicles] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_vehicle_entrance: List[StopPlaceVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_entrance: List[StopPlaceEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance: List[Entrance] = field(
        default_factory=list,
        metadata={
            "name": "Entrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest: List[PointOfInterest] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking: List[Parking] = field(
        default_factory=list,
        metadata={
            "name": "Parking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place: List[StopPlace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_site: List[ServiceSite] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSite",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage: List[Garage] = field(
        default_factory=list,
        metadata={
            "name": "Garage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place: List[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_place: List[EquipmentPlace] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country: List[Country] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    addressable_place: List[AddressablePlace] = field(
        default_factory=list,
        metadata={
            "name": "AddressablePlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    postal_address: List[PostalAddress] = field(
        default_factory=list,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_address: List[RoadAddress] = field(
        default_factory=list,
        metadata={
            "name": "RoadAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_administrative_zone: List[TransportAdministrativeZone] = field(
        default_factory=list,
        metadata={
            "name": "TransportAdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    administrative_zone: List[AdministrativeZone1] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_zone: List[FareZone] = field(
        default_factory=list,
        metadata={
            "name": "FareZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone: List[TariffZone1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_zone: List[GeneralZone] = field(
        default_factory=list,
        metadata={
            "name": "GeneralZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone: List[Zone] = field(
        default_factory=list,
        metadata={
            "name": "Zone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
