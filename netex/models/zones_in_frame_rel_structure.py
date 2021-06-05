from dataclasses import dataclass, field
from typing import List
from netex.models.access_space import AccessSpace
from netex.models.access_zone import AccessZone
from netex.models.address import Address
from netex.models.addressable_place import AddressablePlace
from netex.models.administrative_zone_2 import AdministrativeZone2
from netex.models.administrative_zone_version_structure import (
    AdministrativeZone1,
    TransportAdministrativeZone,
)
from netex.models.boarding_position import BoardingPosition
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.country import Country
from netex.models.entrance import Entrance
from netex.models.equipment_place import EquipmentPlace
from netex.models.fare_zone import FareZone
from netex.models.flexible_area import FlexibleArea
from netex.models.flexible_quay import FlexibleQuay
from netex.models.flexible_stop_place import FlexibleStopPlace
from netex.models.garage import Garage
from netex.models.general_zone import GeneralZone
from netex.models.hail_and_ride_area import HailAndRideArea
from netex.models.parking import Parking
from netex.models.parking_area import ParkingArea
from netex.models.parking_bay import ParkingBay
from netex.models.parking_component import ParkingComponent
from netex.models.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from netex.models.parking_passenger_entrance import ParkingPassengerEntrance
from netex.models.place import Place
from netex.models.point_of_interest import PointOfInterest
from netex.models.point_of_interest_component import PointOfInterestComponent
from netex.models.point_of_interest_entrance import PointOfInterestEntrance
from netex.models.point_of_interest_space import PointOfInterestSpace
from netex.models.point_of_interest_vehicle_entrance import PointOfInterestVehicleEntrance
from netex.models.postal_address import PostalAddress
from netex.models.quay import Quay
from netex.models.road_address import RoadAddress
from netex.models.routing_constraint_zone import RoutingConstraintZone
from netex.models.service_site import ServiceSite
from netex.models.site import Site
from netex.models.site_component import SiteComponent
from netex.models.site_element import SiteElement
from netex.models.stop_area import StopArea
from netex.models.stop_place import StopPlace
from netex.models.stop_place_component import StopPlaceComponent
from netex.models.stop_place_entrance import StopPlaceEntrance
from netex.models.stop_place_space import StopPlaceSpace
from netex.models.stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from netex.models.tariff_zone_1 import TariffZone1
from netex.models.tariff_zone_2 import TariffZone2
from netex.models.topographic_place import TopographicPlace
from netex.models.vehicle_entrance import VehicleEntrance
from netex.models.vehicle_stopping_place import VehicleStoppingPlace
from netex.models.vehicle_stopping_position import VehicleStoppingPosition
from netex.models.zone import Zone

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
            "min_occurs": 1,
        }
    )
    stop_area: List[StopArea] = field(
        default_factory=list,
        metadata={
            "name": "StopArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_zone: List[AccessZone] = field(
        default_factory=list,
        metadata={
            "name": "AccessZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    hail_and_ride_area: List[HailAndRideArea] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_area: List[FlexibleArea] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_quay: List[FlexibleQuay] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleQuay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_stop_place: List[FlexibleStopPlace] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_component: List[PointOfInterestComponent] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_stopping_place: List[VehicleStoppingPlace] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    boarding_position: List[BoardingPosition] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_space: List[AccessSpace] = field(
        default_factory=list,
        metadata={
            "name": "AccessSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    quay: List[Quay] = field(
        default_factory=list,
        metadata={
            "name": "Quay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place_space: List[StopPlaceSpace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place_component: List[StopPlaceComponent] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_space: List[PointOfInterestSpace] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_bay: List[ParkingBay] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_area: List[ParkingArea] = field(
        default_factory=list,
        metadata={
            "name": "ParkingArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_component: List[ParkingComponent] = field(
        default_factory=list,
        metadata={
            "name": "ParkingComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_stopping_position: List[VehicleStoppingPosition] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_vehicle_entrance: List[PointOfInterestVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_entrance: List[PointOfInterestEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_passenger_entrance: List[ParkingPassengerEntrance] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPassengerEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_entrance_for_vehicles: List[ParkingEntranceForVehicles] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place_vehicle_entrance: List[StopPlaceVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place_entrance: List[StopPlaceEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_entrance: List[VehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entrance: List[Entrance] = field(
        default_factory=list,
        metadata={
            "name": "Entrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_component: List[SiteComponent] = field(
        default_factory=list,
        metadata={
            "name": "SiteComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest: List[PointOfInterest] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking: List[Parking] = field(
        default_factory=list,
        metadata={
            "name": "Parking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place: List[StopPlace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_site: List[ServiceSite] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSite",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site: List[Site] = field(
        default_factory=list,
        metadata={
            "name": "Site",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_element: List[SiteElement] = field(
        default_factory=list,
        metadata={
            "name": "SiteElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    garage: List[Garage] = field(
        default_factory=list,
        metadata={
            "name": "Garage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    topographic_place: List[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    equipment_place: List[EquipmentPlace] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    country: List[Country] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    addressable_place: List[AddressablePlace] = field(
        default_factory=list,
        metadata={
            "name": "AddressablePlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    postal_address: List[PostalAddress] = field(
        default_factory=list,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    road_address: List[RoadAddress] = field(
        default_factory=list,
        metadata={
            "name": "RoadAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    place: List[Place] = field(
        default_factory=list,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transport_administrative_zone: List[TransportAdministrativeZone] = field(
        default_factory=list,
        metadata={
            "name": "TransportAdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    administrative_zone: List[AdministrativeZone1] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_administrative_zone: List[AdministrativeZone2] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_zone: List[FareZone] = field(
        default_factory=list,
        metadata={
            "name": "FareZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    tariff_zone: List[TariffZone1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_tariff_zone: List[TariffZone2] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    general_zone: List[GeneralZone] = field(
        default_factory=list,
        metadata={
            "name": "GeneralZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    zone: List[Zone] = field(
        default_factory=list,
        metadata={
            "name": "Zone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
