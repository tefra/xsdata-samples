from dataclasses import dataclass, field
from typing import List, Union
from .access_space import AccessSpace
from .access_zone import AccessZone
from .addressable_place import AddressablePlace
from .administrative_zone_version_structure import (
    AdministrativeZone,
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
from .mobility_service_constraint_zone import MobilityServiceConstraintZone
from .monitored_vehicle_sharing_parking_bay import (
    MonitoredVehicleSharingParkingBay,
)
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
from .tariff_zone import TariffZone
from .taxi_parking_area import TaxiParkingArea
from .taxi_rank import TaxiRank
from .taxi_stand import TaxiStand
from .topographic_place import TopographicPlace
from .vehicle_meeting_place_1 import VehicleMeetingPlace1
from .vehicle_meeting_place_2 import VehicleMeetingPlace2
from .vehicle_pooling_meeting_place import VehiclePoolingMeetingPlace
from .vehicle_pooling_parking_area import VehiclePoolingParkingArea
from .vehicle_pooling_parking_bay import VehiclePoolingParkingBay
from .vehicle_sharing_parking_area import VehicleSharingParkingArea
from .vehicle_sharing_parking_bay import VehicleSharingParkingBay
from .vehicle_stopping_place import VehicleStoppingPlace
from .vehicle_stopping_position import VehicleStoppingPosition
from .zone import Zone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZonesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "zonesInFrame_RelStructure"

    choice: List[
        Union[
            MobilityServiceConstraintZone,
            RoutingConstraintZone,
            StopArea,
            AccessZone,
            VehicleMeetingPlace1,
            VehiclePoolingMeetingPlace,
            VehicleMeetingPlace2,
            HailAndRideArea,
            FlexibleArea,
            FlexibleQuay,
            FlexibleStopPlace,
            Garage,
            EquipmentPlace,
            TaxiStand,
            VehicleStoppingPlace,
            BoardingPosition,
            AccessSpace,
            Quay,
            PointOfInterestSpace,
            ParkingComponent,
            VehicleStoppingPosition,
            VehiclePoolingParkingArea,
            VehicleSharingParkingArea,
            TaxiParkingArea,
            ParkingArea,
            MonitoredVehicleSharingParkingBay,
            VehiclePoolingParkingBay,
            VehicleSharingParkingBay,
            ParkingBay,
            PointOfInterestVehicleEntrance,
            PointOfInterestEntrance,
            ParkingPassengerEntrance,
            ParkingEntranceForVehicles,
            StopPlaceVehicleEntrance,
            StopPlaceEntrance,
            Entrance,
            PointOfInterest,
            Parking,
            TaxiRank,
            StopPlace,
            ServiceSite,
            TopographicPlace,
            Country,
            AddressablePlace,
            PostalAddress,
            RoadAddress,
            TransportAdministrativeZone,
            AdministrativeZone,
            FareZone,
            TariffZone,
            GeneralZone,
            Zone,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityServiceConstraintZone",
                    "type": MobilityServiceConstraintZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingConstraintZone",
                    "type": RoutingConstraintZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopArea",
                    "type": StopArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZone",
                    "type": AccessZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPlace",
                    "type": VehicleMeetingPlace1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingMeetingPlace",
                    "type": VehiclePoolingMeetingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPlace_",
                    "type": VehicleMeetingPlace2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HailAndRideArea",
                    "type": HailAndRideArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleArea",
                    "type": FlexibleArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuay",
                    "type": FlexibleQuay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopPlace",
                    "type": FlexibleStopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Garage",
                    "type": Garage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPlace",
                    "type": EquipmentPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiStand",
                    "type": TaxiStand,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPlace",
                    "type": VehicleStoppingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPosition",
                    "type": BoardingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpace",
                    "type": AccessSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Quay",
                    "type": Quay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpace",
                    "type": PointOfInterestSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingComponent",
                    "type": ParkingComponent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPosition",
                    "type": VehicleStoppingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingArea",
                    "type": VehiclePoolingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingArea",
                    "type": VehicleSharingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingArea",
                    "type": TaxiParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingArea",
                    "type": ParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonitoredVehicleSharingParkingBay",
                    "type": MonitoredVehicleSharingParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingBay",
                    "type": VehiclePoolingParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingBay",
                    "type": VehicleSharingParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBay",
                    "type": ParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestVehicleEntrance",
                    "type": PointOfInterestVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntrance",
                    "type": PointOfInterestEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPassengerEntrance",
                    "type": ParkingPassengerEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehicles",
                    "type": ParkingEntranceForVehicles,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceVehicleEntrance",
                    "type": StopPlaceVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceEntrance",
                    "type": StopPlaceEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Entrance",
                    "type": Entrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterest",
                    "type": PointOfInterest,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Parking",
                    "type": Parking,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiRank",
                    "type": TaxiRank,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlace",
                    "type": StopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSite",
                    "type": ServiceSite,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlace",
                    "type": TopographicPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Country",
                    "type": Country,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressablePlace",
                    "type": AddressablePlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZone",
                    "type": TransportAdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZone",
                    "type": AdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZone",
                    "type": FareZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZone",
                    "type": TariffZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralZone",
                    "type": GeneralZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Zone",
                    "type": Zone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
