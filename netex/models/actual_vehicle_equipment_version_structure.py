from dataclasses import dataclass, field
from typing import Optional, Union
from .access_equipment_ref import AccessEquipmentRef
from .access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from .accessibility_assessment import AccessibilityAssessment
from .activated_equipment_ref import ActivatedEquipmentRef
from .assistance_booking_service_ref import AssistanceBookingServiceRef
from .assistance_service_ref import AssistanceServiceRef
from .catering_service_ref import CateringServiceRef
from .communication_service_ref import CommunicationServiceRef
from .complaints_service_ref import ComplaintsServiceRef
from .compound_train_ref import CompoundTrainRef
from .crossing_equipment_ref import CrossingEquipmentRef
from .customer_service_ref import CustomerServiceRef
from .cycle_storage_equipment_ref import CycleStorageEquipmentRef
from .entrance_equipment_ref import EntranceEquipmentRef
from .equipment_ref import EquipmentRef
from .escalator_equipment_ref import EscalatorEquipmentRef
from .general_sign_ref import GeneralSignRef
from .heading_sign_ref import HeadingSignRef
from .help_point_equipment_ref import HelpPointEquipmentRef
from .hire_service_ref import HireServiceRef
from .left_luggage_service_ref import LeftLuggageServiceRef
from .lift_equipment_ref import LiftEquipmentRef
from .local_service_ref import LocalServiceRef
from .lost_property_service_ref import LostPropertyServiceRef
from .luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from .luggage_service_ref import LuggageServiceRef
from .meeting_point_service_ref import MeetingPointServiceRef
from .money_service_ref import MoneyServiceRef
from .passenger_equipment_ref import PassengerEquipmentRef
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)
from .passenger_information_equipment_ref import (
    PassengerInformationEquipmentRef,
)
from .passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from .place_lighting_equipment_ref import PlaceLightingEquipmentRef
from .place_sign_ref import PlaceSignRef
from .queueing_equipment_ref import QueueingEquipmentRef
from .ramp_equipment_ref import RampEquipmentRef
from .retail_device_ref import RetailDeviceRef
from .retail_service_ref import RetailServiceRef
from .rough_surface_ref import RoughSurfaceRef
from .rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from .sanitary_equipment_ref import SanitaryEquipmentRef
from .seating_equipment_ref import SeatingEquipmentRef
from .shelter_equipment_ref import ShelterEquipmentRef
from .sign_equipment_ref import SignEquipmentRef
from .site_equipment_ref import SiteEquipmentRef
from .staircase_equipment_ref import StaircaseEquipmentRef
from .ticket_validator_equipment_ref import TicketValidatorEquipmentRef
from .ticketing_equipment_ref import TicketingEquipmentRef
from .ticketing_service_ref import TicketingServiceRef
from .train_ref import TrainRef
from .travelator_equipment_ref import TravelatorEquipmentRef
from .trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from .vehicle_charging_equipment_ref import VehicleChargingEquipmentRef
from .vehicle_equipment_ref import VehicleEquipmentRef
from .vehicle_type_ref import VehicleTypeRef
from .waiting_equipment_ref import WaitingEquipmentRef
from .waiting_room_equipment_ref import WaitingRoomEquipmentRef
from .wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActualVehicleEquipmentVersionStructure(
    PassengerEquipmentVersionStructure
):
    class Meta:
        name = "ActualVehicleEquipment_VersionStructure"

    units: Optional[int] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[
        Union[CompoundTrainRef, TrainRef, VehicleTypeRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice: Optional[
        Union[
            RetailDeviceRef,
            AssistanceBookingServiceRef,
            CateringServiceRef,
            RetailServiceRef,
            MoneyServiceRef,
            HireServiceRef,
            CommunicationServiceRef,
            MeetingPointServiceRef,
            LeftLuggageServiceRef,
            LuggageServiceRef,
            LostPropertyServiceRef,
            ComplaintsServiceRef,
            CustomerServiceRef,
            AssistanceServiceRef,
            TicketingServiceRef,
            LocalServiceRef,
            VehicleChargingEquipmentRef,
            CycleStorageEquipmentRef,
            TicketValidatorEquipmentRef,
            TicketingEquipmentRef,
            TrolleyStandEquipmentRef,
            SeatingEquipmentRef,
            ShelterEquipmentRef,
            LuggageLockerEquipmentRef,
            WaitingRoomEquipmentRef,
            WaitingEquipmentRef,
            SiteEquipmentRef,
            HeadingSignRef,
            GeneralSignRef,
            PlaceSignRef,
            SignEquipmentRef,
            PlaceLightingEquipmentRef,
            RoughSurfaceRef,
            StaircaseEquipmentRef,
            QueueingEquipmentRef,
            TravelatorEquipmentRef,
            EscalatorEquipmentRef,
            LiftEquipmentRef,
            CrossingEquipmentRef,
            RampEquipmentRef,
            EntranceEquipmentRef,
            AccessEquipmentRef,
            ActivatedEquipmentRef,
            PassengerInformationEquipmentRef,
            RubbishDisposalEquipmentRef,
            HelpPointEquipmentRef,
            PassengerSafetyEquipmentRef,
            SanitaryEquipmentRef,
            WheelchairVehicleRef,
            AccessVehicleEquipmentRef,
            VehicleEquipmentRef,
            PassengerEquipmentRef,
            EquipmentRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailDeviceRef",
                    "type": RetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingServiceRef",
                    "type": AssistanceBookingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringServiceRef",
                    "type": CateringServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailServiceRef",
                    "type": RetailServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyServiceRef",
                    "type": MoneyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireServiceRef",
                    "type": HireServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationServiceRef",
                    "type": CommunicationServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointServiceRef",
                    "type": MeetingPointServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageServiceRef",
                    "type": LeftLuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageServiceRef",
                    "type": LuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyServiceRef",
                    "type": LostPropertyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsServiceRef",
                    "type": ComplaintsServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerServiceRef",
                    "type": CustomerServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceServiceRef",
                    "type": AssistanceServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingServiceRef",
                    "type": TicketingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LocalServiceRef",
                    "type": LocalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleChargingEquipmentRef",
                    "type": VehicleChargingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleStorageEquipmentRef",
                    "type": CycleStorageEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipmentRef",
                    "type": TicketValidatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipmentRef",
                    "type": TicketingEquipmentRef,
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
                    "name": "AccessEquipmentRef",
                    "type": AccessEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivatedEquipmentRef",
                    "type": ActivatedEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerInformationEquipmentRef",
                    "type": PassengerInformationEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipmentRef",
                    "type": RubbishDisposalEquipmentRef,
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
                    "name": "EquipmentRef",
                    "type": EquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
