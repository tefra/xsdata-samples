from dataclasses import dataclass, field
from typing import List, Union

from .access import Access
from .access_right_parameter_assignment_1 import (
    AccessRightParameterAssignment1,
)
from .access_space import AccessSpace
from .access_vehicle_equipment import AccessVehicleEquipment
from .access_zone import AccessZone
from .accountable_element import AccountableElement
from .activation_assignment import ActivationAssignment
from .activation_link import ActivationLink
from .activation_point_1 import ActivationPoint1
from .additional_driver_option import AdditionalDriverOption
from .addressable_place import AddressablePlace
from .administrative_zones_rel_structure import (
    AdministrativeZone1,
    TransportAdministrativeZone,
)
from .allowed_line_direction import AllowedLineDirection
from .alternative_mode_of_operation_1 import AlternativeModeOfOperation1
from .amount_of_price_unit_product import AmountOfPriceUnitProduct
from .assistance_booking_service import AssistanceBookingService
from .assistance_service import AssistanceService
from .authority import Authority
from .battery_equipment import BatteryEquipment
from .beacon_point import BeaconPoint
from .blacklist import Blacklist
from .block import Block
from .block_part import BlockPart
from .boarding_position import BoardingPosition
from .border_point import BorderPoint
from .branding import Branding
from .cancelling import Cancelling
from .capped_discount_right import CappedDiscountRight
from .capping_rule import CappingRule
from .car_model_profile import CarModelProfile
from .car_pooling_service import CarPoolingService
from .catering_service import CateringService
from .charging_equipment_profile import ChargingEquipmentProfile
from .charging_moment import ChargingMoment
from .charging_policy import ChargingPolicy
from .chauffeured_vehicle_service import ChauffeuredVehicleService
from .check_constraint import CheckConstraint
from .check_constraint_delay import CheckConstraintDelay
from .check_constraint_throughput import CheckConstraintThroughput
from .class_of_use import ClassOfUse
from .commercial_profile import CommercialProfile
from .communication_service import CommunicationService
from .companion_profile import CompanionProfile
from .complaints_service import ComplaintsService
from .complex_feature import ComplexFeature
from .complex_feature_projection import ComplexFeatureProjection
from .compound_block import CompoundBlock
from .compound_train import CompoundTrain
from .connection import Connection
from .contact import Contact
from .containment_aggregation_structure import ContainmentAggregationStructure
from .control_centre import ControlCentre
from .controllable_element import ControllableElement
from .country import Country
from .coupled_journey import CoupledJourney
from .course_of_journeys import CourseOfJourneys
from .crew_base import CrewBase
from .crossing_equipment import CrossingEquipment
from .customer import Customer
from .customer_account import CustomerAccount
from .customer_account_status import CustomerAccountStatus
from .customer_purchase_package import CustomerPurchasePackage
from .customer_purchase_package_element import CustomerPurchasePackageElement
from .customer_purchase_parameter_assignment import (
    CustomerPurchaseParameterAssignment,
)
from .customer_service import CustomerService
from .cycle_model_profile import CycleModelProfile
from .cycle_storage_equipment import CycleStorageEquipment
from .data_source import DataSource
from .dated_service_journey import DatedServiceJourney
from .dated_special_service import DatedSpecialService
from .dated_vehicle_journey import DatedVehicleJourney
from .day_type_assignment import DayTypeAssignment
from .dead_run import DeadRun
from .dead_run_journey_pattern import DeadRunJourneyPattern
from .default_connection import DefaultConnection
from .default_interchange import DefaultInterchange
from .delivery_variant import DeliveryVariant
from .department import Department
from .destination_display import DestinationDisplay
from .destination_display_variant import DestinationDisplayVariant
from .direction import Direction
from .discounting_rule import DiscountingRule
from .display_assignment import DisplayAssignment
from .distance_matrix_element import DistanceMatrixElement
from .distribution_assignment import DistributionAssignment
from .distribution_channel import DistributionChannel
from .driver_schedule_frame import DriverScheduleFrame
from .driver_trip import DriverTrip
from .driver_trip_time import DriverTripTime
from .duty import Duty
from .duty_part import DutyPart
from .dynamic_stop_assignment import DynamicStopAssignment
from .dynamic_vehicle_meeting_point_assignment import (
    DynamicVehicleMeetingPointAssignment,
)
from .eligibility_change_policy import EligibilityChangePolicy
from .emv_card import EmvCard
from .entitlement_given import EntitlementGiven
from .entitlement_product import EntitlementProduct
from .entitlement_required import EntitlementRequired
from .entity_in_version_in_frame_ref_structure import (
    EntityInVersionInFrameRefStructure,
)
from .entity_in_version_structure import (
    AvailabilityCondition,
    DayType1,
    FareDayType,
    OperatingDay,
    OrganisationDayType,
    SimpleAvailabilityCondition,
    ValidDuring,
    ValidityCondition1,
    ValidityRuleParameter,
    ValidityTrigger,
)
from .entrance import Entrance
from .entrance_equipment import EntranceEquipment
from .equipment_place import EquipmentPlace
from .equipment_position import EquipmentPosition
from .escalator_equipment import EscalatorEquipment
from .exchanging import Exchanging
from .facility_requirement import FacilityRequirement
from .fare_contract import FareContract
from .fare_contract_entry_2 import FareContractEntry2
from .fare_demand_factor import FareDemandFactor
from .fare_frame import FareFrame
from .fare_interval import FareInterval
from .fare_quota_factor import FareQuotaFactor
from .fare_scheduled_stop_point import FareScheduledStopPoint
from .fare_structure_element import FareStructureElement
from .fare_structure_factor import FareStructureFactor
from .fare_unit import FareUnit
from .fare_zone import FareZone
from .fleet import Fleet
from .flexible_area import FlexibleArea
from .flexible_line import FlexibleLine
from .flexible_operation import FlexibleOperation
from .flexible_quay import FlexibleQuay
from .flexible_route import FlexibleRoute
from .flexible_service_properties import FlexibleServiceProperties
from .flexible_stop_assignment import FlexibleStopAssignment
from .flexible_stop_place import FlexibleStopPlace
from .frequency_of_use import FrequencyOfUse
from .fulfilment_method import FulfilmentMethod
from .garage import Garage
from .garage_point import GaragePoint
from .general_group_of_entities import GeneralGroupOfEntities
from .general_organisation import GeneralOrganisation
from .general_sign import GeneralSign
from .general_version_frame_structure import (
    CompositeFrame,
    GeneralFrame,
)
from .general_zone import GeneralZone
from .generic_parameter_assignments_rel_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from .geographical_interval import GeographicalInterval
from .geographical_structure_factor import GeographicalStructureFactor
from .geographical_unit import GeographicalUnit
from .group_of_distance_matrix_elements import GroupOfDistanceMatrixElements
from .group_of_distribution_channels import GroupOfDistributionChannels
from .group_of_lines import GroupOfLines
from .group_of_link_sequences import GroupOfLinkSequences
from .group_of_links import GroupOfLinks
from .group_of_operators import GroupOfOperators
from .group_of_places import GroupOfPlaces
from .group_of_points import GroupOfPoints
from .group_of_sales_offer_packages import GroupOfSalesOfferPackages
from .group_of_services import GroupOfServices
from .group_of_single_journeys import GroupOfSingleJourneys
from .group_of_timebands import GroupOfTimebands
from .group_of_timing_links import GroupOfTimingLinks
from .group_ticket import GroupTicket
from .hail_and_ride_area import HailAndRideArea
from .heading_sign import HeadingSign
from .headway_journey_group import HeadwayJourneyGroup
from .help_point_equipment import HelpPointEquipment
from .hire_service import HireService
from .individual_passenger_info import IndividualPassengerInfo
from .individual_traveller import IndividualTraveller
from .infrastructure_frame import InfrastructureFrame
from .interchange_rule import InterchangeRule
from .interchanging import Interchanging
from .journey_accounting import JourneyAccounting
from .journey_meeting import JourneyMeeting
from .journey_part import JourneyPart
from .journey_part_couple import JourneyPartCouple
from .layer import Layer
from .left_luggage_service import LeftLuggageService
from .level import Level
from .lift_equipment import LiftEquipment
from .limiting_rule import LimitingRule
from .limiting_rule_in_context import LimitingRuleInContext
from .line_1 import Line1
from .line_network import LineNetwork
from .line_shape import LineShape
from .link_projection import LinkProjection
from .link_sequence_projection import LinkSequenceProjection
from .logical_display import LogicalDisplay
from .lost_property_service import LostPropertyService
from .luggage_allowance import LuggageAllowance
from .luggage_service import LuggageService
from .management_agent import ManagementAgent
from .medium_access_device_1 import MediumAccessDevice1
from .meeting_point_service import MeetingPointService
from .meeting_restriction import MeetingRestriction
from .minimum_stay import MinimumStay
from .mobile_device import MobileDevice
from .mobility_journey_frame import MobilityJourneyFrame
from .mobility_service_constraint_zone import MobilityServiceConstraintZone
from .mobility_service_frame import MobilityServiceFrame
from .mode_restriction_assessment import ModeRestrictionAssessment
from .money_service import MoneyService
from .monitored_vehicle_sharing_parking_bay import (
    MonitoredVehicleSharingParkingBay,
)
from .month_validity_offset import MonthValidityOffset
from .navigation_path import NavigationPath
from .navigation_path_assignment import NavigationPathAssignment
from .network import Network
from .normal_dated_vehicle_journey import NormalDatedVehicleJourney
from .notice import Notice
from .notice_assignment_1 import NoticeAssignment1
from .offered_travel_specification import OfferedTravelSpecification
from .online_service import OnlineService
from .online_service_operator import OnlineServiceOperator
from .open_transport_mode import OpenTransportMode
from .operating_department import OperatingDepartment
from .operating_period_1 import OperatingPeriod1
from .operational_context import OperationalContext
from .operator import Operator
from .organisation_part_1 import OrganisationPart1
from .organisational_unit import OrganisationalUnit
from .other_organisation import OtherOrganisation
from .overtaking_possibility import OvertakingPossibility
from .parking import Parking
from .parking_area_1 import ParkingArea1
from .parking_bay_1 import ParkingBay1
from .parking_bay_condition import ParkingBayCondition
from .parking_bay_status import ParkingBayStatus
from .parking_component import ParkingComponent
from .parking_entrance_for_vehicles import ParkingEntranceForVehicles
from .parking_passenger_entrance import ParkingPassengerEntrance
from .parking_point_1 import ParkingPoint1
from .parking_tariff import ParkingTariff
from .passenger_carrying_requirement import PassengerCarryingRequirement
from .passenger_carrying_requirements_view import (
    PassengerCarryingRequirementsView,
)
from .passenger_information_equipment import PassengerInformationEquipment
from .passenger_safety_equipment import PassengerSafetyEquipment
from .passenger_stop_assignment import PassengerStopAssignment
from .passing_time_view import PassingTimeView
from .path_junction import PathJunction
from .path_link import PathLink
from .penalty_policy import PenaltyPolicy
from .personal_mode_of_operation import PersonalModeOfOperation
from .place_lighting import PlaceLighting
from .place_sign import PlaceSign
from .point_2 import Point2
from .point_of_interest import PointOfInterest
from .point_of_interest_classification import PointOfInterestClassification
from .point_of_interest_classification_hierarchy import (
    PointOfInterestClassificationHierarchy,
)
from .point_of_interest_entrance import PointOfInterestEntrance
from .point_of_interest_space import PointOfInterestSpace
from .point_of_interest_vehicle_entrance import PointOfInterestVehicleEntrance
from .point_projection import PointProjection
from .pool_of_vehicles import PoolOfVehicles
from .postal_address import PostalAddress
from .preassigned_fare_product import PreassignedFareProduct
from .price_unit import PriceUnit
from .priceable_object_version_structure import (
    FareTable1,
    FareTableInContext,
    ParkingChargeBand,
    PriceGroup1,
)
from .pricing_parameter_set import PricingParameterSet
from .pricing_rule_1 import PricingRule1
from .pricing_service import PricingService
from .purchase_window import PurchaseWindow
from .purpose_of_equipment_profile import PurposeOfEquipmentProfile
from .purpose_of_grouping import PurposeOfGrouping
from .purpose_of_journey_partition import PurposeOfJourneyPartition
from .quality_structure_factor_1 import QualityStructureFactor1
from .quay_1 import Quay1
from .queueing_equipment import QueueingEquipment
from .railway_element import RailwayElement
from .railway_junction import RailwayJunction
from .ramp_equipment import RampEquipment
from .refuelling_equipment import RefuellingEquipment
from .refunding import Refunding
from .relief_opportunity import ReliefOpportunity
from .relief_point_1 import ReliefPoint1
from .rental_availability import RentalAvailability
from .rental_option import RentalOption
from .rental_penalty_policy import RentalPenaltyPolicy
from .replacing import Replacing
from .requested_travel_specification import RequestedTravelSpecification
from .reselling import Reselling
from .reserving import Reserving
from .resource_frame import ResourceFrame
from .responsibility_set import ResponsibilitySet
from .restricted_manoeuvre import RestrictedManoeuvre
from .retail_consortium import RetailConsortium
from .retail_device import RetailDevice
from .retail_service import RetailService
from .rhythmical_journey_group import RhythmicalJourneyGroup
from .road_address import RoadAddress
from .road_element import RoadElement
from .road_junction import RoadJunction
from .rough_surface import RoughSurface
from .round_trip import RoundTrip
from .rounding import Rounding
from .route_1 import Route1
from .route_instruction import RouteInstruction
from .route_link import RouteLink
from .route_point import RoutePoint
from .routing import Routing
from .routing_constraint_zone import RoutingConstraintZone
from .rubbish_disposal_equipment import RubbishDisposalEquipment
from .sale_discount_right import SaleDiscountRight
from .sales_notice_assignment import SalesNoticeAssignment
from .sales_offer_package import SalesOfferPackage
from .sales_offer_package_element import SalesOfferPackageElement
from .sales_offer_package_entitlement_given import (
    SalesOfferPackageEntitlementGiven,
)
from .sales_offer_package_entitlement_required import (
    SalesOfferPackageEntitlementRequired,
)
from .sales_offer_package_substitution import SalesOfferPackageSubstitution
from .sales_transaction import SalesTransaction
from .sales_transaction_frame import SalesTransactionFrame
from .sanitary_equipment import SanitaryEquipment
from .scheduled_operation import ScheduledOperation
from .scheduled_stop_point import ScheduledStopPoint
from .schematic_map import SchematicMap
from .seating_equipment import SeatingEquipment
from .sections_in_sequence_rel_structure import JourneyPattern1
from .series_constraint import SeriesConstraint
from .service_access_code import ServiceAccessCode
from .service_access_right_1 import ServiceAccessRight1
from .service_access_right_2 import ServiceAccessRight2
from .service_calendar import ServiceCalendar
from .service_calendar_frame import ServiceCalendarFrame
from .service_exclusion import ServiceExclusion
from .service_frame import ServiceFrame
from .service_journey_1 import ServiceJourney1
from .service_journey_interchange import ServiceJourneyInterchange
from .service_journey_pattern import ServiceJourneyPattern
from .service_journey_pattern_interchange import (
    ServiceJourneyPatternInterchange,
)
from .service_link import ServiceLink
from .service_pattern import ServicePattern
from .service_site import ServiceSite
from .serviced_organisation import ServicedOrganisation
from .shelter_equipment import ShelterEquipment
from .sign_equipment import SignEquipment
from .simple_feature import SimpleFeature
from .simple_vehicle_type import SimpleVehicleType
from .single_journey import SingleJourney
from .single_journey_path import SingleJourneyPath
from .site_connection import SiteConnection
from .site_frame import SiteFrame
from .site_path_link import SitePathLink
from .smartcard import Smartcard
from .spatial_feature import SpatialFeature
from .special_service import SpecialService
from .specific_parameter_assignments_rel_structure import (
    SpecificParameterAssignment,
)
from .staircase_equipment import StaircaseEquipment
from .standard_fare_table import StandardFareTable
from .step_limit import StepLimit
from .stop_area import StopArea
from .stop_place_1 import StopPlace1
from .stop_place_entrance import StopPlaceEntrance
from .stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from .submode import Submode
from .subscribing import Subscribing
from .supplement_product import SupplementProduct
from .suspending import Suspending
from .tariff import Tariff
from .tariff_zone_1 import TariffZone1
from .taxi_parking_area import TaxiParkingArea
from .taxi_rank import TaxiRank
from .taxi_service import TaxiService
from .taxi_service_place_assignment import TaxiServicePlaceAssignment
from .taxi_stand import TaxiStand
from .template_service_journey import TemplateServiceJourney
from .template_vehicle_journey import TemplateVehicleJourney
from .third_party_product import ThirdPartyProduct
from .ticket_validator_equipment import TicketValidatorEquipment
from .ticketing_equipment import TicketingEquipment
from .ticketing_service import TicketingService
from .time_demand_profile import TimeDemandProfile
from .time_demand_type import TimeDemandType
from .time_demand_type_assignment import TimeDemandTypeAssignment
from .time_interval import TimeInterval
from .time_structure_factor import TimeStructureFactor
from .time_unit import TimeUnit
from .timeband import Timeband
from .timetable_frame import TimetableFrame
from .timing_algorithm_type import TimingAlgorithmType
from .timing_link import TimingLink
from .timing_pattern import TimingPattern
from .timing_point_1 import TimingPoint1
from .topographic_place import TopographicPlace
from .topographic_projection import TopographicProjection
from .traffic_control_point import TrafficControlPoint
from .train import Train
from .train_block import TrainBlock
from .train_block_part import TrainBlockPart
from .train_component import TrainComponent
from .train_component_label_assignment import TrainComponentLabelAssignment
from .train_element import TrainElement
from .train_number import TrainNumber
from .train_stop_assignment import TrainStopAssignment
from .transfer_restriction import TransferRestriction
from .transferability import Transferability
from .transport_type_1 import TransportType1
from .travel_agent import TravelAgent
from .travel_document import TravelDocument
from .travel_specification_1 import TravelSpecification1
from .travel_specification_2 import TravelSpecification2
from .travelator_equipment import TravelatorEquipment
from .trolley_stand_equipment import TrolleyStandEquipment
from .type_of_access_right_assignment import TypeOfAccessRightAssignment
from .type_of_activation import TypeOfActivation
from .type_of_battery_chemistry import TypeOfBatteryChemistry
from .type_of_codespace_assignment import TypeOfCodespaceAssignment
from .type_of_concession import TypeOfConcession
from .type_of_congestion import TypeOfCongestion
from .type_of_customer_account import TypeOfCustomerAccount
from .type_of_delivery_variant import TypeOfDeliveryVariant
from .type_of_entity import TypeOfEntity
from .type_of_equipment import TypeOfEquipment
from .type_of_facility import TypeOfFacility
from .type_of_fare_contract import TypeOfFareContract
from .type_of_fare_contract_entry import TypeOfFareContractEntry
from .type_of_fare_product import TypeOfFareProduct
from .type_of_fare_structure_element import TypeOfFareStructureElement
from .type_of_fare_structure_factor import TypeOfFareStructureFactor
from .type_of_fare_table import TypeOfFareTable
from .type_of_feature import TypeOfFeature
from .type_of_fleet import TypeOfFleet
from .type_of_flexible_service import TypeOfFlexibleService
from .type_of_journey_pattern import TypeOfJourneyPattern
from .type_of_line import TypeOfLine
from .type_of_link import TypeOfLink
from .type_of_link_sequence import TypeOfLinkSequence
from .type_of_machine_readability import TypeOfMachineReadability
from .type_of_medium_access_device import TypeOfMediumAccessDevice
from .type_of_mobility_service import TypeOfMobilityService
from .type_of_mode_of_operation import TypeOfModeOfOperation
from .type_of_notice import TypeOfNotice
from .type_of_operation import TypeOfOperation
from .type_of_organisation import TypeOfOrganisation
from .type_of_organisation_part import TypeOfOrganisationPart
from .type_of_parking import TypeOfParking
from .type_of_passenger_information_equipment import (
    TypeOfPassengerInformationEquipment,
)
from .type_of_payment_method import TypeOfPaymentMethod
from .type_of_place import TypeOfPlace
from .type_of_plug import TypeOfPlug
from .type_of_point import TypeOfPoint
from .type_of_pricing_rule import TypeOfPricingRule
from .type_of_product_category import TypeOfProductCategory
from .type_of_projection import TypeOfProjection
from .type_of_proof import TypeOfProof
from .type_of_responsibility_role import TypeOfResponsibilityRole
from .type_of_retail_device import TypeOfRetailDevice
from .type_of_sales_offer_package import TypeOfSalesOfferPackage
from .type_of_security_list import TypeOfSecurityList
from .type_of_service import TypeOfService
from .type_of_service_feature import TypeOfServiceFeature
from .type_of_tariff import TypeOfTariff
from .type_of_time_demand_type import TypeOfTimeDemandType
from .type_of_transfer import TypeOfTransfer
from .type_of_travel_document import TypeOfTravelDocument
from .type_of_usage_parameter import TypeOfUsageParameter
from .type_of_validity import TypeOfValidity
from .type_of_version import TypeOfVersion
from .type_of_zone import TypeOfZone
from .types_of_frame_rel_structure import TypeOfFrame
from .uic_operating_period import UicOperatingPeriod
from .usage_discount_right import UsageDiscountRight
from .usage_validity_period import UsageValidityPeriod
from .user_profile import UserProfile
from .validable_element import ValidableElement
from .validity_parameter_assignment import ValidityParameterAssignment
from .value_set import ValueSet
from .vehicle import Vehicle
from .vehicle_access_credentials_assignment import (
    VehicleAccessCredentialsAssignment,
)
from .vehicle_charging_equipment import VehicleChargingEquipment
from .vehicle_equipment_profile import VehicleEquipmentProfile
from .vehicle_journey_1 import VehicleJourney1
from .vehicle_journey_stop_assignment import VehicleJourneyStopAssignment
from .vehicle_manoeuvring_requirement import VehicleManoeuvringRequirement
from .vehicle_meeting_link import VehicleMeetingLink
from .vehicle_meeting_place_1 import VehicleMeetingPlace1
from .vehicle_meeting_place_2 import VehicleMeetingPlace2
from .vehicle_meeting_point import VehicleMeetingPoint
from .vehicle_meeting_point_assignment_1 import VehicleMeetingPointAssignment1
from .vehicle_meeting_point_assignment_2 import VehicleMeetingPointAssignment2
from .vehicle_model import VehicleModel
from .vehicle_pooler_profile import VehiclePoolerProfile
from .vehicle_pooling import VehiclePooling
from .vehicle_pooling_driver_info import VehiclePoolingDriverInfo
from .vehicle_pooling_meeting_place import VehiclePoolingMeetingPlace
from .vehicle_pooling_parking_area import VehiclePoolingParkingArea
from .vehicle_pooling_parking_bay import VehiclePoolingParkingBay
from .vehicle_pooling_place_assignment import VehiclePoolingPlaceAssignment
from .vehicle_release_equipment import VehicleReleaseEquipment
from .vehicle_rental import VehicleRental
from .vehicle_rental_service import VehicleRentalService
from .vehicle_schedule_frame import VehicleScheduleFrame
from .vehicle_service import VehicleService
from .vehicle_service_part import VehicleServicePart
from .vehicle_service_place_assignment_1 import VehicleServicePlaceAssignment1
from .vehicle_service_place_assignment_2 import VehicleServicePlaceAssignment2
from .vehicle_sharing import VehicleSharing
from .vehicle_sharing_parking_area import VehicleSharingParkingArea
from .vehicle_sharing_parking_bay import VehicleSharingParkingBay
from .vehicle_sharing_place_assignment import VehicleSharingPlaceAssignment
from .vehicle_sharing_service import VehicleSharingService
from .vehicle_stopping_place import VehicleStoppingPlace
from .vehicle_stopping_position import VehicleStoppingPosition
from .vehicle_type import VehicleType
from .vehicle_type_at_point import VehicleTypeAtPoint
from .vehicle_type_stop_assignment import VehicleTypeStopAssignment
from .version import Version
from .waiting_room_equipment import WaitingRoomEquipment
from .wheelchair_vehicle_equipment import WheelchairVehicleEquipment
from .whitelist import Whitelist
from .wire_element import WireElement
from .wire_junction import WireJunction
from .zone import Zone
from .zone_projection import ZoneProjection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionFrameMembersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "versionFrameMembers_RelStructure"

    choice: List[
        Union[
            EntityInVersionInFrameRefStructure,
            Fleet,
            IndividualPassengerInfo,
            VehiclePoolingDriverInfo,
            IndividualTraveller,
            ParkingBayCondition,
            RentalAvailability,
            Smartcard,
            EmvCard,
            MobileDevice,
            MediumAccessDevice1,
            ServiceAccessCode,
            TravelDocument,
            CustomerAccount,
            SalesTransaction,
            OfferedTravelSpecification,
            RequestedTravelSpecification,
            TravelSpecification1,
            TravelSpecification2,
            FareContractEntry2,
            FareContract,
            Customer,
            ParkingTariff,
            GroupOfSalesOfferPackages,
            DistributionChannel,
            Tariff,
            CustomerPurchasePackage,
            SalesOfferPackage,
            FulfilmentMethod,
            CappingRule,
            EntitlementProduct,
            SupplementProduct,
            PreassignedFareProduct,
            AmountOfPriceUnitProduct,
            CappedDiscountRight,
            UsageDiscountRight,
            ThirdPartyProduct,
            SaleDiscountRight,
            ServiceAccessRight1,
            ServiceAccessRight2,
            TimeInterval,
            FareQuotaFactor,
            FareDemandFactor,
            QualityStructureFactor1,
            ControllableElement,
            ValidableElement,
            AdditionalDriverOption,
            RentalOption,
            RentalPenaltyPolicy,
            VehiclePoolerProfile,
            SalesOfferPackageEntitlementRequired,
            SalesOfferPackageEntitlementGiven,
            MinimumStay,
            Interchanging,
            Suspending,
            UsageValidityPeriod,
            FrequencyOfUse,
            StepLimit,
            Routing,
            RoundTrip,
            LuggageAllowance,
            EntitlementRequired,
            EntitlementGiven,
            EligibilityChangePolicy,
            CompanionProfile,
            GroupTicket,
            CommercialProfile,
            UserProfile,
            Subscribing,
            PenaltyPolicy,
            ChargingPolicy,
            Cancelling,
            Reserving,
            PurchaseWindow,
            Transferability,
            Replacing,
            Refunding,
            Exchanging,
            Reselling,
            GeographicalInterval,
            SeriesConstraint,
            CustomerPurchasePackageElement,
            ParkingChargeBand,
            SalesOfferPackageElement,
            FareStructureElement,
            TimeStructureFactor,
            TimeUnit,
            DistanceMatrixElement,
            GeographicalStructureFactor,
            GeographicalUnit,
            FareUnit,
            FareInterval,
            FareStructureFactor,
            PricingService,
            LimitingRuleInContext,
            LimitingRule,
            DiscountingRule,
            PricingRule1,
            MonthValidityOffset,
            Rounding,
            PricingParameterSet,
            ReliefOpportunity,
            CourseOfJourneys,
            VehicleServicePart,
            VehicleService,
            TrainBlockPart,
            CompoundBlock,
            BlockPart,
            TrainBlock,
            Block,
            DriverTripTime,
            DriverTrip,
            DutyPart,
            AccountableElement,
            Duty,
            TimeDemandProfile,
            VehicleTypeStopAssignment,
            TrainComponentLabelAssignment,
            TrainNumber,
            FlexibleServiceProperties,
            JourneyPartCouple,
            CoupledJourney,
            JourneyPart,
            InterchangeRule,
            ServiceJourneyPatternInterchange,
            ServiceJourneyInterchange,
            DefaultInterchange,
            JourneyMeeting,
            SingleJourney,
            DatedSpecialService,
            NormalDatedVehicleJourney,
            DatedVehicleJourney,
            SpecialService,
            DeadRun,
            ServiceJourney1,
            DatedServiceJourney,
            TemplateServiceJourney,
            TemplateVehicleJourney,
            VehicleJourney1,
            PointOfInterestClassificationHierarchy,
            TimeDemandType,
            VehicleJourneyStopAssignment,
            FlexibleStopAssignment,
            NavigationPathAssignment,
            TrainStopAssignment,
            DynamicStopAssignment,
            PassengerStopAssignment,
            LogicalDisplay,
            LineNetwork,
            ModeRestrictionAssessment,
            RouteInstruction,
            TrainComponent,
            TrainElement,
            CompoundTrain,
            Train,
            CycleModelProfile,
            CarModelProfile,
            Whitelist,
            Blacklist,
            SchematicMap,
            PersonalModeOfOperation,
            AlternativeModeOfOperation1,
            VehiclePooling,
            VehicleSharing,
            VehicleRental,
            FlexibleOperation,
            ScheduledOperation,
            ChargingEquipmentProfile,
            VehicleEquipmentProfile,
            VehicleModel,
            Vehicle,
            PassengerCarryingRequirementsView,
            FacilityRequirement,
            VehicleManoeuvringRequirement,
            PassengerCarryingRequirement,
            SimpleVehicleType,
            VehicleType,
            TransportType1,
            EquipmentPosition,
            Level,
            AllowedLineDirection,
            DestinationDisplayVariant,
            DestinationDisplay,
            FlexibleLine,
            Line1,
            DeliveryVariant,
            Notice,
            OperationalContext,
            OnlineService,
            VehicleRentalService,
            VehicleSharingService,
            ChauffeuredVehicleService,
            CarPoolingService,
            TaxiService,
            AssistanceBookingService,
            CateringService,
            RetailService,
            MoneyService,
            HireService,
            CommunicationService,
            MeetingPointService,
            LostPropertyService,
            LeftLuggageService,
            ComplaintsService,
            CustomerService,
            LuggageService,
            AssistanceService,
            TicketingService,
            RetailDevice,
            BatteryEquipment,
            VehicleReleaseEquipment,
            RefuellingEquipment,
            VehicleChargingEquipment,
            CycleStorageEquipment,
            SeatingEquipment,
            ShelterEquipment,
            TrolleyStandEquipment,
            WaitingRoomEquipment,
            CrossingEquipment,
            QueueingEquipment,
            EntranceEquipment,
            RampEquipment,
            LiftEquipment,
            TravelatorEquipment,
            StaircaseEquipment,
            EscalatorEquipment,
            PlaceLighting,
            RoughSurface,
            GeneralSign,
            HeadingSign,
            PlaceSign,
            SignEquipment,
            PassengerInformationEquipment,
            RubbishDisposalEquipment,
            HelpPointEquipment,
            PassengerSafetyEquipment,
            SanitaryEquipment,
            TicketValidatorEquipment,
            TicketingEquipment,
            WheelchairVehicleEquipment,
            AccessVehicleEquipment,
            ComplexFeature,
            SimpleFeature,
            SpatialFeature,
            SingleJourneyPath,
            ServicePattern,
            NavigationPath,
            ServiceJourneyPattern,
            DeadRunJourneyPattern,
            JourneyPattern1,
            FlexibleRoute,
            Route1,
            TimingPattern,
            Connection,
            DefaultConnection,
            SiteConnection,
            Access,
            Contact,
            ControlCentre,
            OperatingDepartment,
            OrganisationalUnit,
            Department,
            OrganisationPart1,
            RetailConsortium,
            ServicedOrganisation,
            GeneralOrganisation,
            ManagementAgent,
            TravelAgent,
            OtherOrganisation,
            OnlineServiceOperator,
            Authority,
            Operator,
            VehicleMeetingLink,
            ServiceLink,
            SitePathLink,
            PathLink,
            RouteLink,
            TimingLink,
            WireElement,
            RoadElement,
            RailwayElement,
            ActivationLink,
            VehicleMeetingPoint,
            BorderPoint,
            FareScheduledStopPoint,
            ScheduledStopPoint,
            PathJunction,
            RoutePoint,
            ParkingPoint1,
            GaragePoint,
            ReliefPoint1,
            TimingPoint1,
            WireJunction,
            RoadJunction,
            RailwayJunction,
            TrafficControlPoint,
            BeaconPoint,
            ActivationPoint1,
            Point2,
            LineShape,
            TopographicProjection,
            ZoneProjection,
            ComplexFeatureProjection,
            LinkSequenceProjection,
            LinkProjection,
            PointProjection,
            CompositeFrame,
            MobilityJourneyFrame,
            MobilityServiceFrame,
            SalesTransactionFrame,
            FareFrame,
            DriverScheduleFrame,
            VehicleScheduleFrame,
            ServiceFrame,
            TimetableFrame,
            SiteFrame,
            InfrastructureFrame,
            GeneralFrame,
            ResourceFrame,
            ServiceCalendarFrame,
            UicOperatingPeriod,
            OperatingPeriod1,
            OperatingDay,
            ServiceCalendar,
            VehicleSharingPlaceAssignment,
            VehiclePoolingPlaceAssignment,
            TaxiServicePlaceAssignment,
            VehicleServicePlaceAssignment1,
            VehicleServicePlaceAssignment2,
            DynamicVehicleMeetingPointAssignment,
            VehicleMeetingPointAssignment1,
            VehicleMeetingPointAssignment2,
            VehicleAccessCredentialsAssignment,
            DistributionAssignment,
            SalesOfferPackageSubstitution,
            CustomerPurchaseParameterAssignment,
            SpecificParameterAssignment,
            GenericParameterAssignmentInContext,
            GenericParameterAssignment,
            ValidityParameterAssignment,
            AccessRightParameterAssignment1,
            JourneyAccounting,
            TimeDemandTypeAssignment,
            TransferRestriction,
            ServiceExclusion,
            DisplayAssignment,
            OvertakingPossibility,
            MeetingRestriction,
            RestrictedManoeuvre,
            VehicleTypeAtPoint,
            ActivationAssignment,
            SalesNoticeAssignment,
            NoticeAssignment1,
            CheckConstraintThroughput,
            CheckConstraintDelay,
            CheckConstraint,
            DayTypeAssignment,
            GroupOfTimebands,
            Timeband,
            FareDayType,
            OrganisationDayType,
            DayType1,
            PoolOfVehicles,
            GroupOfSingleJourneys,
            GroupOfDistributionChannels,
            GroupOfDistanceMatrixElements,
            PriceGroup1,
            StandardFareTable,
            FareTableInContext,
            FareTable1,
            GroupOfServices,
            RhythmicalJourneyGroup,
            HeadwayJourneyGroup,
            CrewBase,
            GroupOfTimingLinks,
            Network,
            GroupOfLines,
            GroupOfOperators,
            GroupOfPlaces,
            GroupOfLinkSequences,
            MobilityServiceConstraintZone,
            RoutingConstraintZone,
            StopArea,
            AccessZone,
            VehicleMeetingPlace1,
            VehiclePoolingMeetingPlace,
            VehicleMeetingPlace2,
            HailAndRideArea,
            FlexibleArea,
            FlexibleQuay,
            FlexibleStopPlace,
            Garage,
            EquipmentPlace,
            TaxiStand,
            VehicleStoppingPlace,
            BoardingPosition,
            AccessSpace,
            Quay1,
            PointOfInterestSpace,
            ParkingComponent,
            VehicleStoppingPosition,
            VehiclePoolingParkingArea,
            VehicleSharingParkingArea,
            TaxiParkingArea,
            ParkingArea1,
            MonitoredVehicleSharingParkingBay,
            VehiclePoolingParkingBay,
            VehicleSharingParkingBay,
            ParkingBay1,
            PointOfInterestVehicleEntrance,
            PointOfInterestEntrance,
            ParkingPassengerEntrance,
            ParkingEntranceForVehicles,
            StopPlaceVehicleEntrance,
            StopPlaceEntrance,
            Entrance,
            PointOfInterest,
            Parking,
            TaxiRank,
            StopPlace1,
            ServiceSite,
            TopographicPlace,
            Country,
            AddressablePlace,
            PostalAddress,
            RoadAddress,
            TransportAdministrativeZone,
            AdministrativeZone1,
            FareZone,
            TariffZone1,
            GeneralZone,
            Zone,
            GroupOfLinks,
            GroupOfPoints,
            Layer,
            GeneralGroupOfEntities,
            ResponsibilitySet,
            ValueSet,
            TypeOfFleet,
            ParkingBayStatus,
            TypeOfMediumAccessDevice,
            TypeOfMachineReadability,
            TypeOfProof,
            TypeOfConcession,
            ChargingMoment,
            TypeOfUsageParameter,
            TypeOfFareTable,
            TypeOfPricingRule,
            PriceUnit,
            TimingAlgorithmType,
            PurposeOfJourneyPartition,
            PointOfInterestClassification,
            TypeOfParking,
            TypeOfServiceFeature,
            Direction,
            TypeOfSecurityList,
            PurposeOfEquipmentProfile,
            TypeOfProductCategory,
            TypeOfPaymentMethod,
            ClassOfUse,
            Submode,
            OpenTransportMode,
            TypeOfCodespaceAssignment,
            TypeOfValidity,
            PurposeOfGrouping,
            Branding,
            DataSource,
            TypeOfMobilityService,
            TypeOfRetailDevice,
            CustomerAccountStatus,
            TypeOfCustomerAccount,
            TypeOfFareContractEntry,
            TypeOfFareContract,
            TypeOfTravelDocument,
            TypeOfSalesOfferPackage,
            TypeOfFareProduct,
            TypeOfFareStructureElement,
            TypeOfTariff,
            TypeOfAccessRightAssignment,
            TypeOfFareStructureFactor,
            TypeOfFlexibleService,
            TypeOfTimeDemandType,
            TypeOfPassengerInformationEquipment,
            TypeOfJourneyPattern,
            TypeOfActivation,
            TypeOfModeOfOperation,
            TypeOfPlug,
            TypeOfBatteryChemistry,
            TypeOfLine,
            TypeOfDeliveryVariant,
            TypeOfNotice,
            TypeOfCongestion,
            TypeOfFacility,
            TypeOfService,
            TypeOfEquipment,
            TypeOfFeature,
            TypeOfLinkSequence,
            TypeOfPlace,
            TypeOfTransfer,
            TypeOfOperation,
            TypeOfOrganisationPart,
            TypeOfOrganisation,
            TypeOfZone,
            TypeOfLink,
            TypeOfPoint,
            TypeOfProjection,
            TypeOfFrame,
            TypeOfResponsibilityRole,
            TypeOfEntity,
            TypeOfVersion,
            PassingTimeView,
            SimpleAvailabilityCondition,
            ValidDuring,
            AvailabilityCondition,
            ValidityRuleParameter,
            ValidityTrigger,
            ValidityCondition1,
            Version,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EntityInVersionInFrameRef",
                    "type": EntityInVersionInFrameRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Fleet",
                    "type": Fleet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "IndividualPassengerInfo",
                    "type": IndividualPassengerInfo,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingDriverInfo",
                    "type": VehiclePoolingDriverInfo,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "IndividualTraveller",
                    "type": IndividualTraveller,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayCondition",
                    "type": ParkingBayCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalAvailability",
                    "type": RentalAvailability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Smartcard",
                    "type": Smartcard,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EmvCard",
                    "type": EmvCard,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobileDevice",
                    "type": MobileDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MediumAccessDevice",
                    "type": MediumAccessDevice1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessCode",
                    "type": ServiceAccessCode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocument",
                    "type": TravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccount",
                    "type": CustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransaction",
                    "type": SalesTransaction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecification",
                    "type": OfferedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecification",
                    "type": RequestedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification",
                    "type": TravelSpecification1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification_",
                    "type": TravelSpecification2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractEntry_",
                    "type": FareContractEntry2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContract",
                    "type": FareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Customer",
                    "type": Customer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingTariff",
                    "type": ParkingTariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSalesOfferPackages",
                    "type": GroupOfSalesOfferPackages,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionChannel",
                    "type": DistributionChannel,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Tariff",
                    "type": Tariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackage",
                    "type": CustomerPurchasePackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackage",
                    "type": SalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethod",
                    "type": FulfilmentMethod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRule",
                    "type": CappingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementProduct",
                    "type": EntitlementProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplementProduct",
                    "type": SupplementProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProduct",
                    "type": PreassignedFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProduct",
                    "type": AmountOfPriceUnitProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRight",
                    "type": CappedDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRight",
                    "type": UsageDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProduct",
                    "type": ThirdPartyProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRight",
                    "type": SaleDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRight",
                    "type": ServiceAccessRight1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRight_",
                    "type": ServiceAccessRight2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeInterval",
                    "type": TimeInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactor",
                    "type": FareQuotaFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactor",
                    "type": FareDemandFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactor",
                    "type": QualityStructureFactor1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElement",
                    "type": ControllableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElement",
                    "type": ValidableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdditionalDriverOption",
                    "type": AdditionalDriverOption,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalOption",
                    "type": RentalOption,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalPenaltyPolicy",
                    "type": RentalPenaltyPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolerProfile",
                    "type": VehiclePoolerProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequired",
                    "type": SalesOfferPackageEntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGiven",
                    "type": SalesOfferPackageEntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStay",
                    "type": MinimumStay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Interchanging",
                    "type": Interchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Suspending",
                    "type": Suspending,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriod",
                    "type": UsageValidityPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUse",
                    "type": FrequencyOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimit",
                    "type": StepLimit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Routing",
                    "type": Routing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTrip",
                    "type": RoundTrip,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowance",
                    "type": LuggageAllowance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequired",
                    "type": EntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGiven",
                    "type": EntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicy",
                    "type": EligibilityChangePolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfile",
                    "type": CompanionProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicket",
                    "type": GroupTicket,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfile",
                    "type": CommercialProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfile",
                    "type": UserProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Subscribing",
                    "type": Subscribing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicy",
                    "type": PenaltyPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicy",
                    "type": ChargingPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Cancelling",
                    "type": Cancelling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reserving",
                    "type": Reserving,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindow",
                    "type": PurchaseWindow,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Transferability",
                    "type": Transferability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Replacing",
                    "type": Replacing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Refunding",
                    "type": Refunding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Exchanging",
                    "type": Exchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reselling",
                    "type": Reselling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalInterval",
                    "type": GeographicalInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraint",
                    "type": SeriesConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageElement",
                    "type": CustomerPurchasePackageElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBand",
                    "type": ParkingChargeBand,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageElement",
                    "type": SalesOfferPackageElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElement",
                    "type": FareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeStructureFactor",
                    "type": TimeStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnit",
                    "type": TimeUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElement",
                    "type": DistanceMatrixElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactor",
                    "type": GeographicalStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnit",
                    "type": GeographicalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareUnit",
                    "type": FareUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareInterval",
                    "type": FareInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureFactor",
                    "type": FareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingService",
                    "type": PricingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRuleInContext",
                    "type": LimitingRuleInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRule",
                    "type": LimitingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRule",
                    "type": DiscountingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRule",
                    "type": PricingRule1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonthValidityOffset",
                    "type": MonthValidityOffset,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Rounding",
                    "type": Rounding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingParameterSet",
                    "type": PricingParameterSet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefOpportunity",
                    "type": ReliefOpportunity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CourseOfJourneys",
                    "type": CourseOfJourneys,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePart",
                    "type": VehicleServicePart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleService",
                    "type": VehicleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlockPart",
                    "type": TrainBlockPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundBlock",
                    "type": CompoundBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockPart",
                    "type": BlockPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlock",
                    "type": TrainBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Block",
                    "type": Block,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTripTime",
                    "type": DriverTripTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTrip",
                    "type": DriverTrip,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DutyPart",
                    "type": DutyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccountableElement",
                    "type": AccountableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Duty",
                    "type": Duty,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandProfile",
                    "type": TimeDemandProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeStopAssignment",
                    "type": VehicleTypeStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentLabelAssignment",
                    "type": TrainComponentLabelAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumber",
                    "type": TrainNumber,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleServiceProperties",
                    "type": FlexibleServiceProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartCouple",
                    "type": JourneyPartCouple,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoupledJourney",
                    "type": CoupledJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPart",
                    "type": JourneyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRule",
                    "type": InterchangeRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternInterchange",
                    "type": ServiceJourneyPatternInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchange",
                    "type": ServiceJourneyInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultInterchange",
                    "type": DefaultInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyMeeting",
                    "type": JourneyMeeting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleJourney",
                    "type": SingleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialService",
                    "type": DatedSpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourney",
                    "type": NormalDatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourney",
                    "type": DatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialService",
                    "type": SpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRun",
                    "type": DeadRun,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourney",
                    "type": ServiceJourney1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedServiceJourney",
                    "type": DatedServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourney",
                    "type": TemplateServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateVehicleJourney",
                    "type": TemplateVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourney",
                    "type": VehicleJourney1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassificationHierarchy",
                    "type": PointOfInterestClassificationHierarchy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandType",
                    "type": TimeDemandType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyStopAssignment",
                    "type": VehicleJourneyStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopAssignment",
                    "type": FlexibleStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathAssignment",
                    "type": NavigationPathAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainStopAssignment",
                    "type": TrainStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignment",
                    "type": DynamicStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignment",
                    "type": PassengerStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LogicalDisplay",
                    "type": LogicalDisplay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineNetwork",
                    "type": LineNetwork,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ModeRestrictionAssessment",
                    "type": ModeRestrictionAssessment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteInstruction",
                    "type": RouteInstruction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponent",
                    "type": TrainComponent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElement",
                    "type": TrainElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrain",
                    "type": CompoundTrain,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Train",
                    "type": Train,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleModelProfile",
                    "type": CycleModelProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarModelProfile",
                    "type": CarModelProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Whitelist",
                    "type": Whitelist,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Blacklist",
                    "type": Blacklist,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SchematicMap",
                    "type": SchematicMap,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PersonalModeOfOperation",
                    "type": PersonalModeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlternativeModeOfOperation",
                    "type": AlternativeModeOfOperation1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePooling",
                    "type": VehiclePooling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharing",
                    "type": VehicleSharing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRental",
                    "type": VehicleRental,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleOperation",
                    "type": FlexibleOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledOperation",
                    "type": ScheduledOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingEquipmentProfile",
                    "type": ChargingEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentProfile",
                    "type": VehicleEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleModel",
                    "type": VehicleModel,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Vehicle",
                    "type": Vehicle,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirementsView",
                    "type": PassengerCarryingRequirementsView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilityRequirement",
                    "type": FacilityRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleManoeuvringRequirement",
                    "type": VehicleManoeuvringRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirement",
                    "type": PassengerCarryingRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleVehicleType",
                    "type": SimpleVehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleType",
                    "type": VehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportType",
                    "type": TransportType1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPosition",
                    "type": EquipmentPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Level",
                    "type": Level,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedLineDirection",
                    "type": AllowedLineDirection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayVariant",
                    "type": DestinationDisplayVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplay",
                    "type": DestinationDisplay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLine",
                    "type": FlexibleLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Line",
                    "type": Line1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeliveryVariant",
                    "type": DeliveryVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Notice",
                    "type": Notice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperationalContext",
                    "type": OperationalContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnlineService",
                    "type": OnlineService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalService",
                    "type": VehicleRentalService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingService",
                    "type": VehicleSharingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleService",
                    "type": ChauffeuredVehicleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingService",
                    "type": CarPoolingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiService",
                    "type": TaxiService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingService",
                    "type": AssistanceBookingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringService",
                    "type": CateringService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailService",
                    "type": RetailService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyService",
                    "type": MoneyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireService",
                    "type": HireService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationService",
                    "type": CommunicationService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointService",
                    "type": MeetingPointService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyService",
                    "type": LostPropertyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageService",
                    "type": LeftLuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsService",
                    "type": ComplaintsService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerService",
                    "type": CustomerService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageService",
                    "type": LuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceService",
                    "type": AssistanceService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingService",
                    "type": TicketingService,
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
                {
                    "name": "ComplexFeature",
                    "type": ComplexFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleFeature",
                    "type": SimpleFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpatialFeature",
                    "type": SpatialFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleJourneyPath",
                    "type": SingleJourneyPath,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePattern",
                    "type": ServicePattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPath",
                    "type": NavigationPath,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPattern",
                    "type": ServiceJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPattern",
                    "type": DeadRunJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPattern",
                    "type": JourneyPattern1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleRoute",
                    "type": FlexibleRoute,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Route",
                    "type": Route1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPattern",
                    "type": TimingPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Connection",
                    "type": Connection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultConnection",
                    "type": DefaultConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnection",
                    "type": SiteConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Access",
                    "type": Access,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Contact",
                    "type": Contact,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentre",
                    "type": ControlCentre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDepartment",
                    "type": OperatingDepartment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnit",
                    "type": OrganisationalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Department",
                    "type": Department,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPart",
                    "type": OrganisationPart1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailConsortium",
                    "type": RetailConsortium,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisation",
                    "type": ServicedOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisation",
                    "type": GeneralOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgent",
                    "type": ManagementAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgent",
                    "type": TravelAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisation",
                    "type": OtherOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnlineServiceOperator",
                    "type": OnlineServiceOperator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Authority",
                    "type": Authority,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Operator",
                    "type": Operator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingLink",
                    "type": VehicleMeetingLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLink",
                    "type": ServiceLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLink",
                    "type": PathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLink",
                    "type": RouteLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLink",
                    "type": TimingLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireElement",
                    "type": WireElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadElement",
                    "type": RoadElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayElement",
                    "type": RailwayElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLink",
                    "type": ActivationLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPoint",
                    "type": VehicleMeetingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BorderPoint",
                    "type": BorderPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPoint",
                    "type": FareScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPoint",
                    "type": ScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunction",
                    "type": PathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePoint",
                    "type": RoutePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPoint",
                    "type": ParkingPoint1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPoint",
                    "type": ReliefPoint1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPoint",
                    "type": TimingPoint1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireJunction",
                    "type": WireJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadJunction",
                    "type": RoadJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayJunction",
                    "type": RailwayJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPoint",
                    "type": TrafficControlPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPoint",
                    "type": BeaconPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPoint",
                    "type": ActivationPoint1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Point",
                    "type": Point2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineShape",
                    "type": LineShape,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicProjection",
                    "type": TopographicProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneProjection",
                    "type": ZoneProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeatureProjection",
                    "type": ComplexFeatureProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjection",
                    "type": LinkSequenceProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkProjection",
                    "type": LinkProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointProjection",
                    "type": PointProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompositeFrame",
                    "type": CompositeFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityJourneyFrame",
                    "type": MobilityJourneyFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceFrame",
                    "type": MobilityServiceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrame",
                    "type": SalesTransactionFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrame",
                    "type": FareFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrame",
                    "type": DriverScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrame",
                    "type": VehicleScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrame",
                    "type": ServiceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrame",
                    "type": TimetableFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrame",
                    "type": SiteFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrame",
                    "type": InfrastructureFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrame",
                    "type": GeneralFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrame",
                    "type": ResourceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrame",
                    "type": ServiceCalendarFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UicOperatingPeriod",
                    "type": UicOperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriod",
                    "type": OperatingPeriod1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDay",
                    "type": OperatingDay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendar",
                    "type": ServiceCalendar,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingPlaceAssignment",
                    "type": VehicleSharingPlaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingPlaceAssignment",
                    "type": VehiclePoolingPlaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServicePlaceAssignment",
                    "type": TaxiServicePlaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePlaceAssignment",
                    "type": VehicleServicePlaceAssignment1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePlaceAssignment_",
                    "type": VehicleServicePlaceAssignment2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicVehicleMeetingPointAssignment",
                    "type": DynamicVehicleMeetingPointAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointAssignment",
                    "type": VehicleMeetingPointAssignment1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointAssignment_",
                    "type": VehicleMeetingPointAssignment2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleAccessCredentialsAssignment",
                    "type": VehicleAccessCredentialsAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionAssignment",
                    "type": DistributionAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageSubstitution",
                    "type": SalesOfferPackageSubstitution,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchaseParameterAssignment",
                    "type": CustomerPurchaseParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecificParameterAssignment",
                    "type": SpecificParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityParameterAssignment",
                    "type": ValidityParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightParameterAssignment",
                    "type": AccessRightParameterAssignment1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyAccounting",
                    "type": JourneyAccounting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandTypeAssignment",
                    "type": TimeDemandTypeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransferRestriction",
                    "type": TransferRestriction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceExclusion",
                    "type": ServiceExclusion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DisplayAssignment",
                    "type": DisplayAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OvertakingPossibility",
                    "type": OvertakingPossibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingRestriction",
                    "type": MeetingRestriction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RestrictedManoeuvre",
                    "type": RestrictedManoeuvre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeAtPoint",
                    "type": VehicleTypeAtPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationAssignment",
                    "type": ActivationAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesNoticeAssignment",
                    "type": SalesNoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignment",
                    "type": NoticeAssignment1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintThroughput",
                    "type": CheckConstraintThroughput,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintDelay",
                    "type": CheckConstraintDelay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraint",
                    "type": CheckConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeAssignment",
                    "type": DayTypeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimebands",
                    "type": GroupOfTimebands,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Timeband",
                    "type": Timeband,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDayType",
                    "type": FareDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationDayType",
                    "type": OrganisationDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayType",
                    "type": DayType1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PoolOfVehicles",
                    "type": PoolOfVehicles,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSingleJourneys",
                    "type": GroupOfSingleJourneys,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannels",
                    "type": GroupOfDistributionChannels,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElements",
                    "type": GroupOfDistanceMatrixElements,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroup",
                    "type": PriceGroup1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StandardFareTable",
                    "type": StandardFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableInContext",
                    "type": FareTableInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTable",
                    "type": FareTable1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfServices",
                    "type": GroupOfServices,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroup",
                    "type": RhythmicalJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadwayJourneyGroup",
                    "type": HeadwayJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrewBase",
                    "type": CrewBase,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimingLinks",
                    "type": GroupOfTimingLinks,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Network",
                    "type": Network,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLines",
                    "type": GroupOfLines,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperators",
                    "type": GroupOfOperators,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfPlaces",
                    "type": GroupOfPlaces,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinkSequences",
                    "type": GroupOfLinkSequences,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceConstraintZone",
                    "type": MobilityServiceConstraintZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingConstraintZone",
                    "type": RoutingConstraintZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopArea",
                    "type": StopArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZone",
                    "type": AccessZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPlace",
                    "type": VehicleMeetingPlace1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingMeetingPlace",
                    "type": VehiclePoolingMeetingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPlace_",
                    "type": VehicleMeetingPlace2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HailAndRideArea",
                    "type": HailAndRideArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleArea",
                    "type": FlexibleArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuay",
                    "type": FlexibleQuay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopPlace",
                    "type": FlexibleStopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Garage",
                    "type": Garage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPlace",
                    "type": EquipmentPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiStand",
                    "type": TaxiStand,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPlace",
                    "type": VehicleStoppingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPosition",
                    "type": BoardingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpace",
                    "type": AccessSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Quay",
                    "type": Quay1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpace",
                    "type": PointOfInterestSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingComponent",
                    "type": ParkingComponent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPosition",
                    "type": VehicleStoppingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingArea",
                    "type": VehiclePoolingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingArea",
                    "type": VehicleSharingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingArea",
                    "type": TaxiParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingArea",
                    "type": ParkingArea1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonitoredVehicleSharingParkingBay",
                    "type": MonitoredVehicleSharingParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingBay",
                    "type": VehiclePoolingParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingBay",
                    "type": VehicleSharingParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBay",
                    "type": ParkingBay1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestVehicleEntrance",
                    "type": PointOfInterestVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntrance",
                    "type": PointOfInterestEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPassengerEntrance",
                    "type": ParkingPassengerEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehicles",
                    "type": ParkingEntranceForVehicles,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceVehicleEntrance",
                    "type": StopPlaceVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceEntrance",
                    "type": StopPlaceEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Entrance",
                    "type": Entrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterest",
                    "type": PointOfInterest,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Parking",
                    "type": Parking,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiRank",
                    "type": TaxiRank,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlace",
                    "type": StopPlace1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSite",
                    "type": ServiceSite,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlace",
                    "type": TopographicPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Country",
                    "type": Country,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressablePlace",
                    "type": AddressablePlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZone",
                    "type": TransportAdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZone",
                    "type": AdministrativeZone1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZone",
                    "type": FareZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZone",
                    "type": TariffZone1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralZone",
                    "type": GeneralZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Zone",
                    "type": Zone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinks",
                    "type": GroupOfLinks,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfPoints",
                    "type": GroupOfPoints,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Layer",
                    "type": Layer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralGroupOfEntities",
                    "type": GeneralGroupOfEntities,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilitySet",
                    "type": ResponsibilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValueSet",
                    "type": ValueSet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFleet",
                    "type": TypeOfFleet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayStatus",
                    "type": ParkingBayStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMediumAccessDevice",
                    "type": TypeOfMediumAccessDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMachineReadability",
                    "type": TypeOfMachineReadability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProof",
                    "type": TypeOfProof,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfConcession",
                    "type": TypeOfConcession,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingMoment",
                    "type": ChargingMoment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfUsageParameter",
                    "type": TypeOfUsageParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareTable",
                    "type": TypeOfFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPricingRule",
                    "type": TypeOfPricingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceUnit",
                    "type": PriceUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingAlgorithmType",
                    "type": TimingAlgorithmType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfJourneyPartition",
                    "type": PurposeOfJourneyPartition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassification",
                    "type": PointOfInterestClassification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfParking",
                    "type": TypeOfParking,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceFeature",
                    "type": TypeOfServiceFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Direction",
                    "type": Direction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSecurityList",
                    "type": TypeOfSecurityList,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfEquipmentProfile",
                    "type": PurposeOfEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProductCategory",
                    "type": TypeOfProductCategory,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPaymentMethod",
                    "type": TypeOfPaymentMethod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ClassOfUse",
                    "type": ClassOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Submode",
                    "type": Submode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OpenTransportMode",
                    "type": OpenTransportMode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCodespaceAssignment",
                    "type": TypeOfCodespaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfValidity",
                    "type": TypeOfValidity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfGrouping",
                    "type": PurposeOfGrouping,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Branding",
                    "type": Branding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DataSource",
                    "type": DataSource,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMobilityService",
                    "type": TypeOfMobilityService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRetailDevice",
                    "type": TypeOfRetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatus",
                    "type": CustomerAccountStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccount",
                    "type": TypeOfCustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntry",
                    "type": TypeOfFareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContract",
                    "type": TypeOfFareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocument",
                    "type": TypeOfTravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackage",
                    "type": TypeOfSalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProduct",
                    "type": TypeOfFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureElement",
                    "type": TypeOfFareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariff",
                    "type": TypeOfTariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignment",
                    "type": TypeOfAccessRightAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureFactor",
                    "type": TypeOfFareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFlexibleService",
                    "type": TypeOfFlexibleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTimeDemandType",
                    "type": TypeOfTimeDemandType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPassengerInformationEquipment",
                    "type": TypeOfPassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfJourneyPattern",
                    "type": TypeOfJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfActivation",
                    "type": TypeOfActivation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfModeOfOperation",
                    "type": TypeOfModeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlug",
                    "type": TypeOfPlug,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfBatteryChemistry",
                    "type": TypeOfBatteryChemistry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLine",
                    "type": TypeOfLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeliveryVariant",
                    "type": TypeOfDeliveryVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfNotice",
                    "type": TypeOfNotice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCongestion",
                    "type": TypeOfCongestion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacility",
                    "type": TypeOfFacility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfService",
                    "type": TypeOfService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipment",
                    "type": TypeOfEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFeature",
                    "type": TypeOfFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkSequence",
                    "type": TypeOfLinkSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlace",
                    "type": TypeOfPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTransfer",
                    "type": TypeOfTransfer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOperation",
                    "type": TypeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationPart",
                    "type": TypeOfOrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisation",
                    "type": TypeOfOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfZone",
                    "type": TypeOfZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLink",
                    "type": TypeOfLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPoint",
                    "type": TypeOfPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProjection",
                    "type": TypeOfProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrame",
                    "type": TypeOfFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfResponsibilityRole",
                    "type": TypeOfResponsibilityRole,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEntity",
                    "type": TypeOfEntity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfVersion",
                    "type": TypeOfVersion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeView",
                    "type": PassingTimeView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleAvailabilityCondition",
                    "type": SimpleAvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidDuring",
                    "type": ValidDuring,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityCondition",
                    "type": AvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameter",
                    "type": ValidityRuleParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTrigger",
                    "type": ValidityTrigger,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityCondition",
                    "type": ValidityCondition1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Version",
                    "type": Version,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
