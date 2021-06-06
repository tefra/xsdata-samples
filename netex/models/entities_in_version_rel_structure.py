from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .abstract_group_member import AbstractGroupMember
from .access import Access
from .access_equipment import AccessEquipment
from .access_right_in_product import AccessRightInProduct
from .access_right_parameter_assignment_1 import AccessRightParameterAssignment1
from .access_right_parameter_assignment_2 import AccessRightParameterAssignment2
from .access_space import AccessSpace
from .access_vehicle_equipment import AccessVehicleEquipment
from .access_zone import AccessZone
from .accessibility_assessment import AccessibilityAssessment
from .accommodation import Accommodation
from .accountable_element import AccountableElement
from .activation_assignment import ActivationAssignment
from .activation_link import ActivationLink
from .activation_point_1 import ActivationPoint1
from .activation_point_2 import ActivationPoint2
from .actual_vehicle_equipment import ActualVehicleEquipment
from .address import Address
from .addressable_place import AddressablePlace
from .administrative_zone_2 import AdministrativeZone2
from .administrative_zone_version_structure import (
    AdministrativeZone1,
    TransportAdministrativeZone,
)
from .allowed_line_direction import AllowedLineDirection
from .alternative_name import AlternativeName
from .alternative_texts_rel_structure import (
    AlternativeText,
    AvailabilityCondition,
    DayType1,
    DayType2,
    FareDayType,
    OperatingDay,
    OrganisationDayType,
    SimpleAvailabilityCondition,
    ValidDuring,
    ValidityCondition1,
    ValidityCondition2,
    ValidityRuleParameter,
    ValidityTrigger,
)
from .amount_of_price_unit_product import AmountOfPriceUnitProduct
from .assignment_1 import Assignment1
from .assignment_2 import Assignment2
from .assistance_booking_service import AssistanceBookingService
from .assistance_service import AssistanceService
from .authority import Authority
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
from .capping_rule_price import CappingRulePrice
from .catering_service import CateringService
from .cell_2 import Cell2
from .cell_versioned_child_structure import (
    Cell1,
    FareTableInContext,
    FareTable1,
    ParkingChargeBand,
    ParkingPrice,
    PriceGroup1,
)
from .charging_moment import ChargingMoment
from .charging_policy import ChargingPolicy
from .check_constraint import CheckConstraint
from .check_constraint_delay import CheckConstraintDelay
from .check_constraint_throughput import CheckConstraintThroughput
from .class_of_use import ClassOfUse
from .codespace_assignment import CodespaceAssignment
from .commercial_profile import CommercialProfile
from .commercial_profile_eligibility import CommercialProfileEligibility
from .common_frame import CommonFrame
from .common_version_frame_structure import CommonVersionFrameStructure
from .communication_service import CommunicationService
from .companion_profile import CompanionProfile
from .complaints_service import ComplaintsService
from .complex_feature_projection import ComplexFeatureProjection
from .compound_block import CompoundBlock
from .compound_train import CompoundTrain
from .connection import Connection
from .containment_aggregation_structure import ContainmentAggregationStructure
from .control_centre import ControlCentre
from .controllable_element import ControllableElement
from .controllable_element_in_sequence import ControllableElementInSequence
from .controllable_element_price import ControllableElementPrice
from .country import Country
from .coupled_journey import CoupledJourney
from .course_of_journeys import CourseOfJourneys
from .crew_base import CrewBase
from .crossing_equipment import CrossingEquipment
from .customer import Customer
from .customer_account import CustomerAccount
from .customer_account_security_listing import CustomerAccountSecurityListing
from .customer_account_status import CustomerAccountStatus
from .customer_eligibility_1 import CustomerEligibility1
from .customer_eligibility_2 import CustomerEligibility2
from .customer_purchase_package import CustomerPurchasePackage
from .customer_purchase_package_element import CustomerPurchasePackageElement
from .customer_purchase_package_price import CustomerPurchasePackagePrice
from .customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment
from .customer_security_listing import CustomerSecurityListing
from .customer_service import CustomerService
from .cycle_storage_equipment import CycleStorageEquipment
from .data_managed_object import DataManagedObject
from .data_managed_object_view import DataManagedObjectView
from .data_source import DataSource
from .dated_passing_time import DatedPassingTime
from .dated_service_journey import DatedServiceJourney
from .dated_special_service import DatedSpecialService
from .dated_vehicle_journey import DatedVehicleJourney
from .day_type_assignment import DayTypeAssignment
from .dead_run import DeadRun
from .dead_run_journey_pattern import DeadRunJourneyPattern
from .default_connection import DefaultConnection
from .default_dead_run_run_time import DefaultDeadRunRunTime
from .default_interchange import DefaultInterchange
from .default_service_journey_run_time import DefaultServiceJourneyRunTime
from .delivery_variant import DeliveryVariant
from .department import Department
from .destination_display import DestinationDisplay
from .destination_display_variant import DestinationDisplayVariant
from .direction import Direction
from .discounting_rule import DiscountingRule
from .display_assignment import DisplayAssignment
from .distance_matrix_element import DistanceMatrixElement
from .distance_matrix_element_price import DistanceMatrixElementPrice
from .distribution_assignment import DistributionAssignment
from .distribution_channel import DistributionChannel
from .driver_schedule_frame import DriverScheduleFrame
from .driver_trip import DriverTrip
from .driver_trip_time import DriverTripTime
from .duty import Duty
from .duty_part import DutyPart
from .dynamic_stop_assignment import DynamicStopAssignment
from .eligibility_change_policy import EligibilityChangePolicy
from .entitlement_given import EntitlementGiven
from .entitlement_product import EntitlementProduct
from .entitlement_required import EntitlementRequired
from .entity_in_version import EntityInVersion
from .entity_structure import EntityStructure
from .entrance import Entrance
from .entrance_equipment import EntranceEquipment
from .equipment import Equipment
from .equipment_place import EquipmentPlace
from .equipment_position import EquipmentPosition
from .escalator_equipment import EscalatorEquipment
from .estimated_passing_time import EstimatedPassingTime
from .exchanging import Exchanging
from .facility_requirement import FacilityRequirement
from .fare_contract import FareContract
from .fare_contract_entry_1 import FareContractEntry1
from .fare_contract_entry_2 import FareContractEntry2
from .fare_contract_security_listing import FareContractSecurityListing
from .fare_demand_factor import FareDemandFactor
from .fare_element_in_sequence import FareElementInSequence
from .fare_frame import FareFrame
from .fare_interval import FareInterval
from .fare_point_in_pattern import FarePointInPattern
from .fare_price_1 import FarePrice1
from .fare_price_2 import FarePrice2
from .fare_product_1 import FareProduct1
from .fare_product_2 import FareProduct2
from .fare_product_price import FareProductPrice
from .fare_quota_factor import FareQuotaFactor
from .fare_scheduled_stop_point import FareScheduledStopPoint
from .fare_structure_element import FareStructureElement
from .fare_structure_element_in_sequence import FareStructureElementInSequence
from .fare_structure_element_price import FareStructureElementPrice
from .fare_structure_factor import FareStructureFactor
from .fare_table_2 import FareTable2
from .fare_unit import FareUnit
from .fare_zone import FareZone
from .flexible_area import FlexibleArea
from .flexible_line import FlexibleLine
from .flexible_link_properties import FlexibleLinkProperties
from .flexible_point_properties import FlexiblePointProperties
from .flexible_quay import FlexibleQuay
from .flexible_route import FlexibleRoute
from .flexible_service_properties import FlexibleServiceProperties
from .flexible_stop_assignment import FlexibleStopAssignment
from .flexible_stop_place import FlexibleStopPlace
from .frequency_of_use import FrequencyOfUse
from .fulfilment_method import FulfilmentMethod
from .fulfilment_method_price import FulfilmentMethodPrice
from .garage import Garage
from .garage_point import GaragePoint
from .general_frame_member import GeneralFrameMember
from .general_group_of_entities import GeneralGroupOfEntities
from .general_organisation import GeneralOrganisation
from .general_sign import GeneralSign
from .general_zone import GeneralZone
from .generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from .geographical_interval import GeographicalInterval
from .geographical_interval_price import GeographicalIntervalPrice
from .geographical_structure_factor import GeographicalStructureFactor
from .geographical_unit import GeographicalUnit
from .geographical_unit_price import GeographicalUnitPrice
from .group_constraint_member import GroupConstraintMember
from .group_of_distance_matrix_elements import GroupOfDistanceMatrixElements
from .group_of_distribution_channels import GroupOfDistributionChannels
from .group_of_entities import GroupOfEntities
from .group_of_lines import GroupOfLines
from .group_of_link_sequences import GroupOfLinkSequences
from .group_of_links import GroupOfLinks
from .group_of_operators import GroupOfOperators
from .group_of_places import GroupOfPlaces
from .group_of_points import GroupOfPoints
from .group_of_sales_offer_packages import GroupOfSalesOfferPackages
from .group_of_services import GroupOfServices
from .group_of_timebands import GroupOfTimebands
from .group_of_timing_links import GroupOfTimingLinks
from .group_ticket import GroupTicket
from .hail_and_ride_area import HailAndRideArea
from .heading_sign import HeadingSign
from .headway_journey_group import HeadwayJourneyGroup
from .help_point_equipment import HelpPointEquipment
from .hire_service import HireService
from .infrastructure_frame import InfrastructureFrame
from .infrastructure_link_1 import InfrastructureLink1
from .infrastructure_link_2 import InfrastructureLink2
from .infrastructure_link_restriction import InfrastructureLinkRestriction
from .infrastructure_point import InfrastructurePoint
from .installed_equipment import InstalledEquipment
from .interchange_1 import Interchange1
from .interchange_2 import Interchange2
from .interchange_rule import InterchangeRule
from .interchange_rule_timing import InterchangeRuleTiming
from .interchanging import Interchanging
from .journey_1 import Journey1
from .journey_2 import Journey2
from .journey_accounting import JourneyAccounting
from .journey_frequency_group import JourneyFrequencyGroup
from .journey_headway import JourneyHeadway
from .journey_layover import JourneyLayover
from .journey_meeting import JourneyMeeting
from .journey_part import JourneyPart
from .journey_part_couple import JourneyPartCouple
from .journey_part_position import JourneyPartPosition
from .journey_pattern_2 import JourneyPattern2
from .journey_pattern_headway import JourneyPatternHeadway
from .journey_pattern_layover import JourneyPatternLayover
from .journey_pattern_run_time import JourneyPatternRunTime
from .journey_pattern_wait_time import JourneyPatternWaitTime
from .journey_run_time import JourneyRunTime
from .journey_timing import JourneyTiming
from .journey_wait_time import JourneyWaitTime
from .layer import Layer
from .left_luggage_service import LeftLuggageService
from .level import Level
from .lift_equipment import LiftEquipment
from .limiting_rule import LimitingRule
from .limiting_rule_in_context import LimitingRuleInContext
from .line_1 import Line1
from .line_2 import Line2
from .line_network import LineNetwork
from .line_shape import LineShape
from .link import Link
from .link_in_journey_pattern import LinkInJourneyPattern
from .link_in_link_sequence import LinkInLinkSequence
from .link_on_section import LinkOnSection
from .link_projection import LinkProjection
from .link_sequence import LinkSequence
from .link_sequence_projection import LinkSequenceProjection
from .link_sequence_version_structure import (
    JourneyPattern1,
    SectionInSequence,
)
from .local_service import LocalService
from .log import Log
from .log_entry import LogEntry
from .logical_display import LogicalDisplay
from .lost_property_service import LostPropertyService
from .luggage_allowance import LuggageAllowance
from .luggage_locker_equipment import LuggageLockerEquipment
from .luggage_service import LuggageService
from .management_agent import ManagementAgent
from .meeting_point_service import MeetingPointService
from .meeting_restriction import MeetingRestriction
from .minimum_stay import MinimumStay
from .money_service import MoneyService
from .month_validity_offset import MonthValidityOffset
from .navigation_path import NavigationPath
from .navigation_path_assignment import NavigationPathAssignment
from .network import Network
from .network_restriction import NetworkRestriction
from .normal_dated_vehicle_journey import NormalDatedVehicleJourney
from .notice import Notice
from .notice_assignment_1 import NoticeAssignment1
from .notice_assignment_2 import NoticeAssignment2
from .observed_passing_time import ObservedPassingTime
from .offered_travel_specification import OfferedTravelSpecification
from .onboard_stay import OnboardStay
from .open_transport_mode import OpenTransportMode
from .operating_department import OperatingDepartment
from .operating_period import OperatingPeriod
from .operational_context import OperationalContext
from .operator import Operator
from .organisation_1 import Organisation1
from .organisation_2 import Organisation2
from .organisation_part_1 import OrganisationPart1
from .organisation_part_2 import OrganisationPart2
from .organisational_unit import OrganisationalUnit
from .other_organisation import OtherOrganisation
from .overtaking_possibility import OvertakingPossibility
from .parking import Parking
from .parking_area import ParkingArea
from .parking_bay import ParkingBay
from .parking_capacity import ParkingCapacity
from .parking_component import ParkingComponent
from .parking_entrance_for_vehicles import ParkingEntranceForVehicles
from .parking_passenger_entrance import ParkingPassengerEntrance
from .parking_point_1 import ParkingPoint1
from .parking_point_2 import ParkingPoint2
from .parking_properties import ParkingProperties
from .parking_tariff import ParkingTariff
from .passenger_carrying_requirement import PassengerCarryingRequirement
from .passenger_carrying_requirements_view import PassengerCarryingRequirementsView
from .passenger_equipment import PassengerEquipment
from .passenger_information_equipment import PassengerInformationEquipment
from .passenger_safety_equipment import PassengerSafetyEquipment
from .passenger_stop_assignment import PassengerStopAssignment
from .passing_time import PassingTime
from .passing_time_view import PassingTimeView
from .path_junction import PathJunction
from .path_link import PathLink
from .path_link_in_sequence import PathLinkInSequence
from .penalty_policy import PenaltyPolicy
from .place import Place
from .place_equipment import PlaceEquipment
from .place_in_sequence import PlaceInSequence
from .place_lighting import PlaceLighting
from .place_sign import PlaceSign
from .point_2 import Point2
from .point_in_journey_pattern import PointInJourneyPattern
from .point_in_link_sequence import PointInLinkSequence
from .point_of_interest import PointOfInterest
from .point_of_interest_classification import PointOfInterestClassification
from .point_of_interest_classification_hierarchy import PointOfInterestClassificationHierarchy
from .point_of_interest_component import PointOfInterestComponent
from .point_of_interest_entrance import PointOfInterestEntrance
from .point_of_interest_space import PointOfInterestSpace
from .point_of_interest_vehicle_entrance import PointOfInterestVehicleEntrance
from .point_on_line_section import PointOnLineSection
from .point_on_link import PointOnLink
from .point_on_route import PointOnRoute
from .point_on_section_1 import PointOnSection1
from .point_on_section_2 import PointOnSection2
from .point_projection import PointProjection
from .postal_address import PostalAddress
from .preassigned_fare_product import PreassignedFareProduct
from .price_group_2 import PriceGroup2
from .price_unit import PriceUnit
from .priceable_object_1 import PriceableObject1
from .priceable_object_2 import PriceableObject2
from .pricing_parameter_set import PricingParameterSet
from .pricing_rule_1 import PricingRule1
from .pricing_rule_2 import PricingRule2
from .pricing_service import PricingService
from .projection import Projection
from .purchase_window import PurchaseWindow
from .purpose_of_equipment_profile import PurposeOfEquipmentProfile
from .purpose_of_grouping import PurposeOfGrouping
from .purpose_of_journey_partition import PurposeOfJourneyPartition
from .quality_structure_factor_1 import QualityStructureFactor1
from .quality_structure_factor_2 import QualityStructureFactor2
from .quality_structure_factor_price import QualityStructureFactorPrice
from .quay import Quay
from .queueing_equipment import QueueingEquipment
from .railway_element import RailwayElement
from .railway_junction import RailwayJunction
from .ramp_equipment import RampEquipment
from .refunding import Refunding
from .relief_opportunity import ReliefOpportunity
from .relief_point_1 import ReliefPoint1
from .relief_point_2 import ReliefPoint2
from .replacing import Replacing
from .requested_travel_specification import RequestedTravelSpecification
from .reselling import Reselling
from .reserving import Reserving
from .residential_qualification import ResidentialQualification
from .residential_qualification_eligibility import ResidentialQualificationEligibility
from .resource_frame import ResourceFrame
from .responsibility_role import ResponsibilityRole
from .responsibility_set import ResponsibilitySet
from .restricted_manoeuvre import RestrictedManoeuvre
from .retail_consortium import RetailConsortium
from .retail_device import RetailDevice
from .retail_device_security_listing import RetailDeviceSecurityListing
from .retail_service import RetailService
from .rhythmical_journey_group import RhythmicalJourneyGroup
from .road_address import RoadAddress
from .road_element import RoadElement
from .road_junction import RoadJunction
from .rough_surface import RoughSurface
from .round_trip import RoundTrip
from .rounding import Rounding
from .route_1 import Route1
from .route_2 import Route2
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
from .sales_offer_package_entitlement_given import SalesOfferPackageEntitlementGiven
from .sales_offer_package_entitlement_required import SalesOfferPackageEntitlementRequired
from .sales_offer_package_price import SalesOfferPackagePrice
from .sales_offer_package_substitution import SalesOfferPackageSubstitution
from .sales_transaction import SalesTransaction
from .sales_transaction_frame import SalesTransactionFrame
from .sanitary_equipment import SanitaryEquipment
from .scheduled_stop_point import ScheduledStopPoint
from .schematic_map import SchematicMap
from .seating_equipment import SeatingEquipment
from .security_list import SecurityList
from .security_listing_1 import SecurityListing1
from .security_listing_2 import SecurityListing2
from .series_constraint import SeriesConstraint
from .series_constraint_price import SeriesConstraintPrice
from .service_access_right_1 import ServiceAccessRight1
from .service_access_right_2 import ServiceAccessRight2
from .service_calendar import ServiceCalendar
from .service_calendar_frame import ServiceCalendarFrame
from .service_exclusion import ServiceExclusion
from .service_frame import ServiceFrame
from .service_journey_1 import ServiceJourney1
from .service_journey_2 import ServiceJourney2
from .service_journey_interchange import ServiceJourneyInterchange
from .service_journey_pattern import ServiceJourneyPattern
from .service_journey_pattern_interchange import ServiceJourneyPatternInterchange
from .service_link import ServiceLink
from .service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from .service_pattern import ServicePattern
from .service_site import ServiceSite
from .serviced_organisation import ServicedOrganisation
from .shelter_equipment import ShelterEquipment
from .sign_equipment import SignEquipment
from .site import Site
from .site_component import SiteComponent
from .site_connection import SiteConnection
from .site_element import SiteElement
from .site_equipment import SiteEquipment
from .site_frame import SiteFrame
from .site_path_link import SitePathLink
from .special_service import SpecialService
from .specific_parameter_assignment_version_structure import SpecificParameterAssignment
from .stair_equipment import StairEquipment
from .stair_flight import StairFlight
from .staircase_equipment import StaircaseEquipment
from .standard_fare_table import StandardFareTable
from .start_time_at_stop_point import StartTimeAtStopPoint
from .step_limit import StepLimit
from .stop_area import StopArea
from .stop_assignment import StopAssignment
from .stop_place import StopPlace
from .stop_place_component import StopPlaceComponent
from .stop_place_entrance import StopPlaceEntrance
from .stop_place_space import StopPlaceSpace
from .stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from .stop_point_in_journey_pattern import StopPointInJourneyPattern
from .submode import Submode
from .subscribing import Subscribing
from .supplement_product import SupplementProduct
from .suspending import Suspending
from .target_passing_time import TargetPassingTime
from .tariff import Tariff
from .tariff_zone_1 import TariffZone1
from .tariff_zone_2 import TariffZone2
from .template_service_journey import TemplateServiceJourney
from .template_vehicle_journey import TemplateVehicleJourney
from .third_party_product import ThirdPartyProduct
from .ticket_validator_equipment import TicketValidatorEquipment
from .ticketing_equipment import TicketingEquipment
from .ticketing_service import TicketingService
from .time_demand_profile import TimeDemandProfile
from .time_demand_profile_member import TimeDemandProfileMember
from .time_demand_type import TimeDemandType
from .time_demand_type_assignment import TimeDemandTypeAssignment
from .time_interval import TimeInterval
from .time_interval_price import TimeIntervalPrice
from .time_structure_factor import TimeStructureFactor
from .time_unit import TimeUnit
from .time_unit_price import TimeUnitPrice
from .timeband import Timeband
from .timetable_frame import TimetableFrame
from .timetabled_passing_time import TimetabledPassingTime
from .timing_algorithm_type import TimingAlgorithmType
from .timing_link import TimingLink
from .timing_link_in_journey_pattern import TimingLinkInJourneyPattern
from .timing_pattern import TimingPattern
from .timing_point_1 import TimingPoint1
from .timing_point_2 import TimingPoint2
from .timing_point_in_journey_pattern import TimingPointInJourneyPattern
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
from .transfer import Transfer
from .transfer_restriction import TransferRestriction
from .transferability import Transferability
from .transport_organisation import TransportOrganisation
from .travel_agent import TravelAgent
from .travel_document import TravelDocument
from .travel_document_security_listing import TravelDocumentSecurityListing
from .travel_specification_1 import TravelSpecification1
from .travel_specification_2 import TravelSpecification2
from .travelator_equipment import TravelatorEquipment
from .trolley_stand_equipment import TrolleyStandEquipment
from .turnaround_time_limit_time import TurnaroundTimeLimitTime
from .type_of_access_right_assignment import TypeOfAccessRightAssignment
from .type_of_activation import TypeOfActivation
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
from .type_of_flexible_service import TypeOfFlexibleService
from .type_of_journey_pattern import TypeOfJourneyPattern
from .type_of_line import TypeOfLine
from .type_of_link import TypeOfLink
from .type_of_link_sequence import TypeOfLinkSequence
from .type_of_machine_readability import TypeOfMachineReadability
from .type_of_notice import TypeOfNotice
from .type_of_operation import TypeOfOperation
from .type_of_organisation import TypeOfOrganisation
from .type_of_organisation_part import TypeOfOrganisationPart
from .type_of_passenger_information_equipment import TypeOfPassengerInformationEquipment
from .type_of_payment_method import TypeOfPaymentMethod
from .type_of_place import TypeOfPlace
from .type_of_point import TypeOfPoint
from .type_of_pricing_rule import TypeOfPricingRule
from .type_of_product_category import TypeOfProductCategory
from .type_of_projection import TypeOfProjection
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
from .type_of_value import TypeOfValue
from .type_of_version import TypeOfVersion
from .type_of_zone import TypeOfZone
from .types_of_frame_rel_structure import TypeOfFrame
from .uic_operating_period import UicOperatingPeriod
from .usage_discount_right import UsageDiscountRight
from .usage_parameter_1 import UsageParameter1
from .usage_parameter_2 import UsageParameter2
from .usage_parameter_price import UsageParameterPrice
from .usage_validity_period import UsageValidityPeriod
from .user_profile import UserProfile
from .user_profile_eligibility import UserProfileEligibility
from .validable_element import ValidableElement
from .validable_element_price import ValidableElementPrice
from .validity_parameter_assignment import ValidityParameterAssignment
from .value_set import ValueSet
from .vehicle import Vehicle
from .vehicle_charging_equipment import VehicleChargingEquipment
from .vehicle_entrance import VehicleEntrance
from .vehicle_equipment_profile import VehicleEquipmentProfile
from .vehicle_journey_1 import VehicleJourney1
from .vehicle_journey_2 import VehicleJourney2
from .vehicle_journey_headway import VehicleJourneyHeadway
from .vehicle_journey_layover import VehicleJourneyLayover
from .vehicle_journey_run_time import VehicleJourneyRunTime
from .vehicle_journey_stop_assignment import VehicleJourneyStopAssignment
from .vehicle_journey_wait_time import VehicleJourneyWaitTime
from .vehicle_manoeuvring_requirement import VehicleManoeuvringRequirement
from .vehicle_model import VehicleModel
from .vehicle_position_alignment import VehiclePositionAlignment
from .vehicle_quay_alignment import VehicleQuayAlignment
from .vehicle_requirement import VehicleRequirement
from .vehicle_schedule_frame import VehicleScheduleFrame
from .vehicle_service import VehicleService
from .vehicle_service_part import VehicleServicePart
from .vehicle_stopping_place import VehicleStoppingPlace
from .vehicle_stopping_position import VehicleStoppingPosition
from .vehicle_type import VehicleType
from .vehicle_type_at_point import VehicleTypeAtPoint
from .vehicle_type_preference import VehicleTypePreference
from .vehicle_type_stop_assignment import VehicleTypeStopAssignment
from .version import Version
from .version_frame import VersionFrame
from .versioned_child import VersionedChild
from .waiting_equipment import WaitingEquipment
from .waiting_room_equipment import WaitingRoomEquipment
from .wheelchair_vehicle_equipment import WheelchairVehicleEquipment
from .whitelist import Whitelist
from .wire_element import WireElement
from .wire_junction import WireJunction
from .zone import Zone
from .zone_projection import ZoneProjection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitiesInVersionRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "entitiesInVersion_RelStructure"

    residential_qualification_eligibility: List[ResidentialQualificationEligibility] = field(
        default_factory=list,
        metadata={
            "name": "ResidentialQualificationEligibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    commercial_profile_eligibility: List[CommercialProfileEligibility] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfileEligibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    user_profile_eligibility: List[UserProfileEligibility] = field(
        default_factory=list,
        metadata={
            "name": "UserProfileEligibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_eligibility: List[CustomerEligibility1] = field(
        default_factory=list,
        metadata={
            "name": "CustomerEligibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_customer_eligibility: List[CustomerEligibility2] = field(
        default_factory=list,
        metadata={
            "name": "CustomerEligibility_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    residential_qualification: List[ResidentialQualification] = field(
        default_factory=list,
        metadata={
            "name": "ResidentialQualification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_right_in_product: List[AccessRightInProduct] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightInProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_structure_element_in_sequence: List[FareStructureElementInSequence] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    start_time_at_stop_point: List[StartTimeAtStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "StartTimeAtStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    controllable_element_in_sequence: List[ControllableElementInSequence] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_element_in_sequence: List[FareElementInSequence] = field(
        default_factory=list,
        metadata={
            "name": "FareElementInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    cell: List[Cell1] = field(
        default_factory=list,
        metadata={
            "name": "Cell",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_cell: List[Cell2] = field(
        default_factory=list,
        metadata={
            "name": "Cell_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_purchase_package_price: List[CustomerPurchasePackagePrice] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackagePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_price: List[ParkingPrice] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_price: List[SalesOfferPackagePrice] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackagePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fulfilment_method_price: List[FulfilmentMethodPrice] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    capping_rule_price: List[CappingRulePrice] = field(
        default_factory=list,
        metadata={
            "name": "CappingRulePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_product_price: List[FareProductPrice] = field(
        default_factory=list,
        metadata={
            "name": "FareProductPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_structure_element_price: List[FareStructureElementPrice] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_interval_price: List[TimeIntervalPrice] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_unit_price: List[TimeUnitPrice] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnitPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    quality_structure_factor_price: List[QualityStructureFactorPrice] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactorPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    controllable_element_price: List[ControllableElementPrice] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validable_element_price: List[ValidableElementPrice] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_parameter_price: List[UsageParameterPrice] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    distance_matrix_element_price: List[DistanceMatrixElementPrice] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    geographical_interval_price: List[GeographicalIntervalPrice] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    geographical_unit_price: List[GeographicalUnitPrice] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnitPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    series_constraint_price: List[SeriesConstraintPrice] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_price: List[FarePrice1] = field(
        default_factory=list,
        metadata={
            "name": "FarePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_fare_price: List[FarePrice2] = field(
        default_factory=list,
        metadata={
            "name": "FarePrice_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    default_dead_run_run_time: List[DefaultDeadRunRunTime] = field(
        default_factory=list,
        metadata={
            "name": "DefaultDeadRunRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    default_service_journey_run_time: List[DefaultServiceJourneyRunTime] = field(
        default_factory=list,
        metadata={
            "name": "DefaultServiceJourneyRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_demand_profile_member: List[TimeDemandProfileMember] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandProfileMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_part_position: List[JourneyPartPosition] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    estimated_passing_time: List[EstimatedPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    observed_passing_time: List[ObservedPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "ObservedPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    target_passing_time: List[TargetPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "TargetPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    dated_passing_time: List[DatedPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "DatedPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timetabled_passing_time: List[TimetabledPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    passing_time: List[PassingTime] = field(
        default_factory=list,
        metadata={
            "name": "PassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    interchange_rule_timing: List[InterchangeRuleTiming] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRuleTiming",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_capacity: List[ParkingCapacity] = field(
        default_factory=list,
        metadata={
            "name": "ParkingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_properties: List[ParkingProperties] = field(
        default_factory=list,
        metadata={
            "name": "ParkingProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_type_preference: List[VehicleTypePreference] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypePreference",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_position_alignment: List[VehiclePositionAlignment] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePositionAlignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_quay_alignment: List[VehicleQuayAlignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleQuayAlignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stair_flight: List[StairFlight] = field(
        default_factory=list,
        metadata={
            "name": "StairFlight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_point_properties: List[FlexiblePointProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_link_properties: List[FlexibleLinkProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLinkProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_pattern_headway: List[JourneyPatternHeadway] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_pattern_layover: List[JourneyPatternLayover] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternLayover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_pattern_run_time: List[JourneyPatternRunTime] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_pattern_wait_time: List[JourneyPatternWaitTime] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    turnaround_time_limit_time: List[TurnaroundTimeLimitTime] = field(
        default_factory=list,
        metadata={
            "name": "TurnaroundTimeLimitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_journey_layover: List[VehicleJourneyLayover] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyLayover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_journey_run_time: List[VehicleJourneyRunTime] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_journey_wait_time: List[VehicleJourneyWaitTime] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_journey_headway: List[VehicleJourneyHeadway] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_headway: List[JourneyHeadway] = field(
        default_factory=list,
        metadata={
            "name": "JourneyHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_layover: List[JourneyLayover] = field(
        default_factory=list,
        metadata={
            "name": "JourneyLayover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_run_time: List[JourneyRunTime] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_wait_time: List[JourneyWaitTime] = field(
        default_factory=list,
        metadata={
            "name": "JourneyWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_timing: List[JourneyTiming] = field(
        default_factory=list,
        metadata={
            "name": "JourneyTiming",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    travel_document_security_listing: List[TravelDocumentSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocumentSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    retail_device_security_listing: List[RetailDeviceSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_contract_security_listing: List[FareContractSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "FareContractSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_security_listing: List[CustomerSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "CustomerSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_account_security_listing: List[CustomerAccountSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    security_listing: List[SecurityListing1] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_security_listing: List[SecurityListing2] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListing_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    onboard_stay: List[OnboardStay] = field(
        default_factory=list,
        metadata={
            "name": "OnboardStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    accommodation: List[Accommodation] = field(
        default_factory=list,
        metadata={
            "name": "Accommodation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_link_in_journey_pattern: List[ServiceLinkInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLinkInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    path_link_in_sequence: List[PathLinkInSequence] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    link_in_journey_pattern: List[LinkInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "LinkInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timing_link_in_journey_pattern: List[TimingLinkInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "TimingLinkInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    link_in_link_sequence: List[LinkInLinkSequence] = field(
        default_factory=list,
        metadata={
            "name": "LinkInLinkSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_point_in_pattern: List[FarePointInPattern] = field(
        default_factory=list,
        metadata={
            "name": "FarePointInPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_point_in_journey_pattern: List[StopPointInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "StopPointInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    place_in_sequence: List[PlaceInSequence] = field(
        default_factory=list,
        metadata={
            "name": "PlaceInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_in_journey_pattern: List[PointInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "PointInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_on_route: List[PointOnRoute] = field(
        default_factory=list,
        metadata={
            "name": "PointOnRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timing_point_in_journey_pattern: List[TimingPointInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "TimingPointInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_on_line_section: List[PointOnLineSection] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLineSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_on_section: List[PointOnSection1] = field(
        default_factory=list,
        metadata={
            "name": "PointOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_point_on_section: List[PointOnSection2] = field(
        default_factory=list,
        metadata={
            "name": "PointOnSection_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_in_link_sequence: List[PointInLinkSequence] = field(
        default_factory=list,
        metadata={
            "name": "PointInLinkSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    section_in_sequence: List[SectionInSequence] = field(
        default_factory=list,
        metadata={
            "name": "SectionInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    link_on_section: List[LinkOnSection] = field(
        default_factory=list,
        metadata={
            "name": "LinkOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    codespace_assignment: List[CodespaceAssignment] = field(
        default_factory=list,
        metadata={
            "name": "CodespaceAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_on_link: List[PointOnLink] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    accessibility_assessment: List[AccessibilityAssessment] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    alternative_name: List[AlternativeName] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_constraint_member: List[GroupConstraintMember] = field(
        default_factory=list,
        metadata={
            "name": "GroupConstraintMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    abstract_group_member: List[AbstractGroupMember] = field(
        default_factory=list,
        metadata={
            "name": "AbstractGroupMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    alternative_text: List[AlternativeText] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    versioned_child: List[VersionedChild] = field(
        default_factory=list,
        metadata={
            "name": "VersionedChild",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    travel_document: List[TravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_account: List[CustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_transaction: List[SalesTransaction] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransaction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    offered_travel_specification: List[OfferedTravelSpecification] = field(
        default_factory=list,
        metadata={
            "name": "OfferedTravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    requested_travel_specification: List[RequestedTravelSpecification] = field(
        default_factory=list,
        metadata={
            "name": "RequestedTravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    travel_specification: List[TravelSpecification1] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_travel_specification: List[TravelSpecification2] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_contract_entry: List[FareContractEntry1] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_fare_contract_entry: List[FareContractEntry2] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntry_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_contract: List[FareContract] = field(
        default_factory=list,
        metadata={
            "name": "FareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer: List[Customer] = field(
        default_factory=list,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_tariff: List[ParkingTariff] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_sales_offer_packages: List[GroupOfSalesOfferPackages] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSalesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    distribution_channel: List[DistributionChannel] = field(
        default_factory=list,
        metadata={
            "name": "DistributionChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    tariff: List[Tariff] = field(
        default_factory=list,
        metadata={
            "name": "Tariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_purchase_package: List[CustomerPurchasePackage] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package: List[SalesOfferPackage] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fulfilment_method: List[FulfilmentMethod] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    capping_rule: List[CappingRule] = field(
        default_factory=list,
        metadata={
            "name": "CappingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entitlement_product: List[EntitlementProduct] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    supplement_product: List[SupplementProduct] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    preassigned_fare_product: List[PreassignedFareProduct] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    amount_of_price_unit_product: List[AmountOfPriceUnitProduct] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    capped_discount_right: List[CappedDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_discount_right: List[UsageDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    third_party_product: List[ThirdPartyProduct] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sale_discount_right: List[SaleDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_product: List[FareProduct1] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_fare_product: List[FareProduct2] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_access_right: List[ServiceAccessRight1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAccessRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_service_access_right: List[ServiceAccessRight2] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAccessRight_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_interval: List[TimeInterval] = field(
        default_factory=list,
        metadata={
            "name": "TimeInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_quota_factor: List[FareQuotaFactor] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_demand_factor: List[FareDemandFactor] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    quality_structure_factor: List[QualityStructureFactor1] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_quality_structure_factor: List[QualityStructureFactor2] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactor_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    controllable_element: List[ControllableElement] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validable_element: List[ValidableElement] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_entitlement_required: List[SalesOfferPackageEntitlementRequired] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_entitlement_given: List[SalesOfferPackageEntitlementGiven] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementGiven",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    minimum_stay: List[MinimumStay] = field(
        default_factory=list,
        metadata={
            "name": "MinimumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    interchanging: List[Interchanging] = field(
        default_factory=list,
        metadata={
            "name": "Interchanging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    suspending: List[Suspending] = field(
        default_factory=list,
        metadata={
            "name": "Suspending",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_validity_period: List[UsageValidityPeriod] = field(
        default_factory=list,
        metadata={
            "name": "UsageValidityPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    frequency_of_use: List[FrequencyOfUse] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    step_limit: List[StepLimit] = field(
        default_factory=list,
        metadata={
            "name": "StepLimit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    routing: List[Routing] = field(
        default_factory=list,
        metadata={
            "name": "Routing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    round_trip: List[RoundTrip] = field(
        default_factory=list,
        metadata={
            "name": "RoundTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    luggage_allowance: List[LuggageAllowance] = field(
        default_factory=list,
        metadata={
            "name": "LuggageAllowance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entitlement_required: List[EntitlementRequired] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entitlement_given: List[EntitlementGiven] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGiven",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    eligibility_change_policy: List[EligibilityChangePolicy] = field(
        default_factory=list,
        metadata={
            "name": "EligibilityChangePolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    companion_profile: List[CompanionProfile] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_ticket: List[GroupTicket] = field(
        default_factory=list,
        metadata={
            "name": "GroupTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    commercial_profile: List[CommercialProfile] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    user_profile: List[UserProfile] = field(
        default_factory=list,
        metadata={
            "name": "UserProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    subscribing: List[Subscribing] = field(
        default_factory=list,
        metadata={
            "name": "Subscribing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    penalty_policy: List[PenaltyPolicy] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    charging_policy: List[ChargingPolicy] = field(
        default_factory=list,
        metadata={
            "name": "ChargingPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    cancelling: List[Cancelling] = field(
        default_factory=list,
        metadata={
            "name": "Cancelling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    reserving: List[Reserving] = field(
        default_factory=list,
        metadata={
            "name": "Reserving",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    purchase_window: List[PurchaseWindow] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transferability: List[Transferability] = field(
        default_factory=list,
        metadata={
            "name": "Transferability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    replacing: List[Replacing] = field(
        default_factory=list,
        metadata={
            "name": "Replacing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    refunding: List[Refunding] = field(
        default_factory=list,
        metadata={
            "name": "Refunding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    exchanging: List[Exchanging] = field(
        default_factory=list,
        metadata={
            "name": "Exchanging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    reselling: List[Reselling] = field(
        default_factory=list,
        metadata={
            "name": "Reselling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_parameter: List[UsageParameter1] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_usage_parameter: List[UsageParameter2] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    geographical_interval: List[GeographicalInterval] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    series_constraint: List[SeriesConstraint] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_purchase_package_element: List[CustomerPurchasePackageElement] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_charge_band: List[ParkingChargeBand] = field(
        default_factory=list,
        metadata={
            "name": "ParkingChargeBand",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_element: List[SalesOfferPackageElement] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_structure_element: List[FareStructureElement] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_structure_factor: List[TimeStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "TimeStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_unit: List[TimeUnit] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    distance_matrix_element: List[DistanceMatrixElement] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    geographical_structure_factor: List[GeographicalStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    geographical_unit: List[GeographicalUnit] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_unit: List[FareUnit] = field(
        default_factory=list,
        metadata={
            "name": "FareUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_interval: List[FareInterval] = field(
        default_factory=list,
        metadata={
            "name": "FareInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_structure_factor: List[FareStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    priceable_object: List[PriceableObject1] = field(
        default_factory=list,
        metadata={
            "name": "PriceableObject",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_priceable_object: List[PriceableObject2] = field(
        default_factory=list,
        metadata={
            "name": "PriceableObject_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    pricing_service: List[PricingService] = field(
        default_factory=list,
        metadata={
            "name": "PricingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    limiting_rule_in_context: List[LimitingRuleInContext] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRuleInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    limiting_rule: List[LimitingRule] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    discounting_rule: List[DiscountingRule] = field(
        default_factory=list,
        metadata={
            "name": "DiscountingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    pricing_rule: List[PricingRule1] = field(
        default_factory=list,
        metadata={
            "name": "PricingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_pricing_rule: List[PricingRule2] = field(
        default_factory=list,
        metadata={
            "name": "PricingRule_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    month_validity_offset: List[MonthValidityOffset] = field(
        default_factory=list,
        metadata={
            "name": "MonthValidityOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    rounding: List[Rounding] = field(
        default_factory=list,
        metadata={
            "name": "Rounding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    pricing_parameter_set: List[PricingParameterSet] = field(
        default_factory=list,
        metadata={
            "name": "PricingParameterSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    relief_opportunity: List[ReliefOpportunity] = field(
        default_factory=list,
        metadata={
            "name": "ReliefOpportunity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    course_of_journeys: List[CourseOfJourneys] = field(
        default_factory=list,
        metadata={
            "name": "CourseOfJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_service_part: List[VehicleServicePart] = field(
        default_factory=list,
        metadata={
            "name": "VehicleServicePart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_service: List[VehicleService] = field(
        default_factory=list,
        metadata={
            "name": "VehicleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train_block_part: List[TrainBlockPart] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    compound_block: List[CompoundBlock] = field(
        default_factory=list,
        metadata={
            "name": "CompoundBlock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    block_part: List[BlockPart] = field(
        default_factory=list,
        metadata={
            "name": "BlockPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train_block: List[TrainBlock] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    block: List[Block] = field(
        default_factory=list,
        metadata={
            "name": "Block",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    driver_trip_time: List[DriverTripTime] = field(
        default_factory=list,
        metadata={
            "name": "DriverTripTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    driver_trip: List[DriverTrip] = field(
        default_factory=list,
        metadata={
            "name": "DriverTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    duty_part: List[DutyPart] = field(
        default_factory=list,
        metadata={
            "name": "DutyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    accountable_element: List[AccountableElement] = field(
        default_factory=list,
        metadata={
            "name": "AccountableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    duty: List[Duty] = field(
        default_factory=list,
        metadata={
            "name": "Duty",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_demand_profile: List[TimeDemandProfile] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_service_properties: List[FlexibleServiceProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleServiceProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_type_stop_assignment: List[VehicleTypeStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train_component_label_assignment: List[TrainComponentLabelAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentLabelAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train_number: List[TrainNumber] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    dated_special_service: List[DatedSpecialService] = field(
        default_factory=list,
        metadata={
            "name": "DatedSpecialService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    normal_dated_vehicle_journey: List[NormalDatedVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "NormalDatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    dated_vehicle_journey: List[DatedVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    special_service: List[SpecialService] = field(
        default_factory=list,
        metadata={
            "name": "SpecialService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    dead_run: List[DeadRun] = field(
        default_factory=list,
        metadata={
            "name": "DeadRun",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_journey: List[ServiceJourney1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    dated_service_journey: List[DatedServiceJourney] = field(
        default_factory=list,
        metadata={
            "name": "DatedServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    template_service_journey: List[TemplateServiceJourney] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_service_journey: List[ServiceJourney2] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourney_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    template_vehicle_journey: List[TemplateVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "TemplateVehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_journey: List[VehicleJourney1] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_vehicle_journey: List[VehicleJourney2] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourney_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey: List[Journey1] = field(
        default_factory=list,
        metadata={
            "name": "Journey",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_journey: List[Journey2] = field(
        default_factory=list,
        metadata={
            "name": "Journey_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_part_couple: List[JourneyPartCouple] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartCouple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    coupled_journey: List[CoupledJourney] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_part: List[JourneyPart] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    interchange_rule: List[InterchangeRule] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    interchange: List[Interchange1] = field(
        default_factory=list,
        metadata={
            "name": "Interchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_journey_pattern_interchange: List[ServiceJourneyPatternInterchange] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_journey_interchange: List[ServiceJourneyInterchange] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    default_interchange: List[DefaultInterchange] = field(
        default_factory=list,
        metadata={
            "name": "DefaultInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_interchange: List[Interchange2] = field(
        default_factory=list,
        metadata={
            "name": "Interchange_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_meeting: List[JourneyMeeting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyMeeting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_classification_hierarchy: List[PointOfInterestClassificationHierarchy] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationHierarchy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_demand_type: List[TimeDemandType] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_stop_assignment: List[FlexibleStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_journey_stop_assignment: List[VehicleJourneyStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    navigation_path_assignment: List[NavigationPathAssignment] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPathAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train_stop_assignment: List[TrainStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TrainStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    dynamic_stop_assignment: List[DynamicStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DynamicStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    passenger_stop_assignment: List[PassengerStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_assignment: List[StopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "StopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    logical_display: List[LogicalDisplay] = field(
        default_factory=list,
        metadata={
            "name": "LogicalDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    level: List[Level] = field(
        default_factory=list,
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    line_network: List[LineNetwork] = field(
        default_factory=list,
        metadata={
            "name": "LineNetwork",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    route_instruction: List[RouteInstruction] = field(
        default_factory=list,
        metadata={
            "name": "RouteInstruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    allowed_line_direction: List[AllowedLineDirection] = field(
        default_factory=list,
        metadata={
            "name": "AllowedLineDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    destination_display_variant: List[DestinationDisplayVariant] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    destination_display: List[DestinationDisplay] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_line: List[FlexibleLine] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLine",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    line: List[Line1] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_line: List[Line2] = field(
        default_factory=list,
        metadata={
            "name": "Line_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    operational_context: List[OperationalContext] = field(
        default_factory=list,
        metadata={
            "name": "OperationalContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train_component: List[TrainComponent] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train_element: List[TrainElement] = field(
        default_factory=list,
        metadata={
            "name": "TrainElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    compound_train: List[CompoundTrain] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrain",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train: List[Train] = field(
        default_factory=list,
        metadata={
            "name": "Train",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_equipment_profile: List[VehicleEquipmentProfile] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEquipmentProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_model: List[VehicleModel] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    passenger_carrying_requirements_view: List[PassengerCarryingRequirementsView] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCarryingRequirementsView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    facility_requirement: List[FacilityRequirement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_manoeuvring_requirement: List[VehicleManoeuvringRequirement] = field(
        default_factory=list,
        metadata={
            "name": "VehicleManoeuvringRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    passenger_carrying_requirement: List[PassengerCarryingRequirement] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCarryingRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_requirement: List[VehicleRequirement] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_type: List[VehicleType] = field(
        default_factory=list,
        metadata={
            "name": "VehicleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    whitelist: List[Whitelist] = field(
        default_factory=list,
        metadata={
            "name": "Whitelist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    blacklist: List[Blacklist] = field(
        default_factory=list,
        metadata={
            "name": "Blacklist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    security_list: List[SecurityList] = field(
        default_factory=list,
        metadata={
            "name": "SecurityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    schematic_map: List[SchematicMap] = field(
        default_factory=list,
        metadata={
            "name": "SchematicMap",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    delivery_variant: List[DeliveryVariant] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    notice: List[Notice] = field(
        default_factory=list,
        metadata={
            "name": "Notice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    equipment_position: List[EquipmentPosition] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
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
    service_pattern: List[ServicePattern] = field(
        default_factory=list,
        metadata={
            "name": "ServicePattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    navigation_path: List[NavigationPath] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_journey_pattern: List[ServiceJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    dead_run_journey_pattern: List[DeadRunJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_pattern: List[JourneyPattern1] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_journey_pattern: List[JourneyPattern2] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPattern_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_route: List[FlexibleRoute] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    route: List[Route1] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_route: List[Route2] = field(
        default_factory=list,
        metadata={
            "name": "Route_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timing_pattern: List[TimingPattern] = field(
        default_factory=list,
        metadata={
            "name": "TimingPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    link_sequence: List[LinkSequence] = field(
        default_factory=list,
        metadata={
            "name": "LinkSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    default_connection: List[DefaultConnection] = field(
        default_factory=list,
        metadata={
            "name": "DefaultConnection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_connection: List[SiteConnection] = field(
        default_factory=list,
        metadata={
            "name": "SiteConnection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access: List[Access] = field(
        default_factory=list,
        metadata={
            "name": "Access",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transfer: List[Transfer] = field(
        default_factory=list,
        metadata={
            "name": "Transfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    organisational_unit: List[OrganisationalUnit] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationalUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    control_centre: List[ControlCentre] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    operating_department: List[OperatingDepartment] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDepartment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    department: List[Department] = field(
        default_factory=list,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    organisation_part: List[OrganisationPart1] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_organisation_part: List[OrganisationPart2] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPart_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    retail_consortium: List[RetailConsortium] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortium",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    authority: List[Authority] = field(
        default_factory=list,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    operator: List[Operator] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transport_organisation: List[TransportOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisation_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    serviced_organisation: List[ServicedOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "ServicedOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    general_organisation: List[GeneralOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "GeneralOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    management_agent: List[ManagementAgent] = field(
        default_factory=list,
        metadata={
            "name": "ManagementAgent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    travel_agent: List[TravelAgent] = field(
        default_factory=list,
        metadata={
            "name": "TravelAgent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    other_organisation: List[OtherOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "OtherOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    organisation: List[Organisation1] = field(
        default_factory=list,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_organisation: List[Organisation2] = field(
        default_factory=list,
        metadata={
            "name": "Organisation_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_link: List[ServiceLink] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_path_link: List[SitePathLink] = field(
        default_factory=list,
        metadata={
            "name": "SitePathLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    path_link: List[PathLink] = field(
        default_factory=list,
        metadata={
            "name": "PathLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    route_link: List[RouteLink] = field(
        default_factory=list,
        metadata={
            "name": "RouteLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timing_link: List[TimingLink] = field(
        default_factory=list,
        metadata={
            "name": "TimingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    infrastructure_link: List[InfrastructureLink1] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    wire_element: List[WireElement] = field(
        default_factory=list,
        metadata={
            "name": "WireElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    road_element: List[RoadElement] = field(
        default_factory=list,
        metadata={
            "name": "RoadElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    railway_element: List[RailwayElement] = field(
        default_factory=list,
        metadata={
            "name": "RailwayElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_infrastructure_link: List[InfrastructureLink2] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLink_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    activation_link: List[ActivationLink] = field(
        default_factory=list,
        metadata={
            "name": "ActivationLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    link: List[Link] = field(
        default_factory=list,
        metadata={
            "name": "Link",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    border_point: List[BorderPoint] = field(
        default_factory=list,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_scheduled_stop_point: List[FareScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    scheduled_stop_point: List[ScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    path_junction: List[PathJunction] = field(
        default_factory=list,
        metadata={
            "name": "PathJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    route_point: List[RoutePoint] = field(
        default_factory=list,
        metadata={
            "name": "RoutePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_point: List[ParkingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    garage_point: List[GaragePoint] = field(
        default_factory=list,
        metadata={
            "name": "GaragePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_parking_point: List[ParkingPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    relief_point: List[ReliefPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_relief_point: List[ReliefPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timing_point: List[TimingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_timing_point: List[TimingPoint2] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    wire_junction: List[WireJunction] = field(
        default_factory=list,
        metadata={
            "name": "WireJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    road_junction: List[RoadJunction] = field(
        default_factory=list,
        metadata={
            "name": "RoadJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    railway_junction: List[RailwayJunction] = field(
        default_factory=list,
        metadata={
            "name": "RailwayJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    infrastructure_point: List[InfrastructurePoint] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructurePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    traffic_control_point: List[TrafficControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "TrafficControlPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    beacon_point: List[BeaconPoint] = field(
        default_factory=list,
        metadata={
            "name": "BeaconPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    activation_point: List[ActivationPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_activation_point: List[ActivationPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point: List[Point2] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    line_shape: List[LineShape] = field(
        default_factory=list,
        metadata={
            "name": "LineShape",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    topographic_projection: List[TopographicProjection] = field(
        default_factory=list,
        metadata={
            "name": "TopographicProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    zone_projection: List[ZoneProjection] = field(
        default_factory=list,
        metadata={
            "name": "ZoneProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    complex_feature_projection: List[ComplexFeatureProjection] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeatureProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    link_sequence_projection: List[LinkSequenceProjection] = field(
        default_factory=list,
        metadata={
            "name": "LinkSequenceProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    link_projection: List[LinkProjection] = field(
        default_factory=list,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_projection: List[PointProjection] = field(
        default_factory=list,
        metadata={
            "name": "PointProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    projection: List[Projection] = field(
        default_factory=list,
        metadata={
            "name": "Projection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    log_entry: List[LogEntry] = field(
        default_factory=list,
        metadata={
            "name": "LogEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    log: List[Log] = field(
        default_factory=list,
        metadata={
            "name": "Log",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    composite_frame: List["CompositeFrame"] = field(
        default_factory=list,
        metadata={
            "name": "CompositeFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_transaction_frame: List[SalesTransactionFrame] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_frame: List[FareFrame] = field(
        default_factory=list,
        metadata={
            "name": "FareFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    driver_schedule_frame: List[DriverScheduleFrame] = field(
        default_factory=list,
        metadata={
            "name": "DriverScheduleFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_schedule_frame: List[VehicleScheduleFrame] = field(
        default_factory=list,
        metadata={
            "name": "VehicleScheduleFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_frame: List[ServiceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timetable_frame: List[TimetableFrame] = field(
        default_factory=list,
        metadata={
            "name": "TimetableFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_frame: List[SiteFrame] = field(
        default_factory=list,
        metadata={
            "name": "SiteFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    infrastructure_frame: List[InfrastructureFrame] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    general_frame: List["GeneralFrame"] = field(
        default_factory=list,
        metadata={
            "name": "GeneralFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    resource_frame: List[ResourceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ResourceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_calendar_frame: List[ServiceCalendarFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    common_frame: List[CommonFrame] = field(
        default_factory=list,
        metadata={
            "name": "CommonFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    version_frame: List[VersionFrame] = field(
        default_factory=list,
        metadata={
            "name": "VersionFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    uic_operating_period: List[UicOperatingPeriod] = field(
        default_factory=list,
        metadata={
            "name": "UicOperatingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    operating_period: List[OperatingPeriod] = field(
        default_factory=list,
        metadata={
            "name": "OperatingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    operating_day: List[OperatingDay] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_calendar: List[ServiceCalendar] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendar",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    distribution_assignment: List[DistributionAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DistributionAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_substitution: List[SalesOfferPackageSubstitution] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageSubstitution",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_purchase_parameter_assignment: List[CustomerPurchaseParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchaseParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    specific_parameter_assignment: List[SpecificParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    generic_parameter_assignment_in_context: List[GenericParameterAssignmentInContext] = field(
        default_factory=list,
        metadata={
            "name": "GenericParameterAssignmentInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    generic_parameter_assignment: List[GenericParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "GenericParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validity_parameter_assignment: List[ValidityParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ValidityParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_right_parameter_assignment: List[AccessRightParameterAssignment1] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_access_right_parameter_assignment: List[AccessRightParameterAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightParameterAssignment_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_accounting: List[JourneyAccounting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyAccounting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_demand_type_assignment: List[TimeDemandTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transfer_restriction: List[TransferRestriction] = field(
        default_factory=list,
        metadata={
            "name": "TransferRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_exclusion: List[ServiceExclusion] = field(
        default_factory=list,
        metadata={
            "name": "ServiceExclusion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    display_assignment: List[DisplayAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DisplayAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    check_constraint_throughput: List[CheckConstraintThroughput] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintThroughput",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    check_constraint_delay: List[CheckConstraintDelay] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    check_constraint: List[CheckConstraint] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    overtaking_possibility: List[OvertakingPossibility] = field(
        default_factory=list,
        metadata={
            "name": "OvertakingPossibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    meeting_restriction: List[MeetingRestriction] = field(
        default_factory=list,
        metadata={
            "name": "MeetingRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    restricted_manoeuvre: List[RestrictedManoeuvre] = field(
        default_factory=list,
        metadata={
            "name": "RestrictedManoeuvre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    infrastructure_link_restriction: List[InfrastructureLinkRestriction] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLinkRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_type_at_point: List[VehicleTypeAtPoint] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeAtPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    network_restriction: List[NetworkRestriction] = field(
        default_factory=list,
        metadata={
            "name": "NetworkRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    activation_assignment: List[ActivationAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ActivationAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_notice_assignment: List[SalesNoticeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SalesNoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    notice_assignment: List[NoticeAssignment1] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_notice_assignment: List[NoticeAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignment_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    day_type_assignment: List[DayTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    assignment: List[Assignment1] = field(
        default_factory=list,
        metadata={
            "name": "Assignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_assignment: List[Assignment2] = field(
        default_factory=list,
        metadata={
            "name": "Assignment_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_timebands: List[GroupOfTimebands] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimebands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timeband: List[Timeband] = field(
        default_factory=list,
        metadata={
            "name": "Timeband",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_day_type: List[FareDayType] = field(
        default_factory=list,
        metadata={
            "name": "FareDayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    organisation_day_type: List[OrganisationDayType] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationDayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    day_type: List[DayType1] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_day_type: List[DayType2] = field(
        default_factory=list,
        metadata={
            "name": "DayType_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_distribution_channels: List[GroupOfDistributionChannels] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistributionChannels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_distance_matrix_elements: List[GroupOfDistanceMatrixElements] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    price_group: List[PriceGroup1] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_price_group: List[PriceGroup2] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    standard_fare_table: List[StandardFareTable] = field(
        default_factory=list,
        metadata={
            "name": "StandardFareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_table_in_context: List[FareTableInContext] = field(
        default_factory=list,
        metadata={
            "name": "FareTableInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_table: List[FareTable1] = field(
        default_factory=list,
        metadata={
            "name": "FareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_fare_table: List[FareTable2] = field(
        default_factory=list,
        metadata={
            "name": "FareTable_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_services: List[GroupOfServices] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    rhythmical_journey_group: List[RhythmicalJourneyGroup] = field(
        default_factory=list,
        metadata={
            "name": "RhythmicalJourneyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    headway_journey_group: List[HeadwayJourneyGroup] = field(
        default_factory=list,
        metadata={
            "name": "HeadwayJourneyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_frequency_group: List[JourneyFrequencyGroup] = field(
        default_factory=list,
        metadata={
            "name": "JourneyFrequencyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    network: List[Network] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_lines: List[GroupOfLines] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    crew_base: List[CrewBase] = field(
        default_factory=list,
        metadata={
            "name": "CrewBase",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_timing_links: List[GroupOfTimingLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_operators: List[GroupOfOperators] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_places: List[GroupOfPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_link_sequences: List[GroupOfLinkSequences] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinkSequences",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    routing_constraint_zone: List[RoutingConstraintZone] = field(
        default_factory=list,
        metadata={
            "name": "RoutingConstraintZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_area: List[StopArea] = field(
        default_factory=list,
        metadata={
            "name": "StopArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_zone: List[AccessZone] = field(
        default_factory=list,
        metadata={
            "name": "AccessZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    hail_and_ride_area: List[HailAndRideArea] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_area: List[FlexibleArea] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_quay: List[FlexibleQuay] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleQuay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    flexible_stop_place: List[FlexibleStopPlace] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_component: List[PointOfInterestComponent] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_stopping_place: List[VehicleStoppingPlace] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    boarding_position: List[BoardingPosition] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_space: List[AccessSpace] = field(
        default_factory=list,
        metadata={
            "name": "AccessSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    quay: List[Quay] = field(
        default_factory=list,
        metadata={
            "name": "Quay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place_space: List[StopPlaceSpace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place_component: List[StopPlaceComponent] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_space: List[PointOfInterestSpace] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_bay: List[ParkingBay] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_area: List[ParkingArea] = field(
        default_factory=list,
        metadata={
            "name": "ParkingArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_component: List[ParkingComponent] = field(
        default_factory=list,
        metadata={
            "name": "ParkingComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_stopping_position: List[VehicleStoppingPosition] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_vehicle_entrance: List[PointOfInterestVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_entrance: List[PointOfInterestEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_passenger_entrance: List[ParkingPassengerEntrance] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPassengerEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_entrance_for_vehicles: List[ParkingEntranceForVehicles] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place_vehicle_entrance: List[StopPlaceVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place_entrance: List[StopPlaceEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_entrance: List[VehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entrance: List[Entrance] = field(
        default_factory=list,
        metadata={
            "name": "Entrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_component: List[SiteComponent] = field(
        default_factory=list,
        metadata={
            "name": "SiteComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest: List[PointOfInterest] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking: List[Parking] = field(
        default_factory=list,
        metadata={
            "name": "Parking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_place: List[StopPlace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_site: List[ServiceSite] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSite",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site: List[Site] = field(
        default_factory=list,
        metadata={
            "name": "Site",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_element: List[SiteElement] = field(
        default_factory=list,
        metadata={
            "name": "SiteElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    garage: List[Garage] = field(
        default_factory=list,
        metadata={
            "name": "Garage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    topographic_place: List[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    equipment_place: List[EquipmentPlace] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    country: List[Country] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    addressable_place: List[AddressablePlace] = field(
        default_factory=list,
        metadata={
            "name": "AddressablePlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    postal_address: List[PostalAddress] = field(
        default_factory=list,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    road_address: List[RoadAddress] = field(
        default_factory=list,
        metadata={
            "name": "RoadAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    place: List[Place] = field(
        default_factory=list,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transport_administrative_zone: List[TransportAdministrativeZone] = field(
        default_factory=list,
        metadata={
            "name": "TransportAdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    administrative_zone: List[AdministrativeZone1] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_administrative_zone: List[AdministrativeZone2] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_zone: List[FareZone] = field(
        default_factory=list,
        metadata={
            "name": "FareZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    tariff_zone: List[TariffZone1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_tariff_zone: List[TariffZone2] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    general_zone: List[GeneralZone] = field(
        default_factory=list,
        metadata={
            "name": "GeneralZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    zone: List[Zone] = field(
        default_factory=list,
        metadata={
            "name": "Zone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_links: List[GroupOfLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_points: List[GroupOfPoints] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    layer: List[Layer] = field(
        default_factory=list,
        metadata={
            "name": "Layer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    general_group_of_entities: List[GeneralGroupOfEntities] = field(
        default_factory=list,
        metadata={
            "name": "GeneralGroupOfEntities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_entities: List[GroupOfEntities] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfEntities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    responsibility_role: List[ResponsibilityRole] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilityRole",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    responsibility_set: List[ResponsibilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    value_set: List[ValueSet] = field(
        default_factory=list,
        metadata={
            "name": "ValueSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_machine_readability: List[TypeOfMachineReadability] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_concession: List[TypeOfConcession] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfConcession",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    charging_moment: List[ChargingMoment] = field(
        default_factory=list,
        metadata={
            "name": "ChargingMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_usage_parameter: List[TypeOfUsageParameter] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfUsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_table: List[TypeOfFareTable] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_pricing_rule: List[TypeOfPricingRule] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    price_unit: List[PriceUnit] = field(
        default_factory=list,
        metadata={
            "name": "PriceUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timing_algorithm_type: List[TimingAlgorithmType] = field(
        default_factory=list,
        metadata={
            "name": "TimingAlgorithmType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    purpose_of_journey_partition: List[PurposeOfJourneyPartition] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfJourneyPartition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_service_feature: List[TypeOfServiceFeature] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_classification: List[PointOfInterestClassification] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    direction: List[Direction] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    purpose_of_equipment_profile: List[PurposeOfEquipmentProfile] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfEquipmentProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_security_list: List[TypeOfSecurityList] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSecurityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_product_category: List[TypeOfProductCategory] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProductCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_payment_method: List[TypeOfPaymentMethod] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    class_of_use: List[ClassOfUse] = field(
        default_factory=list,
        metadata={
            "name": "ClassOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    submode: List[Submode] = field(
        default_factory=list,
        metadata={
            "name": "Submode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    open_transport_mode: List[OpenTransportMode] = field(
        default_factory=list,
        metadata={
            "name": "OpenTransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_codespace_assignment: List[TypeOfCodespaceAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCodespaceAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_validity: List[TypeOfValidity] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValidity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    purpose_of_grouping: List[PurposeOfGrouping] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfGrouping",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    branding: List[Branding] = field(
        default_factory=list,
        metadata={
            "name": "Branding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    data_source: List[DataSource] = field(
        default_factory=list,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_retail_device: List[TypeOfRetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfRetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_account_status: List[CustomerAccountStatus] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_customer_account: List[TypeOfCustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_contract_entry: List[TypeOfFareContractEntry] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_contract: List[TypeOfFareContract] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_travel_document: List[TypeOfTravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_sales_offer_package: List[TypeOfSalesOfferPackage] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_product: List[TypeOfFareProduct] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_structure_element: List[TypeOfFareStructureElement] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_tariff: List[TypeOfTariff] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_access_right_assignment: List[TypeOfAccessRightAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_structure_factor: List[TypeOfFareStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_flexible_service: List[TypeOfFlexibleService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFlexibleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_time_demand_type: List[TypeOfTimeDemandType] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTimeDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_passenger_information_equipment: List[TypeOfPassengerInformationEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPassengerInformationEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_congestion: List[TypeOfCongestion] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCongestion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_journey_pattern: List[TypeOfJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_line: List[TypeOfLine] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLine",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_activation: List[TypeOfActivation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfActivation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_delivery_variant: List[TypeOfDeliveryVariant] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfDeliveryVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_notice: List[TypeOfNotice] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfNotice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_facility: List[TypeOfFacility] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_service: List[TypeOfService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_equipment: List[TypeOfEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_feature: List[TypeOfFeature] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_link_sequence: List[TypeOfLinkSequence] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_place: List[TypeOfPlace] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_transfer: List[TypeOfTransfer] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_operation: List[TypeOfOperation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOperation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_organisation_part: List[TypeOfOrganisationPart] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_organisation: List[TypeOfOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_zone: List[TypeOfZone] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_link: List[TypeOfLink] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_point: List[TypeOfPoint] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_projection: List[TypeOfProjection] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_frame: List[TypeOfFrame] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_responsibility_role: List[TypeOfResponsibilityRole] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfResponsibilityRole",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_entity: List[TypeOfEntity] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEntity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_version: List[TypeOfVersion] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfVersion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_value: List[TypeOfValue] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    passing_time_view: List[PassingTimeView] = field(
        default_factory=list,
        metadata={
            "name": "PassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    data_managed_object_view: List[DataManagedObjectView] = field(
        default_factory=list,
        metadata={
            "name": "DataManagedObjectView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    simple_availability_condition: List[SimpleAvailabilityCondition] = field(
        default_factory=list,
        metadata={
            "name": "SimpleAvailabilityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    valid_during: List[ValidDuring] = field(
        default_factory=list,
        metadata={
            "name": "ValidDuring",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    availability_condition: List[AvailabilityCondition] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validity_rule_parameter: List[ValidityRuleParameter] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validity_trigger: List[ValidityTrigger] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validity_condition: List[ValidityCondition1] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_validity_condition: List[ValidityCondition2] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    version: List[Version] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    data_managed_object: List[DataManagedObject] = field(
        default_factory=list,
        metadata={
            "name": "DataManagedObject",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entity_in_version: List[EntityInVersion] = field(
        default_factory=list,
        metadata={
            "name": "EntityInVersion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class EntityEntityStructure(EntityStructure):
    class Meta:
        name = "Entity_EntityStructure"

    versions: Optional[EntitiesInVersionRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityEntity(EntityEntityStructure):
    class Meta:
        name = "Entity_Entity"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class GeneralFrameMembersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "generalFrameMembers_RelStructure"

    general_frame_member: List[GeneralFrameMember] = field(
        default_factory=list,
        metadata={
            "name": "GeneralFrameMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_document: List[TravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account: List[CustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transaction: List[SalesTransaction] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransaction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    offered_travel_specification: List[OfferedTravelSpecification] = field(
        default_factory=list,
        metadata={
            "name": "OfferedTravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requested_travel_specification: List[RequestedTravelSpecification] = field(
        default_factory=list,
        metadata={
            "name": "RequestedTravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specification: List[TravelSpecification1] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_travel_specification: List[TravelSpecification2] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_entry: List[FareContractEntry1] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_fare_contract_entry: List[FareContractEntry2] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntry_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract: List[FareContract] = field(
        default_factory=list,
        metadata={
            "name": "FareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer: List[Customer] = field(
        default_factory=list,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_tariff: List[ParkingTariff] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_sales_offer_packages: List[GroupOfSalesOfferPackages] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSalesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_channel: List[DistributionChannel] = field(
        default_factory=list,
        metadata={
            "name": "DistributionChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff: List[Tariff] = field(
        default_factory=list,
        metadata={
            "name": "Tariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package: List[CustomerPurchasePackage] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package: List[SalesOfferPackage] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_method: List[FulfilmentMethod] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capping_rule: List[CappingRule] = field(
        default_factory=list,
        metadata={
            "name": "CappingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_product: List[EntitlementProduct] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supplement_product: List[SupplementProduct] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preassigned_fare_product: List[PreassignedFareProduct] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    amount_of_price_unit_product: List[AmountOfPriceUnitProduct] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capped_discount_right: List[CappedDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_discount_right: List[UsageDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    third_party_product: List[ThirdPartyProduct] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sale_discount_right: List[SaleDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_product: List[FareProduct1] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_fare_product: List[FareProduct2] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_access_right: List[ServiceAccessRight1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAccessRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_service_access_right: List[ServiceAccessRight2] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAccessRight_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_interval: List[TimeInterval] = field(
        default_factory=list,
        metadata={
            "name": "TimeInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_quota_factor: List[FareQuotaFactor] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_demand_factor: List[FareDemandFactor] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factor: List[QualityStructureFactor1] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_quality_structure_factor: List[QualityStructureFactor2] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactor_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element: List[ControllableElement] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element: List[ValidableElement] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_entitlement_required: List[SalesOfferPackageEntitlementRequired] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_entitlement_given: List[SalesOfferPackageEntitlementGiven] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementGiven",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_stay: List[MinimumStay] = field(
        default_factory=list,
        metadata={
            "name": "MinimumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchanging: List[Interchanging] = field(
        default_factory=list,
        metadata={
            "name": "Interchanging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suspending: List[Suspending] = field(
        default_factory=list,
        metadata={
            "name": "Suspending",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_validity_period: List[UsageValidityPeriod] = field(
        default_factory=list,
        metadata={
            "name": "UsageValidityPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency_of_use: List[FrequencyOfUse] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    step_limit: List[StepLimit] = field(
        default_factory=list,
        metadata={
            "name": "StepLimit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routing: List[Routing] = field(
        default_factory=list,
        metadata={
            "name": "Routing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    round_trip: List[RoundTrip] = field(
        default_factory=list,
        metadata={
            "name": "RoundTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_allowance: List[LuggageAllowance] = field(
        default_factory=list,
        metadata={
            "name": "LuggageAllowance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_required: List[EntitlementRequired] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_given: List[EntitlementGiven] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGiven",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    eligibility_change_policy: List[EligibilityChangePolicy] = field(
        default_factory=list,
        metadata={
            "name": "EligibilityChangePolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    companion_profile: List[CompanionProfile] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_ticket: List[GroupTicket] = field(
        default_factory=list,
        metadata={
            "name": "GroupTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    commercial_profile: List[CommercialProfile] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    user_profile: List[UserProfile] = field(
        default_factory=list,
        metadata={
            "name": "UserProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    subscribing: List[Subscribing] = field(
        default_factory=list,
        metadata={
            "name": "Subscribing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    penalty_policy: List[PenaltyPolicy] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_policy: List[ChargingPolicy] = field(
        default_factory=list,
        metadata={
            "name": "ChargingPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cancelling: List[Cancelling] = field(
        default_factory=list,
        metadata={
            "name": "Cancelling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reserving: List[Reserving] = field(
        default_factory=list,
        metadata={
            "name": "Reserving",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purchase_window: List[PurchaseWindow] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transferability: List[Transferability] = field(
        default_factory=list,
        metadata={
            "name": "Transferability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    replacing: List[Replacing] = field(
        default_factory=list,
        metadata={
            "name": "Replacing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    refunding: List[Refunding] = field(
        default_factory=list,
        metadata={
            "name": "Refunding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchanging: List[Exchanging] = field(
        default_factory=list,
        metadata={
            "name": "Exchanging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reselling: List[Reselling] = field(
        default_factory=list,
        metadata={
            "name": "Reselling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameter: List[UsageParameter1] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_usage_parameter: List[UsageParameter2] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval: List[GeographicalInterval] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraint: List[SeriesConstraint] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_element: List[CustomerPurchasePackageElement] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_charge_band: List[ParkingChargeBand] = field(
        default_factory=list,
        metadata={
            "name": "ParkingChargeBand",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_element: List[SalesOfferPackageElement] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element: List[FareStructureElement] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_structure_factor: List[TimeStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "TimeStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit: List[TimeUnit] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element: List[DistanceMatrixElement] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_structure_factor: List[GeographicalStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit: List[GeographicalUnit] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_unit: List[FareUnit] = field(
        default_factory=list,
        metadata={
            "name": "FareUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_interval: List[FareInterval] = field(
        default_factory=list,
        metadata={
            "name": "FareInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_factor: List[FareStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    priceable_object: List[PriceableObject1] = field(
        default_factory=list,
        metadata={
            "name": "PriceableObject",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_priceable_object: List[PriceableObject2] = field(
        default_factory=list,
        metadata={
            "name": "PriceableObject_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_service: List[PricingService] = field(
        default_factory=list,
        metadata={
            "name": "PricingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limiting_rule_in_context: List[LimitingRuleInContext] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRuleInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limiting_rule: List[LimitingRule] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    discounting_rule: List[DiscountingRule] = field(
        default_factory=list,
        metadata={
            "name": "DiscountingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_rule: List[PricingRule1] = field(
        default_factory=list,
        metadata={
            "name": "PricingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_pricing_rule: List[PricingRule2] = field(
        default_factory=list,
        metadata={
            "name": "PricingRule_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    month_validity_offset: List[MonthValidityOffset] = field(
        default_factory=list,
        metadata={
            "name": "MonthValidityOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding: List[Rounding] = field(
        default_factory=list,
        metadata={
            "name": "Rounding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_parameter_set: List[PricingParameterSet] = field(
        default_factory=list,
        metadata={
            "name": "PricingParameterSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_opportunity: List[ReliefOpportunity] = field(
        default_factory=list,
        metadata={
            "name": "ReliefOpportunity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    course_of_journeys: List[CourseOfJourneys] = field(
        default_factory=list,
        metadata={
            "name": "CourseOfJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_service_part: List[VehicleServicePart] = field(
        default_factory=list,
        metadata={
            "name": "VehicleServicePart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_service: List[VehicleService] = field(
        default_factory=list,
        metadata={
            "name": "VehicleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block_part: List[TrainBlockPart] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_block: List[CompoundBlock] = field(
        default_factory=list,
        metadata={
            "name": "CompoundBlock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block_part: List[BlockPart] = field(
        default_factory=list,
        metadata={
            "name": "BlockPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block: List[TrainBlock] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block: List[Block] = field(
        default_factory=list,
        metadata={
            "name": "Block",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_trip_time: List[DriverTripTime] = field(
        default_factory=list,
        metadata={
            "name": "DriverTripTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_trip: List[DriverTrip] = field(
        default_factory=list,
        metadata={
            "name": "DriverTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty_part: List[DutyPart] = field(
        default_factory=list,
        metadata={
            "name": "DutyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accountable_element: List[AccountableElement] = field(
        default_factory=list,
        metadata={
            "name": "AccountableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty: List[Duty] = field(
        default_factory=list,
        metadata={
            "name": "Duty",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_profile: List[TimeDemandProfile] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_service_properties: List[FlexibleServiceProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleServiceProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type_stop_assignment: List[VehicleTypeStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component_label_assignment: List[TrainComponentLabelAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentLabelAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_number: List[TrainNumber] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_special_service: List[DatedSpecialService] = field(
        default_factory=list,
        metadata={
            "name": "DatedSpecialService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    normal_dated_vehicle_journey: List[NormalDatedVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "NormalDatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_vehicle_journey: List[DatedVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    special_service: List[SpecialService] = field(
        default_factory=list,
        metadata={
            "name": "SpecialService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run: List[DeadRun] = field(
        default_factory=list,
        metadata={
            "name": "DeadRun",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey: List[ServiceJourney1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_service_journey: List[DatedServiceJourney] = field(
        default_factory=list,
        metadata={
            "name": "DatedServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    template_service_journey: List[TemplateServiceJourney] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_service_journey: List[ServiceJourney2] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourney_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    template_vehicle_journey: List[TemplateVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "TemplateVehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey: List[VehicleJourney1] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_vehicle_journey: List[VehicleJourney2] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourney_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey: List[Journey1] = field(
        default_factory=list,
        metadata={
            "name": "Journey",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_journey: List[Journey2] = field(
        default_factory=list,
        metadata={
            "name": "Journey_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_couple: List[JourneyPartCouple] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartCouple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    coupled_journey: List[CoupledJourney] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part: List[JourneyPart] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange_rule: List[InterchangeRule] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange: List[Interchange1] = field(
        default_factory=list,
        metadata={
            "name": "Interchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_pattern_interchange: List[ServiceJourneyPatternInterchange] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_interchange: List[ServiceJourneyInterchange] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_interchange: List[DefaultInterchange] = field(
        default_factory=list,
        metadata={
            "name": "DefaultInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_interchange: List[Interchange2] = field(
        default_factory=list,
        metadata={
            "name": "Interchange_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_meeting: List[JourneyMeeting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyMeeting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_classification_hierarchy: List[PointOfInterestClassificationHierarchy] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationHierarchy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type: List[TimeDemandType] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_stop_assignment: List[FlexibleStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey_stop_assignment: List[VehicleJourneyStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_path_assignment: List[NavigationPathAssignment] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPathAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_stop_assignment: List[TrainStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TrainStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dynamic_stop_assignment: List[DynamicStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DynamicStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_stop_assignment: List[PassengerStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_assignment: List[StopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "StopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    logical_display: List[LogicalDisplay] = field(
        default_factory=list,
        metadata={
            "name": "LogicalDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    level: List[Level] = field(
        default_factory=list,
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_network: List[LineNetwork] = field(
        default_factory=list,
        metadata={
            "name": "LineNetwork",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_instruction: List[RouteInstruction] = field(
        default_factory=list,
        metadata={
            "name": "RouteInstruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allowed_line_direction: List[AllowedLineDirection] = field(
        default_factory=list,
        metadata={
            "name": "AllowedLineDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_variant: List[DestinationDisplayVariant] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display: List[DestinationDisplay] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_line: List[FlexibleLine] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLine",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line: List[Line1] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_line: List[Line2] = field(
        default_factory=list,
        metadata={
            "name": "Line_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context: List[OperationalContext] = field(
        default_factory=list,
        metadata={
            "name": "OperationalContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component: List[TrainComponent] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_element: List[TrainElement] = field(
        default_factory=list,
        metadata={
            "name": "TrainElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_train: List[CompoundTrain] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrain",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train: List[Train] = field(
        default_factory=list,
        metadata={
            "name": "Train",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_equipment_profile: List[VehicleEquipmentProfile] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEquipmentProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_model: List[VehicleModel] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_carrying_requirements_view: List[PassengerCarryingRequirementsView] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCarryingRequirementsView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facility_requirement: List[FacilityRequirement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_manoeuvring_requirement: List[VehicleManoeuvringRequirement] = field(
        default_factory=list,
        metadata={
            "name": "VehicleManoeuvringRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_carrying_requirement: List[PassengerCarryingRequirement] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCarryingRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_requirement: List[VehicleRequirement] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type: List[VehicleType] = field(
        default_factory=list,
        metadata={
            "name": "VehicleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    whitelist: List[Whitelist] = field(
        default_factory=list,
        metadata={
            "name": "Whitelist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    blacklist: List[Blacklist] = field(
        default_factory=list,
        metadata={
            "name": "Blacklist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    security_list: List[SecurityList] = field(
        default_factory=list,
        metadata={
            "name": "SecurityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    schematic_map: List[SchematicMap] = field(
        default_factory=list,
        metadata={
            "name": "SchematicMap",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delivery_variant: List[DeliveryVariant] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice: List[Notice] = field(
        default_factory=list,
        metadata={
            "name": "Notice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_position: List[EquipmentPosition] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPosition",
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
    service_pattern: List[ServicePattern] = field(
        default_factory=list,
        metadata={
            "name": "ServicePattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_path: List[NavigationPath] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_pattern: List[ServiceJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_journey_pattern: List[DeadRunJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern: List[JourneyPattern1] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_journey_pattern: List[JourneyPattern2] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPattern_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_route: List[FlexibleRoute] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route: List[Route1] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_route: List[Route2] = field(
        default_factory=list,
        metadata={
            "name": "Route_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_pattern: List[TimingPattern] = field(
        default_factory=list,
        metadata={
            "name": "TimingPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_sequence: List[LinkSequence] = field(
        default_factory=list,
        metadata={
            "name": "LinkSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_connection: List[DefaultConnection] = field(
        default_factory=list,
        metadata={
            "name": "DefaultConnection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_connection: List[SiteConnection] = field(
        default_factory=list,
        metadata={
            "name": "SiteConnection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access: List[Access] = field(
        default_factory=list,
        metadata={
            "name": "Access",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfer: List[Transfer] = field(
        default_factory=list,
        metadata={
            "name": "Transfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisational_unit: List[OrganisationalUnit] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationalUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre: List[ControlCentre] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_department: List[OperatingDepartment] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDepartment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    department: List[Department] = field(
        default_factory=list,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_part: List[OrganisationPart1] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_organisation_part: List[OrganisationPart2] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPart_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_consortium: List[RetailConsortium] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortium",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority: List[Authority] = field(
        default_factory=list,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator: List[Operator] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_organisation: List[TransportOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisation_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    serviced_organisation: List[ServicedOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "ServicedOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_organisation: List[GeneralOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "GeneralOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    management_agent: List[ManagementAgent] = field(
        default_factory=list,
        metadata={
            "name": "ManagementAgent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_agent: List[TravelAgent] = field(
        default_factory=list,
        metadata={
            "name": "TravelAgent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    other_organisation: List[OtherOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "OtherOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation: List[Organisation1] = field(
        default_factory=list,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_organisation: List[Organisation2] = field(
        default_factory=list,
        metadata={
            "name": "Organisation_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_link: List[ServiceLink] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_path_link: List[SitePathLink] = field(
        default_factory=list,
        metadata={
            "name": "SitePathLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_link: List[PathLink] = field(
        default_factory=list,
        metadata={
            "name": "PathLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_link: List[RouteLink] = field(
        default_factory=list,
        metadata={
            "name": "RouteLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link: List[TimingLink] = field(
        default_factory=list,
        metadata={
            "name": "TimingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_link: List[InfrastructureLink1] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_element: List[WireElement] = field(
        default_factory=list,
        metadata={
            "name": "WireElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_element: List[RoadElement] = field(
        default_factory=list,
        metadata={
            "name": "RoadElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_element: List[RailwayElement] = field(
        default_factory=list,
        metadata={
            "name": "RailwayElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_infrastructure_link: List[InfrastructureLink2] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLink_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_link: List[ActivationLink] = field(
        default_factory=list,
        metadata={
            "name": "ActivationLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link: List[Link] = field(
        default_factory=list,
        metadata={
            "name": "Link",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_point: List[BorderPoint] = field(
        default_factory=list,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point: List[FareScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point: List[ScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_junction: List[PathJunction] = field(
        default_factory=list,
        metadata={
            "name": "PathJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_point: List[RoutePoint] = field(
        default_factory=list,
        metadata={
            "name": "RoutePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_point: List[ParkingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage_point: List[GaragePoint] = field(
        default_factory=list,
        metadata={
            "name": "GaragePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_parking_point: List[ParkingPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_point: List[ReliefPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_relief_point: List[ReliefPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point: List[TimingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_timing_point: List[TimingPoint2] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_junction: List[WireJunction] = field(
        default_factory=list,
        metadata={
            "name": "WireJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_junction: List[RoadJunction] = field(
        default_factory=list,
        metadata={
            "name": "RoadJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_junction: List[RailwayJunction] = field(
        default_factory=list,
        metadata={
            "name": "RailwayJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_point: List[InfrastructurePoint] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructurePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    traffic_control_point: List[TrafficControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "TrafficControlPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    beacon_point: List[BeaconPoint] = field(
        default_factory=list,
        metadata={
            "name": "BeaconPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_point: List[ActivationPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_activation_point: List[ActivationPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point: List[Point2] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_shape: List[LineShape] = field(
        default_factory=list,
        metadata={
            "name": "LineShape",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_projection: List[TopographicProjection] = field(
        default_factory=list,
        metadata={
            "name": "TopographicProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_projection: List[ZoneProjection] = field(
        default_factory=list,
        metadata={
            "name": "ZoneProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complex_feature_projection: List[ComplexFeatureProjection] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeatureProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_sequence_projection: List[LinkSequenceProjection] = field(
        default_factory=list,
        metadata={
            "name": "LinkSequenceProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_projection: List[LinkProjection] = field(
        default_factory=list,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_projection: List[PointProjection] = field(
        default_factory=list,
        metadata={
            "name": "PointProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    projection: List[Projection] = field(
        default_factory=list,
        metadata={
            "name": "Projection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    log_entry: List[LogEntry] = field(
        default_factory=list,
        metadata={
            "name": "LogEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    log: List[Log] = field(
        default_factory=list,
        metadata={
            "name": "Log",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    composite_frame: List["CompositeFrame"] = field(
        default_factory=list,
        metadata={
            "name": "CompositeFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transaction_frame: List[SalesTransactionFrame] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_frame: List[FareFrame] = field(
        default_factory=list,
        metadata={
            "name": "FareFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_schedule_frame: List[DriverScheduleFrame] = field(
        default_factory=list,
        metadata={
            "name": "DriverScheduleFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_schedule_frame: List[VehicleScheduleFrame] = field(
        default_factory=list,
        metadata={
            "name": "VehicleScheduleFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_frame: List[ServiceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timetable_frame: List[TimetableFrame] = field(
        default_factory=list,
        metadata={
            "name": "TimetableFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_frame: List[SiteFrame] = field(
        default_factory=list,
        metadata={
            "name": "SiteFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_frame: List[InfrastructureFrame] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_frame: List["GeneralFrame"] = field(
        default_factory=list,
        metadata={
            "name": "GeneralFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    resource_frame: List[ResourceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ResourceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar_frame: List[ServiceCalendarFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    common_frame: List[CommonFrame] = field(
        default_factory=list,
        metadata={
            "name": "CommonFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_frame: List[VersionFrame] = field(
        default_factory=list,
        metadata={
            "name": "VersionFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    uic_operating_period: List[UicOperatingPeriod] = field(
        default_factory=list,
        metadata={
            "name": "UicOperatingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_period: List[OperatingPeriod] = field(
        default_factory=list,
        metadata={
            "name": "OperatingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_day: List[OperatingDay] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar: List[ServiceCalendar] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendar",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_assignment: List[DistributionAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DistributionAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_substitution: List[SalesOfferPackageSubstitution] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageSubstitution",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_parameter_assignment: List[CustomerPurchaseParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchaseParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    specific_parameter_assignment: List[SpecificParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment_in_context: List[GenericParameterAssignmentInContext] = field(
        default_factory=list,
        metadata={
            "name": "GenericParameterAssignmentInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment: List[GenericParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "GenericParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignment: List[ValidityParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ValidityParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_right_parameter_assignment: List[AccessRightParameterAssignment1] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_access_right_parameter_assignment: List[AccessRightParameterAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightParameterAssignment_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_accounting: List[JourneyAccounting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyAccounting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_assignment: List[TimeDemandTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfer_restriction: List[TransferRestriction] = field(
        default_factory=list,
        metadata={
            "name": "TransferRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_exclusion: List[ServiceExclusion] = field(
        default_factory=list,
        metadata={
            "name": "ServiceExclusion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    display_assignment: List[DisplayAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DisplayAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraint_throughput: List[CheckConstraintThroughput] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintThroughput",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraint_delay: List[CheckConstraintDelay] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraint: List[CheckConstraint] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    overtaking_possibility: List[OvertakingPossibility] = field(
        default_factory=list,
        metadata={
            "name": "OvertakingPossibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    meeting_restriction: List[MeetingRestriction] = field(
        default_factory=list,
        metadata={
            "name": "MeetingRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    restricted_manoeuvre: List[RestrictedManoeuvre] = field(
        default_factory=list,
        metadata={
            "name": "RestrictedManoeuvre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_link_restriction: List[InfrastructureLinkRestriction] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLinkRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type_at_point: List[VehicleTypeAtPoint] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeAtPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network_restriction: List[NetworkRestriction] = field(
        default_factory=list,
        metadata={
            "name": "NetworkRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_assignment: List[ActivationAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ActivationAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_notice_assignment: List[SalesNoticeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SalesNoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignment: List[NoticeAssignment1] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_notice_assignment: List[NoticeAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignment_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type_assignment: List[DayTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    assignment: List[Assignment1] = field(
        default_factory=list,
        metadata={
            "name": "Assignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_assignment: List[Assignment2] = field(
        default_factory=list,
        metadata={
            "name": "Assignment_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_timebands: List[GroupOfTimebands] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimebands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timeband: List[Timeband] = field(
        default_factory=list,
        metadata={
            "name": "Timeband",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_day_type: List[FareDayType] = field(
        default_factory=list,
        metadata={
            "name": "FareDayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_day_type: List[OrganisationDayType] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationDayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type: List[DayType1] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_day_type: List[DayType2] = field(
        default_factory=list,
        metadata={
            "name": "DayType_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distribution_channels: List[GroupOfDistributionChannels] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistributionChannels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distance_matrix_elements: List[GroupOfDistanceMatrixElements] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_group: List[PriceGroup1] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_price_group: List[PriceGroup2] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_fare_table: List[StandardFareTable] = field(
        default_factory=list,
        metadata={
            "name": "StandardFareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_table_in_context: List[FareTableInContext] = field(
        default_factory=list,
        metadata={
            "name": "FareTableInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_table: List[FareTable1] = field(
        default_factory=list,
        metadata={
            "name": "FareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_fare_table: List[FareTable2] = field(
        default_factory=list,
        metadata={
            "name": "FareTable_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_services: List[GroupOfServices] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rhythmical_journey_group: List[RhythmicalJourneyGroup] = field(
        default_factory=list,
        metadata={
            "name": "RhythmicalJourneyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headway_journey_group: List[HeadwayJourneyGroup] = field(
        default_factory=list,
        metadata={
            "name": "HeadwayJourneyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_frequency_group: List[JourneyFrequencyGroup] = field(
        default_factory=list,
        metadata={
            "name": "JourneyFrequencyGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network: List[Network] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_lines: List[GroupOfLines] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crew_base: List[CrewBase] = field(
        default_factory=list,
        metadata={
            "name": "CrewBase",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_timing_links: List[GroupOfTimingLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_operators: List[GroupOfOperators] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_places: List[GroupOfPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_link_sequences: List[GroupOfLinkSequences] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinkSequences",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routing_constraint_zone: List[RoutingConstraintZone] = field(
        default_factory=list,
        metadata={
            "name": "RoutingConstraintZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_area: List[StopArea] = field(
        default_factory=list,
        metadata={
            "name": "StopArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_zone: List[AccessZone] = field(
        default_factory=list,
        metadata={
            "name": "AccessZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hail_and_ride_area: List[HailAndRideArea] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_area: List[FlexibleArea] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_quay: List[FlexibleQuay] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleQuay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_stop_place: List[FlexibleStopPlace] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_component: List[PointOfInterestComponent] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_place: List[VehicleStoppingPlace] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position: List[BoardingPosition] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_space: List[AccessSpace] = field(
        default_factory=list,
        metadata={
            "name": "AccessSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay: List[Quay] = field(
        default_factory=list,
        metadata={
            "name": "Quay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_space: List[StopPlaceSpace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_component: List[StopPlaceComponent] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_space: List[PointOfInterestSpace] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_bay: List[ParkingBay] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_area: List[ParkingArea] = field(
        default_factory=list,
        metadata={
            "name": "ParkingArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_component: List[ParkingComponent] = field(
        default_factory=list,
        metadata={
            "name": "ParkingComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_position: List[VehicleStoppingPosition] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_vehicle_entrance: List[PointOfInterestVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_entrance: List[PointOfInterestEntrance] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_passenger_entrance: List[ParkingPassengerEntrance] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPassengerEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_for_vehicles: List[ParkingEntranceForVehicles] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_vehicle_entrance: List[StopPlaceVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_entrance: List[StopPlaceEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_entrance: List[VehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance: List[Entrance] = field(
        default_factory=list,
        metadata={
            "name": "Entrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_component: List[SiteComponent] = field(
        default_factory=list,
        metadata={
            "name": "SiteComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest: List[PointOfInterest] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking: List[Parking] = field(
        default_factory=list,
        metadata={
            "name": "Parking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place: List[StopPlace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_site: List[ServiceSite] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSite",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site: List[Site] = field(
        default_factory=list,
        metadata={
            "name": "Site",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_element: List[SiteElement] = field(
        default_factory=list,
        metadata={
            "name": "SiteElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage: List[Garage] = field(
        default_factory=list,
        metadata={
            "name": "Garage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place: List[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_place: List[EquipmentPlace] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country: List[Country] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    addressable_place: List[AddressablePlace] = field(
        default_factory=list,
        metadata={
            "name": "AddressablePlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    postal_address: List[PostalAddress] = field(
        default_factory=list,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_address: List[RoadAddress] = field(
        default_factory=list,
        metadata={
            "name": "RoadAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place: List[Place] = field(
        default_factory=list,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_administrative_zone: List[TransportAdministrativeZone] = field(
        default_factory=list,
        metadata={
            "name": "TransportAdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    administrative_zone: List[AdministrativeZone1] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_administrative_zone: List[AdministrativeZone2] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_zone: List[FareZone] = field(
        default_factory=list,
        metadata={
            "name": "FareZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone: List[TariffZone1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_tariff_zone: List[TariffZone2] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_zone: List[GeneralZone] = field(
        default_factory=list,
        metadata={
            "name": "GeneralZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone: List[Zone] = field(
        default_factory=list,
        metadata={
            "name": "Zone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_links: List[GroupOfLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_points: List[GroupOfPoints] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layer: List[Layer] = field(
        default_factory=list,
        metadata={
            "name": "Layer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_group_of_entities: List[GeneralGroupOfEntities] = field(
        default_factory=list,
        metadata={
            "name": "GeneralGroupOfEntities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_entities: List[GroupOfEntities] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfEntities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_role: List[ResponsibilityRole] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilityRole",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_set: List[ResponsibilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    value_set: List[ValueSet] = field(
        default_factory=list,
        metadata={
            "name": "ValueSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_machine_readability: List[TypeOfMachineReadability] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_concession: List[TypeOfConcession] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfConcession",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_moment: List[ChargingMoment] = field(
        default_factory=list,
        metadata={
            "name": "ChargingMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_usage_parameter: List[TypeOfUsageParameter] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfUsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_table: List[TypeOfFareTable] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_pricing_rule: List[TypeOfPricingRule] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_unit: List[PriceUnit] = field(
        default_factory=list,
        metadata={
            "name": "PriceUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_algorithm_type: List[TimingAlgorithmType] = field(
        default_factory=list,
        metadata={
            "name": "TimingAlgorithmType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purpose_of_journey_partition: List[PurposeOfJourneyPartition] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfJourneyPartition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_feature: List[TypeOfServiceFeature] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_classification: List[PointOfInterestClassification] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction: List[Direction] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purpose_of_equipment_profile: List[PurposeOfEquipmentProfile] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfEquipmentProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_security_list: List[TypeOfSecurityList] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSecurityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_product_category: List[TypeOfProductCategory] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProductCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_payment_method: List[TypeOfPaymentMethod] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_of_use: List[ClassOfUse] = field(
        default_factory=list,
        metadata={
            "name": "ClassOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    submode: List[Submode] = field(
        default_factory=list,
        metadata={
            "name": "Submode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    open_transport_mode: List[OpenTransportMode] = field(
        default_factory=list,
        metadata={
            "name": "OpenTransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_codespace_assignment: List[TypeOfCodespaceAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCodespaceAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_validity: List[TypeOfValidity] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValidity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purpose_of_grouping: List[PurposeOfGrouping] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfGrouping",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    branding: List[Branding] = field(
        default_factory=list,
        metadata={
            "name": "Branding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_source: List[DataSource] = field(
        default_factory=list,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_retail_device: List[TypeOfRetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfRetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_status: List[CustomerAccountStatus] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_customer_account: List[TypeOfCustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract_entry: List[TypeOfFareContractEntry] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract: List[TypeOfFareContract] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document: List[TypeOfTravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_sales_offer_package: List[TypeOfSalesOfferPackage] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_product: List[TypeOfFareProduct] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_structure_element: List[TypeOfFareStructureElement] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_tariff: List[TypeOfTariff] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_access_right_assignment: List[TypeOfAccessRightAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_structure_factor: List[TypeOfFareStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_flexible_service: List[TypeOfFlexibleService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFlexibleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_time_demand_type: List[TypeOfTimeDemandType] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTimeDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_passenger_information_equipment: List[TypeOfPassengerInformationEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPassengerInformationEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_congestion: List[TypeOfCongestion] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCongestion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_journey_pattern: List[TypeOfJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_line: List[TypeOfLine] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLine",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_activation: List[TypeOfActivation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfActivation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_delivery_variant: List[TypeOfDeliveryVariant] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfDeliveryVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_notice: List[TypeOfNotice] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfNotice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_facility: List[TypeOfFacility] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service: List[TypeOfService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_equipment: List[TypeOfEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_feature: List[TypeOfFeature] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_link_sequence: List[TypeOfLinkSequence] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_place: List[TypeOfPlace] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_transfer: List[TypeOfTransfer] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_operation: List[TypeOfOperation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOperation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_organisation_part: List[TypeOfOrganisationPart] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_organisation: List[TypeOfOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_zone: List[TypeOfZone] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_link: List[TypeOfLink] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_point: List[TypeOfPoint] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_projection: List[TypeOfProjection] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_frame: List[TypeOfFrame] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_responsibility_role: List[TypeOfResponsibilityRole] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfResponsibilityRole",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_entity: List[TypeOfEntity] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEntity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_version: List[TypeOfVersion] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfVersion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_value: List[TypeOfValue] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passing_time_view: List[PassingTimeView] = field(
        default_factory=list,
        metadata={
            "name": "PassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_managed_object_view: List[DataManagedObjectView] = field(
        default_factory=list,
        metadata={
            "name": "DataManagedObjectView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    simple_availability_condition: List[SimpleAvailabilityCondition] = field(
        default_factory=list,
        metadata={
            "name": "SimpleAvailabilityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    valid_during: List[ValidDuring] = field(
        default_factory=list,
        metadata={
            "name": "ValidDuring",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    availability_condition: List[AvailabilityCondition] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_rule_parameter: List[ValidityRuleParameter] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_trigger: List[ValidityTrigger] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_condition: List[ValidityCondition1] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_validity_condition: List[ValidityCondition2] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version: List[Version] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_managed_object: List[DataManagedObject] = field(
        default_factory=list,
        metadata={
            "name": "DataManagedObject",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entity_entity: List[EntityEntity] = field(
        default_factory=list,
        metadata={
            "name": "Entity_Entity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class GeneralVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "General_VersionFrameStructure"

    members: Optional[GeneralFrameMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class GeneralFrame(GeneralVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class FramesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "frames_RelStructure"

    sales_transaction_frame: List[SalesTransactionFrame] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_frame: List[FareFrame] = field(
        default_factory=list,
        metadata={
            "name": "FareFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    driver_schedule_frame: List[DriverScheduleFrame] = field(
        default_factory=list,
        metadata={
            "name": "DriverScheduleFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_schedule_frame: List[VehicleScheduleFrame] = field(
        default_factory=list,
        metadata={
            "name": "VehicleScheduleFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_frame: List[ServiceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timetable_frame: List[TimetableFrame] = field(
        default_factory=list,
        metadata={
            "name": "TimetableFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_frame: List[SiteFrame] = field(
        default_factory=list,
        metadata={
            "name": "SiteFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    infrastructure_frame: List[InfrastructureFrame] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    general_frame: List[GeneralFrame] = field(
        default_factory=list,
        metadata={
            "name": "GeneralFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    resource_frame: List[ResourceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ResourceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_calendar_frame: List[ServiceCalendarFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    common_frame: List[CommonFrame] = field(
        default_factory=list,
        metadata={
            "name": "CommonFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass
class CompositeVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "Composite_VersionFrameStructure"

    frames: Optional[FramesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class CompositeFrame(CompositeVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
