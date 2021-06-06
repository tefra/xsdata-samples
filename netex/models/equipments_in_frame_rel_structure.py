from dataclasses import dataclass, field
from typing import List
from .access_equipment import AccessEquipment
from .access_vehicle_equipment import AccessVehicleEquipment
from .actual_vehicle_equipment import ActualVehicleEquipment
from .assistance_booking_service import AssistanceBookingService
from .assistance_service import AssistanceService
from .catering_service import CateringService
from .communication_service import CommunicationService
from .complaints_service import ComplaintsService
from .containment_aggregation_structure import ContainmentAggregationStructure
from .crossing_equipment import CrossingEquipment
from .customer_service import CustomerService
from .cycle_storage_equipment import CycleStorageEquipment
from .entrance_equipment import EntranceEquipment
from .equipment import Equipment
from .escalator_equipment import EscalatorEquipment
from .general_sign import GeneralSign
from .heading_sign import HeadingSign
from .help_point_equipment import HelpPointEquipment
from .hire_service import HireService
from .installed_equipment import InstalledEquipment
from .left_luggage_service import LeftLuggageService
from .lift_equipment import LiftEquipment
from .local_service import LocalService
from .lost_property_service import LostPropertyService
from .luggage_locker_equipment import LuggageLockerEquipment
from .luggage_service import LuggageService
from .meeting_point_service import MeetingPointService
from .money_service import MoneyService
from .passenger_equipment import PassengerEquipment
from .passenger_information_equipment import PassengerInformationEquipment
from .passenger_safety_equipment import PassengerSafetyEquipment
from .place_equipment import PlaceEquipment
from .place_lighting import PlaceLighting
from .place_sign import PlaceSign
from .queueing_equipment import QueueingEquipment
from .ramp_equipment import RampEquipment
from .retail_device import RetailDevice
from .retail_service import RetailService
from .rough_surface import RoughSurface
from .rubbish_disposal_equipment import RubbishDisposalEquipment
from .sanitary_equipment import SanitaryEquipment
from .seating_equipment import SeatingEquipment
from .shelter_equipment import ShelterEquipment
from .sign_equipment import SignEquipment
from .site_equipment import SiteEquipment
from .stair_equipment import StairEquipment
from .staircase_equipment import StaircaseEquipment
from .ticket_validator_equipment import TicketValidatorEquipment
from .ticketing_equipment import TicketingEquipment
from .ticketing_service import TicketingService
from .travelator_equipment import TravelatorEquipment
from .trolley_stand_equipment import TrolleyStandEquipment
from .vehicle_charging_equipment import VehicleChargingEquipment
from .waiting_equipment import WaitingEquipment
from .waiting_room_equipment import WaitingRoomEquipment
from .wheelchair_vehicle_equipment import WheelchairVehicleEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "equipmentsInFrame_RelStructure"

    assistance_booking_service: List[AssistanceBookingService] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceBookingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    catering_service: List[CateringService] = field(
        default_factory=list,
        metadata={
            "name": "CateringService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    retail_service: List[RetailService] = field(
        default_factory=list,
        metadata={
            "name": "RetailService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    money_service: List[MoneyService] = field(
        default_factory=list,
        metadata={
            "name": "MoneyService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    hire_service: List[HireService] = field(
        default_factory=list,
        metadata={
            "name": "HireService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    communication_service: List[CommunicationService] = field(
        default_factory=list,
        metadata={
            "name": "CommunicationService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    meeting_point_service: List[MeetingPointService] = field(
        default_factory=list,
        metadata={
            "name": "MeetingPointService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    lost_property_service: List[LostPropertyService] = field(
        default_factory=list,
        metadata={
            "name": "LostPropertyService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    left_luggage_service: List[LeftLuggageService] = field(
        default_factory=list,
        metadata={
            "name": "LeftLuggageService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    complaints_service: List[ComplaintsService] = field(
        default_factory=list,
        metadata={
            "name": "ComplaintsService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_service: List[CustomerService] = field(
        default_factory=list,
        metadata={
            "name": "CustomerService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    luggage_service: List[LuggageService] = field(
        default_factory=list,
        metadata={
            "name": "LuggageService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    assistance_service: List[AssistanceService] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    ticketing_service: List[TicketingService] = field(
        default_factory=list,
        metadata={
            "name": "TicketingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    local_service: List[LocalService] = field(
        default_factory=list,
        metadata={
            "name": "LocalService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    retail_device: List[RetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "RetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    ticket_validator_equipment: List[TicketValidatorEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TicketValidatorEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    ticketing_equipment: List[TicketingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TicketingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    seating_equipment: List[SeatingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SeatingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    shelter_equipment: List[ShelterEquipment] = field(
        default_factory=list,
        metadata={
            "name": "ShelterEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    trolley_stand_equipment: List[TrolleyStandEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TrolleyStandEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    waiting_room_equipment: List[WaitingRoomEquipment] = field(
        default_factory=list,
        metadata={
            "name": "WaitingRoomEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    waiting_equipment: List[WaitingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "WaitingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    luggage_locker_equipment: List[LuggageLockerEquipment] = field(
        default_factory=list,
        metadata={
            "name": "LuggageLockerEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_equipment: List[SiteEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SiteEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    crossing_equipment: List[CrossingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "CrossingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    queueing_equipment: List[QueueingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "QueueingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entrance_equipment: List[EntranceEquipment] = field(
        default_factory=list,
        metadata={
            "name": "EntranceEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    ramp_equipment: List[RampEquipment] = field(
        default_factory=list,
        metadata={
            "name": "RampEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    lift_equipment: List[LiftEquipment] = field(
        default_factory=list,
        metadata={
            "name": "LiftEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    travelator_equipment: List[TravelatorEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TravelatorEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    staircase_equipment: List[StaircaseEquipment] = field(
        default_factory=list,
        metadata={
            "name": "StaircaseEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    escalator_equipment: List[EscalatorEquipment] = field(
        default_factory=list,
        metadata={
            "name": "EscalatorEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stair_equipment: List[StairEquipment] = field(
        default_factory=list,
        metadata={
            "name": "StairEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    place_lighting: List[PlaceLighting] = field(
        default_factory=list,
        metadata={
            "name": "PlaceLighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    rough_surface: List[RoughSurface] = field(
        default_factory=list,
        metadata={
            "name": "RoughSurface",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_equipment: List[AccessEquipment] = field(
        default_factory=list,
        metadata={
            "name": "AccessEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    general_sign: List[GeneralSign] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    heading_sign: List[HeadingSign] = field(
        default_factory=list,
        metadata={
            "name": "HeadingSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    place_sign: List[PlaceSign] = field(
        default_factory=list,
        metadata={
            "name": "PlaceSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sign_equipment: List[SignEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SignEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    wheelchair_vehicle_equipment: List[WheelchairVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "WheelchairVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_vehicle_equipment: List[AccessVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "AccessVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_charging_equipment: List[VehicleChargingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleChargingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    cycle_storage_equipment: List[CycleStorageEquipment] = field(
        default_factory=list,
        metadata={
            "name": "CycleStorageEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    place_equipment: List[PlaceEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PlaceEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    passenger_information_equipment: List[PassengerInformationEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    rubbish_disposal_equipment: List[RubbishDisposalEquipment] = field(
        default_factory=list,
        metadata={
            "name": "RubbishDisposalEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    help_point_equipment: List[HelpPointEquipment] = field(
        default_factory=list,
        metadata={
            "name": "HelpPointEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    passenger_safety_equipment: List[PassengerSafetyEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSafetyEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sanitary_equipment: List[SanitaryEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    actual_vehicle_equipment: List[ActualVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "ActualVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    passenger_equipment: List[PassengerEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    installed_equipment: List[InstalledEquipment] = field(
        default_factory=list,
        metadata={
            "name": "InstalledEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    equipment: List[Equipment] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
