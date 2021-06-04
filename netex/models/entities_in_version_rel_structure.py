from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from netex.models.abstract_group_member import AbstractGroupMember
from netex.models.access import Access
from netex.models.access_equipment import AccessEquipment
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_right_parameter_assignment_1 import AccessRightParameterAssignment1
from netex.models.access_right_parameter_assignment_2 import AccessRightParameterAssignment2
from netex.models.access_space import AccessSpace
from netex.models.access_vehicle_equipment import AccessVehicleEquipment
from netex.models.access_zone import AccessZone
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.accommodation import Accommodation
from netex.models.accountable_element import AccountableElement
from netex.models.activation_assignment import ActivationAssignment
from netex.models.activation_link import ActivationLink
from netex.models.activation_point_1 import ActivationPoint1
from netex.models.activation_point_2 import ActivationPoint2
from netex.models.actual_vehicle_equipment import ActualVehicleEquipment
from netex.models.address import Address
from netex.models.addressable_place import AddressablePlace
from netex.models.administrative_zone_1 import AdministrativeZone1
from netex.models.administrative_zone_version_structure import (
    AdministrativeZone2,
    TransportAdministrativeZone,
)
from netex.models.allowed_line_direction import AllowedLineDirection
from netex.models.alternative_name import AlternativeName
from netex.models.alternative_texts_rel_structure import (
    AlternativeText,
    AvailabilityCondition,
    DayType2,
    DayType1,
    FareDayType,
    OperatingDay,
    OrganisationDayType,
    SimpleAvailabilityCondition,
    ValidDuring,
    ValidityCondition2,
    ValidityCondition1,
    ValidityRuleParameter,
    ValidityTrigger,
)
from netex.models.amount_of_price_unit_product import AmountOfPriceUnitProduct
from netex.models.assignment_1 import Assignment1
from netex.models.assignment_2 import Assignment2
from netex.models.assistance_booking_service import AssistanceBookingService
from netex.models.assistance_service import AssistanceService
from netex.models.authority import Authority
from netex.models.beacon_point import BeaconPoint
from netex.models.blacklist import Blacklist
from netex.models.block import Block
from netex.models.block_part import BlockPart
from netex.models.boarding_position import BoardingPosition
from netex.models.border_point import BorderPoint
from netex.models.branding import Branding
from netex.models.cancelling import Cancelling
from netex.models.capped_discount_right import CappedDiscountRight
from netex.models.capping_rule import CappingRule
from netex.models.capping_rule_price import CappingRulePrice
from netex.models.catering_service import CateringService
from netex.models.cell_1 import Cell1
from netex.models.cell_versioned_child_structure import (
    Cell2,
    FareTableInContext,
    FareTable2,
    ParkingChargeBand,
    ParkingPrice,
    PriceGroup2,
)
from netex.models.charging_moment import ChargingMoment
from netex.models.charging_policy import ChargingPolicy
from netex.models.check_constraint import CheckConstraint
from netex.models.check_constraint_delay import CheckConstraintDelay
from netex.models.check_constraint_throughput import CheckConstraintThroughput
from netex.models.class_of_use import ClassOfUse
from netex.models.codespace_assignment import CodespaceAssignment
from netex.models.commercial_profile import CommercialProfile
from netex.models.commercial_profile_eligibility import CommercialProfileEligibility
from netex.models.common_frame import CommonFrame
from netex.models.common_version_frame_structure import CommonVersionFrameStructure
from netex.models.communication_service import CommunicationService
from netex.models.companion_profile import CompanionProfile
from netex.models.complaints_service import ComplaintsService
from netex.models.complex_feature_projection import ComplexFeatureProjection
from netex.models.compound_block import CompoundBlock
from netex.models.compound_train import CompoundTrain
from netex.models.connection import Connection
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.control_centre import ControlCentre
from netex.models.controllable_element import ControllableElement
from netex.models.controllable_element_in_sequence import ControllableElementInSequence
from netex.models.controllable_element_price import ControllableElementPrice
from netex.models.country import Country
from netex.models.coupled_journey import CoupledJourney
from netex.models.course_of_journeys import CourseOfJourneys
from netex.models.crew_base import CrewBase
from netex.models.crossing_equipment import CrossingEquipment
from netex.models.customer import Customer
from netex.models.customer_account import CustomerAccount
from netex.models.customer_account_security_listing import CustomerAccountSecurityListing
from netex.models.customer_account_status import CustomerAccountStatus
from netex.models.customer_eligibility_1 import CustomerEligibility1
from netex.models.customer_eligibility_2 import CustomerEligibility2
from netex.models.customer_purchase_package import CustomerPurchasePackage
from netex.models.customer_purchase_package_element import CustomerPurchasePackageElement
from netex.models.customer_purchase_package_price import CustomerPurchasePackagePrice
from netex.models.customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment
from netex.models.customer_security_listing import CustomerSecurityListing
from netex.models.customer_service import CustomerService
from netex.models.cycle_storage_equipment import CycleStorageEquipment
from netex.models.data_managed_object import DataManagedObject
from netex.models.data_managed_object_view import DataManagedObjectView
from netex.models.data_source import DataSource
from netex.models.dated_passing_time import DatedPassingTime
from netex.models.dated_service_journey import DatedServiceJourney
from netex.models.dated_special_service import DatedSpecialService
from netex.models.dated_vehicle_journey import DatedVehicleJourney
from netex.models.day_type_assignment import DayTypeAssignment
from netex.models.dead_run import DeadRun
from netex.models.dead_run_journey_pattern import DeadRunJourneyPattern
from netex.models.default_connection import DefaultConnection
from netex.models.default_dead_run_run_time import DefaultDeadRunRunTime
from netex.models.default_interchange import DefaultInterchange
from netex.models.default_service_journey_run_time import DefaultServiceJourneyRunTime
from netex.models.delivery_variant import DeliveryVariant
from netex.models.department import Department
from netex.models.destination_display import DestinationDisplay
from netex.models.destination_display_variant import DestinationDisplayVariant
from netex.models.direction import Direction
from netex.models.discounting_rule import DiscountingRule
from netex.models.display_assignment import DisplayAssignment
from netex.models.distance_matrix_element import DistanceMatrixElement
from netex.models.distance_matrix_element_price import DistanceMatrixElementPrice
from netex.models.distribution_assignment import DistributionAssignment
from netex.models.distribution_channel import DistributionChannel
from netex.models.driver_schedule_frame import DriverScheduleFrame
from netex.models.driver_trip import DriverTrip
from netex.models.driver_trip_time import DriverTripTime
from netex.models.duty import Duty
from netex.models.duty_part import DutyPart
from netex.models.dynamic_stop_assignment import DynamicStopAssignment
from netex.models.eligibility_change_policy import EligibilityChangePolicy
from netex.models.entitlement_given import EntitlementGiven
from netex.models.entitlement_product import EntitlementProduct
from netex.models.entitlement_required import EntitlementRequired
from netex.models.entity_in_version import EntityInVersion
from netex.models.entity_structure import EntityStructure
from netex.models.entrance import Entrance
from netex.models.entrance_equipment import EntranceEquipment
from netex.models.equipment import Equipment
from netex.models.equipment_place import EquipmentPlace
from netex.models.equipment_position import EquipmentPosition
from netex.models.escalator_equipment import EscalatorEquipment
from netex.models.estimated_passing_time import EstimatedPassingTime
from netex.models.exchanging import Exchanging
from netex.models.facility_requirement import FacilityRequirement
from netex.models.fare_contract import FareContract
from netex.models.fare_contract_entry_1 import FareContractEntry1
from netex.models.fare_contract_entry_2 import FareContractEntry2
from netex.models.fare_contract_security_listing import FareContractSecurityListing
from netex.models.fare_demand_factor import FareDemandFactor
from netex.models.fare_element_in_sequence import FareElementInSequence
from netex.models.fare_frame import FareFrame
from netex.models.fare_interval import FareInterval
from netex.models.fare_point_in_pattern import FarePointInPattern
from netex.models.fare_price_1 import FarePrice1
from netex.models.fare_price_2 import FarePrice2
from netex.models.fare_product_1 import FareProduct1
from netex.models.fare_product_2 import FareProduct2
from netex.models.fare_product_price import FareProductPrice
from netex.models.fare_quota_factor import FareQuotaFactor
from netex.models.fare_scheduled_stop_point import FareScheduledStopPoint
from netex.models.fare_structure_element import FareStructureElement
from netex.models.fare_structure_element_in_sequence import FareStructureElementInSequence
from netex.models.fare_structure_element_price import FareStructureElementPrice
from netex.models.fare_structure_factor import FareStructureFactor
from netex.models.fare_table_1 import FareTable1
from netex.models.fare_unit import FareUnit
from netex.models.fare_zone import FareZone
from netex.models.flexible_area import FlexibleArea
from netex.models.flexible_line import FlexibleLine
from netex.models.flexible_link_properties import FlexibleLinkProperties
from netex.models.flexible_point_properties import FlexiblePointProperties
from netex.models.flexible_quay import FlexibleQuay
from netex.models.flexible_route import FlexibleRoute
from netex.models.flexible_service_properties import FlexibleServiceProperties
from netex.models.flexible_stop_assignment import FlexibleStopAssignment
from netex.models.flexible_stop_place import FlexibleStopPlace
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.fulfilment_method import FulfilmentMethod
from netex.models.fulfilment_method_price import FulfilmentMethodPrice
from netex.models.garage import Garage
from netex.models.garage_point import GaragePoint
from netex.models.general_frame_member import GeneralFrameMember
from netex.models.general_group_of_entities import GeneralGroupOfEntities
from netex.models.general_organisation import GeneralOrganisation
from netex.models.general_sign import GeneralSign
from netex.models.general_zone import GeneralZone
from netex.models.generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from netex.models.geographical_interval import GeographicalInterval
from netex.models.geographical_interval_price import GeographicalIntervalPrice
from netex.models.geographical_structure_factor import GeographicalStructureFactor
from netex.models.geographical_unit import GeographicalUnit
from netex.models.geographical_unit_price import GeographicalUnitPrice
from netex.models.group_constraint_member import GroupConstraintMember
from netex.models.group_of_distance_matrix_elements import GroupOfDistanceMatrixElements
from netex.models.group_of_distribution_channels import GroupOfDistributionChannels
from netex.models.group_of_entities import GroupOfEntities
from netex.models.group_of_lines import GroupOfLines
from netex.models.group_of_link_sequences import GroupOfLinkSequences
from netex.models.group_of_links import GroupOfLinks
from netex.models.group_of_operators import GroupOfOperators
from netex.models.group_of_places import GroupOfPlaces
from netex.models.group_of_points import GroupOfPoints
from netex.models.group_of_sales_offer_packages import GroupOfSalesOfferPackages
from netex.models.group_of_services import GroupOfServices
from netex.models.group_of_timebands import GroupOfTimebands
from netex.models.group_of_timing_links import GroupOfTimingLinks
from netex.models.group_ticket import GroupTicket
from netex.models.hail_and_ride_area import HailAndRideArea
from netex.models.heading_sign import HeadingSign
from netex.models.headway_journey_group import HeadwayJourneyGroup
from netex.models.help_point_equipment import HelpPointEquipment
from netex.models.hire_service import HireService
from netex.models.infrastructure_frame import InfrastructureFrame
from netex.models.infrastructure_link_1 import InfrastructureLink1
from netex.models.infrastructure_link_2 import InfrastructureLink2
from netex.models.infrastructure_link_restriction import InfrastructureLinkRestriction
from netex.models.infrastructure_point import InfrastructurePoint
from netex.models.installed_equipment import InstalledEquipment
from netex.models.interchange_1 import Interchange1
from netex.models.interchange_2 import Interchange2
from netex.models.interchange_rule import InterchangeRule
from netex.models.interchange_rule_timing import InterchangeRuleTiming
from netex.models.interchanging import Interchanging
from netex.models.journey_1 import Journey1
from netex.models.journey_2 import Journey2
from netex.models.journey_accounting import JourneyAccounting
from netex.models.journey_frequency_group import JourneyFrequencyGroup
from netex.models.journey_headway import JourneyHeadway
from netex.models.journey_layover import JourneyLayover
from netex.models.journey_meeting import JourneyMeeting
from netex.models.journey_part import JourneyPart
from netex.models.journey_part_couple import JourneyPartCouple
from netex.models.journey_part_position import JourneyPartPosition
from netex.models.journey_pattern_1 import JourneyPattern1
from netex.models.journey_pattern_headway import JourneyPatternHeadway
from netex.models.journey_pattern_layover import JourneyPatternLayover
from netex.models.journey_pattern_run_time import JourneyPatternRunTime
from netex.models.journey_pattern_wait_time import JourneyPatternWaitTime
from netex.models.journey_run_time import JourneyRunTime
from netex.models.journey_timing import JourneyTiming
from netex.models.journey_wait_time import JourneyWaitTime
from netex.models.layer import Layer
from netex.models.left_luggage_service import LeftLuggageService
from netex.models.level import Level
from netex.models.lift_equipment import LiftEquipment
from netex.models.limiting_rule import LimitingRule
from netex.models.limiting_rule_in_context import LimitingRuleInContext
from netex.models.line_1 import Line1
from netex.models.line_2 import Line2
from netex.models.line_network import LineNetwork
from netex.models.line_shape import LineShape
from netex.models.link import Link
from netex.models.link_in_journey_pattern import LinkInJourneyPattern
from netex.models.link_in_link_sequence import LinkInLinkSequence
from netex.models.link_on_section import LinkOnSection
from netex.models.link_projection import LinkProjection
from netex.models.link_sequence import LinkSequence
from netex.models.link_sequence_projection import LinkSequenceProjection
from netex.models.link_sequence_version_structure import (
    JourneyPattern2,
    SectionInSequence,
)
from netex.models.local_service import LocalService
from netex.models.log import Log
from netex.models.log_entry import LogEntry
from netex.models.logical_display import LogicalDisplay
from netex.models.lost_property_service import LostPropertyService
from netex.models.luggage_allowance import LuggageAllowance
from netex.models.luggage_locker_equipment import LuggageLockerEquipment
from netex.models.luggage_service import LuggageService
from netex.models.management_agent import ManagementAgent
from netex.models.meeting_point_service import MeetingPointService
from netex.models.meeting_restriction import MeetingRestriction
from netex.models.minimum_stay import MinimumStay
from netex.models.money_service import MoneyService
from netex.models.month_validity_offset import MonthValidityOffset
from netex.models.navigation_path import NavigationPath
from netex.models.navigation_path_assignment import NavigationPathAssignment
from netex.models.network import Network
from netex.models.network_restriction import NetworkRestriction
from netex.models.normal_dated_vehicle_journey import NormalDatedVehicleJourney
from netex.models.notice import Notice
from netex.models.notice_assignment_1 import NoticeAssignment1
from netex.models.notice_assignment_2 import NoticeAssignment2
from netex.models.observed_passing_time import ObservedPassingTime
from netex.models.offered_travel_specification import OfferedTravelSpecification
from netex.models.onboard_stay import OnboardStay
from netex.models.open_transport_mode import OpenTransportMode
from netex.models.operating_department import OperatingDepartment
from netex.models.operating_period import OperatingPeriod
from netex.models.operational_context import OperationalContext
from netex.models.operator import Operator
from netex.models.organisation_1 import Organisation1
from netex.models.organisation_2 import Organisation2
from netex.models.organisation_part_1 import OrganisationPart1
from netex.models.organisation_part_2 import OrganisationPart2
from netex.models.organisational_unit import OrganisationalUnit
from netex.models.other_organisation import OtherOrganisation
from netex.models.overtaking_possibility import OvertakingPossibility
from netex.models.parking import Parking
from netex.models.parking_area import ParkingArea
from netex.models.parking_bay import ParkingBay
from netex.models.parking_capacity import ParkingCapacity
from netex.models.parking_component import ParkingComponent
from netex.models.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from netex.models.parking_passenger_entrance import ParkingPassengerEntrance
from netex.models.parking_point_1 import ParkingPoint1
from netex.models.parking_point_2 import ParkingPoint2
from netex.models.parking_properties import ParkingProperties
from netex.models.parking_tariff import ParkingTariff
from netex.models.passenger_carrying_requirement import PassengerCarryingRequirement
from netex.models.passenger_carrying_requirements_view import PassengerCarryingRequirementsView
from netex.models.passenger_equipment import PassengerEquipment
from netex.models.passenger_information_equipment import PassengerInformationEquipment
from netex.models.passenger_safety_equipment import PassengerSafetyEquipment
from netex.models.passenger_stop_assignment import PassengerStopAssignment
from netex.models.passing_time import PassingTime
from netex.models.passing_time_view import PassingTimeView
from netex.models.path_junction import PathJunction
from netex.models.path_link import PathLink
from netex.models.path_link_in_sequence import PathLinkInSequence
from netex.models.penalty_policy import PenaltyPolicy
from netex.models.place import Place
from netex.models.place_equipment import PlaceEquipment
from netex.models.place_in_sequence import PlaceInSequence
from netex.models.place_lighting import PlaceLighting
from netex.models.place_sign import PlaceSign
from netex.models.point_2 import Point2
from netex.models.point_in_journey_pattern import PointInJourneyPattern
from netex.models.point_in_link_sequence import PointInLinkSequence
from netex.models.point_of_interest import PointOfInterest
from netex.models.point_of_interest_classification import PointOfInterestClassification
from netex.models.point_of_interest_classification_hierarchy import PointOfInterestClassificationHierarchy
from netex.models.point_of_interest_component import PointOfInterestComponent
from netex.models.point_of_interest_entrance import PointOfInterestEntrance
from netex.models.point_of_interest_space import PointOfInterestSpace
from netex.models.point_of_interest_vehicle_entrance import PointOfInterestVehicleEntrance
from netex.models.point_on_line_section import PointOnLineSection
from netex.models.point_on_link import PointOnLink
from netex.models.point_on_route import PointOnRoute
from netex.models.point_on_section_1 import PointOnSection1
from netex.models.point_on_section_2 import PointOnSection2
from netex.models.point_projection import PointProjection
from netex.models.postal_address import PostalAddress
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.price_group_1 import PriceGroup1
from netex.models.price_unit import PriceUnit
from netex.models.priceable_object_1 import PriceableObject1
from netex.models.priceable_object_2 import PriceableObject2
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.pricing_rule_1 import PricingRule1
from netex.models.pricing_rule_2 import PricingRule2
from netex.models.pricing_service import PricingService
from netex.models.projection import Projection
from netex.models.purchase_window import PurchaseWindow
from netex.models.purpose_of_equipment_profile import PurposeOfEquipmentProfile
from netex.models.purpose_of_grouping import PurposeOfGrouping
from netex.models.purpose_of_journey_partition import PurposeOfJourneyPartition
from netex.models.quality_structure_factor_1 import QualityStructureFactor1
from netex.models.quality_structure_factor_2 import QualityStructureFactor2
from netex.models.quality_structure_factor_price import QualityStructureFactorPrice
from netex.models.quay import Quay
from netex.models.queueing_equipment import QueueingEquipment
from netex.models.railway_element import RailwayElement
from netex.models.railway_junction import RailwayJunction
from netex.models.ramp_equipment import RampEquipment
from netex.models.refunding import Refunding
from netex.models.relief_opportunity import ReliefOpportunity
from netex.models.relief_point_1 import ReliefPoint1
from netex.models.relief_point_2 import ReliefPoint2
from netex.models.replacing import Replacing
from netex.models.requested_travel_specification import RequestedTravelSpecification
from netex.models.reselling import Reselling
from netex.models.reserving import Reserving
from netex.models.residential_qualification import ResidentialQualification
from netex.models.residential_qualification_eligibility import ResidentialQualificationEligibility
from netex.models.resource_frame import ResourceFrame
from netex.models.responsibility_role import ResponsibilityRole
from netex.models.responsibility_set import ResponsibilitySet
from netex.models.restricted_manoeuvre import RestrictedManoeuvre
from netex.models.retail_consortium import RetailConsortium
from netex.models.retail_device import RetailDevice
from netex.models.retail_device_security_listing import RetailDeviceSecurityListing
from netex.models.retail_service import RetailService
from netex.models.rhythmical_journey_group import RhythmicalJourneyGroup
from netex.models.road_address import RoadAddress
from netex.models.road_element import RoadElement
from netex.models.road_junction import RoadJunction
from netex.models.rough_surface import RoughSurface
from netex.models.round_trip import RoundTrip
from netex.models.rounding import Rounding
from netex.models.route_1 import Route1
from netex.models.route_2 import Route2
from netex.models.route_instruction import RouteInstruction
from netex.models.route_link import RouteLink
from netex.models.route_point import RoutePoint
from netex.models.routing import Routing
from netex.models.routing_constraint_zone import RoutingConstraintZone
from netex.models.rubbish_disposal_equipment import RubbishDisposalEquipment
from netex.models.sale_discount_right import SaleDiscountRight
from netex.models.sales_notice_assignment import SalesNoticeAssignment
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_entitlement_given import SalesOfferPackageEntitlementGiven
from netex.models.sales_offer_package_entitlement_required import SalesOfferPackageEntitlementRequired
from netex.models.sales_offer_package_price import SalesOfferPackagePrice
from netex.models.sales_offer_package_substitution import SalesOfferPackageSubstitution
from netex.models.sales_transaction import SalesTransaction
from netex.models.sales_transaction_frame import SalesTransactionFrame
from netex.models.sanitary_equipment import SanitaryEquipment
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.schematic_map import SchematicMap
from netex.models.seating_equipment import SeatingEquipment
from netex.models.security_list import SecurityList
from netex.models.security_listing_1 import SecurityListing1
from netex.models.security_listing_2 import SecurityListing2
from netex.models.series_constraint import SeriesConstraint
from netex.models.series_constraint_price import SeriesConstraintPrice
from netex.models.service_access_right_1 import ServiceAccessRight1
from netex.models.service_access_right_2 import ServiceAccessRight2
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_exclusion import ServiceExclusion
from netex.models.service_frame import ServiceFrame
from netex.models.service_journey_1 import ServiceJourney1
from netex.models.service_journey_2 import ServiceJourney2
from netex.models.service_journey_interchange import ServiceJourneyInterchange
from netex.models.service_journey_pattern import ServiceJourneyPattern
from netex.models.service_journey_pattern_interchange import ServiceJourneyPatternInterchange
from netex.models.service_link import ServiceLink
from netex.models.service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from netex.models.service_pattern import ServicePattern
from netex.models.service_site import ServiceSite
from netex.models.serviced_organisation import ServicedOrganisation
from netex.models.shelter_equipment import ShelterEquipment
from netex.models.sign_equipment import SignEquipment
from netex.models.site import Site
from netex.models.site_component import SiteComponent
from netex.models.site_connection import SiteConnection
from netex.models.site_element import SiteElement
from netex.models.site_equipment import SiteEquipment
from netex.models.site_frame import SiteFrame
from netex.models.site_path_link import SitePathLink
from netex.models.special_service import SpecialService
from netex.models.specific_parameter_assignment_version_structure import SpecificParameterAssignment
from netex.models.stair_equipment import StairEquipment
from netex.models.stair_flight import StairFlight
from netex.models.staircase_equipment import StaircaseEquipment
from netex.models.standard_fare_table import StandardFareTable
from netex.models.start_time_at_stop_point import StartTimeAtStopPoint
from netex.models.step_limit import StepLimit
from netex.models.stop_area import StopArea
from netex.models.stop_assignment import StopAssignment
from netex.models.stop_place import StopPlace
from netex.models.stop_place_component import StopPlaceComponent
from netex.models.stop_place_entrance import StopPlaceEntrance
from netex.models.stop_place_space import StopPlaceSpace
from netex.models.stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.submode import Submode
from netex.models.subscribing import Subscribing
from netex.models.supplement_product import SupplementProduct
from netex.models.suspending import Suspending
from netex.models.target_passing_time import TargetPassingTime
from netex.models.tariff import Tariff
from netex.models.tariff_zone_1 import TariffZone1
from netex.models.tariff_zone_2 import TariffZone2
from netex.models.template_service_journey import TemplateServiceJourney
from netex.models.template_vehicle_journey import TemplateVehicleJourney
from netex.models.third_party_product import ThirdPartyProduct
from netex.models.ticket_validator_equipment import TicketValidatorEquipment
from netex.models.ticketing_equipment import TicketingEquipment
from netex.models.ticketing_service import TicketingService
from netex.models.time_demand_profile import TimeDemandProfile
from netex.models.time_demand_profile_member import TimeDemandProfileMember
from netex.models.time_demand_type import TimeDemandType
from netex.models.time_demand_type_assignment import TimeDemandTypeAssignment
from netex.models.time_interval import TimeInterval
from netex.models.time_interval_price import TimeIntervalPrice
from netex.models.time_structure_factor import TimeStructureFactor
from netex.models.time_unit import TimeUnit
from netex.models.time_unit_price import TimeUnitPrice
from netex.models.timeband import Timeband
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetabled_passing_time import TimetabledPassingTime
from netex.models.timing_algorithm_type import TimingAlgorithmType
from netex.models.timing_link import TimingLink
from netex.models.timing_link_in_journey_pattern import TimingLinkInJourneyPattern
from netex.models.timing_pattern import TimingPattern
from netex.models.timing_point_1 import TimingPoint1
from netex.models.timing_point_2 import TimingPoint2
from netex.models.timing_point_in_journey_pattern import TimingPointInJourneyPattern
from netex.models.topographic_place import TopographicPlace
from netex.models.topographic_projection import TopographicProjection
from netex.models.traffic_control_point import TrafficControlPoint
from netex.models.train import Train
from netex.models.train_block import TrainBlock
from netex.models.train_block_part import TrainBlockPart
from netex.models.train_component import TrainComponent
from netex.models.train_component_label_assignment import TrainComponentLabelAssignment
from netex.models.train_element import TrainElement
from netex.models.train_number import TrainNumber
from netex.models.train_stop_assignment import TrainStopAssignment
from netex.models.transfer import Transfer
from netex.models.transfer_restriction import TransferRestriction
from netex.models.transferability import Transferability
from netex.models.transport_organisation import TransportOrganisation
from netex.models.travel_agent import TravelAgent
from netex.models.travel_document import TravelDocument
from netex.models.travel_document_security_listing import TravelDocumentSecurityListing
from netex.models.travel_specification_1 import TravelSpecification1
from netex.models.travel_specification_2 import TravelSpecification2
from netex.models.travelator_equipment import TravelatorEquipment
from netex.models.trolley_stand_equipment import TrolleyStandEquipment
from netex.models.turnaround_time_limit_time import TurnaroundTimeLimitTime
from netex.models.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.models.type_of_activation import TypeOfActivation
from netex.models.type_of_codespace_assignment import TypeOfCodespaceAssignment
from netex.models.type_of_concession import TypeOfConcession
from netex.models.type_of_congestion import TypeOfCongestion
from netex.models.type_of_customer_account import TypeOfCustomerAccount
from netex.models.type_of_delivery_variant import TypeOfDeliveryVariant
from netex.models.type_of_entity import TypeOfEntity
from netex.models.type_of_equipment import TypeOfEquipment
from netex.models.type_of_facility import TypeOfFacility
from netex.models.type_of_fare_contract import TypeOfFareContract
from netex.models.type_of_fare_contract_entry import TypeOfFareContractEntry
from netex.models.type_of_fare_product import TypeOfFareProduct
from netex.models.type_of_fare_structure_element import TypeOfFareStructureElement
from netex.models.type_of_fare_structure_factor import TypeOfFareStructureFactor
from netex.models.type_of_fare_table import TypeOfFareTable
from netex.models.type_of_feature import TypeOfFeature
from netex.models.type_of_flexible_service import TypeOfFlexibleService
from netex.models.type_of_journey_pattern import TypeOfJourneyPattern
from netex.models.type_of_line import TypeOfLine
from netex.models.type_of_link import TypeOfLink
from netex.models.type_of_link_sequence import TypeOfLinkSequence
from netex.models.type_of_machine_readability import TypeOfMachineReadability
from netex.models.type_of_notice import TypeOfNotice
from netex.models.type_of_operation import TypeOfOperation
from netex.models.type_of_organisation import TypeOfOrganisation
from netex.models.type_of_organisation_part import TypeOfOrganisationPart
from netex.models.type_of_passenger_information_equipment import TypeOfPassengerInformationEquipment
from netex.models.type_of_payment_method import TypeOfPaymentMethod
from netex.models.type_of_place import TypeOfPlace
from netex.models.type_of_point import TypeOfPoint
from netex.models.type_of_pricing_rule import TypeOfPricingRule
from netex.models.type_of_product_category import TypeOfProductCategory
from netex.models.type_of_projection import TypeOfProjection
from netex.models.type_of_responsibility_role import TypeOfResponsibilityRole
from netex.models.type_of_retail_device import TypeOfRetailDevice
from netex.models.type_of_sales_offer_package import TypeOfSalesOfferPackage
from netex.models.type_of_security_list import TypeOfSecurityList
from netex.models.type_of_service import TypeOfService
from netex.models.type_of_service_feature import TypeOfServiceFeature
from netex.models.type_of_tariff import TypeOfTariff
from netex.models.type_of_time_demand_type import TypeOfTimeDemandType
from netex.models.type_of_transfer import TypeOfTransfer
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.type_of_usage_parameter import TypeOfUsageParameter
from netex.models.type_of_validity import TypeOfValidity
from netex.models.type_of_value import TypeOfValue
from netex.models.type_of_version import TypeOfVersion
from netex.models.type_of_zone import TypeOfZone
from netex.models.types_of_frame_rel_structure import TypeOfFrame
from netex.models.uic_operating_period import UicOperatingPeriod
from netex.models.usage_discount_right import UsageDiscountRight
from netex.models.usage_parameter_1 import UsageParameter1
from netex.models.usage_parameter_2 import UsageParameter2
from netex.models.usage_parameter_price import UsageParameterPrice
from netex.models.usage_validity_period import UsageValidityPeriod
from netex.models.user_profile import UserProfile
from netex.models.user_profile_eligibility import UserProfileEligibility
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_price import ValidableElementPrice
from netex.models.validity_parameter_assignment import ValidityParameterAssignment
from netex.models.value_set import ValueSet
from netex.models.vehicle import Vehicle
from netex.models.vehicle_charging_equipment import VehicleChargingEquipment
from netex.models.vehicle_entrance import VehicleEntrance
from netex.models.vehicle_equipment_profile import VehicleEquipmentProfile
from netex.models.vehicle_journey_1 import VehicleJourney1
from netex.models.vehicle_journey_2 import VehicleJourney2
from netex.models.vehicle_journey_headway import VehicleJourneyHeadway
from netex.models.vehicle_journey_layover import VehicleJourneyLayover
from netex.models.vehicle_journey_run_time import VehicleJourneyRunTime
from netex.models.vehicle_journey_stop_assignment import VehicleJourneyStopAssignment
from netex.models.vehicle_journey_wait_time import VehicleJourneyWaitTime
from netex.models.vehicle_manoeuvring_requirement import VehicleManoeuvringRequirement
from netex.models.vehicle_model import VehicleModel
from netex.models.vehicle_position_alignment import VehiclePositionAlignment
from netex.models.vehicle_quay_alignment import VehicleQuayAlignment
from netex.models.vehicle_requirement import VehicleRequirement
from netex.models.vehicle_schedule_frame import VehicleScheduleFrame
from netex.models.vehicle_service import VehicleService
from netex.models.vehicle_service_part import VehicleServicePart
from netex.models.vehicle_stopping_place import VehicleStoppingPlace
from netex.models.vehicle_stopping_position import VehicleStoppingPosition
from netex.models.vehicle_type import VehicleType
from netex.models.vehicle_type_at_point import VehicleTypeAtPoint
from netex.models.vehicle_type_preference import VehicleTypePreference
from netex.models.vehicle_type_stop_assignment import VehicleTypeStopAssignment
from netex.models.version import Version
from netex.models.version_frame import VersionFrame
from netex.models.versioned_child import VersionedChild
from netex.models.waiting_equipment import WaitingEquipment
from netex.models.waiting_room_equipment import WaitingRoomEquipment
from netex.models.wheelchair_vehicle_equipment import WheelchairVehicleEquipment
from netex.models.whitelist import Whitelist
from netex.models.wire_element import WireElement
from netex.models.wire_junction import WireJunction
from netex.models.zone import Zone
from netex.models.zone_projection import ZoneProjection

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
    customer_eligibility: List[CustomerEligibility2] = field(
        default_factory=list,
        metadata={
            "name": "CustomerEligibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_customer_eligibility: List[CustomerEligibility1] = field(
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
    cell: List[Cell2] = field(
        default_factory=list,
        metadata={
            "name": "Cell",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_cell: List[Cell1] = field(
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
    fare_price: List[FarePrice2] = field(
        default_factory=list,
        metadata={
            "name": "FarePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_fare_price: List[FarePrice1] = field(
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
    security_listing: List[SecurityListing2] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_security_listing: List[SecurityListing1] = field(
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
    point_on_section: List[PointOnSection2] = field(
        default_factory=list,
        metadata={
            "name": "PointOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_point_on_section: List[PointOnSection1] = field(
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
    travel_specification: List[TravelSpecification2] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_travel_specification: List[TravelSpecification1] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_contract_entry: List[FareContractEntry2] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_fare_contract_entry: List[FareContractEntry1] = field(
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
    fare_product: List[FareProduct2] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_fare_product: List[FareProduct1] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_access_right: List[ServiceAccessRight2] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAccessRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_service_access_right: List[ServiceAccessRight1] = field(
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
    quality_structure_factor: List[QualityStructureFactor2] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_quality_structure_factor: List[QualityStructureFactor1] = field(
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
    usage_parameter: List[UsageParameter2] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_usage_parameter: List[UsageParameter1] = field(
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
    priceable_object: List[PriceableObject2] = field(
        default_factory=list,
        metadata={
            "name": "PriceableObject",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_priceable_object: List[PriceableObject1] = field(
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
    pricing_rule: List[PricingRule2] = field(
        default_factory=list,
        metadata={
            "name": "PricingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_pricing_rule: List[PricingRule1] = field(
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
    service_journey: List[ServiceJourney2] = field(
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
    netex_org_uk_netex_service_journey: List[ServiceJourney1] = field(
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
    vehicle_journey: List[VehicleJourney2] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_vehicle_journey: List[VehicleJourney1] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourney_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey: List[Journey2] = field(
        default_factory=list,
        metadata={
            "name": "Journey",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_journey: List[Journey1] = field(
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
    interchange: List[Interchange2] = field(
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
    netex_org_uk_netex_interchange: List[Interchange1] = field(
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
    line: List[Line2] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_line: List[Line1] = field(
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
    journey_pattern: List[JourneyPattern2] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_journey_pattern: List[JourneyPattern1] = field(
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
    route: List[Route2] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_route: List[Route1] = field(
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
    organisation_part: List[OrganisationPart2] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_organisation_part: List[OrganisationPart1] = field(
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
    organisation: List[Organisation2] = field(
        default_factory=list,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_organisation: List[Organisation1] = field(
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
    infrastructure_link: List[InfrastructureLink2] = field(
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
    netex_org_uk_netex_infrastructure_link: List[InfrastructureLink1] = field(
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
    parking_point: List[ParkingPoint2] = field(
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
    netex_org_uk_netex_parking_point: List[ParkingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    relief_point: List[ReliefPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_relief_point: List[ReliefPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timing_point: List[TimingPoint2] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_timing_point: List[TimingPoint1] = field(
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
    activation_point: List[ActivationPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_activation_point: List[ActivationPoint1] = field(
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
    access_right_parameter_assignment: List[AccessRightParameterAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_access_right_parameter_assignment: List[AccessRightParameterAssignment1] = field(
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
    notice_assignment: List[NoticeAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_notice_assignment: List[NoticeAssignment1] = field(
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
    assignment: List[Assignment2] = field(
        default_factory=list,
        metadata={
            "name": "Assignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_assignment: List[Assignment1] = field(
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
    day_type: List[DayType2] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_day_type: List[DayType1] = field(
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
    price_group: List[PriceGroup2] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_price_group: List[PriceGroup1] = field(
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
    fare_table: List[FareTable2] = field(
        default_factory=list,
        metadata={
            "name": "FareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_fare_table: List[FareTable1] = field(
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
    administrative_zone: List[AdministrativeZone2] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_administrative_zone: List[AdministrativeZone1] = field(
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
    tariff_zone: List[TariffZone2] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_tariff_zone: List[TariffZone1] = field(
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
    validity_condition: List[ValidityCondition2] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_validity_condition: List[ValidityCondition1] = field(
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
    travel_specification: List[TravelSpecification2] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_travel_specification: List[TravelSpecification1] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_entry: List[FareContractEntry2] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_fare_contract_entry: List[FareContractEntry1] = field(
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
    fare_product: List[FareProduct2] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_fare_product: List[FareProduct1] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_access_right: List[ServiceAccessRight2] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAccessRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_service_access_right: List[ServiceAccessRight1] = field(
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
    quality_structure_factor: List[QualityStructureFactor2] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_quality_structure_factor: List[QualityStructureFactor1] = field(
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
    usage_parameter: List[UsageParameter2] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_usage_parameter: List[UsageParameter1] = field(
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
    priceable_object: List[PriceableObject2] = field(
        default_factory=list,
        metadata={
            "name": "PriceableObject",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_priceable_object: List[PriceableObject1] = field(
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
    pricing_rule: List[PricingRule2] = field(
        default_factory=list,
        metadata={
            "name": "PricingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_pricing_rule: List[PricingRule1] = field(
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
    service_journey: List[ServiceJourney2] = field(
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
    netex_org_uk_netex_service_journey: List[ServiceJourney1] = field(
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
    vehicle_journey: List[VehicleJourney2] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_vehicle_journey: List[VehicleJourney1] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourney_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey: List[Journey2] = field(
        default_factory=list,
        metadata={
            "name": "Journey",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_journey: List[Journey1] = field(
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
    interchange: List[Interchange2] = field(
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
    netex_org_uk_netex_interchange: List[Interchange1] = field(
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
    line: List[Line2] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_line: List[Line1] = field(
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
    journey_pattern: List[JourneyPattern2] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_journey_pattern: List[JourneyPattern1] = field(
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
    route: List[Route2] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_route: List[Route1] = field(
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
    organisation_part: List[OrganisationPart2] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_organisation_part: List[OrganisationPart1] = field(
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
    organisation: List[Organisation2] = field(
        default_factory=list,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_organisation: List[Organisation1] = field(
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
    infrastructure_link: List[InfrastructureLink2] = field(
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
    netex_org_uk_netex_infrastructure_link: List[InfrastructureLink1] = field(
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
    parking_point: List[ParkingPoint2] = field(
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
    netex_org_uk_netex_parking_point: List[ParkingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_point: List[ReliefPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_relief_point: List[ReliefPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point: List[TimingPoint2] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_timing_point: List[TimingPoint1] = field(
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
    activation_point: List[ActivationPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_activation_point: List[ActivationPoint1] = field(
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
    access_right_parameter_assignment: List[AccessRightParameterAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_access_right_parameter_assignment: List[AccessRightParameterAssignment1] = field(
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
    notice_assignment: List[NoticeAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_notice_assignment: List[NoticeAssignment1] = field(
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
    assignment: List[Assignment2] = field(
        default_factory=list,
        metadata={
            "name": "Assignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_assignment: List[Assignment1] = field(
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
    day_type: List[DayType2] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_day_type: List[DayType1] = field(
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
    price_group: List[PriceGroup2] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_price_group: List[PriceGroup1] = field(
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
    fare_table: List[FareTable2] = field(
        default_factory=list,
        metadata={
            "name": "FareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_fare_table: List[FareTable1] = field(
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
    administrative_zone: List[AdministrativeZone2] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_administrative_zone: List[AdministrativeZone1] = field(
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
    tariff_zone: List[TariffZone2] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_tariff_zone: List[TariffZone1] = field(
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
    validity_condition: List[ValidityCondition2] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_validity_condition: List[ValidityCondition1] = field(
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
