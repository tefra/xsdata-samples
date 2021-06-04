from dataclasses import dataclass, field
from typing import Optional
from netex.models.abstract_group_member_versioned_child_structure import AbstractGroupMemberVersionedChildStructure
from netex.models.access_ref import AccessRef
from netex.models.access_right_in_product_ref import AccessRightInProductRef
from netex.models.access_space_ref import AccessSpaceRef
from netex.models.access_zone_ref import AccessZoneRef
from netex.models.accommodation_ref import AccommodationRef
from netex.models.accountable_element_ref import AccountableElementRef
from netex.models.activation_link_ref import ActivationLinkRef
from netex.models.activation_point_ref import ActivationPointRef
from netex.models.address_ref import AddressRef
from netex.models.addressable_place_ref import AddressablePlaceRef
from netex.models.administrative_zone_ref import AdministrativeZoneRef
from netex.models.all_authorities_ref import AllAuthoritiesRef
from netex.models.all_distribution_channels_ref import AllDistributionChannelsRef
from netex.models.all_operators_ref import AllOperatorsRef
from netex.models.all_organisations_ref import AllOrganisationsRef
from netex.models.all_transport_organisations_ref import AllTransportOrganisationsRef
from netex.models.allowed_line_direction_ref import AllowedLineDirectionRef
from netex.models.alternative_name_ref import AlternativeNameRef
from netex.models.alternative_text_ref import AlternativeTextRef
from netex.models.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.models.authority_ref import AuthorityRef
from netex.models.availability_condition_ref import AvailabilityConditionRef
from netex.models.beacon_point_ref import BeaconPointRef
from netex.models.blacklist_ref import BlacklistRef
from netex.models.block_part_ref import BlockPartRef
from netex.models.block_ref import BlockRef
from netex.models.boarding_position_ref import BoardingPositionRef
from netex.models.border_point_ref import BorderPointRef
from netex.models.branding_ref import BrandingRef
from netex.models.cancelling_ref import CancellingRef
from netex.models.capped_discount_right_ref import CappedDiscountRightRef
from netex.models.capping_rule_price_ref import CappingRulePriceRef
from netex.models.capping_rule_ref import CappingRuleRef
from netex.models.cell_ref_1 import CellRef1
from netex.models.cell_ref_2 import CellRef2
from netex.models.charging_moment_ref import ChargingMomentRef
from netex.models.charging_policy_ref import ChargingPolicyRef
from netex.models.class_of_use_ref import ClassOfUseRef
from netex.models.commercial_profile_eligibility_ref import CommercialProfileEligibilityRef
from netex.models.commercial_profile_ref import CommercialProfileRef
from netex.models.common_section_ref import CommonSectionRef
from netex.models.companion_profile_ref import CompanionProfileRef
from netex.models.complex_feature_projection_ref import ComplexFeatureProjectionRef
from netex.models.complex_feature_ref_structure import ComplexFeatureRefStructure
from netex.models.composite_frame_ref import CompositeFrameRef
from netex.models.compound_block_ref import CompoundBlockRef
from netex.models.compound_train_ref import CompoundTrainRef
from netex.models.connection_ref import ConnectionRef
from netex.models.control_centre_ref import ControlCentreRef
from netex.models.controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from netex.models.controllable_element_price_ref import ControllableElementPriceRef
from netex.models.controllable_element_ref import ControllableElementRef
from netex.models.coupled_journey_ref import CoupledJourneyRef
from netex.models.course_of_journeys_ref import CourseOfJourneysRef
from netex.models.crew_base_ref import CrewBaseRef
from netex.models.customer_account_ref import CustomerAccountRef
from netex.models.customer_account_security_listing_ref import CustomerAccountSecurityListingRef
from netex.models.customer_account_status_ref import CustomerAccountStatusRef
from netex.models.customer_eligibility_ref import CustomerEligibilityRef
from netex.models.customer_purchase_package_element_ref import CustomerPurchasePackageElementRef
from netex.models.customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from netex.models.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.models.customer_ref import CustomerRef
from netex.models.customer_security_listing_ref import CustomerSecurityListingRef
from netex.models.data_source_ref import DataSourceRef
from netex.models.dated_special_service_ref import DatedSpecialServiceRef
from netex.models.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from netex.models.day_type_ref import DayTypeRef
from netex.models.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from netex.models.dead_run_ref import DeadRunRef
from netex.models.default_connection_ref import DefaultConnectionRef
from netex.models.default_dead_run_run_time_ref import DefaultDeadRunRunTimeRef
from netex.models.default_interchange_ref import DefaultInterchangeRef
from netex.models.default_service_journey_time_ref import DefaultServiceJourneyTimeRef
from netex.models.delivery_variant_ref import DeliveryVariantRef
from netex.models.department_ref import DepartmentRef
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.destination_display_variant_ref import DestinationDisplayVariantRef
from netex.models.direction_ref import DirectionRef
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from netex.models.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.models.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.models.distribution_channel_ref import DistributionChannelRef
from netex.models.driver_ref import DriverRef
from netex.models.driver_schedule_frame_ref import DriverScheduleFrameRef
from netex.models.driver_trip_ref import DriverTripRef
from netex.models.driver_trip_time_ref import DriverTripTimeRef
from netex.models.duty_part_ref import DutyPartRef
from netex.models.duty_ref import DutyRef
from netex.models.eligibility_change_policy_ref import EligibilityChangePolicyRef
from netex.models.entitlement_given_ref import EntitlementGivenRef
from netex.models.entitlement_product_ref import EntitlementProductRef
from netex.models.entitlement_required_ref import EntitlementRequiredRef
from netex.models.entrance_ref import EntranceRef
from netex.models.equipment_place_ref import EquipmentPlaceRef
from netex.models.equipment_position_ref import EquipmentPositionRef
from netex.models.estimated_passing_time_ref import EstimatedPassingTimeRef
from netex.models.exchanging_ref import ExchangingRef
from netex.models.facility_ref import FacilityRef
from netex.models.facility_requirement_ref import FacilityRequirementRef
from netex.models.facility_set_ref import FacilitySetRef
from netex.models.fare_contract_entry_ref import FareContractEntryRef
from netex.models.fare_contract_ref import FareContractRef
from netex.models.fare_contract_security_listing_ref import FareContractSecurityListingRef
from netex.models.fare_day_type_ref import FareDayTypeRef
from netex.models.fare_demand_factor_ref import FareDemandFactorRef
from netex.models.fare_element_in_sequence_ref import FareElementInSequenceRef
from netex.models.fare_frame_ref import FareFrameRef
from netex.models.fare_interval_ref import FareIntervalRef
from netex.models.fare_price_ref import FarePriceRef
from netex.models.fare_product_price_ref import FareProductPriceRef
from netex.models.fare_product_ref import FareProductRef
from netex.models.fare_quota_factor_ref import FareQuotaFactorRef
from netex.models.fare_request_ref import FareRequestRef
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.fare_section_ref import FareSectionRef
from netex.models.fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from netex.models.fare_structure_element_price_ref import FareStructureElementPriceRef
from netex.models.fare_structure_element_ref import FareStructureElementRef
from netex.models.fare_structure_factor_ref import FareStructureFactorRef
from netex.models.fare_table_column_ref import FareTableColumnRef
from netex.models.fare_table_ref import FareTableRef
from netex.models.fare_table_row_ref import FareTableRowRef
from netex.models.fare_unit_ref import FareUnitRef
from netex.models.fare_zone_ref import FareZoneRef
from netex.models.flexible_area_ref import FlexibleAreaRef
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.flexible_link_properties_ref import FlexibleLinkPropertiesRef
from netex.models.flexible_point_properties_ref import FlexiblePointPropertiesRef
from netex.models.flexible_quay_ref import FlexibleQuayRef
from netex.models.flexible_service_properties_ref import FlexibleServicePropertiesRef
from netex.models.flexible_stop_place_ref import FlexibleStopPlaceRef
from netex.models.frequency_of_use_ref import FrequencyOfUseRef
from netex.models.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from netex.models.fulfilment_method_ref import FulfilmentMethodRef
from netex.models.garage_point_ref import GaragePointRef
from netex.models.garage_ref import GarageRef
from netex.models.general_frame_ref import GeneralFrameRef
from netex.models.general_group_of_entities_ref import GeneralGroupOfEntitiesRef
from netex.models.general_organisation_ref import GeneralOrganisationRef
from netex.models.general_section_ref import GeneralSectionRef
from netex.models.geographical_interval_price_ref import GeographicalIntervalPriceRef
from netex.models.geographical_interval_ref import GeographicalIntervalRef
from netex.models.geographical_structure_factor_ref import GeographicalStructureFactorRef
from netex.models.geographical_unit_price_ref import GeographicalUnitPriceRef
from netex.models.geographical_unit_ref import GeographicalUnitRef
from netex.models.group_of_customer_purchase_packages_ref import GroupOfCustomerPurchasePackagesRef
from netex.models.group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from netex.models.group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from netex.models.group_of_entities_ref_1 import GroupOfEntitiesRef1
from netex.models.group_of_entities_ref_2 import GroupOfEntitiesRef2
from netex.models.group_of_lines_ref import GroupOfLinesRef
from netex.models.group_of_link_sequences_ref import GroupOfLinkSequencesRef
from netex.models.group_of_operators_ref import GroupOfOperatorsRef
from netex.models.group_of_places_ref import GroupOfPlacesRef
from netex.models.group_of_points_ref_1 import GroupOfPointsRef1
from netex.models.group_of_points_ref_2 import GroupOfPointsRef2
from netex.models.group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from netex.models.group_of_services_ref import GroupOfServicesRef
from netex.models.group_of_stop_places_ref import GroupOfStopPlacesRef
from netex.models.group_of_timebands_ref import GroupOfTimebandsRef
from netex.models.group_of_timing_links_ref import GroupOfTimingLinksRef
from netex.models.group_ticket_ref import GroupTicketRef
from netex.models.hail_and_ride_area_ref import HailAndRideAreaRef
from netex.models.headway_journey_group_ref import HeadwayJourneyGroupRef
from netex.models.headway_ref import HeadwayRef
from netex.models.infrastructure_frame_ref import InfrastructureFrameRef
from netex.models.infrastructure_link_ref import InfrastructureLinkRef
from netex.models.infrastructure_point_ref import InfrastructurePointRef
from netex.models.interchange_ref import InterchangeRef
from netex.models.interchange_rule_ref import InterchangeRuleRef
from netex.models.interchange_rule_timing_ref import InterchangeRuleTimingRef
from netex.models.interchanging_ref import InterchangingRef
from netex.models.journey_frequency_group_ref import JourneyFrequencyGroupRef
from netex.models.journey_meeting_ref import JourneyMeetingRef
from netex.models.journey_part_couple_ref import JourneyPartCoupleRef
from netex.models.journey_part_ref import JourneyPartRef
from netex.models.journey_pattern_headway_ref import JourneyPatternHeadwayRef
from netex.models.journey_pattern_layover_ref import JourneyPatternLayoverRef
from netex.models.journey_pattern_ref import JourneyPatternRef
from netex.models.journey_pattern_run_time_ref import JourneyPatternRunTimeRef
from netex.models.journey_pattern_wait_time_ref import JourneyPatternWaitTimeRef
from netex.models.journey_ref import JourneyRef
from netex.models.journey_timing_ref import JourneyTimingRef
from netex.models.layer_ref import LayerRef
from netex.models.level_ref import LevelRef
from netex.models.limiting_rule_ref import LimitingRuleRef
from netex.models.line_link_ref import LineLinkRef
from netex.models.line_network_ref import LineNetworkRef
from netex.models.line_ref import LineRef
from netex.models.line_section_ref import LineSectionRef
from netex.models.link_projection_ref import LinkProjectionRef
from netex.models.link_ref import LinkRef
from netex.models.link_sequence_projection_ref import LinkSequenceProjectionRef
from netex.models.link_sequence_ref import LinkSequenceRef
from netex.models.log_entry_ref import LogEntryRef
from netex.models.log_ref import LogRef
from netex.models.logical_display_ref import LogicalDisplayRef
from netex.models.luggage_allowance_ref import LuggageAllowanceRef
from netex.models.management_agent_ref import ManagementAgentRef
from netex.models.minimum_stay_ref import MinimumStayRef
from netex.models.mode_ref import ModeRef
from netex.models.month_validity_offset_ref import MonthValidityOffsetRef
from netex.models.navigation_path_ref import NavigationPathRef
from netex.models.network_ref import NetworkRef
from netex.models.notice_ref import NoticeRef
from netex.models.observed_passing_time_ref import ObservedPassingTimeRef
from netex.models.offered_travel_specification_ref import OfferedTravelSpecificationRef
from netex.models.onboard_stay_ref import OnboardStayRef
from netex.models.open_transport_mode_ref import OpenTransportModeRef
from netex.models.operating_day_ref import OperatingDayRef
from netex.models.operating_department_ref import OperatingDepartmentRef
from netex.models.operating_period_ref import OperatingPeriodRef
from netex.models.operational_context_ref import OperationalContextRef
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_part_ref import OrganisationPartRef
from netex.models.organisation_ref import OrganisationRef
from netex.models.organisational_unit_ref import OrganisationalUnitRef
from netex.models.other_organisation_ref import OtherOrganisationRef
from netex.models.parent_common_section_ref import ParentCommonSectionRef
from netex.models.parent_section_ref import ParentSectionRef
from netex.models.parking_area_ref import ParkingAreaRef
from netex.models.parking_bay_ref import ParkingBayRef
from netex.models.parking_capacity_ref import ParkingCapacityRef
from netex.models.parking_charge_band_ref import ParkingChargeBandRef
from netex.models.parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from netex.models.parking_entrance_ref import ParkingEntranceRef
from netex.models.parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from netex.models.parking_point_ref import ParkingPointRef
from netex.models.parking_price_ref import ParkingPriceRef
from netex.models.parking_properties_ref import ParkingPropertiesRef
from netex.models.parking_ref import ParkingRef
from netex.models.parking_tariff_ref import ParkingTariffRef
from netex.models.passenger_capacity_ref import PassengerCapacityRef
from netex.models.passenger_carrying_requirement_ref import PassengerCarryingRequirementRef
from netex.models.passenger_information_request_ref import PassengerInformationRequestRef
from netex.models.passenger_seat_ref import PassengerSeatRef
from netex.models.passing_time_ref import PassingTimeRef
from netex.models.path_junction_ref import PathJunctionRef
from netex.models.path_link_ref import PathLinkRef
from netex.models.penalty_policy_ref import PenaltyPolicyRef
from netex.models.place_ref_1 import PlaceRef1
from netex.models.place_ref_2 import PlaceRef2
from netex.models.point_of_interest_classification_ref import PointOfInterestClassificationRef
from netex.models.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from netex.models.point_of_interest_hierarchy_ref import PointOfInterestHierarchyRef
from netex.models.point_of_interest_ref import PointOfInterestRef
from netex.models.point_of_interest_space_ref import PointOfInterestSpaceRef
from netex.models.point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from netex.models.point_on_link_ref import PointOnLinkRef
from netex.models.point_projection_ref import PointProjectionRef
from netex.models.point_ref import PointRef
from netex.models.postal_address_ref import PostalAddressRef
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.price_group_ref import PriceGroupRef
from netex.models.price_unit_ref import PriceUnitRef
from netex.models.priceable_object_ref import PriceableObjectRef
from netex.models.pricing_parameter_set_ref import PricingParameterSetRef
from netex.models.pricing_rule_ref import PricingRuleRef
from netex.models.pricing_service_ref import PricingServiceRef
from netex.models.profile_parameter_ref import ProfileParameterRef
from netex.models.projection_ref import ProjectionRef
from netex.models.purchase_window_ref import PurchaseWindowRef
from netex.models.purpose_of_equipment_profile_ref import PurposeOfEquipmentProfileRef
from netex.models.purpose_of_grouping_ref import PurposeOfGroupingRef
from netex.models.purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from netex.models.quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from netex.models.quality_structure_factor_ref import QualityStructureFactorRef
from netex.models.quay_ref import QuayRef
from netex.models.railway_link_ref import RailwayLinkRef
from netex.models.railway_point_ref import RailwayPointRef
from netex.models.refunding_ref import RefundingRef
from netex.models.relief_opportunity_ref import ReliefOpportunityRef
from netex.models.relief_point_ref import ReliefPointRef
from netex.models.repeated_trip_fare_request_ref import RepeatedTripFareRequestRef
from netex.models.replacing_ref import ReplacingRef
from netex.models.requested_travel_specification_ref import RequestedTravelSpecificationRef
from netex.models.reselling_ref import ResellingRef
from netex.models.reserving_ref import ReservingRef
from netex.models.residential_qualification_eligibility_ref import ResidentialQualificationEligibilityRef
from netex.models.residential_qualification_ref import ResidentialQualificationRef
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.responsibility_role_ref import ResponsibilityRoleRef
from netex.models.responsibility_set_ref import ResponsibilitySetRef
from netex.models.retail_consortium_ref import RetailConsortiumRef
from netex.models.retail_device_security_listing_ref import RetailDeviceSecurityListingRef
from netex.models.rhythmical_journey_group_ref import RhythmicalJourneyGroupRef
from netex.models.road_address_ref import RoadAddressRef
from netex.models.road_link_ref import RoadLinkRef
from netex.models.road_point_ref import RoadPointRef
from netex.models.round_trip_ref import RoundTripRef
from netex.models.rounding_ref import RoundingRef
from netex.models.rounding_step_ref import RoundingStepRef
from netex.models.route_instruction_ref import RouteInstructionRef
from netex.models.route_link_ref import RouteLinkRef
from netex.models.route_point_ref import RoutePointRef
from netex.models.route_ref import RouteRef
from netex.models.routing_constraint_zone_ref import RoutingConstraintZoneRef
from netex.models.routing_ref import RoutingRef
from netex.models.sale_discount_right_ref import SaleDiscountRightRef
from netex.models.sales_offer_package_element_ref import SalesOfferPackageElementRef
from netex.models.sales_offer_package_entitlement_given_ref import SalesOfferPackageEntitlementGivenRef
from netex.models.sales_offer_package_entitlement_required_ref import SalesOfferPackageEntitlementRequiredRef
from netex.models.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_transaction_frame_ref import SalesTransactionFrameRef
from netex.models.sales_transaction_ref import SalesTransactionRef
from netex.models.schedule_request_ref import ScheduleRequestRef
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.schematic_map_member_ref import SchematicMapMemberRef
from netex.models.schematic_map_ref import SchematicMapRef
from netex.models.section_ref import SectionRef
from netex.models.security_list_ref import SecurityListRef
from netex.models.security_listing_ref import SecurityListingRef
from netex.models.series_constraint_price_ref import SeriesConstraintPriceRef
from netex.models.series_constraint_ref import SeriesConstraintRef
from netex.models.service_access_right_ref import ServiceAccessRightRef
from netex.models.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.models.service_calendar_ref import ServiceCalendarRef
from netex.models.service_facility_set_ref import ServiceFacilitySetRef
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.service_journey_interchange_ref import ServiceJourneyInterchangeRef
from netex.models.service_journey_pattern_interchange_ref import ServiceJourneyPatternInterchangeRef
from netex.models.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.models.service_journey_ref import ServiceJourneyRef
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.service_site_ref import ServiceSiteRef
from netex.models.serviced_organisation_ref import ServicedOrganisationRef
from netex.models.simple_feature_ref import SimpleFeatureRef
from netex.models.single_trip_fare_request_ref import SingleTripFareRequestRef
from netex.models.site_component_ref import SiteComponentRef
from netex.models.site_connection_ref import SiteConnectionRef
from netex.models.site_element_ref import SiteElementRef
from netex.models.site_facility_set_ref import SiteFacilitySetRef
from netex.models.site_frame_ref import SiteFrameRef
from netex.models.site_ref import SiteRef
from netex.models.special_service_ref import SpecialServiceRef
from netex.models.standard_fare_table_ref import StandardFareTableRef
from netex.models.start_time_at_stop_point_ref import StartTimeAtStopPointRef
from netex.models.step_limit_ref import StepLimitRef
from netex.models.stop_area_ref import StopAreaRef
from netex.models.stop_event_request_ref import StopEventRequestRef
from netex.models.stop_finder_request_ref import StopFinderRequestRef
from netex.models.stop_place_entrance_ref import StopPlaceEntranceRef
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_place_space_ref import StopPlaceSpaceRef
from netex.models.stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from netex.models.submode_ref import SubmodeRef
from netex.models.subscribing_ref import SubscribingRef
from netex.models.supplement_product_ref import SupplementProductRef
from netex.models.supply_contract_ref import SupplyContractRef
from netex.models.suspending_ref import SuspendingRef
from netex.models.target_passing_time_ref import TargetPassingTimeRef
from netex.models.tariff_object_ref import TariffObjectRef
from netex.models.tariff_ref import TariffRef
from netex.models.tariff_zone_ref_1 import TariffZoneRef1
from netex.models.tariff_zone_ref_2 import TariffZoneRef2
from netex.models.template_service_journey_ref import TemplateServiceJourneyRef
from netex.models.third_party_product_ref import ThirdPartyProductRef
from netex.models.time_demand_profile_ref import TimeDemandProfileRef
from netex.models.time_demand_type_ref import TimeDemandTypeRef
from netex.models.time_interval_price_ref import TimeIntervalPriceRef
from netex.models.time_interval_ref import TimeIntervalRef
from netex.models.time_structure_factor_ref import TimeStructureFactorRef
from netex.models.time_unit_price_ref import TimeUnitPriceRef
from netex.models.time_unit_ref import TimeUnitRef
from netex.models.timeband_ref import TimebandRef
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.timetabled_passing_time_ref import TimetabledPassingTimeRef
from netex.models.timing_algorithm_type_ref import TimingAlgorithmTypeRef
from netex.models.timing_link_ref import TimingLinkRef
from netex.models.timing_pattern_ref import TimingPatternRef
from netex.models.timing_point_ref import TimingPointRef
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.topographic_projection_ref import TopographicProjectionRef
from netex.models.traffic_control_point_ref import TrafficControlPointRef
from netex.models.train_block_part_ref import TrainBlockPartRef
from netex.models.train_block_ref import TrainBlockRef
from netex.models.train_component_ref import TrainComponentRef
from netex.models.train_element_ref import TrainElementRef
from netex.models.train_in_compound_train_ref import TrainInCompoundTrainRef
from netex.models.train_number_ref import TrainNumberRef
from netex.models.train_ref import TrainRef
from netex.models.transfer_ref import TransferRef
from netex.models.transferability_ref import TransferabilityRef
from netex.models.transport_administrative_zone_ref import TransportAdministrativeZoneRef
from netex.models.transport_organisation_ref import TransportOrganisationRef
from netex.models.travel_agent_ref import TravelAgentRef
from netex.models.travel_document_ref import TravelDocumentRef
from netex.models.travel_document_security_listing_ref import TravelDocumentSecurityListingRef
from netex.models.travel_specification_ref import TravelSpecificationRef
from netex.models.trip_plan_request_ref import TripPlanRequestRef
from netex.models.turnaround_time_limit_time_ref import TurnaroundTimeLimitTimeRef
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_activation_ref import TypeOfActivationRef
from netex.models.type_of_codespace_assignment_ref import TypeOfCodespaceAssignmentRef
from netex.models.type_of_concession_ref import TypeOfConcessionRef
from netex.models.type_of_congestion_ref import TypeOfCongestionRef
from netex.models.type_of_customer_account_ref import TypeOfCustomerAccountRef
from netex.models.type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from netex.models.type_of_entity_ref import TypeOfEntityRef
from netex.models.type_of_equipment_ref import TypeOfEquipmentRef
from netex.models.type_of_facility_ref import TypeOfFacilityRef
from netex.models.type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef
from netex.models.type_of_fare_contract_ref import TypeOfFareContractRef
from netex.models.type_of_fare_product_ref import TypeOfFareProductRef
from netex.models.type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from netex.models.type_of_fare_structure_factor_ref import TypeOfFareStructureFactorRef
from netex.models.type_of_fare_table_ref import TypeOfFareTableRef
from netex.models.type_of_feature_ref import TypeOfFeatureRef
from netex.models.type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from netex.models.type_of_frame_ref import TypeOfFrameRef
from netex.models.type_of_journey_pattern_ref import TypeOfJourneyPatternRef
from netex.models.type_of_line_ref import TypeOfLineRef
from netex.models.type_of_link_ref import TypeOfLinkRef
from netex.models.type_of_link_sequence_ref import TypeOfLinkSequenceRef
from netex.models.type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from netex.models.type_of_notice_ref import TypeOfNoticeRef
from netex.models.type_of_operation_ref import TypeOfOperationRef
from netex.models.type_of_organisation_part_ref import TypeOfOrganisationPartRef
from netex.models.type_of_organisation_ref import TypeOfOrganisationRef
from netex.models.type_of_passenger_information_equipment_ref import TypeOfPassengerInformationEquipmentRef
from netex.models.type_of_payment_method_ref import TypeOfPaymentMethodRef
from netex.models.type_of_place_ref import TypeOfPlaceRef
from netex.models.type_of_point_ref import TypeOfPointRef
from netex.models.type_of_pricing_rule_ref import TypeOfPricingRuleRef
from netex.models.type_of_product_category_ref import TypeOfProductCategoryRef
from netex.models.type_of_projection_ref import TypeOfProjectionRef
from netex.models.type_of_responsibility_role_ref import TypeOfResponsibilityRoleRef
from netex.models.type_of_retail_device_ref import TypeOfRetailDeviceRef
from netex.models.type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef
from netex.models.type_of_security_list_ref import TypeOfSecurityListRef
from netex.models.type_of_service_feature_ref import TypeOfServiceFeatureRef
from netex.models.type_of_service_ref import TypeOfServiceRef
from netex.models.type_of_tariff_ref import TypeOfTariffRef
from netex.models.type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from netex.models.type_of_transfer_ref import TypeOfTransferRef
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.type_of_usage_parameter_ref import TypeOfUsageParameterRef
from netex.models.type_of_validity_ref import TypeOfValidityRef
from netex.models.type_of_value_ref import TypeOfValueRef
from netex.models.type_of_zone_ref import TypeOfZoneRef
from netex.models.usage_discount_right_ref import UsageDiscountRightRef
from netex.models.usage_parameter_price_ref import UsageParameterPriceRef
from netex.models.usage_parameter_ref import UsageParameterRef
from netex.models.usage_validity_period_ref import UsageValidityPeriodRef
from netex.models.user_profile_eligibility_ref import UserProfileEligibilityRef
from netex.models.user_profile_ref import UserProfileRef
from netex.models.validable_element_price_ref import ValidableElementPriceRef
from netex.models.validable_element_ref import ValidableElementRef
from netex.models.validity_condition_ref import ValidityConditionRef
from netex.models.validity_rule_parameter_ref import ValidityRuleParameterRef
from netex.models.validity_trigger_ref import ValidityTriggerRef
from netex.models.vehicle_entrance_ref import VehicleEntranceRef
from netex.models.vehicle_equipment_profile_ref import VehicleEquipmentProfileRef
from netex.models.vehicle_journey_ref import VehicleJourneyRef
from netex.models.vehicle_manoeuvring_requirement_ref import VehicleManoeuvringRequirementRef
from netex.models.vehicle_model_ref import VehicleModelRef
from netex.models.vehicle_position_alignment_ref import VehiclePositionAlignmentRef
from netex.models.vehicle_quay_alignment_ref import VehicleQuayAlignmentRef
from netex.models.vehicle_ref import VehicleRef
from netex.models.vehicle_requirement_ref import VehicleRequirementRef
from netex.models.vehicle_schedule_frame_ref import VehicleScheduleFrameRef
from netex.models.vehicle_service_part_ref import VehicleServicePartRef
from netex.models.vehicle_service_ref import VehicleServiceRef
from netex.models.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from netex.models.vehicle_stopping_position_ref import VehicleStoppingPositionRef
from netex.models.vehicle_type_preference_ref import VehicleTypePreferenceRef
from netex.models.vehicle_type_ref import VehicleTypeRef
from netex.models.version_frame_ref import VersionFrameRef
from netex.models.version_of_object_ref import VersionOfObjectRef
from netex.models.version_ref import VersionRef
from netex.models.whitelist_ref import WhitelistRef
from netex.models.wire_link_ref import WireLinkRef
from netex.models.wire_point_ref import WirePointRef
from netex.models.zone_projection_ref import ZoneProjectionRef
from netex.models.zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplexFeatureMemberVersionedChildStructure(AbstractGroupMemberVersionedChildStructure):
    class Meta:
        name = "ComplexFeatureMember_VersionedChildStructure"

    complex_feature_ref: Optional[ComplexFeatureRefStructure] = field(
        default=None,
        metadata={
            "name": "ComplexFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    simple_feature_ref: Optional[SimpleFeatureRef] = field(
        default=None,
        metadata={
            "name": "SimpleFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_document_ref: Optional[TravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    repeated_trip_fare_request_ref: Optional[RepeatedTripFareRequestRef] = field(
        default=None,
        metadata={
            "name": "RepeatedTripFareRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    single_trip_fare_request_ref: Optional[SingleTripFareRequestRef] = field(
        default=None,
        metadata={
            "name": "SingleTripFareRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_request_ref: Optional[FareRequestRef] = field(
        default=None,
        metadata={
            "name": "FareRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_finder_request_ref: Optional[StopFinderRequestRef] = field(
        default=None,
        metadata={
            "name": "StopFinderRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_event_request_ref: Optional[StopEventRequestRef] = field(
        default=None,
        metadata={
            "name": "StopEventRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    schedule_request_ref: Optional[ScheduleRequestRef] = field(
        default=None,
        metadata={
            "name": "ScheduleRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trip_plan_request_ref: Optional[TripPlanRequestRef] = field(
        default=None,
        metadata={
            "name": "TripPlanRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_information_request_ref: Optional[PassengerInformationRequestRef] = field(
        default=None,
        metadata={
            "name": "PassengerInformationRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    residential_qualification_eligibility_ref: Optional[ResidentialQualificationEligibilityRef] = field(
        default=None,
        metadata={
            "name": "ResidentialQualificationEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    commercial_profile_eligibility_ref: Optional[CommercialProfileEligibilityRef] = field(
        default=None,
        metadata={
            "name": "CommercialProfileEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    user_profile_eligibility_ref: Optional[UserProfileEligibilityRef] = field(
        default=None,
        metadata={
            "name": "UserProfileEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_eligibility_ref: Optional[CustomerEligibilityRef] = field(
        default=None,
        metadata={
            "name": "CustomerEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_ref: Optional[FareContractRef] = field(
        default=None,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time_at_stop_point_ref: Optional[StartTimeAtStopPointRef] = field(
        default=None,
        metadata={
            "name": "StartTimeAtStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    residential_qualification_ref: Optional[ResidentialQualificationRef] = field(
        default=None,
        metadata={
            "name": "ResidentialQualificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_concession_ref: Optional[TypeOfConcessionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_usage_parameter_ref: Optional[TypeOfUsageParameterRef] = field(
        default=None,
        metadata={
            "name": "TypeOfUsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_object_ref: Optional[TariffObjectRef] = field(
        default=None,
        metadata={
            "name": "TariffObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_tariff_ref: Optional[ParkingTariffRef] = field(
        default=None,
        metadata={
            "name": "ParkingTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_ref: Optional[TariffRef] = field(
        default=None,
        metadata={
            "name": "TariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_table_ref: Optional[TypeOfFareTableRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_table_row_ref: Optional[FareTableRowRef] = field(
        default=None,
        metadata={
            "name": "FareTableRowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_table_column_ref: Optional[FareTableColumnRef] = field(
        default=None,
        metadata={
            "name": "FareTableColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_unit_ref: Optional[FareUnitRef] = field(
        default=None,
        metadata={
            "name": "FareUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_in_sequence_ref: Optional[ControllableElementInSequenceRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_in_sequence_ref: Optional[FareStructureElementInSequenceRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_right_in_product_ref: Optional[AccessRightInProductRef] = field(
        default=None,
        metadata={
            "name": "AccessRightInProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_element_in_sequence_ref: Optional[FareElementInSequenceRef] = field(
        default=None,
        metadata={
            "name": "FareElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cell_ref: Optional[CellRef2] = field(
        default=None,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_cell_ref: Optional[CellRef1] = field(
        default=None,
        metadata={
            "name": "CellRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_price_ref: Optional[CustomerPurchasePackagePriceRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_price_ref: Optional[ParkingPriceRef] = field(
        default=None,
        metadata={
            "name": "ParkingPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_interval_price_ref: Optional[TimeIntervalPriceRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit_price_ref: Optional[TimeUnitPriceRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factor_price_ref: Optional[QualityStructureFactorPriceRef] = field(
        default=None,
        metadata={
            "name": "QualityStructureFactorPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_price_ref: Optional[ControllableElementPriceRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element_price_ref: Optional[ValidableElementPriceRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval_price_ref: Optional[GeographicalIntervalPriceRef] = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_price_ref: Optional[GeographicalUnitPriceRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameter_price_ref: Optional[UsageParameterPriceRef] = field(
        default=None,
        metadata={
            "name": "UsageParameterPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_price_ref: Optional[SalesOfferPackagePriceRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_price_ref: Optional[DistanceMatrixElementPriceRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_price_ref: Optional[FareStructureElementPriceRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_method_price_ref: Optional[FulfilmentMethodPriceRef] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraint_price_ref: Optional[SeriesConstraintPriceRef] = field(
        default=None,
        metadata={
            "name": "SeriesConstraintPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capping_rule_price_ref: Optional[CappingRulePriceRef] = field(
        default=None,
        metadata={
            "name": "CappingRulePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_product_price_ref: Optional[FareProductPriceRef] = field(
        default=None,
        metadata={
            "name": "FareProductPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_price_ref: Optional[FarePriceRef] = field(
        default=None,
        metadata={
            "name": "FarePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_element_ref: Optional[CustomerPurchasePackageElementRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_ref: Optional[CustomerPurchasePackageRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_ref: Optional[ControllableElementRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_entitlement_given_ref: Optional[SalesOfferPackageEntitlementGivenRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageEntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_entitlement_required_ref: Optional[SalesOfferPackageEntitlementRequiredRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageEntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_stay_ref: Optional[MinimumStayRef] = field(
        default=None,
        metadata={
            "name": "MinimumStayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchanging_ref: Optional[InterchangingRef] = field(
        default=None,
        metadata={
            "name": "InterchangingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency_of_use_ref: Optional[FrequencyOfUseRef] = field(
        default=None,
        metadata={
            "name": "FrequencyOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suspending_ref: Optional[SuspendingRef] = field(
        default=None,
        metadata={
            "name": "SuspendingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_validity_period_ref: Optional[UsageValidityPeriodRef] = field(
        default=None,
        metadata={
            "name": "UsageValidityPeriodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    step_limit_ref: Optional[StepLimitRef] = field(
        default=None,
        metadata={
            "name": "StepLimitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routing_ref: Optional[RoutingRef] = field(
        default=None,
        metadata={
            "name": "RoutingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    round_trip_ref: Optional[RoundTripRef] = field(
        default=None,
        metadata={
            "name": "RoundTripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_allowance_ref: Optional[LuggageAllowanceRef] = field(
        default=None,
        metadata={
            "name": "LuggageAllowanceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_given_ref: Optional[EntitlementGivenRef] = field(
        default=None,
        metadata={
            "name": "EntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_required_ref: Optional[EntitlementRequiredRef] = field(
        default=None,
        metadata={
            "name": "EntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    eligibility_change_policy_ref: Optional[EligibilityChangePolicyRef] = field(
        default=None,
        metadata={
            "name": "EligibilityChangePolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_ticket_ref: Optional[GroupTicketRef] = field(
        default=None,
        metadata={
            "name": "GroupTicketRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    commercial_profile_ref: Optional[CommercialProfileRef] = field(
        default=None,
        metadata={
            "name": "CommercialProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    companion_profile_ref: Optional[CompanionProfileRef] = field(
        default=None,
        metadata={
            "name": "CompanionProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    user_profile_ref: Optional[UserProfileRef] = field(
        default=None,
        metadata={
            "name": "UserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    profile_parameter_ref: Optional[ProfileParameterRef] = field(
        default=None,
        metadata={
            "name": "ProfileParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    subscribing_ref: Optional[SubscribingRef] = field(
        default=None,
        metadata={
            "name": "SubscribingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    penalty_policy_ref: Optional[PenaltyPolicyRef] = field(
        default=None,
        metadata={
            "name": "PenaltyPolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_policy_ref: Optional[ChargingPolicyRef] = field(
        default=None,
        metadata={
            "name": "ChargingPolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transferability_ref: Optional[TransferabilityRef] = field(
        default=None,
        metadata={
            "name": "TransferabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    replacing_ref: Optional[ReplacingRef] = field(
        default=None,
        metadata={
            "name": "ReplacingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    refunding_ref: Optional[RefundingRef] = field(
        default=None,
        metadata={
            "name": "RefundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchanging_ref: Optional[ExchangingRef] = field(
        default=None,
        metadata={
            "name": "ExchangingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reselling_ref: Optional[ResellingRef] = field(
        default=None,
        metadata={
            "name": "ResellingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cancelling_ref: Optional[CancellingRef] = field(
        default=None,
        metadata={
            "name": "CancellingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reserving_ref: Optional[ReservingRef] = field(
        default=None,
        metadata={
            "name": "ReservingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purchase_window_ref: Optional[PurchaseWindowRef] = field(
        default=None,
        metadata={
            "name": "PurchaseWindowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameter_ref: Optional[UsageParameterRef] = field(
        default=None,
        metadata={
            "name": "UsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_element_ref: Optional[SalesOfferPackageElementRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_inverse_ref: Optional[DistanceMatrixElementInverseRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementInverseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_ref: Optional[DistanceMatrixElementRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_method_ref: Optional[FulfilmentMethodRef] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraint_ref: Optional[SeriesConstraintRef] = field(
        default=None,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capping_rule_ref: Optional[CappingRuleRef] = field(
        default=None,
        metadata={
            "name": "CappingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_product_ref: Optional[EntitlementProductRef] = field(
        default=None,
        metadata={
            "name": "EntitlementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supplement_product_ref: Optional[SupplementProductRef] = field(
        default=None,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preassigned_fare_product_ref: Optional[PreassignedFareProductRef] = field(
        default=None,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    amount_of_price_unit_product_ref: Optional[AmountOfPriceUnitProductRef] = field(
        default=None,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_discount_right_ref: Optional[UsageDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    third_party_product_ref: Optional[ThirdPartyProductRef] = field(
        default=None,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capped_discount_right_ref: Optional[CappedDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sale_discount_right_ref: Optional[SaleDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_product_ref: Optional[FareProductRef] = field(
        default=None,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_access_right_ref: Optional[ServiceAccessRightRef] = field(
        default=None,
        metadata={
            "name": "ServiceAccessRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_interval_ref: Optional[TimeIntervalRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval_ref: Optional[GeographicalIntervalRef] = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_interval_ref: Optional[FareIntervalRef] = field(
        default=None,
        metadata={
            "name": "FareIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_charge_band_ref: Optional[ParkingChargeBandRef] = field(
        default=None,
        metadata={
            "name": "ParkingChargeBandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_structure_factor_ref: Optional[TimeStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "TimeStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_quota_factor_ref: Optional[FareQuotaFactorRef] = field(
        default=None,
        metadata={
            "name": "FareQuotaFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_demand_factor_ref: Optional[FareDemandFactorRef] = field(
        default=None,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factor_ref: Optional[QualityStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "QualityStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_structure_factor_ref: Optional[GeographicalStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "GeographicalStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_factor_ref: Optional[FareStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "FareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    priceable_object_ref: Optional[PriceableObjectRef] = field(
        default=None,
        metadata={
            "name": "PriceableObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    month_validity_offset_ref: Optional[MonthValidityOffsetRef] = field(
        default=None,
        metadata={
            "name": "MonthValidityOffsetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limiting_rule_ref: Optional[LimitingRuleRef] = field(
        default=None,
        metadata={
            "name": "LimitingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    discounting_rule_ref: Optional[DiscountingRuleRef] = field(
        default=None,
        metadata={
            "name": "DiscountingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_rule_ref: Optional[PricingRuleRef] = field(
        default=None,
        metadata={
            "name": "PricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_service_ref: Optional[PricingServiceRef] = field(
        default=None,
        metadata={
            "name": "PricingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_step_ref: Optional[RoundingStepRef] = field(
        default=None,
        metadata={
            "name": "RoundingStepRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_parameter_set_ref: Optional[PricingParameterSetRef] = field(
        default=None,
        metadata={
            "name": "PricingParameterSetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supply_contract_ref: Optional[SupplyContractRef] = field(
        default=None,
        metadata={
            "name": "SupplyContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_service_properties_ref: Optional[FlexibleServicePropertiesRef] = field(
        default=None,
        metadata={
            "name": "FlexibleServicePropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_trip_time_ref: Optional[DriverTripTimeRef] = field(
        default=None,
        metadata={
            "name": "DriverTripTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_trip_ref: Optional[DriverTripRef] = field(
        default=None,
        metadata={
            "name": "DriverTripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty_part_ref: Optional[DutyPartRef] = field(
        default=None,
        metadata={
            "name": "DutyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accountable_element_ref: Optional[AccountableElementRef] = field(
        default=None,
        metadata={
            "name": "AccountableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty_ref: Optional[DutyRef] = field(
        default=None,
        metadata={
            "name": "DutyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_opportunity_ref: Optional[ReliefOpportunityRef] = field(
        default=None,
        metadata={
            "name": "ReliefOpportunityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    course_of_journeys_ref: Optional[CourseOfJourneysRef] = field(
        default=None,
        metadata={
            "name": "CourseOfJourneysRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_ref: Optional[DriverRef] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_service_part_ref: Optional[VehicleServicePartRef] = field(
        default=None,
        metadata={
            "name": "VehicleServicePartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_service_ref: Optional[VehicleServiceRef] = field(
        default=None,
        metadata={
            "name": "VehicleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_block_ref: Optional[CompoundBlockRef] = field(
        default=None,
        metadata={
            "name": "CompoundBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block_part_ref: Optional[TrainBlockPartRef] = field(
        default=None,
        metadata={
            "name": "TrainBlockPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block_part_ref: Optional[BlockPartRef] = field(
        default=None,
        metadata={
            "name": "BlockPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block_ref: Optional[TrainBlockRef] = field(
        default=None,
        metadata={
            "name": "TrainBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block_ref: Optional[BlockRef] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_couple_ref: Optional[JourneyPartCoupleRef] = field(
        default=None,
        metadata={
            "name": "JourneyPartCoupleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    coupled_journey_ref: Optional[CoupledJourneyRef] = field(
        default=None,
        metadata={
            "name": "CoupledJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_ref: Optional[JourneyPartRef] = field(
        default=None,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timetabled_passing_time_ref: Optional[TimetabledPassingTimeRef] = field(
        default=None,
        metadata={
            "name": "TimetabledPassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    estimated_passing_time_ref: Optional[EstimatedPassingTimeRef] = field(
        default=None,
        metadata={
            "name": "EstimatedPassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    observed_passing_time_ref: Optional[ObservedPassingTimeRef] = field(
        default=None,
        metadata={
            "name": "ObservedPassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    target_passing_time_ref: Optional[TargetPassingTimeRef] = field(
        default=None,
        metadata={
            "name": "TargetPassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passing_time_ref: Optional[PassingTimeRef] = field(
        default=None,
        metadata={
            "name": "PassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange_rule_timing_ref: Optional[InterchangeRuleTimingRef] = field(
        default=None,
        metadata={
            "name": "InterchangeRuleTimingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange_rule_ref: Optional[InterchangeRuleRef] = field(
        default=None,
        metadata={
            "name": "InterchangeRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_pattern_interchange_ref: Optional[ServiceJourneyPatternInterchangeRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_interchange_ref: Optional[ServiceJourneyInterchangeRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_interchange_ref: Optional[DefaultInterchangeRef] = field(
        default=None,
        metadata={
            "name": "DefaultInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange_ref: Optional[InterchangeRef] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_meeting_ref: Optional[JourneyMeetingRef] = field(
        default=None,
        metadata={
            "name": "JourneyMeetingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_number_ref: Optional[TrainNumberRef] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routing_constraint_zone_ref: Optional[RoutingConstraintZoneRef] = field(
        default=None,
        metadata={
            "name": "RoutingConstraintZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_position_alignment_ref: Optional[VehiclePositionAlignmentRef] = field(
        default=None,
        metadata={
            "name": "VehiclePositionAlignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_quay_alignment_ref: Optional[VehicleQuayAlignmentRef] = field(
        default=None,
        metadata={
            "name": "VehicleQuayAlignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    logical_display_ref: Optional[LogicalDisplayRef] = field(
        default=None,
        metadata={
            "name": "LogicalDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_area_ref: Optional[ParkingAreaRef] = field(
        default=None,
        metadata={
            "name": "ParkingAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_properties_ref: Optional[ParkingPropertiesRef] = field(
        default=None,
        metadata={
            "name": "ParkingPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_capacity_ref: Optional[ParkingCapacityRef] = field(
        default=None,
        metadata={
            "name": "ParkingCapacityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_network_ref: Optional[LineNetworkRef] = field(
        default=None,
        metadata={
            "name": "LineNetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_instruction_ref: Optional[RouteInstructionRef] = field(
        default=None,
        metadata={
            "name": "RouteInstructionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    level_ref: Optional[LevelRef] = field(
        default=None,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_point_properties_ref: Optional[FlexiblePointPropertiesRef] = field(
        default=None,
        metadata={
            "name": "FlexiblePointPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_link_properties_ref: Optional[FlexibleLinkPropertiesRef] = field(
        default=None,
        metadata={
            "name": "FlexibleLinkPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_profile_ref: Optional[TimeDemandProfileRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type_preference_ref: Optional[VehicleTypePreferenceRef] = field(
        default=None,
        metadata={
            "name": "VehicleTypePreferenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_headway_ref: Optional[JourneyPatternHeadwayRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternHeadwayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_layover_ref: Optional[JourneyPatternLayoverRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternLayoverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_run_time_ref: Optional[JourneyPatternRunTimeRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRunTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_wait_time_ref: Optional[JourneyPatternWaitTimeRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternWaitTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_service_journey_time_ref: Optional[DefaultServiceJourneyTimeRef] = field(
        default=None,
        metadata={
            "name": "DefaultServiceJourneyTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_dead_run_run_time_ref: Optional[DefaultDeadRunRunTimeRef] = field(
        default=None,
        metadata={
            "name": "DefaultDeadRunRunTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    turnaround_time_limit_time_ref: Optional[TurnaroundTimeLimitTimeRef] = field(
        default=None,
        metadata={
            "name": "TurnaroundTimeLimitTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headway_ref: Optional[HeadwayRef] = field(
        default=None,
        metadata={
            "name": "HeadwayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_timing_ref: Optional[JourneyTimingRef] = field(
        default=None,
        metadata={
            "name": "JourneyTimingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crew_base_ref: Optional[CrewBaseRef] = field(
        default=None,
        metadata={
            "name": "CrewBaseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_seat_ref: Optional[PassengerSeatRef] = field(
        default=None,
        metadata={
            "name": "PassengerSeatRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_department_ref: Optional[OperatingDepartmentRef] = field(
        default=None,
        metadata={
            "name": "OperatingDepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component_ref: Optional[TrainComponentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_element_ref: Optional[TrainElementRef] = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_in_compound_train_ref: Optional[TrainInCompoundTrainRef] = field(
        default=None,
        metadata={
            "name": "TrainInCompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_document_security_listing_ref: Optional[TravelDocumentSecurityListingRef] = field(
        default=None,
        metadata={
            "name": "TravelDocumentSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_device_security_listing_ref: Optional[RetailDeviceSecurityListingRef] = field(
        default=None,
        metadata={
            "name": "RetailDeviceSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_security_listing_ref: Optional[CustomerAccountSecurityListingRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_security_listing_ref: Optional[FareContractSecurityListingRef] = field(
        default=None,
        metadata={
            "name": "FareContractSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_security_listing_ref: Optional[CustomerSecurityListingRef] = field(
        default=None,
        metadata={
            "name": "CustomerSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    security_listing_ref: Optional[SecurityListingRef] = field(
        default=None,
        metadata={
            "name": "SecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    whitelist_ref: Optional[WhitelistRef] = field(
        default=None,
        metadata={
            "name": "WhitelistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    blacklist_ref: Optional[BlacklistRef] = field(
        default=None,
        metadata={
            "name": "BlacklistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    security_list_ref: Optional[SecurityListRef] = field(
        default=None,
        metadata={
            "name": "SecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    schematic_map_member_ref: Optional[SchematicMapMemberRef] = field(
        default=None,
        metadata={
            "name": "SchematicMapMemberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    schematic_map_ref: Optional[SchematicMapRef] = field(
        default=None,
        metadata={
            "name": "SchematicMapRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delivery_variant_ref: Optional[DeliveryVariantRef] = field(
        default=None,
        metadata={
            "name": "DeliveryVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_ref: Optional[NoticeRef] = field(
        default=None,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_equipment_profile_ref: Optional[VehicleEquipmentProfileRef] = field(
        default=None,
        metadata={
            "name": "VehicleEquipmentProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_model_ref: Optional[VehicleModelRef] = field(
        default=None,
        metadata={
            "name": "VehicleModelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_capacity_ref: Optional[PassengerCapacityRef] = field(
        default=None,
        metadata={
            "name": "PassengerCapacityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facility_requirement_ref: Optional[FacilityRequirementRef] = field(
        default=None,
        metadata={
            "name": "FacilityRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_manoeuvring_requirement_ref: Optional[VehicleManoeuvringRequirementRef] = field(
        default=None,
        metadata={
            "name": "VehicleManoeuvringRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_carrying_requirement_ref: Optional[PassengerCarryingRequirementRef] = field(
        default=None,
        metadata={
            "name": "PassengerCarryingRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_requirement_ref: Optional[VehicleRequirementRef] = field(
        default=None,
        metadata={
            "name": "VehicleRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_train_ref: Optional[CompoundTrainRef] = field(
        default=None,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_ref: Optional[TrainRef] = field(
        default=None,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    onboard_stay_ref: Optional[OnboardStayRef] = field(
        default=None,
        metadata={
            "name": "OnboardStayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accommodation_ref: Optional[AccommodationRef] = field(
        default=None,
        metadata={
            "name": "AccommodationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_set_ref: Optional[ServiceFacilitySetRef] = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_facility_set_ref: Optional[SiteFacilitySetRef] = field(
        default=None,
        metadata={
            "name": "SiteFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facility_set_ref: Optional[FacilitySetRef] = field(
        default=None,
        metadata={
            "name": "FacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facility_ref: Optional[FacilityRef] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mode_ref: Optional[ModeRef] = field(
        default=None,
        metadata={
            "name": "ModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    submode_ref: Optional[SubmodeRef] = field(
        default=None,
        metadata={
            "name": "SubmodeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    open_transport_mode_ref: Optional[OpenTransportModeRef] = field(
        default=None,
        metadata={
            "name": "OpenTransportModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_projection_ref: Optional[TopographicProjectionRef] = field(
        default=None,
        metadata={
            "name": "TopographicProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complex_feature_projection_ref: Optional[ComplexFeatureProjectionRef] = field(
        default=None,
        metadata={
            "name": "ComplexFeatureProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_sequence_projection_ref: Optional[LinkSequenceProjectionRef] = field(
        default=None,
        metadata={
            "name": "LinkSequenceProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_projection_ref: Optional[ZoneProjectionRef] = field(
        default=None,
        metadata={
            "name": "ZoneProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_projection_ref: Optional[LinkProjectionRef] = field(
        default=None,
        metadata={
            "name": "LinkProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_projection_ref: Optional[PointProjectionRef] = field(
        default=None,
        metadata={
            "name": "PointProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    projection_ref: Optional[ProjectionRef] = field(
        default=None,
        metadata={
            "name": "ProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_link_sequences_ref: Optional[GroupOfLinkSequencesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfLinkSequencesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_special_service_ref: Optional[DatedSpecialServiceRef] = field(
        default=None,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    special_service_ref: Optional[SpecialServiceRef] = field(
        default=None,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    template_service_journey_ref: Optional[TemplateServiceJourneyRef] = field(
        default=None,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_ref: Optional[ServiceJourneyRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_ref: Optional[DeadRunRef] = field(
        default=None,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_ref: Optional[JourneyRef] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_path_ref: Optional[NavigationPathRef] = field(
        default=None,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_pattern_ref: Optional[ServiceJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_pattern_ref: Optional[ServicePatternRef] = field(
        default=None,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_journey_pattern_ref: Optional[DeadRunJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_ref: Optional[JourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_pattern_ref: Optional[TimingPatternRef] = field(
        default=None,
        metadata={
            "name": "TimingPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_sequence_ref: Optional[LinkSequenceRef] = field(
        default=None,
        metadata={
            "name": "LinkSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transaction_ref: Optional[SalesTransactionRef] = field(
        default=None,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    offered_travel_specification_ref: Optional[OfferedTravelSpecificationRef] = field(
        default=None,
        metadata={
            "name": "OfferedTravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requested_travel_specification_ref: Optional[RequestedTravelSpecificationRef] = field(
        default=None,
        metadata={
            "name": "RequestedTravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specification_ref: Optional[TravelSpecificationRef] = field(
        default=None,
        metadata={
            "name": "TravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_entry_ref: Optional[FareContractEntryRef] = field(
        default=None,
        metadata={
            "name": "FareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    log_entry_ref: Optional[LogEntryRef] = field(
        default=None,
        metadata={
            "name": "LogEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_name_ref: Optional[AlternativeNameRef] = field(
        default=None,
        metadata={
            "name": "AlternativeNameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timeband_ref: Optional[TimebandRef] = field(
        default=None,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_day_type_ref: Optional[FareDayTypeRef] = field(
        default=None,
        metadata={
            "name": "FareDayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type_ref: Optional[DayTypeRef] = field(
        default=None,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_connection_ref: Optional[DefaultConnectionRef] = field(
        default=None,
        metadata={
            "name": "DefaultConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_connection_ref: Optional[SiteConnectionRef] = field(
        default=None,
        metadata={
            "name": "SiteConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connection_ref: Optional[ConnectionRef] = field(
        default=None,
        metadata={
            "name": "ConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_ref: Optional[AccessRef] = field(
        default=None,
        metadata={
            "name": "AccessRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfer_ref: Optional[TransferRef] = field(
        default=None,
        metadata={
            "name": "TransferRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hail_and_ride_area_ref: Optional[HailAndRideAreaRef] = field(
        default=None,
        metadata={
            "name": "HailAndRideAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_area_ref: Optional[FlexibleAreaRef] = field(
        default=None,
        metadata={
            "name": "FlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_quay_ref: Optional[FlexibleQuayRef] = field(
        default=None,
        metadata={
            "name": "FlexibleQuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_stop_place_ref: Optional[FlexibleStopPlaceRef] = field(
        default=None,
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_junction_ref: Optional[PathJunctionRef] = field(
        default=None,
        metadata={
            "name": "PathJunctionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_place_ref: Optional[EquipmentPlaceRef] = field(
        default=None,
        metadata={
            "name": "EquipmentPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_position_ref: Optional[EquipmentPositionRef] = field(
        default=None,
        metadata={
            "name": "EquipmentPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_position_ref: Optional[VehicleStoppingPositionRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_place_ref: Optional[VehicleStoppingPlaceRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_space_ref: Optional[AccessSpaceRef] = field(
        default=None,
        metadata={
            "name": "AccessSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_ref: Optional[QuayRef] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_space_ref: Optional[StopPlaceSpaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_bay_ref: Optional[ParkingBayRef] = field(
        default=None,
        metadata={
            "name": "ParkingBayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_space_ref: Optional[PointOfInterestSpaceRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_vehicle_entrance_ref: Optional[StopPlaceVehicleEntranceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_entrance_ref: Optional[StopPlaceEntranceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_for_vehicles_ref: Optional[ParkingEntranceForVehiclesRef] = field(
        default=None,
        metadata={
            "name": "ParkingEntranceForVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_passenger_entrance_ref: Optional[ParkingPassengerEntranceRef] = field(
        default=None,
        metadata={
            "name": "ParkingPassengerEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_ref: Optional[ParkingEntranceRef] = field(
        default=None,
        metadata={
            "name": "ParkingEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_vehicle_entrance_ref: Optional[PointOfInterestVehicleEntranceRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_entrance_ref: Optional[PointOfInterestEntranceRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_entrance_ref: Optional[VehicleEntranceRef] = field(
        default=None,
        metadata={
            "name": "VehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_ref: Optional[EntranceRef] = field(
        default=None,
        metadata={
            "name": "EntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_component_ref: Optional[SiteComponentRef] = field(
        default=None,
        metadata={
            "name": "SiteComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_ref: Optional[ParkingRef] = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_ref: Optional[PointOfInterestRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_site_ref: Optional[ServiceSiteRef] = field(
        default=None,
        metadata={
            "name": "ServiceSiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_ref: Optional[SiteRef] = field(
        default=None,
        metadata={
            "name": "SiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_element_ref: Optional[SiteElementRef] = field(
        default=None,
        metadata={
            "name": "SiteElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage_ref: Optional[GarageRef] = field(
        default=None,
        metadata={
            "name": "GarageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    addressable_place_ref: Optional[AddressablePlaceRef] = field(
        default=None,
        metadata={
            "name": "AddressablePlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    postal_address_ref: Optional[PostalAddressRef] = field(
        default=None,
        metadata={
            "name": "PostalAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_address_ref: Optional[RoadAddressRef] = field(
        default=None,
        metadata={
            "name": "RoadAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    address_ref: Optional[AddressRef] = field(
        default=None,
        metadata={
            "name": "AddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_ref: Optional[PlaceRef1] = field(
        default=None,
        metadata={
            "name": "PlaceRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_link_ref: Optional[ServiceLinkRef] = field(
        default=None,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_link_ref: Optional[LineLinkRef] = field(
        default=None,
        metadata={
            "name": "LineLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_link_ref: Optional[PathLinkRef] = field(
        default=None,
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_ref: Optional[TimingLinkRef] = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_link_ref: Optional[RouteLinkRef] = field(
        default=None,
        metadata={
            "name": "RouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_link_ref: Optional[WireLinkRef] = field(
        default=None,
        metadata={
            "name": "WireLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_link_ref: Optional[RoadLinkRef] = field(
        default=None,
        metadata={
            "name": "RoadLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_link_ref: Optional[RailwayLinkRef] = field(
        default=None,
        metadata={
            "name": "RailwayLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_link_ref: Optional[InfrastructureLinkRef] = field(
        default=None,
        metadata={
            "name": "InfrastructureLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_link_ref: Optional[ActivationLinkRef] = field(
        default=None,
        metadata={
            "name": "ActivationLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_ref: Optional[LinkRef] = field(
        default=None,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_point_ref: Optional[BorderPointRef] = field(
        default=None,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref: Optional[FareScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage_point_ref: Optional[GaragePointRef] = field(
        default=None,
        metadata={
            "name": "GaragePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_point_ref: Optional[ParkingPointRef] = field(
        default=None,
        metadata={
            "name": "ParkingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_point_ref: Optional[ReliefPointRef] = field(
        default=None,
        metadata={
            "name": "ReliefPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_ref: Optional[TimingPointRef] = field(
        default=None,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_point_ref: Optional[RoutePointRef] = field(
        default=None,
        metadata={
            "name": "RoutePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_point_ref: Optional[WirePointRef] = field(
        default=None,
        metadata={
            "name": "WirePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_point_ref: Optional[RoadPointRef] = field(
        default=None,
        metadata={
            "name": "RoadPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_point_ref: Optional[RailwayPointRef] = field(
        default=None,
        metadata={
            "name": "RailwayPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_point_ref: Optional[InfrastructurePointRef] = field(
        default=None,
        metadata={
            "name": "InfrastructurePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    traffic_control_point_ref: Optional[TrafficControlPointRef] = field(
        default=None,
        metadata={
            "name": "TrafficControlPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    beacon_point_ref: Optional[BeaconPointRef] = field(
        default=None,
        metadata={
            "name": "BeaconPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_point_ref: Optional[ActivationPointRef] = field(
        default=None,
        metadata={
            "name": "ActivationPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_on_link_ref: Optional[PointOnLinkRef] = field(
        default=None,
        metadata={
            "name": "PointOnLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_ref: Optional[PointRef] = field(
        default=None,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_period_ref: Optional[OperatingPeriodRef] = field(
        default=None,
        metadata={
            "name": "OperatingPeriodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_day_ref: Optional[OperatingDayRef] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar_ref: Optional[ServiceCalendarRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_text_ref: Optional[AlternativeTextRef] = field(
        default=None,
        metadata={
            "name": "AlternativeTextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    availability_condition_ref: Optional[AvailabilityConditionRef] = field(
        default=None,
        metadata={
            "name": "AvailabilityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_rule_parameter_ref: Optional[ValidityRuleParameterRef] = field(
        default=None,
        metadata={
            "name": "ValidityRuleParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_trigger_ref: Optional[ValidityTriggerRef] = field(
        default=None,
        metadata={
            "name": "ValidityTriggerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_condition_ref: Optional[ValidityConditionRef] = field(
        default=None,
        metadata={
            "name": "ValidityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_role_ref: Optional[ResponsibilityRoleRef] = field(
        default=None,
        metadata={
            "name": "ResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre_ref: Optional[ControlCentreRef] = field(
        default=None,
        metadata={
            "name": "ControlCentreRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisational_unit_ref: Optional[OrganisationalUnitRef] = field(
        default=None,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    department_ref: Optional[DepartmentRef] = field(
        default=None,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_part_ref: Optional[OrganisationPartRef] = field(
        default=None,
        metadata={
            "name": "OrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_authorities_ref: Optional[AllAuthoritiesRef] = field(
        default=None,
        metadata={
            "name": "AllAuthoritiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_operators_ref: Optional[AllOperatorsRef] = field(
        default=None,
        metadata={
            "name": "AllOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_transport_organisations_ref: Optional[AllTransportOrganisationsRef] = field(
        default=None,
        metadata={
            "name": "AllTransportOrganisationsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_organisations_ref: Optional[AllOrganisationsRef] = field(
        default=None,
        metadata={
            "name": "AllOrganisationsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_consortium_ref: Optional[RetailConsortiumRef] = field(
        default=None,
        metadata={
            "name": "RetailConsortiumRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref: Optional[AuthorityRef] = field(
        default=None,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_organisation_ref: Optional[TransportOrganisationRef] = field(
        default=None,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_organisation_ref: Optional[GeneralOrganisationRef] = field(
        default=None,
        metadata={
            "name": "GeneralOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    management_agent_ref: Optional[ManagementAgentRef] = field(
        default=None,
        metadata={
            "name": "ManagementAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    serviced_organisation_ref: Optional[ServicedOrganisationRef] = field(
        default=None,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_agent_ref: Optional[TravelAgentRef] = field(
        default=None,
        metadata={
            "name": "TravelAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    other_organisation_ref: Optional[OtherOrganisationRef] = field(
        default=None,
        metadata={
            "name": "OtherOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_ref: Optional[OrganisationRef] = field(
        default=None,
        metadata={
            "name": "OrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_set_ref: Optional[ResponsibilitySetRef] = field(
        default=None,
        metadata={
            "name": "ResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_variant_ref: Optional[DestinationDisplayVariantRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allowed_line_direction_ref: Optional[AllowedLineDirectionRef] = field(
        default=None,
        metadata={
            "name": "AllowedLineDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_line_ref: Optional[FlexibleLineRef] = field(
        default=None,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_entities_ref: Optional[GroupOfEntitiesRef2] = field(
        default=None,
        metadata={
            "name": "GroupOfEntitiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_customer_purchase_packages_ref: Optional[GroupOfCustomerPurchasePackagesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfCustomerPurchasePackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_sales_offer_packages_ref: Optional[GroupOfSalesOfferPackagesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distance_matrix_elements_ref: Optional[GroupOfDistanceMatrixElementsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distribution_channels_ref: Optional[GroupOfDistributionChannelsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfDistributionChannelsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_fare_table_ref: Optional[StandardFareTableRef] = field(
        default=None,
        metadata={
            "name": "StandardFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_table_ref: Optional[FareTableRef] = field(
        default=None,
        metadata={
            "name": "FareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_group_ref: Optional[PriceGroupRef] = field(
        default=None,
        metadata={
            "name": "PriceGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rhythmical_journey_group_ref: Optional[RhythmicalJourneyGroupRef] = field(
        default=None,
        metadata={
            "name": "RhythmicalJourneyGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headway_journey_group_ref: Optional[HeadwayJourneyGroupRef] = field(
        default=None,
        metadata={
            "name": "HeadwayJourneyGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_frequency_group_ref: Optional[JourneyFrequencyGroupRef] = field(
        default=None,
        metadata={
            "name": "JourneyFrequencyGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_services_ref: Optional[GroupOfServicesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfServicesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_stop_places_ref: Optional[GroupOfStopPlacesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfStopPlacesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_hierarchy_ref: Optional[PointOfInterestHierarchyRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestHierarchyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_timing_links_ref: Optional[GroupOfTimingLinksRef] = field(
        default=None,
        metadata={
            "name": "GroupOfTimingLinksRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_operators_ref: Optional[GroupOfOperatorsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_places_ref: Optional[GroupOfPlacesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfPlacesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_section_ref: Optional[ParentSectionRef] = field(
        default=None,
        metadata={
            "name": "ParentSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_common_section_ref: Optional[ParentCommonSectionRef] = field(
        default=None,
        metadata={
            "name": "ParentCommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    common_section_ref: Optional[CommonSectionRef] = field(
        default=None,
        metadata={
            "name": "CommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_section_ref: Optional[LineSectionRef] = field(
        default=None,
        metadata={
            "name": "LineSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_section_ref: Optional[FareSectionRef] = field(
        default=None,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_section_ref: Optional[GeneralSectionRef] = field(
        default=None,
        metadata={
            "name": "GeneralSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    log_ref: Optional[LogRef] = field(
        default=None,
        metadata={
            "name": "LogRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_timebands_ref: Optional[GroupOfTimebandsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfTimebandsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_place_ref: Optional[PlaceRef2] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_points_ref: Optional[GroupOfPointsRef2] = field(
        default=None,
        metadata={
            "name": "GroupOfPointsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_area_ref: Optional[StopAreaRef] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_zone_ref: Optional[AccessZoneRef] = field(
        default=None,
        metadata={
            "name": "AccessZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_administrative_zone_ref: Optional[TransportAdministrativeZoneRef] = field(
        default=None,
        metadata={
            "name": "TransportAdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    administrative_zone_ref: Optional[AdministrativeZoneRef] = field(
        default=None,
        metadata={
            "name": "AdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_zone_ref: Optional[FareZoneRef] = field(
        default=None,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone_ref: Optional[TariffZoneRef2] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_tariff_zone_ref: Optional[TariffZoneRef1] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_ref: Optional[ZoneRef] = field(
        default=None,
        metadata={
            "name": "ZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_group_of_points_ref: Optional[GroupOfPointsRef1] = field(
        default=None,
        metadata={
            "name": "GroupOfPointsRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layer_ref: Optional[LayerRef] = field(
        default=None,
        metadata={
            "name": "LayerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network_ref: Optional[NetworkRef] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_lines_ref: Optional[GroupOfLinesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_group_of_entities_ref: Optional[GeneralGroupOfEntitiesRef] = field(
        default=None,
        metadata={
            "name": "GeneralGroupOfEntitiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_group_of_entities_ref: Optional[GroupOfEntitiesRef1] = field(
        default=None,
        metadata={
            "name": "GroupOfEntitiesRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transaction_frame_ref: Optional[SalesTransactionFrameRef] = field(
        default=None,
        metadata={
            "name": "SalesTransactionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_frame_ref: Optional[FareFrameRef] = field(
        default=None,
        metadata={
            "name": "FareFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_frame_ref: Optional[ServiceFrameRef] = field(
        default=None,
        metadata={
            "name": "ServiceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_schedule_frame_ref: Optional[DriverScheduleFrameRef] = field(
        default=None,
        metadata={
            "name": "DriverScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_schedule_frame_ref: Optional[VehicleScheduleFrameRef] = field(
        default=None,
        metadata={
            "name": "VehicleScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timetable_frame_ref: Optional[TimetableFrameRef] = field(
        default=None,
        metadata={
            "name": "TimetableFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_frame_ref: Optional[SiteFrameRef] = field(
        default=None,
        metadata={
            "name": "SiteFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_frame_ref: Optional[InfrastructureFrameRef] = field(
        default=None,
        metadata={
            "name": "InfrastructureFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_frame_ref: Optional[GeneralFrameRef] = field(
        default=None,
        metadata={
            "name": "GeneralFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    resource_frame_ref: Optional[ResourceFrameRef] = field(
        default=None,
        metadata={
            "name": "ResourceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar_frame_ref: Optional[ServiceCalendarFrameRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    composite_frame_ref: Optional[CompositeFrameRef] = field(
        default=None,
        metadata={
            "name": "CompositeFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_frame_ref: Optional[VersionFrameRef] = field(
        default=None,
        metadata={
            "name": "VersionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_channel_ref: Optional[DistributionChannelRef] = field(
        default=None,
        metadata={
            "name": "DistributionChannelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_moment_ref: Optional[ChargingMomentRef] = field(
        default=None,
        metadata={
            "name": "ChargingMomentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purpose_of_journey_partition_ref: Optional[PurposeOfJourneyPartitionRef] = field(
        default=None,
        metadata={
            "name": "PurposeOfJourneyPartitionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_algorithm_type_ref: Optional[TimingAlgorithmTypeRef] = field(
        default=None,
        metadata={
            "name": "TimingAlgorithmTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_classification_ref: Optional[PointOfInterestClassificationRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_activation_ref: Optional[TypeOfActivationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purpose_of_equipment_profile_ref: Optional[PurposeOfEquipmentProfileRef] = field(
        default=None,
        metadata={
            "name": "PurposeOfEquipmentProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_payment_method_ref: Optional[TypeOfPaymentMethodRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_operation_ref: Optional[TypeOfOperationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfOperationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_codespace_assignment_ref: Optional[TypeOfCodespaceAssignmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfCodespaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    branding_ref: Optional[BrandingRef] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_responsibility_role_ref: Optional[TypeOfResponsibilityRoleRef] = field(
        default=None,
        metadata={
            "name": "TypeOfResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purpose_of_grouping_ref: Optional[PurposeOfGroupingRef] = field(
        default=None,
        metadata={
            "name": "PurposeOfGroupingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_retail_device_ref: Optional[TypeOfRetailDeviceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfRetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_status_ref: Optional[CustomerAccountStatusRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_customer_account_ref: Optional[TypeOfCustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "TypeOfCustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract_entry_ref: Optional[TypeOfFareContractEntryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract_ref: Optional[TypeOfFareContractRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_access_right_assignment_ref: Optional[TypeOfAccessRightAssignmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfAccessRightAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_sales_offer_package_ref: Optional[TypeOfSalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_structure_element_ref: Optional[TypeOfFareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_tariff_ref: Optional[TypeOfTariffRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_distribution_channels_ref: Optional[AllDistributionChannelsRef] = field(
        default=None,
        metadata={
            "name": "AllDistributionChannelsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_machine_readability_ref: Optional[TypeOfMachineReadabilityRef] = field(
        default=None,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document_ref: Optional[TypeOfTravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_product_ref: Optional[TypeOfFareProductRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_structure_factor_ref: Optional[TypeOfFareStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_pricing_rule_ref: Optional[TypeOfPricingRuleRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_flexible_service_ref: Optional[TypeOfFlexibleServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFlexibleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_passenger_information_equipment_ref: Optional[TypeOfPassengerInformationEquipmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPassengerInformationEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_feature_ref: Optional[TypeOfServiceFeatureRef] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_congestion_ref: Optional[TypeOfCongestionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfCongestionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_time_demand_type_ref: Optional[TypeOfTimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_journey_pattern_ref: Optional[TypeOfJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_security_list_ref: Optional[TypeOfSecurityListRef] = field(
        default=None,
        metadata={
            "name": "TypeOfSecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_delivery_variant_ref: Optional[TypeOfDeliveryVariantRef] = field(
        default=None,
        metadata={
            "name": "TypeOfDeliveryVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_notice_ref: Optional[TypeOfNoticeRef] = field(
        default=None,
        metadata={
            "name": "TypeOfNoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_ref: Optional[TypeOfServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_facility_ref: Optional[TypeOfFacilityRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_equipment_ref: Optional[TypeOfEquipmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_projection_ref: Optional[TypeOfProjectionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_feature_ref: Optional[TypeOfFeatureRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_link_sequence_ref: Optional[TypeOfLinkSequenceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfLinkSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_organisation_part_ref: Optional[TypeOfOrganisationPartRef] = field(
        default=None,
        metadata={
            "name": "TypeOfOrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_organisation_ref: Optional[TypeOfOrganisationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_place_ref: Optional[TypeOfPlaceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_transfer_ref: Optional[TypeOfTransferRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTransferRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_zone_ref: Optional[TypeOfZoneRef] = field(
        default=None,
        metadata={
            "name": "TypeOfZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_link_ref: Optional[TypeOfLinkRef] = field(
        default=None,
        metadata={
            "name": "TypeOfLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_point_ref: Optional[TypeOfPointRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_line_ref: Optional[TypeOfLineRef] = field(
        default=None,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_validity_ref: Optional[TypeOfValidityRef] = field(
        default=None,
        metadata={
            "name": "TypeOfValidityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_frame_ref: Optional[TypeOfFrameRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_entity_ref: Optional[TypeOfEntityRef] = field(
        default=None,
        metadata={
            "name": "TypeOfEntityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_value_ref: Optional[TypeOfValueRef] = field(
        default=None,
        metadata={
            "name": "TypeOfValueRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_source_ref: Optional[DataSourceRef] = field(
        default=None,
        metadata={
            "name": "DataSourceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_ref: Optional[VersionRef] = field(
        default=None,
        metadata={
            "name": "VersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_of_object_ref: Optional[VersionOfObjectRef] = field(
        default=None,
        metadata={
            "name": "VersionOfObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
