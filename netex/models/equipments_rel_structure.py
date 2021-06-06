from dataclasses import dataclass, field
from typing import List
from .access_equipment import AccessEquipment
from .access_equipment_ref import AccessEquipmentRef
from .access_vehicle_equipment import AccessVehicleEquipment
from .access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from .activated_equipment_ref import ActivatedEquipmentRef
from .actual_vehicle_equipment import ActualVehicleEquipment
from .assistance_booking_service import AssistanceBookingService
from .assistance_booking_service_ref import AssistanceBookingServiceRef
from .assistance_service import AssistanceService
from .assistance_service_ref import AssistanceServiceRef
from .catering_service import CateringService
from .catering_service_ref import CateringServiceRef
from .communication_service import CommunicationService
from .communication_service_ref import CommunicationServiceRef
from .complaints_service import ComplaintsService
from .complaints_service_ref import ComplaintsServiceRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .crossing_equipment import CrossingEquipment
from .crossing_equipment_ref import CrossingEquipmentRef
from .customer_service import CustomerService
from .customer_service_ref import CustomerServiceRef
from .cycle_storage_equipment import CycleStorageEquipment
from .cycle_storage_equipment_ref import CycleStorageEquipmentRef
from .entrance_equipment import EntranceEquipment
from .entrance_equipment_ref import EntranceEquipmentRef
from .equipment import Equipment
from .equipment_ref import EquipmentRef
from .escalator_equipment import EscalatorEquipment
from .escalator_equipment_ref import EscalatorEquipmentRef
from .general_sign import GeneralSign
from .general_sign_ref import GeneralSignRef
from .heading_sign import HeadingSign
from .heading_sign_ref import HeadingSignRef
from .help_point_equipment import HelpPointEquipment
from .help_point_equipment_ref import HelpPointEquipmentRef
from .hire_service import HireService
from .hire_service_ref import HireServiceRef
from .installed_equipment import InstalledEquipment
from .installed_equipment_ref import InstalledEquipmentRef
from .left_luggage_service import LeftLuggageService
from .left_luggage_service_ref import LeftLuggageServiceRef
from .lift_equipment import LiftEquipment
from .lift_equipment_ref import LiftEquipmentRef
from .local_service import LocalService
from .local_service_ref import LocalServiceRef
from .lost_property_service import LostPropertyService
from .lost_property_service_ref import LostPropertyServiceRef
from .luggage_locker_equipment import LuggageLockerEquipment
from .luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from .luggage_service import LuggageService
from .luggage_service_ref import LuggageServiceRef
from .meeting_point_service import MeetingPointService
from .meeting_point_service_ref import MeetingPointServiceRef
from .money_service import MoneyService
from .money_service_ref import MoneyServiceRef
from .passenger_equipment import PassengerEquipment
from .passenger_equipment_ref import PassengerEquipmentRef
from .passenger_information_equipment import PassengerInformationEquipment
from .passenger_information_equipment_ref import PassengerInformationEquipmentRef
from .passenger_safety_equipment import PassengerSafetyEquipment
from .passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from .place_equipment import PlaceEquipment
from .place_lighting import PlaceLighting
from .place_lighting_equipment_ref import PlaceLightingEquipmentRef
from .place_sign import PlaceSign
from .place_sign_ref import PlaceSignRef
from .queueing_equipment import QueueingEquipment
from .queueing_equipment_ref import QueueingEquipmentRef
from .ramp_equipment import RampEquipment
from .ramp_equipment_ref import RampEquipmentRef
from .retail_device import RetailDevice
from .retail_device_ref import RetailDeviceRef
from .retail_service import RetailService
from .retail_service_ref import RetailServiceRef
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
from .site_equipment import SiteEquipment
from .site_equipment_ref import SiteEquipmentRef
from .stair_equipment import StairEquipment
from .staircase_equipment import StaircaseEquipment
from .staircase_equipment_ref import StaircaseEquipmentRef
from .ticket_validator_equipment import TicketValidatorEquipment
from .ticket_validator_equipment_ref import TicketValidatorEquipmentRef
from .ticketing_equipment import TicketingEquipment
from .ticketing_equipment_ref import TicketingEquipmentRef
from .ticketing_service import TicketingService
from .ticketing_service_ref import TicketingServiceRef
from .travelator_equipment import TravelatorEquipment
from .travelator_equipment_ref import TravelatorEquipmentRef
from .trolley_stand_equipment import TrolleyStandEquipment
from .trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from .vehicle_charging_equipment import VehicleChargingEquipment
from .vehicle_charging_equipment_ref import VehicleChargingEquipmentRef
from .vehicle_equipment_ref import VehicleEquipmentRef
from .waiting_equipment import WaitingEquipment
from .waiting_equipment_ref import WaitingEquipmentRef
from .waiting_room_equipment import WaitingRoomEquipment
from .waiting_room_equipment_ref import WaitingRoomEquipmentRef
from .wheelchair_vehicle_equipment import WheelchairVehicleEquipment
from .wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "equipments_RelStructure"

    retail_device_ref: List[RetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    assistance_booking_service_ref: List[AssistanceBookingServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceBookingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    catering_service_ref: List[CateringServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "CateringServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_service_ref: List[RetailServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    money_service_ref: List[MoneyServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "MoneyServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hire_service_ref: List[HireServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "HireServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    communication_service_ref: List[CommunicationServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "CommunicationServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    meeting_point_service_ref: List[MeetingPointServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "MeetingPointServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    left_luggage_service_ref: List[LeftLuggageServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LeftLuggageServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_service_ref: List[LuggageServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LuggageServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lost_property_service_ref: List[LostPropertyServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LostPropertyServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complaints_service_ref: List[ComplaintsServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "ComplaintsServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_service_ref: List[CustomerServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    assistance_service_ref: List[AssistanceServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_service_ref: List[TicketingServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    local_service_ref: List[LocalServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LocalServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_charging_equipment_ref: List[VehicleChargingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleChargingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cycle_storage_equipment_ref: List[CycleStorageEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "CycleStorageEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticket_validator_equipment_ref: List[TicketValidatorEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketValidatorEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_equipment_ref: List[TicketingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trolley_stand_equipment_ref: List[TrolleyStandEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TrolleyStandEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    seating_equipment_ref: List[SeatingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SeatingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    shelter_equipment_ref: List[ShelterEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "ShelterEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_locker_equipment_ref: List[LuggageLockerEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "LuggageLockerEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    waiting_room_equipment_ref: List[WaitingRoomEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "WaitingRoomEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    waiting_equipment_ref: List[WaitingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "WaitingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_equipment_ref: List[SiteEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    heading_sign_ref: List[HeadingSignRef] = field(
        default_factory=list,
        metadata={
            "name": "HeadingSignRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_sign_ref: List[GeneralSignRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSignRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_sign_ref: List[PlaceSignRef] = field(
        default_factory=list,
        metadata={
            "name": "PlaceSignRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sign_equipment_ref: List[SignEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SignEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_lighting_equipment_ref: List[PlaceLightingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PlaceLightingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rough_surface_ref: List[RoughSurfaceRef] = field(
        default_factory=list,
        metadata={
            "name": "RoughSurfaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    staircase_equipment_ref: List[StaircaseEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "StaircaseEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    queueing_equipment_ref: List[QueueingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "QueueingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travelator_equipment_ref: List[TravelatorEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelatorEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    escalator_equipment_ref: List[EscalatorEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "EscalatorEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lift_equipment_ref: List[LiftEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "LiftEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crossing_equipment_ref: List[CrossingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "CrossingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ramp_equipment_ref: List[RampEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "RampEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_equipment_ref: List[EntranceEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "EntranceEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_equipment_ref: List[AccessEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activated_equipment_ref: List[ActivatedEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "ActivatedEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_information_equipment_ref: List[PassengerInformationEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rubbish_disposal_equipment_ref: List[RubbishDisposalEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "RubbishDisposalEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    help_point_equipment_ref: List[HelpPointEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "HelpPointEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_safety_equipment_ref: List[PassengerSafetyEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSafetyEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sanitary_equipment_ref: List[SanitaryEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_vehicle_ref: List[WheelchairVehicleRef] = field(
        default_factory=list,
        metadata={
            "name": "WheelchairVehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_vehicle_equipment_ref: List[AccessVehicleEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessVehicleEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_equipment_ref: List[VehicleEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_equipment_ref: List[PassengerEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    installed_equipment_ref: List[InstalledEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "InstalledEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_ref: List[EquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    assistance_booking_service: List[AssistanceBookingService] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceBookingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    catering_service: List[CateringService] = field(
        default_factory=list,
        metadata={
            "name": "CateringService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_service: List[RetailService] = field(
        default_factory=list,
        metadata={
            "name": "RetailService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    money_service: List[MoneyService] = field(
        default_factory=list,
        metadata={
            "name": "MoneyService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hire_service: List[HireService] = field(
        default_factory=list,
        metadata={
            "name": "HireService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    communication_service: List[CommunicationService] = field(
        default_factory=list,
        metadata={
            "name": "CommunicationService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    meeting_point_service: List[MeetingPointService] = field(
        default_factory=list,
        metadata={
            "name": "MeetingPointService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lost_property_service: List[LostPropertyService] = field(
        default_factory=list,
        metadata={
            "name": "LostPropertyService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    left_luggage_service: List[LeftLuggageService] = field(
        default_factory=list,
        metadata={
            "name": "LeftLuggageService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complaints_service: List[ComplaintsService] = field(
        default_factory=list,
        metadata={
            "name": "ComplaintsService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_service: List[CustomerService] = field(
        default_factory=list,
        metadata={
            "name": "CustomerService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_service: List[LuggageService] = field(
        default_factory=list,
        metadata={
            "name": "LuggageService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    assistance_service: List[AssistanceService] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_service: List[TicketingService] = field(
        default_factory=list,
        metadata={
            "name": "TicketingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    local_service: List[LocalService] = field(
        default_factory=list,
        metadata={
            "name": "LocalService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_device: List[RetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "RetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticket_validator_equipment: List[TicketValidatorEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TicketValidatorEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_equipment: List[TicketingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TicketingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    seating_equipment: List[SeatingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SeatingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    shelter_equipment: List[ShelterEquipment] = field(
        default_factory=list,
        metadata={
            "name": "ShelterEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trolley_stand_equipment: List[TrolleyStandEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TrolleyStandEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    waiting_room_equipment: List[WaitingRoomEquipment] = field(
        default_factory=list,
        metadata={
            "name": "WaitingRoomEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    waiting_equipment: List[WaitingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "WaitingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_locker_equipment: List[LuggageLockerEquipment] = field(
        default_factory=list,
        metadata={
            "name": "LuggageLockerEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_equipment: List[SiteEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SiteEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crossing_equipment: List[CrossingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "CrossingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    queueing_equipment: List[QueueingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "QueueingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_equipment: List[EntranceEquipment] = field(
        default_factory=list,
        metadata={
            "name": "EntranceEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ramp_equipment: List[RampEquipment] = field(
        default_factory=list,
        metadata={
            "name": "RampEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lift_equipment: List[LiftEquipment] = field(
        default_factory=list,
        metadata={
            "name": "LiftEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travelator_equipment: List[TravelatorEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TravelatorEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    staircase_equipment: List[StaircaseEquipment] = field(
        default_factory=list,
        metadata={
            "name": "StaircaseEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    escalator_equipment: List[EscalatorEquipment] = field(
        default_factory=list,
        metadata={
            "name": "EscalatorEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stair_equipment: List[StairEquipment] = field(
        default_factory=list,
        metadata={
            "name": "StairEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_lighting: List[PlaceLighting] = field(
        default_factory=list,
        metadata={
            "name": "PlaceLighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rough_surface: List[RoughSurface] = field(
        default_factory=list,
        metadata={
            "name": "RoughSurface",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_equipment: List[AccessEquipment] = field(
        default_factory=list,
        metadata={
            "name": "AccessEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_sign: List[GeneralSign] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    heading_sign: List[HeadingSign] = field(
        default_factory=list,
        metadata={
            "name": "HeadingSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_sign: List[PlaceSign] = field(
        default_factory=list,
        metadata={
            "name": "PlaceSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sign_equipment: List[SignEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SignEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_vehicle_equipment: List[WheelchairVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "WheelchairVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_vehicle_equipment: List[AccessVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "AccessVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_charging_equipment: List[VehicleChargingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleChargingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cycle_storage_equipment: List[CycleStorageEquipment] = field(
        default_factory=list,
        metadata={
            "name": "CycleStorageEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_equipment: List[PlaceEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PlaceEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_information_equipment: List[PassengerInformationEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rubbish_disposal_equipment: List[RubbishDisposalEquipment] = field(
        default_factory=list,
        metadata={
            "name": "RubbishDisposalEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    help_point_equipment: List[HelpPointEquipment] = field(
        default_factory=list,
        metadata={
            "name": "HelpPointEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_safety_equipment: List[PassengerSafetyEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSafetyEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sanitary_equipment: List[SanitaryEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    actual_vehicle_equipment: List[ActualVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "ActualVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_equipment: List[PassengerEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    installed_equipment: List[InstalledEquipment] = field(
        default_factory=list,
        metadata={
            "name": "InstalledEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment: List[Equipment] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
