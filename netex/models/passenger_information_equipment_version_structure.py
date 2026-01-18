from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal

from .access_space_ref import AccessSpaceRef
from .accessibility_info_facility_list import AccessibilityInfoFacilityList
from .boarding_position_ref import BoardingPositionRef
from .entrance_ref import EntranceRef
from .logical_display_ref import LogicalDisplayRef
from .monitored_vehicle_sharing_parking_bay_ref import (
    MonitoredVehicleSharingParkingBayRef,
)
from .parking_area_ref import ParkingAreaRef
from .parking_bay_ref import ParkingBayRef
from .parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from .parking_entrance_ref import ParkingEntranceRef
from .parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)
from .passenger_information_equipment_enumeration import (
    PassengerInformationEquipmentEnumeration,
)
from .passenger_information_facility_list import (
    PassengerInformationFacilityList,
)
from .point_of_interest_entrance_ref import PointOfInterestEntranceRef
from .point_of_interest_space_ref import PointOfInterestSpaceRef
from .point_of_interest_vehicle_entrance_ref import (
    PointOfInterestVehicleEntranceRef,
)
from .quay_ref import QuayRef
from .site_component_ref import SiteComponentRef
from .stop_place_entrance_ref import StopPlaceEntranceRef
from .stop_place_ref import StopPlaceRef
from .stop_place_space_ref import StopPlaceSpaceRef
from .stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from .taxi_parking_area_ref import TaxiParkingAreaRef
from .taxi_rank_ref import TaxiRankRef
from .taxi_stand_ref import TaxiStandRef
from .type_of_passenger_information_equipment_ref import (
    TypeOfPassengerInformationEquipmentRef,
)
from .vehicle_entrance_ref import VehicleEntranceRef
from .vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from .vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from .vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from .vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerInformationEquipmentVersionStructure(
    PassengerEquipmentVersionStructure
):
    class Meta:
        name = "PassengerInformationEquipment_VersionStructure"

    logical_display_ref: LogicalDisplayRef | None = field(
        default=None,
        metadata={
            "name": "LogicalDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_place_ref: TaxiRankRef | StopPlaceRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice: (
        VehicleStoppingPositionRef
        | VehicleStoppingPlaceRef
        | BoardingPositionRef
        | AccessSpaceRef
        | TaxiStandRef
        | QuayRef
        | StopPlaceSpaceRef
        | VehiclePoolingParkingBayRef
        | MonitoredVehicleSharingParkingBayRef
        | VehicleSharingParkingBayRef
        | ParkingBayRef
        | VehiclePoolingParkingAreaRef
        | VehicleSharingParkingAreaRef
        | TaxiParkingAreaRef
        | ParkingAreaRef
        | PointOfInterestSpaceRef
        | StopPlaceVehicleEntranceRef
        | StopPlaceEntranceRef
        | ParkingEntranceForVehiclesRef
        | ParkingPassengerEntranceRef
        | ParkingEntranceRef
        | PointOfInterestVehicleEntranceRef
        | PointOfInterestEntranceRef
        | VehicleEntranceRef
        | EntranceRef
        | SiteComponentRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
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
                    "name": "VehiclePoolingParkingBayRef",
                    "type": VehiclePoolingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonitoredVehicleSharingParkingBayRef",
                    "type": MonitoredVehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingBayRef",
                    "type": VehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayRef",
                    "type": ParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingAreaRef",
                    "type": VehiclePoolingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingAreaRef",
                    "type": VehicleSharingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingAreaRef",
                    "type": TaxiParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
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
            ),
        },
    )
    passenger_information_equipment_list: Iterable[
        PassengerInformationEquipmentEnumeration
    ] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationEquipmentList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    type_of_passenger_information_equipment_ref: (
        TypeOfPassengerInformationEquipmentRef | None
    ) = field(
        default=None,
        metadata={
            "name": "TypeOfPassengerInformationEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    low_counter_access: bool | None = field(
        default=None,
        metadata={
            "name": "LowCounterAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_low_counter: Decimal | None = field(
        default=None,
        metadata={
            "name": "HeightOfLowCounter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    induction_loops: bool | None = field(
        default=None,
        metadata={
            "name": "InductionLoops",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_interface_available: bool | None = field(
        default=None,
        metadata={
            "name": "TactileInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_interface_available: bool | None = field(
        default=None,
        metadata={
            "name": "AudioInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    disabled_priority: bool | None = field(
        default=None,
        metadata={
            "name": "DisabledPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_suitable: bool | None = field(
        default=None,
        metadata={
            "name": "WheelchairSuitable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_information_facility_list: (
        PassengerInformationFacilityList | None
    ) = field(
        default=None,
        metadata={
            "name": "PassengerInformationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_info_facility_list: AccessibilityInfoFacilityList | None = (
        field(
            default=None,
            metadata={
                "name": "AccessibilityInfoFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
