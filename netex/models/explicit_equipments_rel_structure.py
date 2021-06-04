from dataclasses import dataclass, field
from typing import List
from netex.models.access_equipment import AccessEquipment
from netex.models.access_vehicle_equipment import AccessVehicleEquipment
from netex.models.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from netex.models.actual_vehicle_equipment import ActualVehicleEquipment
from netex.models.assistance_booking_service import AssistanceBookingService
from netex.models.assistance_booking_service_ref import AssistanceBookingServiceRef
from netex.models.assistance_service import AssistanceService
from netex.models.assistance_service_ref import AssistanceServiceRef
from netex.models.catering_service import CateringService
from netex.models.catering_service_ref import CateringServiceRef
from netex.models.communication_service import CommunicationService
from netex.models.communication_service_ref import CommunicationServiceRef
from netex.models.complaints_service import ComplaintsService
from netex.models.complaints_service_ref import ComplaintsServiceRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.crossing_equipment import CrossingEquipment
from netex.models.customer_service import CustomerService
from netex.models.customer_service_ref import CustomerServiceRef
from netex.models.cycle_storage_equipment import CycleStorageEquipment
from netex.models.entrance_equipment import EntranceEquipment
from netex.models.escalator_equipment import EscalatorEquipment
from netex.models.general_sign import GeneralSign
from netex.models.heading_sign import HeadingSign
from netex.models.help_point_equipment import HelpPointEquipment
from netex.models.help_point_equipment_ref import HelpPointEquipmentRef
from netex.models.hire_service import HireService
from netex.models.hire_service_ref import HireServiceRef
from netex.models.installed_equipment import InstalledEquipment
from netex.models.installed_equipment_ref import InstalledEquipmentRef
from netex.models.left_luggage_service import LeftLuggageService
from netex.models.left_luggage_service_ref import LeftLuggageServiceRef
from netex.models.lift_equipment import LiftEquipment
from netex.models.local_service import LocalService
from netex.models.local_service_ref import LocalServiceRef
from netex.models.lost_property_service import LostPropertyService
from netex.models.lost_property_service_ref import LostPropertyServiceRef
from netex.models.luggage_locker_equipment import LuggageLockerEquipment
from netex.models.luggage_service import LuggageService
from netex.models.luggage_service_ref import LuggageServiceRef
from netex.models.meeting_point_service import MeetingPointService
from netex.models.meeting_point_service_ref import MeetingPointServiceRef
from netex.models.money_service import MoneyService
from netex.models.money_service_ref import MoneyServiceRef
from netex.models.other_place_equipment import OtherPlaceEquipment
from netex.models.passenger_equipment import PassengerEquipment
from netex.models.passenger_equipment_ref import PassengerEquipmentRef
from netex.models.passenger_information_equipment import PassengerInformationEquipment
from netex.models.passenger_information_equipment_ref import PassengerInformationEquipmentRef
from netex.models.passenger_safety_equipment import PassengerSafetyEquipment
from netex.models.passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from netex.models.place_equipment import PlaceEquipment
from netex.models.place_lighting import PlaceLighting
from netex.models.place_sign import PlaceSign
from netex.models.queueing_equipment import QueueingEquipment
from netex.models.ramp_equipment import RampEquipment
from netex.models.retail_device import RetailDevice
from netex.models.retail_service import RetailService
from netex.models.retail_service_ref import RetailServiceRef
from netex.models.rough_surface import RoughSurface
from netex.models.rubbish_disposal_equipment import RubbishDisposalEquipment
from netex.models.rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from netex.models.sanitary_equipment import SanitaryEquipment
from netex.models.sanitary_equipment_ref import SanitaryEquipmentRef
from netex.models.seating_equipment import SeatingEquipment
from netex.models.shelter_equipment import ShelterEquipment
from netex.models.sign_equipment import SignEquipment
from netex.models.site_equipment import SiteEquipment
from netex.models.stair_equipment import StairEquipment
from netex.models.staircase_equipment import StaircaseEquipment
from netex.models.ticket_validator_equipment import TicketValidatorEquipment
from netex.models.ticketing_equipment import TicketingEquipment
from netex.models.ticketing_service import TicketingService
from netex.models.ticketing_service_ref import TicketingServiceRef
from netex.models.travelator_equipment import TravelatorEquipment
from netex.models.trolley_stand_equipment import TrolleyStandEquipment
from netex.models.vehicle_charging_equipment import VehicleChargingEquipment
from netex.models.vehicle_equipment_ref import VehicleEquipmentRef
from netex.models.waiting_equipment import WaitingEquipment
from netex.models.waiting_room_equipment import WaitingRoomEquipment
from netex.models.wheelchair_vehicle_equipment import WheelchairVehicleEquipment
from netex.models.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ExplicitEquipmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "explicitEquipments_RelStructure"

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
    other_place_equipment: List[OtherPlaceEquipment] = field(
        default_factory=list,
        metadata={
            "name": "OtherPlaceEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
