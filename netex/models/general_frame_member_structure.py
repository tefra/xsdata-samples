from dataclasses import dataclass, field
from typing import List, Optional
from .access_ref import AccessRef
from .access_right_in_product_ref import AccessRightInProductRef
from .access_space_ref import AccessSpaceRef
from .access_zone_ref import AccessZoneRef
from .accommodation_ref import AccommodationRef
from .accountable_element_ref import AccountableElementRef
from .activation_link_ref import ActivationLinkRef
from .activation_point_ref import ActivationPointRef
from .address_ref import AddressRef
from .addressable_place_ref import AddressablePlaceRef
from .administrative_zone_ref import AdministrativeZoneRef
from .all_authorities_ref import AllAuthoritiesRef
from .all_distribution_channels_ref import AllDistributionChannelsRef
from .all_operators_ref import AllOperatorsRef
from .all_organisations_ref import AllOrganisationsRef
from .all_transport_organisations_ref import AllTransportOrganisationsRef
from .allowed_line_direction_ref import AllowedLineDirectionRef
from .alternative_name_ref import AlternativeNameRef
from .alternative_text_ref import AlternativeTextRef
from .alternative_texts_rel_structure import VersionedChildStructure
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .authority_ref import AuthorityRef
from .availability_condition_ref import AvailabilityConditionRef
from .beacon_point_ref import BeaconPointRef
from .blacklist_ref import BlacklistRef
from .block_part_ref import BlockPartRef
from .block_ref import BlockRef
from .boarding_position_ref import BoardingPositionRef
from .border_point_ref import BorderPointRef
from .branding_ref import BrandingRef
from .cancelling_ref import CancellingRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .capping_rule_price_ref import CappingRulePriceRef
from .capping_rule_ref import CappingRuleRef
from .cell_ref_1 import CellRef1
from .cell_ref_2 import CellRef2
from .charging_moment_ref import ChargingMomentRef
from .charging_policy_ref import ChargingPolicyRef
from .class_of_use_ref import ClassOfUseRef
from .commercial_profile_eligibility_ref import CommercialProfileEligibilityRef
from .commercial_profile_ref import CommercialProfileRef
from .common_section_ref import CommonSectionRef
from .companion_profile_ref import CompanionProfileRef
from .complex_feature_projection_ref import ComplexFeatureProjectionRef
from .composite_frame_ref import CompositeFrameRef
from .compound_block_ref import CompoundBlockRef
from .compound_train_ref import CompoundTrainRef
from .connection_ref import ConnectionRef
from .control_centre_ref import ControlCentreRef
from .controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from .controllable_element_price_ref import ControllableElementPriceRef
from .controllable_element_ref import ControllableElementRef
from .coupled_journey_ref import CoupledJourneyRef
from .course_of_journeys_ref import CourseOfJourneysRef
from .crew_base_ref import CrewBaseRef
from .customer_account_ref import CustomerAccountRef
from .customer_account_security_listing_ref import CustomerAccountSecurityListingRef
from .customer_account_status_ref import CustomerAccountStatusRef
from .customer_eligibility_ref import CustomerEligibilityRef
from .customer_purchase_package_element_ref import CustomerPurchasePackageElementRef
from .customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .customer_ref import CustomerRef
from .customer_security_listing_ref import CustomerSecurityListingRef
from .data_source_ref import DataSourceRef
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .day_type_ref import DayTypeRef
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .dead_run_ref import DeadRunRef
from .default_connection_ref import DefaultConnectionRef
from .default_dead_run_run_time_ref import DefaultDeadRunRunTimeRef
from .default_interchange_ref import DefaultInterchangeRef
from .default_service_journey_time_ref import DefaultServiceJourneyTimeRef
from .delivery_variant_ref import DeliveryVariantRef
from .department_ref import DepartmentRef
from .destination_display_ref import DestinationDisplayRef
from .destination_display_variant_ref import DestinationDisplayVariantRef
from .direction_ref import DirectionRef
from .discounting_rule_ref import DiscountingRuleRef
from .distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from .distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from .distance_matrix_element_ref import DistanceMatrixElementRef
from .distribution_channel_ref import DistributionChannelRef
from .driver_ref import DriverRef
from .driver_schedule_frame_ref import DriverScheduleFrameRef
from .driver_trip_ref import DriverTripRef
from .driver_trip_time_ref import DriverTripTimeRef
from .duty_part_ref import DutyPartRef
from .duty_ref import DutyRef
from .eligibility_change_policy_ref import EligibilityChangePolicyRef
from .entitlement_given_ref import EntitlementGivenRef
from .entitlement_product_ref import EntitlementProductRef
from .entitlement_required_ref import EntitlementRequiredRef
from .entrance_ref import EntranceRef
from .equipment_place_ref import EquipmentPlaceRef
from .equipment_position_ref import EquipmentPositionRef
from .estimated_passing_time_ref import EstimatedPassingTimeRef
from .exchanging_ref import ExchangingRef
from .facility_ref import FacilityRef
from .facility_requirement_ref import FacilityRequirementRef
from .facility_set_ref import FacilitySetRef
from .fare_contract_entry_ref import FareContractEntryRef
from .fare_contract_ref import FareContractRef
from .fare_contract_security_listing_ref import FareContractSecurityListingRef
from .fare_day_type_ref import FareDayTypeRef
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_element_in_sequence_ref import FareElementInSequenceRef
from .fare_frame_ref import FareFrameRef
from .fare_interval_ref import FareIntervalRef
from .fare_price_ref import FarePriceRef
from .fare_product_price_ref import FareProductPriceRef
from .fare_product_ref import FareProductRef
from .fare_quota_factor_ref import FareQuotaFactorRef
from .fare_request_ref import FareRequestRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .fare_section_ref import FareSectionRef
from .fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from .fare_structure_element_price_ref import FareStructureElementPriceRef
from .fare_structure_element_ref import FareStructureElementRef
from .fare_structure_factor_ref import FareStructureFactorRef
from .fare_table_column_ref import FareTableColumnRef
from .fare_table_ref import FareTableRef
from .fare_table_row_ref import FareTableRowRef
from .fare_unit_ref import FareUnitRef
from .fare_zone_ref import FareZoneRef
from .flexible_area_ref import FlexibleAreaRef
from .flexible_line_ref import FlexibleLineRef
from .flexible_link_properties_ref import FlexibleLinkPropertiesRef
from .flexible_point_properties_ref import FlexiblePointPropertiesRef
from .flexible_quay_ref import FlexibleQuayRef
from .flexible_service_properties_ref import FlexibleServicePropertiesRef
from .flexible_stop_place_ref import FlexibleStopPlaceRef
from .frequency_of_use_ref import FrequencyOfUseRef
from .fulfilment_method_price_ref import FulfilmentMethodPriceRef
from .fulfilment_method_ref import FulfilmentMethodRef
from .garage_point_ref import GaragePointRef
from .garage_ref import GarageRef
from .general_frame_ref import GeneralFrameRef
from .general_group_of_entities_ref import GeneralGroupOfEntitiesRef
from .general_organisation_ref import GeneralOrganisationRef
from .general_section_ref import GeneralSectionRef
from .geographical_interval_price_ref import GeographicalIntervalPriceRef
from .geographical_interval_ref import GeographicalIntervalRef
from .geographical_structure_factor_ref import GeographicalStructureFactorRef
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .geographical_unit_ref import GeographicalUnitRef
from .group_of_customer_purchase_packages_ref import GroupOfCustomerPurchasePackagesRef
from .group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from .group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from .group_of_entities_ref_1 import GroupOfEntitiesRef1
from .group_of_entities_ref_2 import GroupOfEntitiesRef2
from .group_of_lines_ref import GroupOfLinesRef
from .group_of_link_sequences_ref import GroupOfLinkSequencesRef
from .group_of_operators_ref import GroupOfOperatorsRef
from .group_of_places_ref import GroupOfPlacesRef
from .group_of_points_ref_1 import GroupOfPointsRef1
from .group_of_points_ref_2 import GroupOfPointsRef2
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .group_of_services_ref import GroupOfServicesRef
from .group_of_stop_places_ref import GroupOfStopPlacesRef
from .group_of_timebands_ref import GroupOfTimebandsRef
from .group_of_timing_links_ref import GroupOfTimingLinksRef
from .group_ticket_ref import GroupTicketRef
from .hail_and_ride_area_ref import HailAndRideAreaRef
from .headway_journey_group_ref import HeadwayJourneyGroupRef
from .headway_ref import HeadwayRef
from .infrastructure_frame_ref import InfrastructureFrameRef
from .infrastructure_link_ref import InfrastructureLinkRef
from .infrastructure_point_ref import InfrastructurePointRef
from .interchange_ref import InterchangeRef
from .interchange_rule_ref import InterchangeRuleRef
from .interchange_rule_timing_ref import InterchangeRuleTimingRef
from .interchanging_ref import InterchangingRef
from .journey_frequency_group_ref import JourneyFrequencyGroupRef
from .journey_meeting_ref import JourneyMeetingRef
from .journey_part_couple_ref import JourneyPartCoupleRef
from .journey_part_ref import JourneyPartRef
from .journey_pattern_headway_ref import JourneyPatternHeadwayRef
from .journey_pattern_layover_ref import JourneyPatternLayoverRef
from .journey_pattern_ref import JourneyPatternRef
from .journey_pattern_run_time_ref import JourneyPatternRunTimeRef
from .journey_pattern_wait_time_ref import JourneyPatternWaitTimeRef
from .journey_ref import JourneyRef
from .journey_timing_ref import JourneyTimingRef
from .layer_ref import LayerRef
from .level_ref import LevelRef
from .limiting_rule_ref import LimitingRuleRef
from .line_link_ref import LineLinkRef
from .line_network_ref import LineNetworkRef
from .line_ref import LineRef
from .line_section_ref import LineSectionRef
from .link_projection_ref import LinkProjectionRef
from .link_ref import LinkRef
from .link_sequence_projection_ref import LinkSequenceProjectionRef
from .link_sequence_ref import LinkSequenceRef
from .log_entry_ref import LogEntryRef
from .log_ref import LogRef
from .logical_display_ref import LogicalDisplayRef
from .luggage_allowance_ref import LuggageAllowanceRef
from .management_agent_ref import ManagementAgentRef
from .minimum_stay_ref import MinimumStayRef
from .mode_ref import ModeRef
from .month_validity_offset_ref import MonthValidityOffsetRef
from .multilingual_string import MultilingualString
from .navigation_path_ref import NavigationPathRef
from .network_ref import NetworkRef
from .notice_ref import NoticeRef
from .observed_passing_time_ref import ObservedPassingTimeRef
from .offered_travel_specification_ref import OfferedTravelSpecificationRef
from .onboard_stay_ref import OnboardStayRef
from .open_transport_mode_ref import OpenTransportModeRef
from .operating_day_ref import OperatingDayRef
from .operating_department_ref import OperatingDepartmentRef
from .operating_period_ref import OperatingPeriodRef
from .operational_context_ref import OperationalContextRef
from .operator_ref import OperatorRef
from .organisation_part_ref import OrganisationPartRef
from .organisation_ref import OrganisationRef
from .organisational_unit_ref import OrganisationalUnitRef
from .other_organisation_ref import OtherOrganisationRef
from .parent_common_section_ref import ParentCommonSectionRef
from .parent_section_ref import ParentSectionRef
from .parking_area_ref import ParkingAreaRef
from .parking_bay_ref import ParkingBayRef
from .parking_capacity_ref import ParkingCapacityRef
from .parking_charge_band_ref import ParkingChargeBandRef
from .parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from .parking_entrance_ref import ParkingEntranceRef
from .parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from .parking_point_ref import ParkingPointRef
from .parking_price_ref import ParkingPriceRef
from .parking_properties_ref import ParkingPropertiesRef
from .parking_ref import ParkingRef
from .parking_tariff_ref import ParkingTariffRef
from .passenger_capacity_ref import PassengerCapacityRef
from .passenger_carrying_requirement_ref import PassengerCarryingRequirementRef
from .passenger_information_request_ref import PassengerInformationRequestRef
from .passenger_seat_ref import PassengerSeatRef
from .passing_time_ref import PassingTimeRef
from .path_junction_ref import PathJunctionRef
from .path_link_ref import PathLinkRef
from .penalty_policy_ref import PenaltyPolicyRef
from .place_ref_1 import PlaceRef1
from .place_ref_2 import PlaceRef2
from .point_of_interest_classification_ref import PointOfInterestClassificationRef
from .point_of_interest_entrance_ref import PointOfInterestEntranceRef
from .point_of_interest_hierarchy_ref import PointOfInterestHierarchyRef
from .point_of_interest_ref import PointOfInterestRef
from .point_of_interest_space_ref import PointOfInterestSpaceRef
from .point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from .point_on_link_ref import PointOnLinkRef
from .point_projection_ref import PointProjectionRef
from .point_ref import PointRef
from .postal_address_ref import PostalAddressRef
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .price_group_ref import PriceGroupRef
from .price_unit_ref import PriceUnitRef
from .priceable_object_ref import PriceableObjectRef
from .pricing_parameter_set_ref import PricingParameterSetRef
from .pricing_rule_ref import PricingRuleRef
from .pricing_service_ref import PricingServiceRef
from .profile_parameter_ref import ProfileParameterRef
from .projection_ref import ProjectionRef
from .purchase_window_ref import PurchaseWindowRef
from .purpose_of_equipment_profile_ref import PurposeOfEquipmentProfileRef
from .purpose_of_grouping_ref import PurposeOfGroupingRef
from .purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from .quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from .quality_structure_factor_ref import QualityStructureFactorRef
from .quay_ref import QuayRef
from .railway_link_ref import RailwayLinkRef
from .railway_point_ref import RailwayPointRef
from .refunding_ref import RefundingRef
from .relief_opportunity_ref import ReliefOpportunityRef
from .relief_point_ref import ReliefPointRef
from .repeated_trip_fare_request_ref import RepeatedTripFareRequestRef
from .replacing_ref import ReplacingRef
from .requested_travel_specification_ref import RequestedTravelSpecificationRef
from .reselling_ref import ResellingRef
from .reserving_ref import ReservingRef
from .residential_qualification_eligibility_ref import ResidentialQualificationEligibilityRef
from .residential_qualification_ref import ResidentialQualificationRef
from .resource_frame_ref import ResourceFrameRef
from .responsibility_role_ref import ResponsibilityRoleRef
from .responsibility_set_ref import ResponsibilitySetRef
from .retail_consortium_ref import RetailConsortiumRef
from .retail_device_security_listing_ref import RetailDeviceSecurityListingRef
from .rhythmical_journey_group_ref import RhythmicalJourneyGroupRef
from .road_address_ref import RoadAddressRef
from .road_link_ref import RoadLinkRef
from .road_point_ref import RoadPointRef
from .round_trip_ref import RoundTripRef
from .rounding_ref import RoundingRef
from .rounding_step_ref import RoundingStepRef
from .route_instruction_ref import RouteInstructionRef
from .route_link_ref import RouteLinkRef
from .route_point_ref import RoutePointRef
from .route_ref import RouteRef
from .routing_constraint_zone_ref import RoutingConstraintZoneRef
from .routing_ref import RoutingRef
from .sale_discount_right_ref import SaleDiscountRightRef
from .sales_offer_package_element_ref import SalesOfferPackageElementRef
from .sales_offer_package_entitlement_given_ref import SalesOfferPackageEntitlementGivenRef
from .sales_offer_package_entitlement_required_ref import SalesOfferPackageEntitlementRequiredRef
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .sales_offer_package_ref import SalesOfferPackageRef
from .sales_transaction_frame_ref import SalesTransactionFrameRef
from .sales_transaction_ref import SalesTransactionRef
from .schedule_request_ref import ScheduleRequestRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .schematic_map_member_ref import SchematicMapMemberRef
from .schematic_map_ref import SchematicMapRef
from .section_ref import SectionRef
from .security_list_ref import SecurityListRef
from .security_listing_ref import SecurityListingRef
from .series_constraint_price_ref import SeriesConstraintPriceRef
from .series_constraint_ref import SeriesConstraintRef
from .service_access_right_ref import ServiceAccessRightRef
from .service_calendar_frame_ref import ServiceCalendarFrameRef
from .service_calendar_ref import ServiceCalendarRef
from .service_facility_set_ref import ServiceFacilitySetRef
from .service_frame_ref import ServiceFrameRef
from .service_journey_interchange_ref import ServiceJourneyInterchangeRef
from .service_journey_pattern_interchange_ref import ServiceJourneyPatternInterchangeRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_journey_ref import ServiceJourneyRef
from .service_link_ref import ServiceLinkRef
from .service_pattern_ref import ServicePatternRef
from .service_site_ref import ServiceSiteRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .single_trip_fare_request_ref import SingleTripFareRequestRef
from .site_component_ref import SiteComponentRef
from .site_connection_ref import SiteConnectionRef
from .site_element_ref import SiteElementRef
from .site_facility_set_ref import SiteFacilitySetRef
from .site_frame_ref import SiteFrameRef
from .site_ref import SiteRef
from .special_service_ref import SpecialServiceRef
from .standard_fare_table_ref import StandardFareTableRef
from .start_time_at_stop_point_ref import StartTimeAtStopPointRef
from .step_limit_ref import StepLimitRef
from .stop_area_ref import StopAreaRef
from .stop_event_request_ref import StopEventRequestRef
from .stop_finder_request_ref import StopFinderRequestRef
from .stop_place_entrance_ref import StopPlaceEntranceRef
from .stop_place_ref import StopPlaceRef
from .stop_place_space_ref import StopPlaceSpaceRef
from .stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from .submode_ref import SubmodeRef
from .subscribing_ref import SubscribingRef
from .supplement_product_ref import SupplementProductRef
from .supply_contract_ref import SupplyContractRef
from .suspending_ref import SuspendingRef
from .target_passing_time_ref import TargetPassingTimeRef
from .tariff_object_ref import TariffObjectRef
from .tariff_ref import TariffRef
from .tariff_zone_ref_1 import TariffZoneRef1
from .tariff_zone_ref_2 import TariffZoneRef2
from .template_service_journey_ref import TemplateServiceJourneyRef
from .third_party_product_ref import ThirdPartyProductRef
from .time_demand_profile_ref import TimeDemandProfileRef
from .time_demand_type_ref import TimeDemandTypeRef
from .time_interval_price_ref import TimeIntervalPriceRef
from .time_interval_ref import TimeIntervalRef
from .time_structure_factor_ref import TimeStructureFactorRef
from .time_unit_price_ref import TimeUnitPriceRef
from .time_unit_ref import TimeUnitRef
from .timeband_ref import TimebandRef
from .timetable_frame_ref import TimetableFrameRef
from .timetabled_passing_time_ref import TimetabledPassingTimeRef
from .timing_algorithm_type_ref import TimingAlgorithmTypeRef
from .timing_link_ref import TimingLinkRef
from .timing_pattern_ref import TimingPatternRef
from .timing_point_ref import TimingPointRef
from .topographic_place_ref import TopographicPlaceRef
from .topographic_projection_ref import TopographicProjectionRef
from .traffic_control_point_ref import TrafficControlPointRef
from .train_block_part_ref import TrainBlockPartRef
from .train_block_ref import TrainBlockRef
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_in_compound_train_ref import TrainInCompoundTrainRef
from .train_number_ref import TrainNumberRef
from .train_ref import TrainRef
from .transfer_ref import TransferRef
from .transferability_ref import TransferabilityRef
from .transport_administrative_zone_ref import TransportAdministrativeZoneRef
from .transport_organisation_ref import TransportOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .travel_document_ref import TravelDocumentRef
from .travel_document_security_listing_ref import TravelDocumentSecurityListingRef
from .travel_specification_ref import TravelSpecificationRef
from .trip_plan_request_ref import TripPlanRequestRef
from .turnaround_time_limit_time_ref import TurnaroundTimeLimitTimeRef
from .type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from .type_of_activation_ref import TypeOfActivationRef
from .type_of_codespace_assignment_ref import TypeOfCodespaceAssignmentRef
from .type_of_concession_ref import TypeOfConcessionRef
from .type_of_congestion_ref import TypeOfCongestionRef
from .type_of_customer_account_ref import TypeOfCustomerAccountRef
from .type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from .type_of_entity_ref import TypeOfEntityRef
from .type_of_equipment_ref import TypeOfEquipmentRef
from .type_of_facility_ref import TypeOfFacilityRef
from .type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef
from .type_of_fare_contract_ref import TypeOfFareContractRef
from .type_of_fare_product_ref import TypeOfFareProductRef
from .type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from .type_of_fare_structure_factor_ref import TypeOfFareStructureFactorRef
from .type_of_fare_table_ref import TypeOfFareTableRef
from .type_of_feature_ref import TypeOfFeatureRef
from .type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from .type_of_frame_ref import TypeOfFrameRef
from .type_of_journey_pattern_ref import TypeOfJourneyPatternRef
from .type_of_line_ref import TypeOfLineRef
from .type_of_link_ref import TypeOfLinkRef
from .type_of_link_sequence_ref import TypeOfLinkSequenceRef
from .type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from .type_of_notice_ref import TypeOfNoticeRef
from .type_of_operation_ref import TypeOfOperationRef
from .type_of_organisation_part_ref import TypeOfOrganisationPartRef
from .type_of_organisation_ref import TypeOfOrganisationRef
from .type_of_passenger_information_equipment_ref import TypeOfPassengerInformationEquipmentRef
from .type_of_payment_method_ref import TypeOfPaymentMethodRef
from .type_of_place_ref import TypeOfPlaceRef
from .type_of_point_ref import TypeOfPointRef
from .type_of_pricing_rule_ref import TypeOfPricingRuleRef
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .type_of_projection_ref import TypeOfProjectionRef
from .type_of_responsibility_role_ref import TypeOfResponsibilityRoleRef
from .type_of_retail_device_ref import TypeOfRetailDeviceRef
from .type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef
from .type_of_security_list_ref import TypeOfSecurityListRef
from .type_of_service_feature_ref import TypeOfServiceFeatureRef
from .type_of_service_ref import TypeOfServiceRef
from .type_of_tariff_ref import TypeOfTariffRef
from .type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from .type_of_transfer_ref import TypeOfTransferRef
from .type_of_travel_document_ref import TypeOfTravelDocumentRef
from .type_of_usage_parameter_ref import TypeOfUsageParameterRef
from .type_of_validity_ref import TypeOfValidityRef
from .type_of_value_ref import TypeOfValueRef
from .type_of_zone_ref import TypeOfZoneRef
from .usage_discount_right_ref import UsageDiscountRightRef
from .usage_parameter_price_ref import UsageParameterPriceRef
from .usage_parameter_ref import UsageParameterRef
from .usage_validity_period_ref import UsageValidityPeriodRef
from .user_profile_eligibility_ref import UserProfileEligibilityRef
from .user_profile_ref import UserProfileRef
from .validable_element_price_ref import ValidableElementPriceRef
from .validable_element_ref import ValidableElementRef
from .validity_condition_ref import ValidityConditionRef
from .validity_rule_parameter_ref import ValidityRuleParameterRef
from .validity_trigger_ref import ValidityTriggerRef
from .vehicle_entrance_ref import VehicleEntranceRef
from .vehicle_equipment_profile_ref import VehicleEquipmentProfileRef
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_manoeuvring_requirement_ref import VehicleManoeuvringRequirementRef
from .vehicle_model_ref import VehicleModelRef
from .vehicle_position_alignment_ref import VehiclePositionAlignmentRef
from .vehicle_quay_alignment_ref import VehicleQuayAlignmentRef
from .vehicle_ref import VehicleRef
from .vehicle_requirement_ref import VehicleRequirementRef
from .vehicle_schedule_frame_ref import VehicleScheduleFrameRef
from .vehicle_service_part_ref import VehicleServicePartRef
from .vehicle_service_ref import VehicleServiceRef
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef
from .vehicle_type_preference_ref import VehicleTypePreferenceRef
from .vehicle_type_ref import VehicleTypeRef
from .version_frame_ref import VersionFrameRef
from .version_of_object_ref import VersionOfObjectRef
from .version_ref import VersionRef
from .whitelist_ref import WhitelistRef
from .wire_link_ref import WireLinkRef
from .wire_point_ref import WirePointRef
from .zone_projection_ref import ZoneProjectionRef
from .zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralFrameMemberStructure(VersionedChildStructure):
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_document_ref: List[TravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    repeated_trip_fare_request_ref: List[RepeatedTripFareRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "RepeatedTripFareRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    single_trip_fare_request_ref: List[SingleTripFareRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "SingleTripFareRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    fare_request_ref: List[FareRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "FareRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    stop_finder_request_ref: List[StopFinderRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "StopFinderRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    stop_event_request_ref: List[StopEventRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "StopEventRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    schedule_request_ref: List[ScheduleRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "ScheduleRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    trip_plan_request_ref: List[TripPlanRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "TripPlanRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    passenger_information_request_ref: List[PassengerInformationRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    residential_qualification_eligibility_ref: List[ResidentialQualificationEligibilityRef] = field(
        default_factory=list,
        metadata={
            "name": "ResidentialQualificationEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    commercial_profile_eligibility_ref: List[CommercialProfileEligibilityRef] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfileEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    user_profile_eligibility_ref: List[UserProfileEligibilityRef] = field(
        default_factory=list,
        metadata={
            "name": "UserProfileEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    customer_eligibility_ref: List[CustomerEligibilityRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customer_account_ref: List[CustomerAccountRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    fare_contract_ref: List[FareContractRef] = field(
        default_factory=list,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customer_ref: List[CustomerRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    start_time_at_stop_point_ref: List[StartTimeAtStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "StartTimeAtStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    residential_qualification_ref: List[ResidentialQualificationRef] = field(
        default_factory=list,
        metadata={
            "name": "ResidentialQualificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_concession_ref: List[TypeOfConcessionRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_usage_parameter_ref: List[TypeOfUsageParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfUsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    tariff_object_ref: List[TariffObjectRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    parking_tariff_ref: List[ParkingTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    tariff_ref: List[TariffRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_fare_table_ref: List[TypeOfFareTableRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    fare_table_row_ref: List[FareTableRowRef] = field(
        default_factory=list,
        metadata={
            "name": "FareTableRowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    fare_table_column_ref: List[FareTableColumnRef] = field(
        default_factory=list,
        metadata={
            "name": "FareTableColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    time_unit_ref: List[TimeUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    geographical_unit_ref: List[GeographicalUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_unit_ref: List[FareUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "FareUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    controllable_element_in_sequence_ref: List[ControllableElementInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_structure_element_in_sequence_ref: List[FareStructureElementInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    access_right_in_product_ref: List[AccessRightInProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightInProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_element_in_sequence_ref: List[FareElementInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    cell_ref: List[CellRef1] = field(
        default_factory=list,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    netex_org_uk_netex_cell_ref: List[CellRef2] = field(
        default_factory=list,
        metadata={
            "name": "CellRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customer_purchase_package_price_ref: List[CustomerPurchasePackagePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    parking_price_ref: List[ParkingPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    time_interval_price_ref: List[TimeIntervalPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    time_unit_price_ref: List[TimeUnitPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    quality_structure_factor_price_ref: List[QualityStructureFactorPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactorPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    controllable_element_price_ref: List[ControllableElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    validable_element_price_ref: List[ValidableElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    geographical_interval_price_ref: List[GeographicalIntervalPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    geographical_unit_price_ref: List[GeographicalUnitPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    usage_parameter_price_ref: List[UsageParameterPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    sales_offer_package_price_ref: List[SalesOfferPackagePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    distance_matrix_element_price_ref: List[DistanceMatrixElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_structure_element_price_ref: List[FareStructureElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fulfilment_method_price_ref: List[FulfilmentMethodPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    series_constraint_price_ref: List[SeriesConstraintPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    capping_rule_price_ref: List[CappingRulePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "CappingRulePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_product_price_ref: List[FareProductPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareProductPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_price_ref: List[FarePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FarePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customer_purchase_package_element_ref: List[CustomerPurchasePackageElementRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    customer_purchase_package_ref: List[CustomerPurchasePackageRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    controllable_element_ref: List[ControllableElementRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    validable_element_ref: List[ValidableElementRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    sales_offer_package_entitlement_given_ref: List[SalesOfferPackageEntitlementGivenRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    sales_offer_package_entitlement_required_ref: List[SalesOfferPackageEntitlementRequiredRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    minimum_stay_ref: List[MinimumStayRef] = field(
        default_factory=list,
        metadata={
            "name": "MinimumStayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    interchanging_ref: List[InterchangingRef] = field(
        default_factory=list,
        metadata={
            "name": "InterchangingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    frequency_of_use_ref: List[FrequencyOfUseRef] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    suspending_ref: List[SuspendingRef] = field(
        default_factory=list,
        metadata={
            "name": "SuspendingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    usage_validity_period_ref: List[UsageValidityPeriodRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageValidityPeriodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    step_limit_ref: List[StepLimitRef] = field(
        default_factory=list,
        metadata={
            "name": "StepLimitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    routing_ref: List[RoutingRef] = field(
        default_factory=list,
        metadata={
            "name": "RoutingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    round_trip_ref: List[RoundTripRef] = field(
        default_factory=list,
        metadata={
            "name": "RoundTripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    luggage_allowance_ref: List[LuggageAllowanceRef] = field(
        default_factory=list,
        metadata={
            "name": "LuggageAllowanceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    entitlement_given_ref: List[EntitlementGivenRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    entitlement_required_ref: List[EntitlementRequiredRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    eligibility_change_policy_ref: List[EligibilityChangePolicyRef] = field(
        default_factory=list,
        metadata={
            "name": "EligibilityChangePolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    group_ticket_ref: List[GroupTicketRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupTicketRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    commercial_profile_ref: List[CommercialProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    companion_profile_ref: List[CompanionProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    user_profile_ref: List[UserProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "UserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    profile_parameter_ref: List[ProfileParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "ProfileParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    subscribing_ref: List[SubscribingRef] = field(
        default_factory=list,
        metadata={
            "name": "SubscribingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    penalty_policy_ref: List[PenaltyPolicyRef] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyPolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    charging_policy_ref: List[ChargingPolicyRef] = field(
        default_factory=list,
        metadata={
            "name": "ChargingPolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    transferability_ref: List[TransferabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TransferabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    replacing_ref: List[ReplacingRef] = field(
        default_factory=list,
        metadata={
            "name": "ReplacingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    refunding_ref: List[RefundingRef] = field(
        default_factory=list,
        metadata={
            "name": "RefundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    exchanging_ref: List[ExchangingRef] = field(
        default_factory=list,
        metadata={
            "name": "ExchangingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    reselling_ref: List[ResellingRef] = field(
        default_factory=list,
        metadata={
            "name": "ResellingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    cancelling_ref: List[CancellingRef] = field(
        default_factory=list,
        metadata={
            "name": "CancellingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    reserving_ref: List[ReservingRef] = field(
        default_factory=list,
        metadata={
            "name": "ReservingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    purchase_window_ref: List[PurchaseWindowRef] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseWindowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    usage_parameter_ref: List[UsageParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    sales_offer_package_element_ref: List[SalesOfferPackageElementRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    sales_offer_package_ref: List[SalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    distance_matrix_element_inverse_ref: List[DistanceMatrixElementInverseRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementInverseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    distance_matrix_element_ref: List[DistanceMatrixElementRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_structure_element_ref: List[FareStructureElementRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fulfilment_method_ref: List[FulfilmentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    series_constraint_ref: List[SeriesConstraintRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    capping_rule_ref: List[CappingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "CappingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    entitlement_product_ref: List[EntitlementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    supplement_product_ref: List[SupplementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    preassigned_fare_product_ref: List[PreassignedFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    amount_of_price_unit_product_ref: List[AmountOfPriceUnitProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    usage_discount_right_ref: List[UsageDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    third_party_product_ref: List[ThirdPartyProductRef] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    capped_discount_right_ref: List[CappedDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    sale_discount_right_ref: List[SaleDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    fare_product_ref: List[FareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    service_access_right_ref: List[ServiceAccessRightRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAccessRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    time_interval_ref: List[TimeIntervalRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    geographical_interval_ref: List[GeographicalIntervalRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    fare_interval_ref: List[FareIntervalRef] = field(
        default_factory=list,
        metadata={
            "name": "FareIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    parking_charge_band_ref: List[ParkingChargeBandRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingChargeBandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    time_structure_factor_ref: List[TimeStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    fare_quota_factor_ref: List[FareQuotaFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    fare_demand_factor_ref: List[FareDemandFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    quality_structure_factor_ref: List[QualityStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    geographical_structure_factor_ref: List[GeographicalStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    fare_structure_factor_ref: List[FareStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    priceable_object_ref: List[PriceableObjectRef] = field(
        default_factory=list,
        metadata={
            "name": "PriceableObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    month_validity_offset_ref: List[MonthValidityOffsetRef] = field(
        default_factory=list,
        metadata={
            "name": "MonthValidityOffsetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    limiting_rule_ref: List[LimitingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    discounting_rule_ref: List[DiscountingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "DiscountingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    pricing_rule_ref: List[PricingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "PricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    pricing_service_ref: List[PricingServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "PricingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    rounding_step_ref: List[RoundingStepRef] = field(
        default_factory=list,
        metadata={
            "name": "RoundingStepRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    rounding_ref: List[RoundingRef] = field(
        default_factory=list,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    pricing_parameter_set_ref: List[PricingParameterSetRef] = field(
        default_factory=list,
        metadata={
            "name": "PricingParameterSetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    supply_contract_ref: List[SupplyContractRef] = field(
        default_factory=list,
        metadata={
            "name": "SupplyContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    flexible_service_properties_ref: List[FlexibleServicePropertiesRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleServicePropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    driver_trip_time_ref: List[DriverTripTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "DriverTripTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    driver_trip_ref: List[DriverTripRef] = field(
        default_factory=list,
        metadata={
            "name": "DriverTripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    duty_part_ref: List[DutyPartRef] = field(
        default_factory=list,
        metadata={
            "name": "DutyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    accountable_element_ref: List[AccountableElementRef] = field(
        default_factory=list,
        metadata={
            "name": "AccountableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    duty_ref: List[DutyRef] = field(
        default_factory=list,
        metadata={
            "name": "DutyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    relief_opportunity_ref: List[ReliefOpportunityRef] = field(
        default_factory=list,
        metadata={
            "name": "ReliefOpportunityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    course_of_journeys_ref: List[CourseOfJourneysRef] = field(
        default_factory=list,
        metadata={
            "name": "CourseOfJourneysRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    driver_ref: List[DriverRef] = field(
        default_factory=list,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_service_part_ref: List[VehicleServicePartRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleServicePartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_service_ref: List[VehicleServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    compound_block_ref: List[CompoundBlockRef] = field(
        default_factory=list,
        metadata={
            "name": "CompoundBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    train_block_part_ref: List[TrainBlockPartRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    block_part_ref: List[BlockPartRef] = field(
        default_factory=list,
        metadata={
            "name": "BlockPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    train_block_ref: List[TrainBlockRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    block_ref: List[BlockRef] = field(
        default_factory=list,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    journey_part_couple_ref: List[JourneyPartCoupleRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartCoupleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    coupled_journey_ref: List[CoupledJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    journey_part_ref: List[JourneyPartRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    timetabled_passing_time_ref: List[TimetabledPassingTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledPassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    estimated_passing_time_ref: List[EstimatedPassingTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedPassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    observed_passing_time_ref: List[ObservedPassingTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "ObservedPassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    target_passing_time_ref: List[TargetPassingTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "TargetPassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    passing_time_ref: List[PassingTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "PassingTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    interchange_rule_timing_ref: List[InterchangeRuleTimingRef] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRuleTimingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    interchange_rule_ref: List[InterchangeRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_journey_pattern_interchange_ref: List[ServiceJourneyPatternInterchangeRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_journey_interchange_ref: List[ServiceJourneyInterchangeRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    default_interchange_ref: List[DefaultInterchangeRef] = field(
        default_factory=list,
        metadata={
            "name": "DefaultInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    interchange_ref: List[InterchangeRef] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    journey_meeting_ref: List[JourneyMeetingRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyMeetingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    train_number_ref: List[TrainNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    routing_constraint_zone_ref: List[RoutingConstraintZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "RoutingConstraintZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_position_alignment_ref: List[VehiclePositionAlignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePositionAlignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_quay_alignment_ref: List[VehicleQuayAlignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleQuayAlignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    logical_display_ref: List[LogicalDisplayRef] = field(
        default_factory=list,
        metadata={
            "name": "LogicalDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    parking_area_ref: List[ParkingAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    parking_properties_ref: List[ParkingPropertiesRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    parking_capacity_ref: List[ParkingCapacityRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingCapacityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    line_network_ref: List[LineNetworkRef] = field(
        default_factory=list,
        metadata={
            "name": "LineNetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    route_instruction_ref: List[RouteInstructionRef] = field(
        default_factory=list,
        metadata={
            "name": "RouteInstructionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    level_ref: List[LevelRef] = field(
        default_factory=list,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    flexible_point_properties_ref: List[FlexiblePointPropertiesRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexiblePointPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    flexible_link_properties_ref: List[FlexibleLinkPropertiesRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLinkPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    time_demand_profile_ref: List[TimeDemandProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    time_demand_type_ref: List[TimeDemandTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_type_preference_ref: List[VehicleTypePreferenceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypePreferenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    journey_pattern_headway_ref: List[JourneyPatternHeadwayRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternHeadwayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    journey_pattern_layover_ref: List[JourneyPatternLayoverRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternLayoverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    journey_pattern_run_time_ref: List[JourneyPatternRunTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternRunTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    journey_pattern_wait_time_ref: List[JourneyPatternWaitTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternWaitTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    default_service_journey_time_ref: List[DefaultServiceJourneyTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "DefaultServiceJourneyTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    default_dead_run_run_time_ref: List[DefaultDeadRunRunTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "DefaultDeadRunRunTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    turnaround_time_limit_time_ref: List[TurnaroundTimeLimitTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "TurnaroundTimeLimitTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    headway_ref: List[HeadwayRef] = field(
        default_factory=list,
        metadata={
            "name": "HeadwayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    journey_timing_ref: List[JourneyTimingRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyTimingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    crew_base_ref: List[CrewBaseRef] = field(
        default_factory=list,
        metadata={
            "name": "CrewBaseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    passenger_seat_ref: List[PassengerSeatRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSeatRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    operating_department_ref: List[OperatingDepartmentRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    operational_context_ref: List[OperationalContextRef] = field(
        default_factory=list,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    train_component_ref: List[TrainComponentRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    train_element_ref: List[TrainElementRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    train_in_compound_train_ref: List[TrainInCompoundTrainRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainInCompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    travel_document_security_listing_ref: List[TravelDocumentSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocumentSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    retail_device_security_listing_ref: List[RetailDeviceSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    customer_account_security_listing_ref: List[CustomerAccountSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_contract_security_listing_ref: List[FareContractSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "FareContractSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    customer_security_listing_ref: List[CustomerSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    security_listing_ref: List[SecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    whitelist_ref: List[WhitelistRef] = field(
        default_factory=list,
        metadata={
            "name": "WhitelistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    blacklist_ref: List[BlacklistRef] = field(
        default_factory=list,
        metadata={
            "name": "BlacklistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    security_list_ref: List[SecurityListRef] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    schematic_map_member_ref: List[SchematicMapMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "SchematicMapMemberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    schematic_map_ref: List[SchematicMapRef] = field(
        default_factory=list,
        metadata={
            "name": "SchematicMapRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    delivery_variant_ref: List[DeliveryVariantRef] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    notice_ref: List[NoticeRef] = field(
        default_factory=list,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_equipment_profile_ref: List[VehicleEquipmentProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEquipmentProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_model_ref: List[VehicleModelRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_ref: List[VehicleRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    passenger_capacity_ref: List[PassengerCapacityRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCapacityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    facility_requirement_ref: List[FacilityRequirementRef] = field(
        default_factory=list,
        metadata={
            "name": "FacilityRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_manoeuvring_requirement_ref: List[VehicleManoeuvringRequirementRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleManoeuvringRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    passenger_carrying_requirement_ref: List[PassengerCarryingRequirementRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCarryingRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_requirement_ref: List[VehicleRequirementRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    compound_train_ref: List[CompoundTrainRef] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    train_ref: List[TrainRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_type_ref: List[VehicleTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    onboard_stay_ref: List[OnboardStayRef] = field(
        default_factory=list,
        metadata={
            "name": "OnboardStayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    accommodation_ref: List[AccommodationRef] = field(
        default_factory=list,
        metadata={
            "name": "AccommodationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    service_facility_set_ref: List[ServiceFacilitySetRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    site_facility_set_ref: List[SiteFacilitySetRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    facility_set_ref: List[FacilitySetRef] = field(
        default_factory=list,
        metadata={
            "name": "FacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    facility_ref: List[FacilityRef] = field(
        default_factory=list,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    mode_ref: List[ModeRef] = field(
        default_factory=list,
        metadata={
            "name": "ModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    submode_ref: List[SubmodeRef] = field(
        default_factory=list,
        metadata={
            "name": "SubmodeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    open_transport_mode_ref: List[OpenTransportModeRef] = field(
        default_factory=list,
        metadata={
            "name": "OpenTransportModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    topographic_projection_ref: List[TopographicProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "TopographicProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    complex_feature_projection_ref: List[ComplexFeatureProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeatureProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    link_sequence_projection_ref: List[LinkSequenceProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LinkSequenceProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    zone_projection_ref: List[ZoneProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ZoneProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    link_projection_ref: List[LinkProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LinkProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    point_projection_ref: List[PointProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "PointProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    projection_ref: List[ProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    group_of_link_sequences_ref: List[GroupOfLinkSequencesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinkSequencesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    dated_vehicle_journey_ref: List[DatedVehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    dated_special_service_ref: List[DatedSpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    special_service_ref: List[SpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    template_service_journey_ref: List[TemplateServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    service_journey_ref: List[ServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    vehicle_journey_ref: List[VehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    journey_ref: List[JourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    navigation_path_ref: List[NavigationPathRef] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_journey_pattern_ref: List[ServiceJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    service_pattern_ref: List[ServicePatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    dead_run_journey_pattern_ref: List[DeadRunJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    journey_pattern_ref: List[JourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    timing_pattern_ref: List[TimingPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    route_ref: List[RouteRef] = field(
        default_factory=list,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    link_sequence_ref: List[LinkSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "LinkSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    sales_transaction_ref: List[SalesTransactionRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    offered_travel_specification_ref: List[OfferedTravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "OfferedTravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    requested_travel_specification_ref: List[RequestedTravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "RequestedTravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    travel_specification_ref: List[TravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    fare_contract_entry_ref: List[FareContractEntryRef] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    log_entry_ref: List[LogEntryRef] = field(
        default_factory=list,
        metadata={
            "name": "LogEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    alternative_name_ref: List[AlternativeNameRef] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeNameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    timeband_ref: List[TimebandRef] = field(
        default_factory=list,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    fare_day_type_ref: List[FareDayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    day_type_ref: List[DayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    default_connection_ref: List[DefaultConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "DefaultConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    site_connection_ref: List[SiteConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    connection_ref: List[ConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    access_ref: List[AccessRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    transfer_ref: List[TransferRef] = field(
        default_factory=list,
        metadata={
            "name": "TransferRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    hail_and_ride_area_ref: List[HailAndRideAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    flexible_area_ref: List[FlexibleAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    flexible_quay_ref: List[FlexibleQuayRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleQuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    flexible_stop_place_ref: List[FlexibleStopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    path_junction_ref: List[PathJunctionRef] = field(
        default_factory=list,
        metadata={
            "name": "PathJunctionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    topographic_place_ref: List[TopographicPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    equipment_place_ref: List[EquipmentPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    equipment_position_ref: List[EquipmentPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_stopping_position_ref: List[VehicleStoppingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    vehicle_stopping_place_ref: List[VehicleStoppingPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    boarding_position_ref: List[BoardingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    access_space_ref: List[AccessSpaceRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    quay_ref: List[QuayRef] = field(
        default_factory=list,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    stop_place_space_ref: List[StopPlaceSpaceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    parking_bay_ref: List[ParkingBayRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    point_of_interest_space_ref: List[PointOfInterestSpaceRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    stop_place_vehicle_entrance_ref: List[StopPlaceVehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    stop_place_entrance_ref: List[StopPlaceEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    parking_entrance_for_vehicles_ref: List[ParkingEntranceForVehiclesRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 8,
            "sequential": True,
        }
    )
    parking_passenger_entrance_ref: List[ParkingPassengerEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPassengerEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 8,
            "sequential": True,
        }
    )
    parking_entrance_ref: List[ParkingEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    point_of_interest_vehicle_entrance_ref: List[PointOfInterestVehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestVehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    point_of_interest_entrance_ref: List[PointOfInterestEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    vehicle_entrance_ref: List[VehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    entrance_ref: List[EntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "EntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    site_component_ref: List[SiteComponentRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    stop_place_ref: List[StopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    parking_ref: List[ParkingRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    point_of_interest_ref: List[PointOfInterestRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    service_site_ref: List[ServiceSiteRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    site_ref: List[SiteRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    site_element_ref: List[SiteElementRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    garage_ref: List[GarageRef] = field(
        default_factory=list,
        metadata={
            "name": "GarageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    addressable_place_ref: List[AddressablePlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "AddressablePlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    postal_address_ref: List[PostalAddressRef] = field(
        default_factory=list,
        metadata={
            "name": "PostalAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    road_address_ref: List[RoadAddressRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    address_ref: List[AddressRef] = field(
        default_factory=list,
        metadata={
            "name": "AddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    place_ref: List[PlaceRef2] = field(
        default_factory=list,
        metadata={
            "name": "PlaceRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    service_link_ref: List[ServiceLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    line_link_ref: List[LineLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "LineLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    path_link_ref: List[PathLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    timing_link_ref: List[TimingLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    route_link_ref: List[RouteLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    wire_link_ref: List[WireLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "WireLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    road_link_ref: List[RoadLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    railway_link_ref: List[RailwayLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RailwayLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    infrastructure_link_ref: List[InfrastructureLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    activation_link_ref: List[ActivationLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "ActivationLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    link_ref: List[LinkRef] = field(
        default_factory=list,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    border_point_ref: List[BorderPointRef] = field(
        default_factory=list,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    scheduled_stop_point_ref: List[ScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    garage_point_ref: List[GaragePointRef] = field(
        default_factory=list,
        metadata={
            "name": "GaragePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 7,
            "sequential": True,
        }
    )
    parking_point_ref: List[ParkingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    relief_point_ref: List[ReliefPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    timing_point_ref: List[TimingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    route_point_ref: List[RoutePointRef] = field(
        default_factory=list,
        metadata={
            "name": "RoutePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    wire_point_ref: List[WirePointRef] = field(
        default_factory=list,
        metadata={
            "name": "WirePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    road_point_ref: List[RoadPointRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    railway_point_ref: List[RailwayPointRef] = field(
        default_factory=list,
        metadata={
            "name": "RailwayPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    infrastructure_point_ref: List[InfrastructurePointRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructurePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    traffic_control_point_ref: List[TrafficControlPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TrafficControlPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    beacon_point_ref: List[BeaconPointRef] = field(
        default_factory=list,
        metadata={
            "name": "BeaconPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    activation_point_ref: List[ActivationPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    point_on_link_ref: List[PointOnLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    point_ref: List[PointRef] = field(
        default_factory=list,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    operating_period_ref: List[OperatingPeriodRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatingPeriodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    operating_day_ref: List[OperatingDayRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    service_calendar_ref: List[ServiceCalendarRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    alternative_text_ref: List[AlternativeTextRef] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeTextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    availability_condition_ref: List[AvailabilityConditionRef] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    validity_rule_parameter_ref: List[ValidityRuleParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    validity_trigger_ref: List[ValidityTriggerRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTriggerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    validity_condition_ref: List[ValidityConditionRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    responsibility_role_ref: List[ResponsibilityRoleRef] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    control_centre_ref: List[ControlCentreRef] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentreRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    organisational_unit_ref: List[OrganisationalUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    department_ref: List[DepartmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    organisation_part_ref: List[OrganisationPartRef] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    all_authorities_ref: List[AllAuthoritiesRef] = field(
        default_factory=list,
        metadata={
            "name": "AllAuthoritiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    all_operators_ref: List[AllOperatorsRef] = field(
        default_factory=list,
        metadata={
            "name": "AllOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    all_transport_organisations_ref: List[AllTransportOrganisationsRef] = field(
        default_factory=list,
        metadata={
            "name": "AllTransportOrganisationsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    all_organisations_ref: List[AllOrganisationsRef] = field(
        default_factory=list,
        metadata={
            "name": "AllOrganisationsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    retail_consortium_ref: List[RetailConsortiumRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortiumRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    authority_ref: List[AuthorityRef] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    operator_ref: List[OperatorRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    transport_organisation_ref: List[TransportOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    general_organisation_ref: List[GeneralOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    management_agent_ref: List[ManagementAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "ManagementAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    serviced_organisation_ref: List[ServicedOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    travel_agent_ref: List[TravelAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    other_organisation_ref: List[OtherOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "OtherOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    organisation_ref: List[OrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    responsibility_set_ref: List[ResponsibilitySetRef] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    destination_display_variant_ref: List[DestinationDisplayVariantRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    destination_display_ref: List[DestinationDisplayRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    allowed_line_direction_ref: List[AllowedLineDirectionRef] = field(
        default_factory=list,
        metadata={
            "name": "AllowedLineDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    line_ref: List[LineRef] = field(
        default_factory=list,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    group_of_entities_ref: List[GroupOfEntitiesRef1] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfEntitiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    group_of_customer_purchase_packages_ref: List[GroupOfCustomerPurchasePackagesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfCustomerPurchasePackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_sales_offer_packages_ref: List[GroupOfSalesOfferPackagesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_distance_matrix_elements_ref: List[GroupOfDistanceMatrixElementsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_distribution_channels_ref: List[GroupOfDistributionChannelsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistributionChannelsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    standard_fare_table_ref: List[StandardFareTableRef] = field(
        default_factory=list,
        metadata={
            "name": "StandardFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    fare_table_ref: List[FareTableRef] = field(
        default_factory=list,
        metadata={
            "name": "FareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    price_group_ref: List[PriceGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    rhythmical_journey_group_ref: List[RhythmicalJourneyGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "RhythmicalJourneyGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    headway_journey_group_ref: List[HeadwayJourneyGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "HeadwayJourneyGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    journey_frequency_group_ref: List[JourneyFrequencyGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyFrequencyGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_services_ref: List[GroupOfServicesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServicesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_stop_places_ref: List[GroupOfStopPlacesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfStopPlacesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    point_of_interest_hierarchy_ref: List[PointOfInterestHierarchyRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestHierarchyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_timing_links_ref: List[GroupOfTimingLinksRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimingLinksRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_operators_ref: List[GroupOfOperatorsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_places_ref: List[GroupOfPlacesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPlacesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    parent_section_ref: List[ParentSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ParentSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    parent_common_section_ref: List[ParentCommonSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ParentCommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    common_section_ref: List[CommonSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "CommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    line_section_ref: List[LineSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LineSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    fare_section_ref: List[FareSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    general_section_ref: List[GeneralSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    section_ref: List[SectionRef] = field(
        default_factory=list,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    log_ref: List[LogRef] = field(
        default_factory=list,
        metadata={
            "name": "LogRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_timebands_ref: List[GroupOfTimebandsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimebandsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    netex_org_uk_netex_place_ref: List[PlaceRef1] = field(
        default_factory=list,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    group_of_points_ref: List[GroupOfPointsRef1] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPointsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    stop_area_ref: List[StopAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    access_zone_ref: List[AccessZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    transport_administrative_zone_ref: List[TransportAdministrativeZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TransportAdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    administrative_zone_ref: List[AdministrativeZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    fare_zone_ref: List[FareZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    tariff_zone_ref: List[TariffZoneRef1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    netex_org_uk_netex_tariff_zone_ref: List[TariffZoneRef2] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 5,
            "sequential": True,
        }
    )
    zone_ref: List[ZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "ZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    netex_org_uk_netex_group_of_points_ref: List[GroupOfPointsRef2] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPointsRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    layer_ref: List[LayerRef] = field(
        default_factory=list,
        metadata={
            "name": "LayerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    network_ref: List[NetworkRef] = field(
        default_factory=list,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    group_of_lines_ref: List[GroupOfLinesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    general_group_of_entities_ref: List[GeneralGroupOfEntitiesRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralGroupOfEntitiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    netex_org_uk_netex_group_of_entities_ref: List[GroupOfEntitiesRef2] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfEntitiesRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    sales_transaction_frame_ref: List[SalesTransactionFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_frame_ref: List[FareFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "FareFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_frame_ref: List[ServiceFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    driver_schedule_frame_ref: List[DriverScheduleFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "DriverScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_schedule_frame_ref: List[VehicleScheduleFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    timetable_frame_ref: List[TimetableFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "TimetableFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    site_frame_ref: List[SiteFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    infrastructure_frame_ref: List[InfrastructureFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    general_frame_ref: List[GeneralFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    resource_frame_ref: List[ResourceFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ResourceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_calendar_frame_ref: List[ServiceCalendarFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    composite_frame_ref: List[CompositeFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "CompositeFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    version_frame_ref: List[VersionFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "VersionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    distribution_channel_ref: List[DistributionChannelRef] = field(
        default_factory=list,
        metadata={
            "name": "DistributionChannelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    charging_moment_ref: List[ChargingMomentRef] = field(
        default_factory=list,
        metadata={
            "name": "ChargingMomentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    price_unit_ref: List[PriceUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    purpose_of_journey_partition_ref: List[PurposeOfJourneyPartitionRef] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfJourneyPartitionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    timing_algorithm_type_ref: List[TimingAlgorithmTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingAlgorithmTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    point_of_interest_classification_ref: List[PointOfInterestClassificationRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    direction_ref: List[DirectionRef] = field(
        default_factory=list,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    type_of_activation_ref: List[TypeOfActivationRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    purpose_of_equipment_profile_ref: List[PurposeOfEquipmentProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfEquipmentProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    type_of_product_category_ref: List[TypeOfProductCategoryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    type_of_payment_method_ref: List[TypeOfPaymentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    class_of_use_ref: List[ClassOfUseRef] = field(
        default_factory=list,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    type_of_operation_ref: List[TypeOfOperationRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOperationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    type_of_codespace_assignment_ref: List[TypeOfCodespaceAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCodespaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    branding_ref: List[BrandingRef] = field(
        default_factory=list,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    type_of_responsibility_role_ref: List[TypeOfResponsibilityRoleRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    purpose_of_grouping_ref: List[PurposeOfGroupingRef] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfGroupingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    type_of_retail_device_ref: List[TypeOfRetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfRetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    customer_account_status_ref: List[CustomerAccountStatusRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_customer_account_ref: List[TypeOfCustomerAccountRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_fare_contract_entry_ref: List[TypeOfFareContractEntryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_fare_contract_ref: List[TypeOfFareContractRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_access_right_assignment_ref: List[TypeOfAccessRightAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_sales_offer_package_ref: List[TypeOfSalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_fare_structure_element_ref: List[TypeOfFareStructureElementRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_tariff_ref: List[TypeOfTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    all_distribution_channels_ref: List[AllDistributionChannelsRef] = field(
        default_factory=list,
        metadata={
            "name": "AllDistributionChannelsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_machine_readability_ref: List[TypeOfMachineReadabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_travel_document_ref: List[TypeOfTravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_fare_product_ref: List[TypeOfFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_fare_structure_factor_ref: List[TypeOfFareStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_pricing_rule_ref: List[TypeOfPricingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_flexible_service_ref: List[TypeOfFlexibleServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFlexibleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_passenger_information_equipment_ref: List[TypeOfPassengerInformationEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPassengerInformationEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_service_feature_ref: List[TypeOfServiceFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_congestion_ref: List[TypeOfCongestionRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCongestionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_time_demand_type_ref: List[TypeOfTimeDemandTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_journey_pattern_ref: List[TypeOfJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_security_list_ref: List[TypeOfSecurityListRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_delivery_variant_ref: List[TypeOfDeliveryVariantRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfDeliveryVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_notice_ref: List[TypeOfNoticeRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfNoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_service_ref: List[TypeOfServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_facility_ref: List[TypeOfFacilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_equipment_ref: List[TypeOfEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_projection_ref: List[TypeOfProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_feature_ref: List[TypeOfFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_link_sequence_ref: List[TypeOfLinkSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_organisation_part_ref: List[TypeOfOrganisationPartRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_organisation_ref: List[TypeOfOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_place_ref: List[TypeOfPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_transfer_ref: List[TypeOfTransferRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTransferRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_zone_ref: List[TypeOfZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_link_ref: List[TypeOfLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_point_ref: List[TypeOfPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_line_ref: List[TypeOfLineRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_validity_ref: List[TypeOfValidityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValidityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_frame_ref: List[TypeOfFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 4,
            "sequential": True,
        }
    )
    type_of_entity_ref: List[TypeOfEntityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEntityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    type_of_value_ref: List[TypeOfValueRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValueRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    data_source_ref: List[DataSourceRef] = field(
        default_factory=list,
        metadata={
            "name": "DataSourceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    version_ref: List[VersionRef] = field(
        default_factory=list,
        metadata={
            "name": "VersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    version_of_object_ref: Optional[VersionOfObjectRef] = field(
        default=None,
        metadata={
            "name": "VersionOfObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
