from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.access_equipment_ref import AccessEquipmentRef
from netex.models.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.activated_equipment_ref import ActivatedEquipmentRef
from netex.models.assistance_booking_service_ref import AssistanceBookingServiceRef
from netex.models.assistance_service_ref import AssistanceServiceRef
from netex.models.catering_service_ref import CateringServiceRef
from netex.models.communication_service_ref import CommunicationServiceRef
from netex.models.complaints_service_ref import ComplaintsServiceRef
from netex.models.compound_train_ref import CompoundTrainRef
from netex.models.crossing_equipment_ref import CrossingEquipmentRef
from netex.models.customer_service_ref import CustomerServiceRef
from netex.models.cycle_storage_equipment_ref import CycleStorageEquipmentRef
from netex.models.entrance_equipment_ref import EntranceEquipmentRef
from netex.models.equipment_ref import EquipmentRef
from netex.models.escalator_equipment_ref import EscalatorEquipmentRef
from netex.models.general_sign_ref import GeneralSignRef
from netex.models.heading_sign_ref import HeadingSignRef
from netex.models.help_point_equipment_ref import HelpPointEquipmentRef
from netex.models.hire_service_ref import HireServiceRef
from netex.models.installed_equipment_ref import InstalledEquipmentRef
from netex.models.left_luggage_service_ref import LeftLuggageServiceRef
from netex.models.lift_equipment_ref import LiftEquipmentRef
from netex.models.local_service_ref import LocalServiceRef
from netex.models.lost_property_service_ref import LostPropertyServiceRef
from netex.models.luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from netex.models.luggage_service_ref import LuggageServiceRef
from netex.models.meeting_point_service_ref import MeetingPointServiceRef
from netex.models.money_service_ref import MoneyServiceRef
from netex.models.passenger_equipment_ref import PassengerEquipmentRef
from netex.models.passenger_equipment_version_structure import PassengerEquipmentVersionStructure
from netex.models.passenger_information_equipment_ref import PassengerInformationEquipmentRef
from netex.models.passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from netex.models.place_lighting_equipment_ref import PlaceLightingEquipmentRef
from netex.models.place_sign_ref import PlaceSignRef
from netex.models.queueing_equipment_ref import QueueingEquipmentRef
from netex.models.ramp_equipment_ref import RampEquipmentRef
from netex.models.retail_device_ref import RetailDeviceRef
from netex.models.retail_service_ref import RetailServiceRef
from netex.models.rough_surface_ref import RoughSurfaceRef
from netex.models.rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from netex.models.sanitary_equipment_ref import SanitaryEquipmentRef
from netex.models.seating_equipment_ref import SeatingEquipmentRef
from netex.models.shelter_equipment_ref import ShelterEquipmentRef
from netex.models.sign_equipment_ref import SignEquipmentRef
from netex.models.site_equipment_ref import SiteEquipmentRef
from netex.models.staircase_equipment_ref import StaircaseEquipmentRef
from netex.models.ticket_validator_equipment_ref import TicketValidatorEquipmentRef
from netex.models.ticketing_equipment_ref import TicketingEquipmentRef
from netex.models.ticketing_service_ref import TicketingServiceRef
from netex.models.train_ref import TrainRef
from netex.models.travelator_equipment_ref import TravelatorEquipmentRef
from netex.models.trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from netex.models.vehicle_charging_equipment_ref import VehicleChargingEquipmentRef
from netex.models.vehicle_equipment_ref import VehicleEquipmentRef
from netex.models.vehicle_type_ref import VehicleTypeRef
from netex.models.waiting_equipment_ref import WaitingEquipmentRef
from netex.models.waiting_room_equipment_ref import WaitingRoomEquipmentRef
from netex.models.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActualVehicleEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    class Meta:
        name = "ActualVehicleEquipment_VersionStructure"

    units: Optional[int] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_train_ref: List[CompoundTrainRef] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    train_ref: List[TrainRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_type_ref: Optional[VehicleTypeRef] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_device_ref: List[RetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    assistance_booking_service_ref: List[AssistanceBookingServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceBookingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    catering_service_ref: List[CateringServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "CateringServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    retail_service_ref: List[RetailServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    money_service_ref: List[MoneyServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "MoneyServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    hire_service_ref: List[HireServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "HireServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    communication_service_ref: List[CommunicationServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "CommunicationServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    meeting_point_service_ref: List[MeetingPointServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "MeetingPointServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    left_luggage_service_ref: List[LeftLuggageServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LeftLuggageServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    luggage_service_ref: List[LuggageServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LuggageServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    lost_property_service_ref: List[LostPropertyServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LostPropertyServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    complaints_service_ref: List[ComplaintsServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "ComplaintsServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    customer_service_ref: List[CustomerServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    assistance_service_ref: List[AssistanceServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    ticketing_service_ref: List[TicketingServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    local_service_ref: List[LocalServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "LocalServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_charging_equipment_ref: List[VehicleChargingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleChargingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    cycle_storage_equipment_ref: List[CycleStorageEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "CycleStorageEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    ticket_validator_equipment_ref: List[TicketValidatorEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketValidatorEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    ticketing_equipment_ref: List[TicketingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    trolley_stand_equipment_ref: List[TrolleyStandEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TrolleyStandEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    seating_equipment_ref: List[SeatingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SeatingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    shelter_equipment_ref: List[ShelterEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "ShelterEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    luggage_locker_equipment_ref: List[LuggageLockerEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "LuggageLockerEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    waiting_room_equipment_ref: List[WaitingRoomEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "WaitingRoomEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    waiting_equipment_ref: List[WaitingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "WaitingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    site_equipment_ref: List[SiteEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    heading_sign_ref: List[HeadingSignRef] = field(
        default_factory=list,
        metadata={
            "name": "HeadingSignRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    general_sign_ref: List[GeneralSignRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSignRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    place_sign_ref: List[PlaceSignRef] = field(
        default_factory=list,
        metadata={
            "name": "PlaceSignRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    sign_equipment_ref: List[SignEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SignEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    place_lighting_equipment_ref: List[PlaceLightingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PlaceLightingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    rough_surface_ref: List[RoughSurfaceRef] = field(
        default_factory=list,
        metadata={
            "name": "RoughSurfaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    staircase_equipment_ref: List[StaircaseEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "StaircaseEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    queueing_equipment_ref: List[QueueingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "QueueingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    travelator_equipment_ref: List[TravelatorEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelatorEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    escalator_equipment_ref: List[EscalatorEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "EscalatorEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    lift_equipment_ref: List[LiftEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "LiftEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    crossing_equipment_ref: List[CrossingEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "CrossingEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    ramp_equipment_ref: List[RampEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "RampEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    entrance_equipment_ref: List[EntranceEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "EntranceEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    access_equipment_ref: List[AccessEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    activated_equipment_ref: List[ActivatedEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "ActivatedEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    passenger_information_equipment_ref: List[PassengerInformationEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    rubbish_disposal_equipment_ref: List[RubbishDisposalEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "RubbishDisposalEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    help_point_equipment_ref: List[HelpPointEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "HelpPointEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    passenger_safety_equipment_ref: List[PassengerSafetyEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSafetyEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    sanitary_equipment_ref: List[SanitaryEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    wheelchair_vehicle_ref: List[WheelchairVehicleRef] = field(
        default_factory=list,
        metadata={
            "name": "WheelchairVehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
            "sequential": True,
        }
    )
    access_vehicle_equipment_ref: List[AccessVehicleEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessVehicleEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
            "sequential": True,
        }
    )
    vehicle_equipment_ref: List[VehicleEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    passenger_equipment_ref: List[PassengerEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    installed_equipment_ref: List[InstalledEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "InstalledEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    equipment_ref: Optional[EquipmentRef] = field(
        default=None,
        metadata={
            "name": "EquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
