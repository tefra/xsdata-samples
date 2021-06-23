from dataclasses import dataclass, field
from typing import List, Optional
from .access_space_ref import AccessSpaceRef
from .accessibility_info_facility_enumeration import AccessibilityInfoFacilityEnumeration
from .boarding_position_ref import BoardingPositionRef
from .entrance_ref import EntranceRef
from .logical_display_ref import LogicalDisplayRef
from .parking_bay_ref import ParkingBayRef
from .parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from .parking_entrance_ref import ParkingEntranceRef
from .parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from .passenger_equipment_version_structure import PassengerEquipmentVersionStructure
from .passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from .point_of_interest_entrance_ref import PointOfInterestEntranceRef
from .point_of_interest_space_ref import PointOfInterestSpaceRef
from .point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from .quay_ref import QuayRef
from .site_component_ref import SiteComponentRef
from .stop_place_entrance_ref import StopPlaceEntranceRef
from .stop_place_ref import StopPlaceRef
from .stop_place_space_ref import StopPlaceSpaceRef
from .stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from .type_of_passenger_information_equipment_ref import TypeOfPassengerInformationEquipmentRef
from .vehicle_entrance_ref import VehicleEntranceRef
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerInformationEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    class Meta:
        name = "PassengerInformationEquipment_VersionStructure"

    logical_display_ref: Optional[LogicalDisplayRef] = field(
        default=None,
        metadata={
            "name": "LogicalDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_position_ref: Optional[VehicleStoppingPositionRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_place_ref: Optional[VehicleStoppingPlaceRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_space_ref: Optional[AccessSpaceRef] = field(
        default=None,
        metadata={
            "name": "AccessSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_ref: Optional[QuayRef] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_space_ref: Optional[StopPlaceSpaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_bay_ref: Optional[ParkingBayRef] = field(
        default=None,
        metadata={
            "name": "ParkingBayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_space_ref: Optional[PointOfInterestSpaceRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_vehicle_entrance_ref: Optional[StopPlaceVehicleEntranceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_entrance_ref: Optional[StopPlaceEntranceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_for_vehicles_ref: Optional[ParkingEntranceForVehiclesRef] = field(
        default=None,
        metadata={
            "name": "ParkingEntranceForVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_passenger_entrance_ref: Optional[ParkingPassengerEntranceRef] = field(
        default=None,
        metadata={
            "name": "ParkingPassengerEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_ref: Optional[ParkingEntranceRef] = field(
        default=None,
        metadata={
            "name": "ParkingEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_vehicle_entrance_ref: Optional[PointOfInterestVehicleEntranceRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_entrance_ref: Optional[PointOfInterestEntranceRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_entrance_ref: Optional[VehicleEntranceRef] = field(
        default=None,
        metadata={
            "name": "VehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_ref: Optional[EntranceRef] = field(
        default=None,
        metadata={
            "name": "EntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_component_ref: Optional[SiteComponentRef] = field(
        default=None,
        metadata={
            "name": "SiteComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_passenger_information_equipment_ref: Optional[TypeOfPassengerInformationEquipmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPassengerInformationEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_information_facility_list: List[PassengerInformationFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    accessibility_info_facility_list: List[AccessibilityInfoFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityInfoFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
