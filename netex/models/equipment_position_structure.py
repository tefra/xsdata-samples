from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
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
    retail_device_ref: List[RetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
            "min_occurs": 1,
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
