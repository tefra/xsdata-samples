from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .access_equipment_ref import AccessEquipmentRef
from .access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from .activated_equipment_ref import ActivatedEquipmentRef
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .assistance_booking_service_ref import AssistanceBookingServiceRef
from .assistance_service_ref import AssistanceServiceRef
from .catering_service_ref import CateringServiceRef
from .communication_service_ref import CommunicationServiceRef
from .complaints_service_ref import ComplaintsServiceRef
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
from .installed_equipment_ref import InstalledEquipmentRef
from .left_luggage_service_ref import LeftLuggageServiceRef
from .lift_equipment_ref import LiftEquipmentRef
from .local_service_ref import LocalServiceRef
from .location_structure_2 import LocationStructure2
from .lost_property_service_ref import LostPropertyServiceRef
from .luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from .luggage_service_ref import LuggageServiceRef
from .meeting_point_service_ref import MeetingPointServiceRef
from .money_service_ref import MoneyServiceRef
from .multilingual_string import MultilingualString
from .passenger_equipment_ref import PassengerEquipmentRef
from .passenger_information_equipment_ref import PassengerInformationEquipmentRef
from .passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from .place_lighting_equipment_ref import PlaceLightingEquipmentRef
from .place_sign_ref import PlaceSignRef
from .point_ref_structure import PointRefStructure
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
from .travelator_equipment_ref import TravelatorEquipmentRef
from .trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from .vehicle_charging_equipment_ref import VehicleChargingEquipmentRef
from .vehicle_equipment_ref import VehicleEquipmentRef
from .waiting_equipment_ref import WaitingEquipmentRef
from .waiting_room_equipment_ref import WaitingRoomEquipmentRef
from .wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentPositionStructure(DataManagedObjectStructure):
    retail_device_ref: Optional[RetailDeviceRef] = field(
        default=None,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    assistance_booking_service_ref: Optional[AssistanceBookingServiceRef] = field(
        default=None,
        metadata={
            "name": "AssistanceBookingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    catering_service_ref: Optional[CateringServiceRef] = field(
        default=None,
        metadata={
            "name": "CateringServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    retail_service_ref: Optional[RetailServiceRef] = field(
        default=None,
        metadata={
            "name": "RetailServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    money_service_ref: Optional[MoneyServiceRef] = field(
        default=None,
        metadata={
            "name": "MoneyServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    hire_service_ref: Optional[HireServiceRef] = field(
        default=None,
        metadata={
            "name": "HireServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    communication_service_ref: Optional[CommunicationServiceRef] = field(
        default=None,
        metadata={
            "name": "CommunicationServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    meeting_point_service_ref: Optional[MeetingPointServiceRef] = field(
        default=None,
        metadata={
            "name": "MeetingPointServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    left_luggage_service_ref: Optional[LeftLuggageServiceRef] = field(
        default=None,
        metadata={
            "name": "LeftLuggageServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    luggage_service_ref: Optional[LuggageServiceRef] = field(
        default=None,
        metadata={
            "name": "LuggageServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    lost_property_service_ref: Optional[LostPropertyServiceRef] = field(
        default=None,
        metadata={
            "name": "LostPropertyServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    complaints_service_ref: Optional[ComplaintsServiceRef] = field(
        default=None,
        metadata={
            "name": "ComplaintsServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    customer_service_ref: Optional[CustomerServiceRef] = field(
        default=None,
        metadata={
            "name": "CustomerServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    assistance_service_ref: Optional[AssistanceServiceRef] = field(
        default=None,
        metadata={
            "name": "AssistanceServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    ticketing_service_ref: Optional[TicketingServiceRef] = field(
        default=None,
        metadata={
            "name": "TicketingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    local_service_ref: Optional[LocalServiceRef] = field(
        default=None,
        metadata={
            "name": "LocalServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_charging_equipment_ref: Optional[VehicleChargingEquipmentRef] = field(
        default=None,
        metadata={
            "name": "VehicleChargingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    cycle_storage_equipment_ref: Optional[CycleStorageEquipmentRef] = field(
        default=None,
        metadata={
            "name": "CycleStorageEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    ticket_validator_equipment_ref: Optional[TicketValidatorEquipmentRef] = field(
        default=None,
        metadata={
            "name": "TicketValidatorEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    ticketing_equipment_ref: Optional[TicketingEquipmentRef] = field(
        default=None,
        metadata={
            "name": "TicketingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    trolley_stand_equipment_ref: Optional[TrolleyStandEquipmentRef] = field(
        default=None,
        metadata={
            "name": "TrolleyStandEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    seating_equipment_ref: Optional[SeatingEquipmentRef] = field(
        default=None,
        metadata={
            "name": "SeatingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    shelter_equipment_ref: Optional[ShelterEquipmentRef] = field(
        default=None,
        metadata={
            "name": "ShelterEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    luggage_locker_equipment_ref: Optional[LuggageLockerEquipmentRef] = field(
        default=None,
        metadata={
            "name": "LuggageLockerEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    waiting_room_equipment_ref: Optional[WaitingRoomEquipmentRef] = field(
        default=None,
        metadata={
            "name": "WaitingRoomEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    waiting_equipment_ref: Optional[WaitingEquipmentRef] = field(
        default=None,
        metadata={
            "name": "WaitingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    site_equipment_ref: Optional[SiteEquipmentRef] = field(
        default=None,
        metadata={
            "name": "SiteEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    heading_sign_ref: Optional[HeadingSignRef] = field(
        default=None,
        metadata={
            "name": "HeadingSignRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    general_sign_ref: Optional[GeneralSignRef] = field(
        default=None,
        metadata={
            "name": "GeneralSignRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    place_sign_ref: Optional[PlaceSignRef] = field(
        default=None,
        metadata={
            "name": "PlaceSignRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    sign_equipment_ref: Optional[SignEquipmentRef] = field(
        default=None,
        metadata={
            "name": "SignEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    place_lighting_equipment_ref: Optional[PlaceLightingEquipmentRef] = field(
        default=None,
        metadata={
            "name": "PlaceLightingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    rough_surface_ref: Optional[RoughSurfaceRef] = field(
        default=None,
        metadata={
            "name": "RoughSurfaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    staircase_equipment_ref: Optional[StaircaseEquipmentRef] = field(
        default=None,
        metadata={
            "name": "StaircaseEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    queueing_equipment_ref: Optional[QueueingEquipmentRef] = field(
        default=None,
        metadata={
            "name": "QueueingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    travelator_equipment_ref: Optional[TravelatorEquipmentRef] = field(
        default=None,
        metadata={
            "name": "TravelatorEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    escalator_equipment_ref: Optional[EscalatorEquipmentRef] = field(
        default=None,
        metadata={
            "name": "EscalatorEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    lift_equipment_ref: Optional[LiftEquipmentRef] = field(
        default=None,
        metadata={
            "name": "LiftEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    crossing_equipment_ref: Optional[CrossingEquipmentRef] = field(
        default=None,
        metadata={
            "name": "CrossingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    ramp_equipment_ref: Optional[RampEquipmentRef] = field(
        default=None,
        metadata={
            "name": "RampEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    entrance_equipment_ref: Optional[EntranceEquipmentRef] = field(
        default=None,
        metadata={
            "name": "EntranceEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    access_equipment_ref: Optional[AccessEquipmentRef] = field(
        default=None,
        metadata={
            "name": "AccessEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    activated_equipment_ref: Optional[ActivatedEquipmentRef] = field(
        default=None,
        metadata={
            "name": "ActivatedEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    passenger_information_equipment_ref: Optional[PassengerInformationEquipmentRef] = field(
        default=None,
        metadata={
            "name": "PassengerInformationEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    rubbish_disposal_equipment_ref: Optional[RubbishDisposalEquipmentRef] = field(
        default=None,
        metadata={
            "name": "RubbishDisposalEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    help_point_equipment_ref: Optional[HelpPointEquipmentRef] = field(
        default=None,
        metadata={
            "name": "HelpPointEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    passenger_safety_equipment_ref: Optional[PassengerSafetyEquipmentRef] = field(
        default=None,
        metadata={
            "name": "PassengerSafetyEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    sanitary_equipment_ref: Optional[SanitaryEquipmentRef] = field(
        default=None,
        metadata={
            "name": "SanitaryEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    wheelchair_vehicle_ref: Optional[WheelchairVehicleRef] = field(
        default=None,
        metadata={
            "name": "WheelchairVehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    access_vehicle_equipment_ref: Optional[AccessVehicleEquipmentRef] = field(
        default=None,
        metadata={
            "name": "AccessVehicleEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_equipment_ref: Optional[VehicleEquipmentRef] = field(
        default=None,
        metadata={
            "name": "VehicleEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    passenger_equipment_ref: Optional[PassengerEquipmentRef] = field(
        default=None,
        metadata={
            "name": "PassengerEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    installed_equipment_ref: Optional[InstalledEquipmentRef] = field(
        default=None,
        metadata={
            "name": "InstalledEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    equipment_ref: Optional[EquipmentRef] = field(
        default=None,
        metadata={
            "name": "EquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    location: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reference_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "ReferencePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    xoffset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    yoffset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "YOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
