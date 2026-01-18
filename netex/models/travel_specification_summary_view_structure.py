from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from .activated_equipment_ref import ActivatedEquipmentRef
from .assistance_booking_service_ref import AssistanceBookingServiceRef
from .assistance_service_ref import AssistanceServiceRef
from .authority_ref import AuthorityRef
from .battery_equipment_ref import BatteryEquipmentRef
from .car_pooling_service_ref import CarPoolingServiceRef
from .catering_service_ref import CateringServiceRef
from .chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from .class_of_use_ref import ClassOfUseRef
from .communication_service_ref import CommunicationServiceRef
from .companion_profile_ref import CompanionProfileRef
from .complaints_service_ref import ComplaintsServiceRef
from .crossing_equipment_ref import CrossingEquipmentRef
from .customer_service_ref import CustomerServiceRef
from .cycle_storage_equipment_ref import CycleStorageEquipmentRef
from .entrance_equipment_ref import EntranceEquipmentRef
from .equipment_ref import EquipmentRef
from .escalator_equipment_ref import EscalatorEquipmentRef
from .fare_class import FareClass
from .general_sign_ref import GeneralSignRef
from .group_of_operators_ref import GroupOfOperatorsRef
from .group_ticket_ref import GroupTicketRef
from .heading_sign_ref import HeadingSignRef
from .help_point_equipment_ref import HelpPointEquipmentRef
from .hire_service_ref import HireServiceRef
from .left_luggage_service_ref import LeftLuggageServiceRef
from .lift_call_equipment_ref import LiftCallEquipmentRef
from .lift_equipment_ref import LiftEquipmentRef
from .local_service_ref import LocalServiceRef
from .lost_property_service_ref import LostPropertyServiceRef
from .luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from .luggage_service_ref import LuggageServiceRef
from .meeting_point_service_ref import MeetingPointServiceRef
from .money_service_ref import MoneyServiceRef
from .online_service_ref import OnlineServiceRef
from .operator_ref import OperatorRef
from .passenger_beacon_equipment_ref import PassengerBeaconEquipmentRef
from .passenger_equipment_ref import PassengerEquipmentRef
from .passenger_information_equipment_ref import (
    PassengerInformationEquipmentRef,
)
from .passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from .passenger_seat_ref import PassengerSeatRef
from .place_lighting_equipment_ref import PlaceLightingEquipmentRef
from .place_sign_ref import PlaceSignRef
from .queueing_equipment_ref import QueueingEquipmentRef
from .ramp_equipment_ref import RampEquipmentRef
from .refuelling_equipment_ref import RefuellingEquipmentRef
from .retail_device_ref import RetailDeviceRef
from .retail_service_ref import RetailServiceRef
from .rough_surface_ref import RoughSurfaceRef
from .rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from .sanitary_equipment_ref import SanitaryEquipmentRef
from .seating_equipment_ref import SeatingEquipmentRef
from .series_constraint_refs_rel_structure import (
    SeriesConstraintRefsRelStructure,
)
from .service_facility_set import ServiceFacilitySet
from .shelter_equipment_ref import ShelterEquipmentRef
from .sign_equipment_ref import SignEquipmentRef
from .site_equipment_ref import SiteEquipmentRef
from .staircase_equipment_ref import StaircaseEquipmentRef
from .taxi_service_ref import TaxiServiceRef
from .ticket_validator_equipment_ref import TicketValidatorEquipmentRef
from .ticketing_equipment_ref import TicketingEquipmentRef
from .ticketing_service_ref import TicketingServiceRef
from .train_component_label_assignment_ref import (
    TrainComponentLabelAssignmentRef,
)
from .train_element_ref import TrainElementRef
from .travel_specification_journey_refs_rel_structure import (
    TravelSpecificationJourneyRefsRelStructure,
)
from .travel_specification_summary_endpoint_structure import (
    TravelSpecificationSummaryEndpointStructure,
)
from .travelator_equipment_ref import TravelatorEquipmentRef
from .trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from .type_of_fare_product_ref import TypeOfFareProductRef
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .user_profile_ref import UserProfileRef
from .vehicle_charging_equipment_ref import VehicleChargingEquipmentRef
from .vehicle_equipment_ref import VehicleEquipmentRef
from .vehicle_pooler_profile_ref import VehiclePoolerProfileRef
from .vehicle_release_equipment_ref import VehicleReleaseEquipmentRef
from .vehicle_rental_service_ref import VehicleRentalServiceRef
from .vehicle_sharing_service_ref import VehicleSharingServiceRef
from .waiting_equipment_ref import WaitingEquipmentRef
from .waiting_room_equipment_ref import WaitingRoomEquipmentRef
from .wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecificationSummaryViewStructure:
    origin: None | TravelSpecificationSummaryEndpointStructure = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination: None | TravelSpecificationSummaryEndpointStructure = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duration: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journeys: None | TravelSpecificationJourneyRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    series_constraints: None | SeriesConstraintRefsRelStructure = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    authority_ref_or_operator_ref_or_group_of_operators_ref: (
        None | AuthorityRef | OperatorRef | GroupOfOperatorsRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_product_category_ref: None | TypeOfProductCategoryRef = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_product_ref: None | TypeOfFareProductRef = field(
        default=None,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_class: None | FareClass = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: None | ClassOfUseRef = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_profile_ref: (
        None | VehiclePoolerProfileRef | CompanionProfileRef | UserProfileRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolerProfileRef",
                    "type": VehiclePoolerProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    group_ticket_ref: None | GroupTicketRef = field(
        default=None,
        metadata={
            "name": "GroupTicketRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_users: None | int = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfUsers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_element_ref: None | TrainElementRef = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_component_label_assignment_ref: (
        None | TrainComponentLabelAssignmentRef
    ) = field(
        default=None,
        metadata={
            "name": "TrainComponentLabelAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_seat_ref: None | PassengerSeatRef = field(
        default=None,
        metadata={
            "name": "PassengerSeatRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_facility_set: None | ServiceFacilitySet = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: (
        None
        | RetailDeviceRef
        | OnlineServiceRef
        | VehicleRentalServiceRef
        | VehicleSharingServiceRef
        | ChauffeuredVehicleServiceRef
        | TaxiServiceRef
        | CarPoolingServiceRef
        | ActivatedEquipmentRef
        | BatteryEquipmentRef
        | RefuellingEquipmentRef
        | VehicleChargingEquipmentRef
        | AssistanceBookingServiceRef
        | CateringServiceRef
        | RetailServiceRef
        | MoneyServiceRef
        | HireServiceRef
        | CommunicationServiceRef
        | MeetingPointServiceRef
        | LeftLuggageServiceRef
        | LuggageServiceRef
        | LostPropertyServiceRef
        | ComplaintsServiceRef
        | CustomerServiceRef
        | AssistanceServiceRef
        | TicketingServiceRef
        | LocalServiceRef
        | VehicleReleaseEquipmentRef
        | TicketValidatorEquipmentRef
        | TicketingEquipmentRef
        | PassengerInformationEquipmentRef
        | CycleStorageEquipmentRef
        | TrolleyStandEquipmentRef
        | SeatingEquipmentRef
        | ShelterEquipmentRef
        | LuggageLockerEquipmentRef
        | WaitingRoomEquipmentRef
        | WaitingEquipmentRef
        | SiteEquipmentRef
        | PlaceLightingEquipmentRef
        | RoughSurfaceRef
        | StaircaseEquipmentRef
        | QueueingEquipmentRef
        | TravelatorEquipmentRef
        | EscalatorEquipmentRef
        | LiftCallEquipmentRef
        | LiftEquipmentRef
        | CrossingEquipmentRef
        | RampEquipmentRef
        | EntranceEquipmentRef
        | HeadingSignRef
        | GeneralSignRef
        | PlaceSignRef
        | SignEquipmentRef
        | RubbishDisposalEquipmentRef
        | PassengerBeaconEquipmentRef
        | HelpPointEquipmentRef
        | PassengerSafetyEquipmentRef
        | SanitaryEquipmentRef
        | WheelchairVehicleRef
        | AccessVehicleEquipmentRef
        | VehicleEquipmentRef
        | PassengerEquipmentRef
        | EquipmentRef
    ) = field(
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
                    "name": "OnlineServiceRef",
                    "type": OnlineServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivatedEquipmentRef",
                    "type": ActivatedEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BatteryEquipmentRef",
                    "type": BatteryEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefuellingEquipmentRef",
                    "type": RefuellingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleChargingEquipmentRef",
                    "type": VehicleChargingEquipmentRef,
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
                    "name": "VehicleReleaseEquipmentRef",
                    "type": VehicleReleaseEquipmentRef,
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
                    "name": "EquipmentRef",
                    "type": EquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
