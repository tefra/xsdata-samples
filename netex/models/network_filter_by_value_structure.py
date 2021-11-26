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
        hail_and_ride_area_ref: List[HailAndRideAreaRef] = field(
            default_factory=list,
            metadata={
                "name": "HailAndRideAreaRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        flexible_area_ref: List[FlexibleAreaRef] = field(
            default_factory=list,
            metadata={
                "name": "FlexibleAreaRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        flexible_quay_ref: List[FlexibleQuayRef] = field(
            default_factory=list,
            metadata={
                "name": "FlexibleQuayRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        flexible_stop_place_ref: List[FlexibleStopPlaceRef] = field(
            default_factory=list,
            metadata={
                "name": "FlexibleStopPlaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        path_junction_ref: List[PathJunctionRef] = field(
            default_factory=list,
            metadata={
                "name": "PathJunctionRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        topographic_place_ref: List[TopographicPlaceRef] = field(
            default_factory=list,
            metadata={
                "name": "TopographicPlaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        equipment_place_ref: List[EquipmentPlaceRef] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentPlaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        equipment_position_ref: List[EquipmentPositionRef] = field(
            default_factory=list,
            metadata={
                "name": "EquipmentPositionRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        vehicle_stopping_position_ref: List[VehicleStoppingPositionRef] = field(
            default_factory=list,
            metadata={
                "name": "VehicleStoppingPositionRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        vehicle_stopping_place_ref: List[VehicleStoppingPlaceRef] = field(
            default_factory=list,
            metadata={
                "name": "VehicleStoppingPlaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        boarding_position_ref: List[BoardingPositionRef] = field(
            default_factory=list,
            metadata={
                "name": "BoardingPositionRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        access_space_ref: List[AccessSpaceRef] = field(
            default_factory=list,
            metadata={
                "name": "AccessSpaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        quay_ref: List[QuayRef] = field(
            default_factory=list,
            metadata={
                "name": "QuayRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        stop_place_space_ref: List[StopPlaceSpaceRef] = field(
            default_factory=list,
            metadata={
                "name": "StopPlaceSpaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        parking_bay_ref: List[ParkingBayRef] = field(
            default_factory=list,
            metadata={
                "name": "ParkingBayRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        point_of_interest_space_ref: List[PointOfInterestSpaceRef] = field(
            default_factory=list,
            metadata={
                "name": "PointOfInterestSpaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        stop_place_vehicle_entrance_ref: List[StopPlaceVehicleEntranceRef] = field(
            default_factory=list,
            metadata={
                "name": "StopPlaceVehicleEntranceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        stop_place_entrance_ref: List[StopPlaceEntranceRef] = field(
            default_factory=list,
            metadata={
                "name": "StopPlaceEntranceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        parking_entrance_for_vehicles_ref: List[ParkingEntranceForVehiclesRef] = field(
            default_factory=list,
            metadata={
                "name": "ParkingEntranceForVehiclesRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        parking_passenger_entrance_ref: List[ParkingPassengerEntranceRef] = field(
            default_factory=list,
            metadata={
                "name": "ParkingPassengerEntranceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        parking_entrance_ref: List[ParkingEntranceRef] = field(
            default_factory=list,
            metadata={
                "name": "ParkingEntranceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        point_of_interest_vehicle_entrance_ref: List[PointOfInterestVehicleEntranceRef] = field(
            default_factory=list,
            metadata={
                "name": "PointOfInterestVehicleEntranceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        point_of_interest_entrance_ref: List[PointOfInterestEntranceRef] = field(
            default_factory=list,
            metadata={
                "name": "PointOfInterestEntranceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        vehicle_entrance_ref: List[VehicleEntranceRef] = field(
            default_factory=list,
            metadata={
                "name": "VehicleEntranceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        entrance_ref: List[EntranceRef] = field(
            default_factory=list,
            metadata={
                "name": "EntranceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        site_component_ref: List[SiteComponentRef] = field(
            default_factory=list,
            metadata={
                "name": "SiteComponentRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        stop_place_ref: List[StopPlaceRef] = field(
            default_factory=list,
            metadata={
                "name": "StopPlaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        parking_ref: List[ParkingRef] = field(
            default_factory=list,
            metadata={
                "name": "ParkingRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        point_of_interest_ref: List[PointOfInterestRef] = field(
            default_factory=list,
            metadata={
                "name": "PointOfInterestRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        service_site_ref: List[ServiceSiteRef] = field(
            default_factory=list,
            metadata={
                "name": "ServiceSiteRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        site_ref: List[SiteRef] = field(
            default_factory=list,
            metadata={
                "name": "SiteRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        site_element_ref: List[SiteElementRef] = field(
            default_factory=list,
            metadata={
                "name": "SiteElementRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        garage_ref: List[GarageRef] = field(
            default_factory=list,
            metadata={
                "name": "GarageRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        addressable_place_ref: List[AddressablePlaceRef] = field(
            default_factory=list,
            metadata={
                "name": "AddressablePlaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        postal_address_ref: List[PostalAddressRef] = field(
            default_factory=list,
            metadata={
                "name": "PostalAddressRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        road_address_ref: List[RoadAddressRef] = field(
            default_factory=list,
            metadata={
                "name": "RoadAddressRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        address_ref: List[AddressRef] = field(
            default_factory=list,
            metadata={
                "name": "AddressRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
