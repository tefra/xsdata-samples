from dataclasses import dataclass, field
from typing import List, Optional
from .access_space_ref import AccessSpaceRef
from .address_ref import AddressRef
from .addressable_place_ref import AddressablePlaceRef
from .boarding_position_ref import BoardingPositionRef
from .entrance_ref import EntranceRef
from .equipment_place_ref import EquipmentPlaceRef
from .equipment_position_ref import EquipmentPositionRef
from .flexible_area_ref import FlexibleAreaRef
from .flexible_quay_ref import FlexibleQuayRef
from .flexible_stop_place_ref import FlexibleStopPlaceRef
from .garage_ref import GarageRef
from .hail_and_ride_area_ref import HailAndRideAreaRef
from .network_ref import NetworkRef
from .object_filter_by_value_structure import ObjectFilterByValueStructure
from .parking_bay_ref import ParkingBayRef
from .parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from .parking_entrance_ref import ParkingEntranceRef
from .parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from .parking_ref import ParkingRef
from .path_junction_ref import PathJunctionRef
from .point_of_interest_entrance_ref import PointOfInterestEntranceRef
from .point_of_interest_ref import PointOfInterestRef
from .point_of_interest_space_ref import PointOfInterestSpaceRef
from .point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from .postal_address_ref import PostalAddressRef
from .quay_ref import QuayRef
from .road_address_ref import RoadAddressRef
from .service_site_ref import ServiceSiteRef
from .site_component_ref import SiteComponentRef
from .site_element_ref import SiteElementRef
from .site_ref import SiteRef
from .stop_place_entrance_ref import StopPlaceEntranceRef
from .stop_place_ref import StopPlaceRef
from .stop_place_space_ref import StopPlaceSpaceRef
from .stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from .topographic_place_ref import TopographicPlaceRef
from .vehicle_entrance_ref import VehicleEntranceRef
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkFilterByValueStructure(ObjectFilterByValueStructure):
    network_ref: Optional[NetworkRef] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    places: Optional["NetworkFilterByValueStructure.Places"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class Places:
        choice: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "HailAndRideAreaRef",
                        "type": HailAndRideAreaRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "FlexibleAreaRef",
                        "type": FlexibleAreaRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "FlexibleQuayRef",
                        "type": FlexibleQuayRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "FlexibleStopPlaceRef",
                        "type": FlexibleStopPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "PathJunctionRef",
                        "type": PathJunctionRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "TopographicPlaceRef",
                        "type": TopographicPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "EquipmentPlaceRef",
                        "type": EquipmentPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "EquipmentPositionRef",
                        "type": EquipmentPositionRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "VehicleStoppingPositionRef",
                        "type": VehicleStoppingPositionRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "VehicleStoppingPlaceRef",
                        "type": VehicleStoppingPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "BoardingPositionRef",
                        "type": BoardingPositionRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "AccessSpaceRef",
                        "type": AccessSpaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "QuayRef",
                        "type": QuayRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "StopPlaceSpaceRef",
                        "type": StopPlaceSpaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ParkingBayRef",
                        "type": ParkingBayRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "PointOfInterestSpaceRef",
                        "type": PointOfInterestSpaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "StopPlaceVehicleEntranceRef",
                        "type": StopPlaceVehicleEntranceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "StopPlaceEntranceRef",
                        "type": StopPlaceEntranceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ParkingEntranceForVehiclesRef",
                        "type": ParkingEntranceForVehiclesRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ParkingPassengerEntranceRef",
                        "type": ParkingPassengerEntranceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ParkingEntranceRef",
                        "type": ParkingEntranceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "PointOfInterestVehicleEntranceRef",
                        "type": PointOfInterestVehicleEntranceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "PointOfInterestEntranceRef",
                        "type": PointOfInterestEntranceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "VehicleEntranceRef",
                        "type": VehicleEntranceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "EntranceRef",
                        "type": EntranceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "SiteComponentRef",
                        "type": SiteComponentRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "StopPlaceRef",
                        "type": StopPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ParkingRef",
                        "type": ParkingRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "PointOfInterestRef",
                        "type": PointOfInterestRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ServiceSiteRef",
                        "type": ServiceSiteRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "SiteRef",
                        "type": SiteRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "SiteElementRef",
                        "type": SiteElementRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "GarageRef",
                        "type": GarageRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "AddressablePlaceRef",
                        "type": AddressablePlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "PostalAddressRef",
                        "type": PostalAddressRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "RoadAddressRef",
                        "type": RoadAddressRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "AddressRef",
                        "type": AddressRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            }
        )
