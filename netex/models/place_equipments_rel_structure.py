from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .access_vehicle_equipment import AccessVehicleEquipment
from .access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from .battery_equipment import BatteryEquipment
from .containment_aggregation_structure import ContainmentAggregationStructure
from .crossing_equipment import CrossingEquipment
from .crossing_equipment_ref import CrossingEquipmentRef
from .cycle_storage_equipment import CycleStorageEquipment
from .cycle_storage_equipment_ref import CycleStorageEquipmentRef
from .entrance_equipment import EntranceEquipment
from .entrance_equipment_ref import EntranceEquipmentRef
from .escalator_equipment import EscalatorEquipment
from .escalator_equipment_ref import EscalatorEquipmentRef
from .general_sign import GeneralSign
from .general_sign_ref import GeneralSignRef
from .heading_sign import HeadingSign
from .heading_sign_ref import HeadingSignRef
from .help_point_equipment import HelpPointEquipment
from .help_point_equipment_ref import HelpPointEquipmentRef
from .lift_call_equipment import LiftCallEquipment
from .lift_call_equipment_ref import LiftCallEquipmentRef
from .lift_equipment import LiftEquipment
from .lift_equipment_ref import LiftEquipmentRef
from .luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from .passenger_beacon_equipment import PassengerBeaconEquipment
from .passenger_beacon_equipment_ref import PassengerBeaconEquipmentRef
from .passenger_equipment_ref import PassengerEquipmentRef
from .passenger_information_equipment import PassengerInformationEquipment
from .passenger_information_equipment_ref import (
    PassengerInformationEquipmentRef,
)
from .passenger_safety_equipment import PassengerSafetyEquipment
from .passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from .place_lighting import PlaceLighting
from .place_lighting_equipment_ref import PlaceLightingEquipmentRef
from .place_sign import PlaceSign
from .place_sign_ref import PlaceSignRef
from .queueing_equipment import QueueingEquipment
from .queueing_equipment_ref import QueueingEquipmentRef
from .ramp_equipment import RampEquipment
from .ramp_equipment_ref import RampEquipmentRef
from .refuelling_equipment import RefuellingEquipment
from .retail_device import RetailDevice
from .rough_surface import RoughSurface
from .rough_surface_ref import RoughSurfaceRef
from .rubbish_disposal_equipment import RubbishDisposalEquipment
from .rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from .sanitary_equipment import SanitaryEquipment
from .sanitary_equipment_ref import SanitaryEquipmentRef
from .seating_equipment import SeatingEquipment
from .seating_equipment_ref import SeatingEquipmentRef
from .shelter_equipment import ShelterEquipment
from .shelter_equipment_ref import ShelterEquipmentRef
from .sign_equipment import SignEquipment
from .sign_equipment_ref import SignEquipmentRef
from .site_equipment_ref import SiteEquipmentRef
from .staircase_equipment import StaircaseEquipment
from .staircase_equipment_ref import StaircaseEquipmentRef
from .ticket_validator_equipment import TicketValidatorEquipment
from .ticketing_equipment import TicketingEquipment
from .travelator_equipment import TravelatorEquipment
from .travelator_equipment_ref import TravelatorEquipmentRef
from .trolley_stand_equipment import TrolleyStandEquipment
from .trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from .vehicle_charging_equipment import VehicleChargingEquipment
from .vehicle_equipment_ref import VehicleEquipmentRef
from .vehicle_release_equipment import VehicleReleaseEquipment
from .waiting_equipment_ref import WaitingEquipmentRef
from .waiting_room_equipment import WaitingRoomEquipment
from .waiting_room_equipment_ref import WaitingRoomEquipmentRef
from .wheelchair_vehicle_equipment import WheelchairVehicleEquipment
from .wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceEquipmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "placeEquipments_RelStructure"

    choice: Iterable[
        PassengerInformationEquipmentRef | CycleStorageEquipmentRef | TrolleyStandEquipmentRef | SeatingEquipmentRef | ShelterEquipmentRef | LuggageLockerEquipmentRef | WaitingRoomEquipmentRef | WaitingEquipmentRef | SiteEquipmentRef | PlaceLightingEquipmentRef | RoughSurfaceRef | StaircaseEquipmentRef | QueueingEquipmentRef | TravelatorEquipmentRef | EscalatorEquipmentRef | LiftCallEquipmentRef | LiftEquipmentRef | CrossingEquipmentRef | RampEquipmentRef | EntranceEquipmentRef | HeadingSignRef | GeneralSignRef | PlaceSignRef | SignEquipmentRef | RubbishDisposalEquipmentRef | PassengerBeaconEquipmentRef | HelpPointEquipmentRef | PassengerSafetyEquipmentRef | SanitaryEquipmentRef | WheelchairVehicleRef | AccessVehicleEquipmentRef | VehicleEquipmentRef | PassengerEquipmentRef | RetailDevice | BatteryEquipment | VehicleReleaseEquipment | RefuellingEquipment | VehicleChargingEquipment | CycleStorageEquipment | SeatingEquipment | ShelterEquipment | TrolleyStandEquipment | WaitingRoomEquipment | CrossingEquipment | QueueingEquipment | EntranceEquipment | RampEquipment | LiftCallEquipment | LiftEquipment | TravelatorEquipment | StaircaseEquipment | EscalatorEquipment | PlaceLighting | RoughSurface | GeneralSign | HeadingSign | PlaceSign | SignEquipment | PassengerInformationEquipment | RubbishDisposalEquipment | PassengerBeaconEquipment | HelpPointEquipment | PassengerSafetyEquipment | SanitaryEquipment | TicketValidatorEquipment | TicketingEquipment | WheelchairVehicleEquipment | AccessVehicleEquipment
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerInformationEquipmentRef",
                    "type": PassengerInformationEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleStorageEquipmentRef",
                    "type": CycleStorageEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrolleyStandEquipmentRef",
                    "type": TrolleyStandEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeatingEquipmentRef",
                    "type": SeatingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ShelterEquipmentRef",
                    "type": ShelterEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageLockerEquipmentRef",
                    "type": LuggageLockerEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingRoomEquipmentRef",
                    "type": WaitingRoomEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingEquipmentRef",
                    "type": WaitingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteEquipmentRef",
                    "type": SiteEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLightingEquipmentRef",
                    "type": PlaceLightingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurfaceRef",
                    "type": RoughSurfaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipmentRef",
                    "type": StaircaseEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipmentRef",
                    "type": QueueingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipmentRef",
                    "type": TravelatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipmentRef",
                    "type": EscalatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftCallEquipmentRef",
                    "type": LiftCallEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipmentRef",
                    "type": LiftEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipmentRef",
                    "type": CrossingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipmentRef",
                    "type": RampEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipmentRef",
                    "type": EntranceEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSignRef",
                    "type": HeadingSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSignRef",
                    "type": GeneralSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSignRef",
                    "type": PlaceSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SignEquipmentRef",
                    "type": SignEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipmentRef",
                    "type": RubbishDisposalEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerBeaconEquipmentRef",
                    "type": PassengerBeaconEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipmentRef",
                    "type": HelpPointEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipmentRef",
                    "type": PassengerSafetyEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipmentRef",
                    "type": SanitaryEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleRef",
                    "type": WheelchairVehicleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessVehicleEquipmentRef",
                    "type": AccessVehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentRef",
                    "type": VehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerEquipmentRef",
                    "type": PassengerEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDevice",
                    "type": RetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BatteryEquipment",
                    "type": BatteryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleReleaseEquipment",
                    "type": VehicleReleaseEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefuellingEquipment",
                    "type": RefuellingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleChargingEquipment",
                    "type": VehicleChargingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleStorageEquipment",
                    "type": CycleStorageEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeatingEquipment",
                    "type": SeatingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ShelterEquipment",
                    "type": ShelterEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrolleyStandEquipment",
                    "type": TrolleyStandEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingRoomEquipment",
                    "type": WaitingRoomEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipment",
                    "type": CrossingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipment",
                    "type": QueueingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipment",
                    "type": EntranceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipment",
                    "type": RampEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftCallEquipment",
                    "type": LiftCallEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipment",
                    "type": LiftEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipment",
                    "type": TravelatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipment",
                    "type": StaircaseEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipment",
                    "type": EscalatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLighting",
                    "type": PlaceLighting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurface",
                    "type": RoughSurface,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSign",
                    "type": GeneralSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSign",
                    "type": HeadingSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSign",
                    "type": PlaceSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SignEquipment",
                    "type": SignEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerInformationEquipment",
                    "type": PassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipment",
                    "type": RubbishDisposalEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerBeaconEquipment",
                    "type": PassengerBeaconEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipment",
                    "type": HelpPointEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipment",
                    "type": PassengerSafetyEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipment",
                    "type": SanitaryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipment",
                    "type": TicketValidatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipment",
                    "type": TicketingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleEquipment",
                    "type": WheelchairVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessVehicleEquipment",
                    "type": AccessVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
