from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.account_status_type_enumeration import AccountStatusTypeEnumeration
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.baggage_type_enumeration import BaggageTypeEnumeration
from netex.models.bay_geometry_enumeration import BayGeometryEnumeration
from netex.models.blacklist import Blacklist
from netex.models.blacklists_in_frame_rel_structure import BlacklistsInFrameRelStructure
from netex.models.booking_access_enumeration import BookingAccessEnumeration
from netex.models.booking_charge_type_enumeration import BookingChargeTypeEnumeration
from netex.models.booking_method_enumeration import BookingMethodEnumeration
from netex.models.branding import Branding
from netex.models.branding_ref import BrandingRef
from netex.models.car_model_profile import CarModelProfile
from netex.models.car_model_profile_ref import CarModelProfileRef
from netex.models.car_pooling_service import CarPoolingService
from netex.models.car_pooling_service_ref import CarPoolingServiceRef
from netex.models.charging_moment_enumeration import ChargingMomentEnumeration
from netex.models.child_seat_enumeration import ChildSeatEnumeration
from netex.models.codespace import Codespace
from netex.models.codespace_ref import CodespaceRef
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.composite_frame_ref import CompositeFrameRef
from netex.models.condition_summary import ConditionSummary
from netex.models.contact_structure import ContactStructure
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.customer import Customer
from netex.models.customer_account import CustomerAccount
from netex.models.customer_account_ref import CustomerAccountRef
from netex.models.customer_accounts_rel_structure import CustomerAccountsRelStructure
from netex.models.customer_eligibilities_rel_structure import CustomerEligibilitiesRelStructure
from netex.models.customer_payment_means import CustomerPaymentMeans
from netex.models.customer_payment_means_ref import CustomerPaymentMeansRef
from netex.models.customer_payment_means_rel_structure import CustomerPaymentMeansRelStructure
from netex.models.customer_purchase_package import CustomerPurchasePackage
from netex.models.customer_purchase_package_element import CustomerPurchasePackageElement
from netex.models.customer_purchase_package_element_access import CustomerPurchasePackageElementAccess
from netex.models.customer_purchase_package_element_accesses_rel_structure import CustomerPurchasePackageElementAccessesRelStructure
from netex.models.customer_purchase_package_elements_rel_structure import CustomerPurchasePackageElementsRelStructure
from netex.models.customer_purchase_package_price_versioned_child_structure import CustomerPurchasePackagePriceVersionedChildStructure
from netex.models.customer_purchase_package_prices_rel_structure import CustomerPurchasePackagePricesRelStructure
from netex.models.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.models.customer_purchase_package_refs_rel_structure import CustomerPurchasePackageRefsRelStructure
from netex.models.customer_purchase_packages_in_frame_rel_structure import CustomerPurchasePackagesInFrameRelStructure
from netex.models.customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment
from netex.models.customer_purchase_parameter_assignments_rel_structure import CustomerPurchaseParameterAssignmentsRelStructure
from netex.models.customer_ref import CustomerRef
from netex.models.customer_security_listing import CustomerSecurityListing
from netex.models.customers_in_frame_rel_structure import CustomersInFrameRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.data_role_type_enumeration import DataRoleTypeEnumeration
from netex.models.data_source import DataSource
from netex.models.data_source_ref_structure import DataSourceRefStructure
from netex.models.data_sources_in_frame_rel_structure import DataSourcesInFrameRelStructure
from netex.models.distance_matrix_element import DistanceMatrixElement
from netex.models.distance_matrix_element_price import DistanceMatrixElementPrice
from netex.models.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.models.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.models.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.models.distribution_assignment import DistributionAssignment
from netex.models.distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from netex.models.distribution_channel import DistributionChannel
from netex.models.distribution_channel_ref import DistributionChannelRef
from netex.models.distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from netex.models.distribution_channels_in_frame_rel_structure import DistributionChannelsInFrameRelStructure
from netex.models.distribution_rights_enumeration import DistributionRightsEnumeration
from netex.models.driving_style_enumeration import DrivingStyleEnumeration
from netex.models.emv_card import EmvCard
from netex.models.emv_card_ref import EmvCardRef
from netex.models.entitlement_constraint_structure import EntitlementConstraintStructure
from netex.models.entitlement_required import EntitlementRequired
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import OperatingDay
from netex.models.entity_in_version_structure import ValidBetween
from netex.models.equipment_place import EquipmentPlace
from netex.models.equipment_places_rel_structure import EquipmentPlacesRelStructure
from netex.models.external_object_ref_structure import ExternalObjectRefStructure
from netex.models.fare_contract import FareContract
from netex.models.fare_contract_entries_rel_structure import FareContractEntriesRelStructure
from netex.models.fare_contracts_rel_structure import FareContractsRelStructure
from netex.models.fare_frame import FareFrame
from netex.models.fare_frame_ref import FareFrameRef
from netex.models.fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from netex.models.fare_structure_element import FareStructureElement
from netex.models.fare_structure_element_ref import FareStructureElementRef
from netex.models.fare_structure_element_refs_rel_structure import FareStructureElementRefsRelStructure
from netex.models.fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from netex.models.fare_structure_type_enumeration import FareStructureTypeEnumeration
from netex.models.fare_table_specifics_structure import FareTableSpecificsStructure
from netex.models.fare_tables_in_frame_rel_structure import FareTablesInFrameRelStructure
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.models.fuel_type_enumeration import FuelTypeEnumeration
from netex.models.fulfilment_method import FulfilmentMethod
from netex.models.fulfilment_method_ref import FulfilmentMethodRef
from netex.models.fulfilment_method_type_enumeration import FulfilmentMethodTypeEnumeration
from netex.models.fulfilment_methods_in_frame_rel_structure import FulfilmentMethodsInFrameRelStructure
from netex.models.gender_enumeration import GenderEnumeration
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.generic_parameter_assignments_rel_structure import GenericParameterAssignment
from netex.models.generic_parameter_assignments_rel_structure import GenericParameterAssignmentsRelStructure
from netex.models.individual_passenger_info import IndividualPassengerInfo
from netex.models.individual_passenger_infos_rel_structure import IndividualPassengerInfosRelStructure
from netex.models.individual_traveller import IndividualTraveller
from netex.models.individual_traveller_ref import IndividualTravellerRef
from netex.models.individual_travellers_in_frame_rel_structure import IndividualTravellersInFrameRelStructure
from netex.models.info_link import InfoLink
from netex.models.info_links_rel_structure import InfoLinksRelStructure
from netex.models.layer_ref import LayerRef
from netex.models.licence_requirements_enumeration import LicenceRequirementsEnumeration
from netex.models.location_structure_2 import LocationStructure2
from netex.models.logical_operation_enumeration import LogicalOperationEnumeration
from netex.models.luggage_allowance import LuggageAllowance
from netex.models.machine_readable_enumeration import MachineReadableEnumeration
from netex.models.marked_as_enumeration import MarkedAsEnumeration
from netex.models.media_type_enumeration import MediaTypeEnumeration
from netex.models.medium_access_device_refs_rel_structure import MediumAccessDeviceRefsRelStructure
from netex.models.medium_access_device_security_listing import MediumAccessDeviceSecurityListing
from netex.models.medium_access_devices_in_frame_rel_structure import MediumAccessDevicesInFrameRelStructure
from netex.models.medium_application_instance import MediumApplicationInstance
from netex.models.medium_application_instance_ref import MediumApplicationInstanceRef
from netex.models.medium_application_instance_rel_structure import MediumApplicationInstanceRelStructure
from netex.models.meeting_usage_enumeration import MeetingUsageEnumeration
from netex.models.mobile_device import MobileDevice
from netex.models.mobile_device_ref import MobileDeviceRef
from netex.models.mobility_journey_frame import MobilityJourneyFrame
from netex.models.mobility_service_frame import MobilityServiceFrame
from netex.models.mobility_service_frame_ref import MobilityServiceFrameRef
from netex.models.mobility_service_refs_rel_structure import MobilityServiceRefsRelStructure
from netex.models.mobility_services_rel_structure import MobilityServicesRelStructure
from netex.models.mode_restriction_assessment import ModeRestrictionAssessment
from netex.models.mode_restriction_assessments_rel_structure import ModeRestrictionAssessmentsRelStructure
from netex.models.modes_of_operation_rel_structure import ModesOfOperationRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.network_filter_by_value_structure import NetworkFilterByValueStructure
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from netex.models.nuisance_facility_list import NuisanceFacilityList
from netex.models.object_filter_by_value_structure import ObjectFilterByValueStructure
from netex.models.offered_travel_specification import OfferedTravelSpecification
from netex.models.offered_travel_specification_ref import OfferedTravelSpecificationRef
from netex.models.online_service import OnlineService
from netex.models.online_service_operator import OnlineServiceOperator
from netex.models.online_service_operator_ref import OnlineServiceOperatorRef
from netex.models.online_service_operator_version_structure import OnlineServiceOperatorVersionStructure
from netex.models.online_service_ref import OnlineServiceRef
from netex.models.online_service_refs_rel_structure import OnlineServiceRefsRelStructure
from netex.models.online_services_rel_structure import OnlineServicesRelStructure
from netex.models.onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from netex.models.operating_day_ref import OperatingDayRef
from netex.models.operating_days_in_frame_rel_structure import OperatingDaysInFrameRelStructure
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.organisation_type_enumeration import OrganisationTypeEnumeration
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.parking import Parking
from netex.models.parking_areas_rel_structure import ParkingAreasRelStructure
from netex.models.parking_bays_rel_structure import ParkingBaysRelStructure
from netex.models.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from netex.models.parking_entrances_for_vehicles_rel_structure import ParkingEntrancesForVehiclesRelStructure
from netex.models.parking_layout_enumeration import ParkingLayoutEnumeration
from netex.models.parking_payment_process_enumeration import ParkingPaymentProcessEnumeration
from netex.models.parking_properties import ParkingProperties
from netex.models.parking_properties_rel_structure import ParkingPropertiesRelStructure
from netex.models.parking_reservation_enumeration import ParkingReservationEnumeration
from netex.models.parking_stay_enumeration import ParkingStayEnumeration
from netex.models.parking_type_enumeration import ParkingTypeEnumeration
from netex.models.parking_user_enumeration import ParkingUserEnumeration
from netex.models.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.models.parking_visibility_enumeration import ParkingVisibilityEnumeration
from netex.models.parkings_in_frame_rel_structure import ParkingsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.place_equipments_rel_structure import PlaceEquipmentsRelStructure
from netex.models.point_in_single_journey_path_ref import PointInSingleJourneyPathRef
from netex.models.point_of_interest import PointOfInterest
from netex.models.point_of_interest_ref import PointOfInterestRef
from netex.models.point_ref_structure import PointRefStructure
from netex.models.points_of_interest_in_frame_rel_structure import PointsOfInterestInFrameRelStructure
from netex.models.postal_address import PostalAddress
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.preassigned_fare_product_enumeration import PreassignedFareProductEnumeration
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.price_rule_step_result_structure import PriceRuleStepResultStructure
from netex.models.price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from netex.models.priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from netex.models.priceable_object_version_structure import FarePricesRelStructure
from netex.models.priceable_object_version_structure import FareTable
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.pricing_rule_ref import PricingRuleRef
from netex.models.pricing_service import PricingService
from netex.models.pricing_service_ref import PricingServiceRef
from netex.models.pricing_services_rel_structure import PricingServicesRelStructure
from netex.models.propulsion_type_enumeration import PropulsionTypeEnumeration
from netex.models.public_use_enumeration import PublicUseEnumeration
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.models.purchase_when_enumeration import PurchaseWhenEnumeration
from netex.models.quay import Quay
from netex.models.quay_type_enumeration import QuayTypeEnumeration
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.refund_policy_enumeration import RefundPolicyEnumeration
from netex.models.refund_type_enumeration import RefundTypeEnumeration
from netex.models.refunding import Refunding
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.responsibility_role_assignment import ResponsibilityRoleAssignment
from netex.models.responsibility_role_assignments_rel_structure import ResponsibilityRoleAssignmentsRelStructure
from netex.models.responsibility_set import ResponsibilitySet
from netex.models.responsibility_sets_in_frame_rel_structure import ResponsibilitySetsInFrameRelStructure
from netex.models.road_address import RoadAddress
from netex.models.route_link import RouteLink
from netex.models.route_links_in_frame_rel_structure import RouteLinksInFrameRelStructure
from netex.models.route_point import RoutePoint
from netex.models.route_point_ref_structure import RoutePointRefStructure
from netex.models.route_points_in_frame_rel_structure import RoutePointsInFrameRelStructure
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_element_ref import SalesOfferPackageElementRef
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.sales_transaction import SalesTransaction
from netex.models.sales_transaction_frame import SalesTransactionFrame
from netex.models.sales_transaction_ref import SalesTransactionRef
from netex.models.same_user_enumeration import SameUserEnumeration
from netex.models.security_listings_rel_structure import SecurityListingsRelStructure
from netex.models.self_drive_submode import SelfDriveSubmode
from netex.models.self_drive_submode_enumeration import SelfDriveSubmodeEnumeration
from netex.models.service_booking_arrangements_structure import ServiceBookingArrangementsStructure
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_facility_set import ServiceFacilitySet
from netex.models.service_facility_set_ref import ServiceFacilitySetRef
from netex.models.service_facility_sets_in_frame_rel_structure import ServiceFacilitySetsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.simple_vehicle_category_enumeration import SimpleVehicleCategoryEnumeration
from netex.models.simple_vehicle_type import SimpleVehicleType
from netex.models.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.models.single_journey import SingleJourney
from netex.models.single_journey_path import SingleJourneyPath
from netex.models.single_journey_path_ref import SingleJourneyPathRef
from netex.models.single_journey_paths_rel_structure import SingleJourneyPathsRelStructure
from netex.models.single_journey_ref import SingleJourneyRef
from netex.models.single_journeys_rel_structure import SingleJourneysRelStructure
from netex.models.site_connection import SiteConnection
from netex.models.site_connection_end_structure import SiteConnectionEndStructure
from netex.models.site_frame import SiteFrame
from netex.models.site_frame_ref import SiteFrameRef
from netex.models.site_refs_rel_structure import SiteRefsRelStructure
from netex.models.site_type_enumeration import SiteTypeEnumeration
from netex.models.specific_parameter_assignments_rel_structure import SpecificParameterAssignment
from netex.models.specific_parameter_assignments_rel_structure import SpecificParameterAssignmentsRelStructure
from netex.models.stakeholder_role_type_enumeration import StakeholderRoleTypeEnumeration
from netex.models.stop_place import StopPlace
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.submode import Submode
from netex.models.submodes_rel_structure import SubmodesRelStructure
from netex.models.target_passing_time import TargetPassingTime
from netex.models.target_passing_time_versioned_child_structure import TargetPassingTimeVersionedChildStructure
from netex.models.target_passing_times_rel_structure import TargetPassingTimesRelStructure
from netex.models.tariff import Tariff
from netex.models.tariff_basis_enumeration import TariffBasisEnumeration
from netex.models.tariff_ref import TariffRef
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.taxi_rank import TaxiRank
from netex.models.taxi_rank_ref import TaxiRankRef
from netex.models.taxi_stand import TaxiStand
from netex.models.taxi_stands_rel_structure import TaxiStandsRelStructure
from netex.models.telephone_contact_structure import TelephoneContactStructure
from netex.models.third_party_product import ThirdPartyProduct
from netex.models.third_party_product_ref import ThirdPartyProductRef
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.ticketing_service_facility_list import TicketingServiceFacilityList
from netex.models.topographic_place import TopographicPlace
from netex.models.topographic_place_descriptor_versioned_child_structure import TopographicPlaceDescriptorVersionedChildStructure
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.topographic_places_in_frame_rel_structure import TopographicPlacesInFrameRelStructure
from netex.models.transfer_duration_structure import TransferDurationStructure
from netex.models.transfers_in_frame_rel_structure import TransfersInFrameRelStructure
from netex.models.transmission_enumeration import TransmissionEnumeration
from netex.models.transport_mode_structure import TransportModeStructure
from netex.models.transport_modes_rel_structure import TransportModesRelStructure
from netex.models.transport_organisation_version_structure import TransportOrganisationVersionStructure
from netex.models.transport_submode import TransportSubmode
from netex.models.transport_type_version_structure import TransportTypeVersionStructure
from netex.models.travel_document import TravelDocument
from netex.models.travel_document_ref import TravelDocumentRef
from netex.models.travel_documents_rel_structure import TravelDocumentsRelStructure
from netex.models.travel_specification_summary_endpoint_structure import TravelSpecificationSummaryEndpointStructure
from netex.models.travel_specification_summary_view import TravelSpecificationSummaryView
from netex.models.travel_specifications_rel_structure import TravelSpecificationsRelStructure
from netex.models.trip_leg_ref import TripLegRef
from netex.models.trip_ref import TripRef
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef
from netex.models.type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from netex.models.type_of_infolink_enumeration import TypeOfInfolinkEnumeration
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.type_of_travel_document_refs_rel_structure import TypeOfTravelDocumentRefsRelStructure
from netex.models.types_of_travel_document_in_frame_rel_structure import TypesOfTravelDocumentInFrameRelStructure
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_end_enumeration import UsageEndEnumeration
from netex.models.usage_parameters_rel_structure import UsageParametersRelStructure
from netex.models.usage_trigger_enumeration import UsageTriggerEnumeration
from netex.models.usage_validity_period import UsageValidityPeriod
from netex.models.usage_validity_type_enumeration import UsageValidityTypeEnumeration
from netex.models.used_in_refs_rel_structure import UsedInRefsRelStructure
from netex.models.user_profile_eligibility import UserProfileEligibility
from netex.models.user_type_enumeration import UserTypeEnumeration
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_ref import ValidableElementRef
from netex.models.validable_elements_rel_structure import ValidableElementsRelStructure
from netex.models.validity_parameters_rel_structure import ValidityParametersRelStructure
from netex.models.value_set import ValueSet
from netex.models.vehicle import Vehicle
from netex.models.vehicle_charging_equipment import VehicleChargingEquipment
from netex.models.vehicle_meeting_link import VehicleMeetingLink
from netex.models.vehicle_meeting_links_in_frame_rel_structure import VehicleMeetingLinksInFrameRelStructure
from netex.models.vehicle_meeting_places_rel_structure import VehicleMeetingPlacesRelStructure
from netex.models.vehicle_meeting_point import VehicleMeetingPoint
from netex.models.vehicle_meeting_point_assignment_1 import VehicleMeetingPointAssignment1
from netex.models.vehicle_meeting_point_assignments_rel_structure import VehicleMeetingPointAssignmentsRelStructure
from netex.models.vehicle_meeting_point_in_path import VehicleMeetingPointInPath
from netex.models.vehicle_meeting_point_ref import VehicleMeetingPointRef
from netex.models.vehicle_meeting_point_ref_structure import VehicleMeetingPointRefStructure
from netex.models.vehicle_meeting_points_in_frame_rel_structure import VehicleMeetingPointsInFrameRelStructure
from netex.models.vehicle_meeting_points_in_sequence_rel_structure import VehicleMeetingPointsInSequenceRelStructure
from netex.models.vehicle_model import VehicleModel
from netex.models.vehicle_model_profiles_in_frame_rel_structure import VehicleModelProfilesInFrameRelStructure
from netex.models.vehicle_model_ref import VehicleModelRef
from netex.models.vehicle_models_in_frame_rel_structure import VehicleModelsInFrameRelStructure
from netex.models.vehicle_pooler_profile import VehiclePoolerProfile
from netex.models.vehicle_pooler_profile_ref import VehiclePoolerProfileRef
from netex.models.vehicle_pooling import VehiclePooling
from netex.models.vehicle_pooling_driver_info import VehiclePoolingDriverInfo
from netex.models.vehicle_pooling_driver_info_ref import VehiclePoolingDriverInfoRef
from netex.models.vehicle_pooling_driver_infos_rel_structure import VehiclePoolingDriverInfosRelStructure
from netex.models.vehicle_pooling_meeting_place import VehiclePoolingMeetingPlace
from netex.models.vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from netex.models.vehicle_pooling_parking_area import VehiclePoolingParkingArea
from netex.models.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.models.vehicle_pooling_parking_bay import VehiclePoolingParkingBay
from netex.models.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.models.vehicle_pooling_place_assignment import VehiclePoolingPlaceAssignment
from netex.models.vehicle_pooling_ref import VehiclePoolingRef
from netex.models.vehicle_pooling_type_enumeration import VehiclePoolingTypeEnumeration
from netex.models.vehicle_ref import VehicleRef
from netex.models.vehicle_service_place_assignments_rel_structure import VehicleServicePlaceAssignmentsRelStructure
from netex.models.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure
from netex.models.vehicles_in_frame_rel_structure import VehiclesInFrameRelStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from netex.models.whitelist import Whitelist
from netex.models.whitelists_in_frame_rel_structure import WhitelistsInFrameRelStructure
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2020, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2020, 12, 17, 9, 30, 46, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        ),
        description=MultilingualString(
            value='Request for ryde 1  tariff'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        validity_condition=[
                            AvailabilityCondition(
                                id='r1',
                                version='any',
                                from_date=XmlDateTime(2020, 1, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        NetworkFilterByValueStructure(
                            layer_ref=LayerRef(
                                ref='fxc:fareNetwork_fareProducts_farePrices'
                            ),
                            object_references=ObjectFilterByValueStructure.ObjectReferences(
                                choice=[
                                    OperatorRef(
                                        version='any',
                                        ref='noc:XRYD'
                                    ),
                                    VehiclePoolingRef(
                                        ref='ride_share'
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example  of simple car pooling  ride offfer and fare '
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='rd:ride_sharing_example',
                validity_conditions_or_valid_between=[
                    ValidBetween(
                        from_date=XmlDateTime(2020, 6, 1, 0, 0, 0),
                        to_date=XmlDateTime(2020, 12, 31, 12, 0, 0)
                    ),
                ],
                data_source_ref_attribute='rd:ryde',
                version='1.0',
                responsibility_set_ref_attribute='rd:tariffs',
                name=MultilingualString(
                    value='Ride Sharing  Example'
                ),
                description=MultilingualString(
                    value='This is an example showing how one might encode  static aspects of a car ride  sharing scheme "ryde"  in NeTEx.  It includes some  prices.'
                ),
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        CodespaceRef(
                            ref='ryd_data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='ryd_data'
                    ),
                    default_data_source_ref=DataSourceRefStructure(
                        version='any',
                        ref='rd:ryde'
                    ),
                    default_currency='GBP'
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ResourceFrame(
                            id='rd:ride_sharing_example',
                            version='1.0',
                            responsibility_set_ref_attribute='rd:network_data',
                            name=MultilingualString(
                                value='ryde Operator specific  common resources'
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    Codespace(
                                        id='ryd_data',
                                        xmlns='rd',
                                        xmlns_url='http://www.ryde.eu/data',
                                        description='ryde data'
                                    ),
                                ]
                            ),
                            data_sources=DataSourcesInFrameRelStructure(
                                data_source=[
                                    DataSource(
                                        id='rd:ryde',
                                        version='any',
                                        email='feedback@ryde.eu',
                                        data_licence_code=ExternalObjectRefStructure(
                                            type_value='SPX',
                                            ref='GSCYQ'
                                        ),
                                        data_licence_url='https://opendata.eu/vanilla'
                                    ),
                                ]
                            ),
                            responsibility_sets=ResponsibilitySetsInFrameRelStructure(
                                responsibility_set=[
                                    ResponsibilitySet(
                                        id='rd:tariffs',
                                        version='any',
                                        name=MultilingualString(
                                            value='Operator Tariffs'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='rd:tariff_data@creates',
                                                    version='any',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.CREATES,
                                                    ],
                                                    stakeholder_role_type=[
                                                        StakeholderRoleTypeEnumeration.FARE_MANAGEMENT,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        value='noc:XRYD',
                                                        version='any',
                                                        ref='noc:XRYD'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ResponsibilitySet(
                                        id='rd:network_data',
                                        version='any',
                                        name=MultilingualString(
                                            value='Operator data'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='rd:network_data@creates',
                                                    version='any',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.CREATES,
                                                    ],
                                                    stakeholder_role_type=[
                                                        StakeholderRoleTypeEnumeration.PLANNING,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        value='noc:XRYD',
                                                        version='any',
                                                        ref='noc:XRYD'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            types_of_value=TypesOfValueInFrameRelStructure(
                                choice=[
                                    ValueSet(
                                        id='allBranding',
                                        version='any',
                                        name=MultilingualString(
                                            value='Brands'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                Branding(
                                                    id='myBrand',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='ryde'
                                                    ),
                                                    url='https://www.ryde.eu/static/images/logo.png'
                                                ),
                                            ]
                                        ),
                                        class_of_values='Branding'
                                    ),
                                ]
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    Operator(
                                        id='noc:XRYD',
                                        version='any',
                                        name=MultilingualString(
                                            value='ryde'
                                        ),
                                        short_name=MultilingualString(
                                            value='Ryde'
                                        ),
                                        trading_name=MultilingualString(
                                            value='Ticket to Ryde SA'
                                        ),
                                        description=MultilingualString(
                                            value='Members only system to  to allocate and match ride shares between commuters in the Metropolis  area'
                                        ),
                                        contact_details=ContactStructure(
                                            phone='+32 1293 449191',
                                            url='https://www.ryde.eu'
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.OPERATOR,
                                        ],
                                        address=TransportOrganisationVersionStructure.Address(
                                            street=MultilingualString(
                                                value='Alpha1'
                                            ),
                                            town=MultilingualString(
                                                value='Metropolis'
                                            ),
                                            post_code='RH10 9UA',
                                            postal_region='Metroland'
                                        ),
                                        primary_mode=AllModesEnumeration.SELF_DRIVE,
                                        choice=SelfDriveSubmode(
                                            value=SelfDriveSubmodeEnumeration.OWN_CAR
                                        ),
                                        mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=VehiclePoolingRef(
                                            version='any',
                                            ref='ride_share'
                                        )
                                    ),
                                    OnlineServiceOperator(
                                        id='floggit',
                                        version='any',
                                        name=MultilingualString(
                                            value='Online transport services'
                                        ),
                                        trading_name=MultilingualString(
                                            value='Web Floggers SA'
                                        ),
                                        description=MultilingualString(
                                            value='Thord  party providers of on;ine systems for Ryde'
                                        ),
                                        contact_details=ContactStructure(
                                            email='barrowboy@floggit.com'
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.ONLINE_PROVIDER,
                                        ],
                                        address=OnlineServiceOperatorVersionStructure.Address(
                                            street=MultilingualString(
                                                value='Rue des Postes.'
                                            ),
                                            town=MultilingualString(
                                                value='Betaville'
                                            ),
                                            postal_region='Metroland'
                                        )
                                    ),
                                ]
                            ),
                            modes_of_operation=ModesOfOperationRelStructure(
                                mode_of_operation_or_alternative_mode_of_operation_or_conventional_mode_of_operation=[
                                    VehiclePooling(
                                        id='ride_share',
                                        version='any',
                                        name=MultilingualString(
                                            value='Commuter  car pool'
                                        ),
                                        description=MultilingualString(
                                            value='Available/ wanted Rides in comtters own cars matched'
                                        ),
                                        submodes=SubmodesRelStructure(
                                            submode=[
                                                Submode(
                                                    id='ride_share',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.SELF_DRIVE,
                                                    choice=SelfDriveSubmode(
                                                        value=SelfDriveSubmodeEnumeration.OWN_CAR
                                                    )
                                                ),
                                            ]
                                        ),
                                        vehicle_pooling_type=VehiclePoolingTypeEnumeration.COMMUTER_CAR_POOLING
                                    ),
                                ]
                            ),
                            service_facility_sets=ServiceFacilitySetsInFrameRelStructure(
                                service_facility_set=[
                                    ServiceFacilitySet(
                                        id='no_smoking',
                                        version='any',
                                        nuisance_facility_list=NuisanceFacilityList(
                                            value=[
                                                NuisanceFacilityEnumeration.NO_SMOKING,
                                            ]
                                        )
                                    ),
                                    ServiceFacilitySet(
                                        id='smoking',
                                        version='any',
                                        nuisance_facility_list=NuisanceFacilityList(
                                            value=[
                                                NuisanceFacilityEnumeration.SMOKING,
                                            ]
                                        )
                                    ),
                                    ServiceFacilitySet(
                                        id='no_pets',
                                        version='any',
                                        nuisance_facility_list=NuisanceFacilityList(
                                            value=[
                                                NuisanceFacilityEnumeration.NO_ANIMALS,
                                            ]
                                        )
                                    ),
                                    ServiceFacilitySet(
                                        id='pets_allowed',
                                        version='any',
                                        nuisance_facility_list=NuisanceFacilityList(
                                            value=[
                                                NuisanceFacilityEnumeration.ANIMALS_ALLOWED,
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='rd:ride_sharing_example',
                            version='1.0',
                            responsibility_set_ref_attribute='rd:network_data',
                            name=MultilingualString(
                                value='Places localities used by services'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='rd:ride_sharing_example'
                                    ),
                                ]
                            ),
                            topographic_places=TopographicPlacesInFrameRelStructure(
                                topographic_place=[
                                    TopographicPlace(
                                        id='alphaville',
                                        version='any',
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal('1.35250'),
                                                latitude=Decimal('52.44692'),
                                                id='alphaville'
                                            )
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='Alphaville'
                                            )
                                        )
                                    ),
                                    TopographicPlace(
                                        id='gamma_sur_mer',
                                        version='any',
                                        name=MultilingualString(
                                            value='Gamma'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal('2.35250'),
                                                latitude=Decimal('53.44692'),
                                                id='Gamma-sur-mer'
                                            )
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='Gamma-sur-mer'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace(
                                        id='alphaville_gare@taxi',
                                        version='any',
                                        name=MultilingualString(
                                            value="Gare d'Alphaville",
                                            lang='fr'
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='alphaville'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='alphaville_gare@taxi_set_down',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Alphaville station set down Area'
                                                    ),
                                                    covered=CoveredEnumeration.COVERED,
                                                    transport_mode=AllVehicleModesOfTransportEnumeration.TAXI,
                                                    boarding_use=False,
                                                    alighting_use=True
                                                ),
                                                Quay(
                                                    id='alphaville_gare@taxi_pick_up',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='>Alphaville station pick up   Area'
                                                    ),
                                                    covered=CoveredEnumeration.COVERED,
                                                    transport_mode=AllVehicleModesOfTransportEnumeration.TAXI,
                                                    boarding_use=True,
                                                    alighting_use=False
                                                ),
                                            ]
                                        )
                                    ),
                                    TaxiRank(
                                        id='alphaville_hdv_taxi',
                                        version='any',
                                        name=MultilingualString(
                                            value='Taxi Rank at Alphaville Hotel de Ville'
                                        ),
                                        adjacent_sites=SiteRefsRelStructure(
                                            stop_place_ref_or_site_ref=[
                                                PointOfInterestRef(
                                                    version='any',
                                                    ref='alphaville_hdv'
                                                ),
                                            ]
                                        ),
                                        stop_place_type=StopTypeEnumeration.TAXI_RANK,
                                        taxi_stands=TaxiStandsRelStructure(
                                            taxi_stand=[
                                                TaxiStand(
                                                    id='alphaville_hdv_taxi@s1',
                                                    version='any',
                                                    boarding_use=True,
                                                    alighting_use=True,
                                                    quay_type=QuayTypeEnumeration.TAXI_STAND
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='alphaville_hdv',
                                        version='any',
                                        name=MultilingualString(
                                            value='ALphaville Hotel de Ville'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal('2.35250'),
                                                latitude=Decimal('53.44692'),
                                                id='alphaville_hdv'
                                            )
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='alphaville'
                                        ),
                                        site_type=SiteTypeEnumeration.GOVERNMENT
                                    ),
                                ]
                            ),
                            parkings=ParkingsInFrameRelStructure(
                                parking=[
                                    Parking(
                                        id='delta_park_and_ride',
                                        version='any',
                                        name=MultilingualString(
                                            value='Delta Park and Ride ',
                                            lang='en'
                                        ),
                                        cross_road=MultilingualString(
                                            value='Delta road'
                                        ),
                                        landmark=MultilingualString(
                                            value='Gas works'
                                        ),
                                        covered=CoveredEnumeration.OUTDOORS,
                                        all_areas_wheelchair_accessible=True,
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='gamma_sur_mer'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:XRYD'
                                        ),
                                        parking_type=ParkingTypeEnumeration.PARK_AND_RIDE,
                                        parking_vehicle_types=[
                                            ParkingVehicleEnumeration.ALL_PASSENGER_VEHICLES,
                                        ],
                                        parking_layout=ParkingLayoutEnumeration.OPEN_SPACE,
                                        total_capacity=3,
                                        overnight_parking_permitted=True,
                                        recharging_available=True,
                                        secure=False,
                                        real_time_occupancy_available=True,
                                        parking_payment_process=[
                                            ParkingPaymentProcessEnumeration.PAY_AT_MACHINE_ON_FOOT_PRIOR_TO_EXIT,
                                            ParkingPaymentProcessEnumeration.PAY_BY_MOBILE_DEVICE,
                                        ],
                                        payment_methods=[
                                            PaymentMethodEnumeration.CREDIT_CARD,
                                            PaymentMethodEnumeration.DEBIT_CARD,
                                            PaymentMethodEnumeration.MOBILE_APP,
                                        ],
                                        parking_reservation=ParkingReservationEnumeration.NO_RESERVATIONS,
                                        free_parking_out_of_hours=True,
                                        parking_properties=ParkingPropertiesRelStructure(
                                            parking_properties=[
                                                ParkingProperties(
                                                    id='delta_park_and_ride_overall',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Overall properties'
                                                    ),
                                                    parking_user_types=[
                                                        ParkingUserEnumeration.ALL,
                                                    ],
                                                    parking_vehicle_types=[
                                                        ParkingVehicleEnumeration.ALL_PASSENGER_VEHICLES,
                                                    ],
                                                    maximum_stay=XmlDuration("P1D"),
                                                    secure_parking=False,
                                                    bay_geometry=BayGeometryEnumeration.ORTHOGONAL,
                                                    parking_visibility=ParkingVisibilityEnumeration.DEMARCATED
                                                ),
                                            ]
                                        ),
                                        parking_areas=ParkingAreasRelStructure(
                                            parking_area_ref_or_parking_area=[
                                                VehiclePoolingParkingArea(
                                                    id='delta_park_and_ride@A1',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Resereved area for car pooling - allowed to leave cars for longer'
                                                    ),
                                                    equipment_places=EquipmentPlacesRelStructure(
                                                        equipment_place_ref_or_equipment_place=[
                                                            EquipmentPlace(
                                                                id='delta_park_and_ride@A1_charger',
                                                                version='any'
                                                            ),
                                                        ]
                                                    ),
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            VehicleChargingEquipment(
                                                                id='delta_park_and_ride@A1@01',
                                                                version='any',
                                                                free_recharging=True,
                                                                reservation_required=True,
                                                                reservation_url='chargme.eu/bookings'
                                                            ),
                                                        ]
                                                    ),
                                                    parking_properties_or_parking_properties=ParkingProperties(
                                                        id='delta_park_and_ride@A1',
                                                        version='any',
                                                        parking_user_types=[
                                                            ParkingUserEnumeration.VEHICLE_SHARING,
                                                        ],
                                                        parking_stay_list=[
                                                            ParkingStayEnumeration.MID_TERM,
                                                        ],
                                                        maximum_stay=XmlDuration("P3D"),
                                                        parking_visibility=ParkingVisibilityEnumeration.DEMARCATED
                                                    ),
                                                    bays=ParkingBaysRelStructure(
                                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref_or_parking_bay=[
                                                            VehiclePoolingParkingBay(
                                                                id='delta_park_and_ride@A1@01',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.CAR,
                                                                bay_geometry=BayGeometryEnumeration.ANGLED
                                                            ),
                                                            VehiclePoolingParkingBay(
                                                                id='delta_park_and_ride@A1@02',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.CAR,
                                                                bay_geometry=BayGeometryEnumeration.ANGLED,
                                                                length=Decimal('4.00'),
                                                                width=Decimal('3.00'),
                                                                recharging_available=False
                                                            ),
                                                            VehiclePoolingParkingBay(
                                                                id='delta_park_and_ride@A1@03',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.CAR,
                                                                bay_geometry=BayGeometryEnumeration.ORTHOGONAL,
                                                                length=Decimal('4.00'),
                                                                width=Decimal('3.00'),
                                                                recharging_available=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        vehicle_entrances=ParkingEntrancesForVehiclesRelStructure(
                                            parking_entrance_for_vehicles_ref_or_parking_entrance_for_vehicles=[
                                                ParkingEntranceForVehicles(
                                                    id='delta_park_and_ride@main_entrance',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Main Entrance'
                                                    ),
                                                    public_use=PublicUseEnumeration.ALL,
                                                    label=MultilingualString(
                                                        value='ENTRANCE A -y'
                                                    ),
                                                    is_entry=True
                                                ),
                                                ParkingEntranceForVehicles(
                                                    id='delta_park_and_ride@pooler_entrance',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Special entrance for car poolers'
                                                    ),
                                                    public_use=PublicUseEnumeration.AUTHORISED_PUBLIC_ONLY,
                                                    label=MultilingualString(
                                                        value='ENTRANCE B - Car Poolers only'
                                                    ),
                                                    is_entry=True,
                                                    drop_off_point_close=True,
                                                    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=VehiclePoolingRef(
                                                        version='any',
                                                        ref='ride_share'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='rd:ride_sharing_example',
                            version='1.0',
                            responsibility_set_ref_attribute='rd:route_data',
                            name=MultilingualString(
                                value='Routes'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='rd:ride_sharing_example'
                                    ),
                                ]
                            ),
                            route_points=RoutePointsInFrameRelStructure(
                                route_point=[
                                    RoutePoint(
                                        id='rd:h1@p1',
                                        version='1.0'
                                    ),
                                    RoutePoint(
                                        id='rd:h1@p2',
                                        version='1.0'
                                    ),
                                    RoutePoint(
                                        id='rd:h1@p3',
                                        version='1.0'
                                    ),
                                ]
                            ),
                            route_links=RouteLinksInFrameRelStructure(
                                route_link=[
                                    RouteLink(
                                        id='h1@p1+h1@p2',
                                        version='any',
                                        from_point_ref=RoutePointRefStructure(
                                            version='1.0',
                                            ref='rd:h1@p1'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='1.0',
                                            ref='rd:h1@p2'
                                        ),
                                        mode_restriction_assessments=ModeRestrictionAssessmentsRelStructure(
                                            mode_restriction_assessment_ref_or_mode_restriction_assessment=[
                                                ModeRestrictionAssessment(
                                                    id='h1@p1+h1@p2',
                                                    version='1.0',
                                                    transport_modes=TransportModesRelStructure(
                                                        open_transport_mode_ref_or_transport_mode=[
                                                            TransportModeStructure(
                                                                transport_mode=AllModesEnumeration.SELF_DRIVE,
                                                                choice=SelfDriveSubmode(
                                                                    value=SelfDriveSubmodeEnumeration.ALL_HIRE_VEHICLES
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=VehiclePoolingRef(
                                                        version='any',
                                                        ref='ride_share'
                                                    ),
                                                    minimum_number_of_passengers=1
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            connections=TransfersInFrameRelStructure(
                                transfer=[
                                    SiteConnection(
                                        id='alphaville_gare1+alphaville_station',
                                        version='any',
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT6M")
                                        ),
                                        from_value=SiteConnectionEndStructure(
                                            transport_mode=AllVehicleModesOfTransportEnumeration.SELF_DRIVE,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=PointRefStructure(
                                                version='any',
                                                ref='alphaville_gare'
                                            )
                                        ),
                                        to=SiteConnectionEndStructure(
                                            transport_mode=AllVehicleModesOfTransportEnumeration.RAIL,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=PointRefStructure(
                                                ref='alphaville_station',
                                                version_ref='EXTERNAL'
                                            ),
                                            choice=[
                                                TaxiRankRef(
                                                    ref='alphaville_station@taxi',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        MobilityServiceFrame(
                            id='rd:ride_sharing_example',
                            version='1.0',
                            responsibility_set_ref_attribute='rd:network_data',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='rd:ride_sharing_example'
                                    ),
                                ]
                            ),
                            mobility_services=MobilityServicesRelStructure(
                                mobility_service_or_common_vehicle_service_or_vehicle_pooling_service=[
                                    CarPoolingService(
                                        id='ryde',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Ryde car scharing scheme.'
                                        ),
                                        start_date=XmlDate(2018, 1, 1),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:XRYD'
                                        ),
                                        service_booking_arrangements=ServiceBookingArrangementsStructure(
                                            booking_contact=ContactStructure(
                                                url='https://www.ryde.eu/booking'
                                            ),
                                            booking_methods=[
                                                BookingMethodEnumeration.MOBILE_APP,
                                                BookingMethodEnumeration.ONLINE,
                                            ],
                                            booking_access=BookingAccessEnumeration.AUTHORISED_PUBLIC,
                                            book_when=PurchaseWhenEnumeration.ADVANCE_AND_DAY_OF_TRAVEL,
                                            buy_when=[
                                                PurchaseMomentEnumeration.ON_CHECK_OUT,
                                            ],
                                            minimum_booking_period=XmlDuration("PT2H"),
                                            booking_url='https://www.ryde.eu/booking',
                                            booking_note=MultilingualString(
                                                value='Booklings made using app. Bookings can be made up to two hour before travel. '
                                            ),
                                            deposit_required=False,
                                            booking_charge_type=BookingChargeTypeEnumeration.NONE
                                        ),
                                        booking_required=True,
                                        registration_required=True,
                                        proposed_by_services=OnlineServiceRefsRelStructure(
                                            online_service_ref=[
                                                OnlineServiceRef(
                                                    version='any',
                                                    ref='ryde_online'
                                                ),
                                            ]
                                        ),
                                        vehicle_pooling_ref=VehiclePoolingRef(
                                            version='any',
                                            ref='ride_share'
                                        )
                                    ),
                                ]
                            ),
                            online_services=OnlineServicesRelStructure(
                                online_service=[
                                    OnlineService(
                                        id='ryde_online',
                                        version='any',
                                        name=MultilingualString(
                                            value='Online registration for ryde'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        ),
                                        proposing_services=MobilityServiceRefsRelStructure(
                                            mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref=[
                                                CarPoolingServiceRef(
                                                    version='any',
                                                    ref='ryde'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            vehicle_meeting_points=VehicleMeetingPointsInFrameRelStructure(
                                vehicle_meeting_point=[
                                    VehicleMeetingPoint(
                                        id='gamma_area',
                                        version='any',
                                        name=MultilingualString(
                                            value='Pickup/Set down  in Gamma area'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('1.45250'),
                                            latitude=Decimal('52.54692')
                                        )
                                    ),
                                    VehicleMeetingPoint(
                                        id='alphaville_centre',
                                        version='any',
                                        name=MultilingualString(
                                            value='Pickup/Set down  in Alphaville centre'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('1.35250'),
                                            latitude=Decimal('52.44692')
                                        )
                                    ),
                                    VehicleMeetingPoint(
                                        id='alphaville_gare',
                                        version='any',
                                        name=MultilingualString(
                                            value='Pickup/Set down  at Alphaville station'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('1.36250'),
                                            latitude=Decimal('52.45692')
                                        )
                                    ),
                                ]
                            ),
                            vehicle_meeting_links=VehicleMeetingLinksInFrameRelStructure(
                                vehicle_meeting_link=[
                                    VehicleMeetingLink(
                                        id='gamma_area+alphaville_centre',
                                        version='any',
                                        distance=Decimal('20'),
                                        from_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='gamma_area'
                                        ),
                                        to_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_centre'
                                        )
                                    ),
                                    VehicleMeetingLink(
                                        id='gamma_area+alphaville_gare',
                                        version='any',
                                        distance=Decimal('23'),
                                        from_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='gamma_area'
                                        ),
                                        to_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_gare'
                                        )
                                    ),
                                    VehicleMeetingLink(
                                        id='alphaville_gare+alphaville_centre',
                                        version='any',
                                        distance=Decimal('3'),
                                        from_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_gare'
                                        ),
                                        to_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_centre'
                                        )
                                    ),
                                ]
                            ),
                            vehicle_meeting_places=VehicleMeetingPlacesRelStructure(
                                vehicle_meeting_place=[
                                    VehiclePoolingMeetingPlace(
                                        id='delta_park_and_ride',
                                        version='any',
                                        name=MultilingualString(
                                            value='Delta Park and ride'
                                        ),
                                        topographic_place_ref=TopographicPlaceRef(
                                            value=' ',
                                            version='any',
                                            ref='gamma_sur_mer'
                                        )
                                    ),
                                    VehiclePoolingMeetingPlace(
                                        id='bull_and_bush_inn',
                                        version='any',
                                        name=MultilingualString(
                                            value='TheBull and bush, Gamma'
                                        ),
                                        road_address=RoadAddress(
                                            id='bull_and_bush_inn',
                                            version='any',
                                            road_number='A512',
                                            road_name=MultilingualString(
                                                value='High Street'
                                            )
                                        ),
                                        topographic_place_ref=TopographicPlaceRef(
                                            value=' ',
                                            version='any',
                                            ref='gamma_sur_mer'
                                        )
                                    ),
                                    VehiclePoolingMeetingPlace(
                                        id='town_hall',
                                        version='any',
                                        name=MultilingualString(
                                            value='Town Hall'
                                        ),
                                        postal_address=PostalAddress(
                                            id='town_hall',
                                            version='any',
                                            street=MultilingualString(
                                                value='Grand Rue'
                                            ),
                                            town=MultilingualString(
                                                value='Alphaville'
                                            )
                                        ),
                                        topographic_place_ref=TopographicPlaceRef(
                                            value=' ',
                                            version='any',
                                            ref='alphaville'
                                        )
                                    ),
                                    VehiclePoolingMeetingPlace(
                                        id='alphaville_gare',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alphaville Station'
                                        ),
                                        postal_address=PostalAddress(
                                            id='alphaville_gare',
                                            version='any',
                                            street=MultilingualString(
                                                value='Rue de Gare'
                                            ),
                                            town=MultilingualString(
                                                value='Alphaville'
                                            )
                                        ),
                                        topographic_place_ref=TopographicPlaceRef(
                                            value=' ',
                                            version='any',
                                            ref='alphaville'
                                        ),
                                        choice=TaxiRankRef(
                                            ref='alphaville_gare@taxi',
                                            version_ref='EXTERNAL'
                                        )
                                    ),
                                ]
                            ),
                            vehicle_meeting_place_assignments=VehicleServicePlaceAssignmentsRelStructure(
                                vehicle_sharing_place_assignment_or_vehicle_pooling_place_assignment_or_taxi_service_place_assignment=[
                                    VehiclePoolingPlaceAssignment(
                                        id='delta_park_and_ride',
                                        version='any',
                                        order=1,
                                        vehicle_pooling_service_ref=CarPoolingServiceRef(
                                            version='any',
                                            ref='ryde'
                                        ),
                                        vehicle_pooling_meeting_place_ref_or_vehicle_pooling_parking_area_ref=VehiclePoolingMeetingPlaceRef(
                                            version='any',
                                            ref='delta_park_and_ride'
                                        )
                                    ),
                                    VehiclePoolingPlaceAssignment(
                                        id='delta_park_and_ride@A1',
                                        version='any',
                                        order=2,
                                        vehicle_pooling_service_ref=CarPoolingServiceRef(
                                            version='any',
                                            ref='ryde'
                                        ),
                                        vehicle_pooling_meeting_place_ref_or_vehicle_pooling_parking_area_ref=VehiclePoolingMeetingPlaceRef(
                                            version='any',
                                            ref='delta_park_and_ride'
                                        ),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=VehiclePoolingParkingBayRef(
                                            version='any',
                                            ref='delta_park_and_ride@A1@01'
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='rd:ride_sharing_example',
                            data_source_ref_attribute='rd:ryde',
                            version='1.0',
                            responsibility_set_ref_attribute='rd:tariffs',
                            name=MultilingualString(
                                value='ryde 1'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    MobilityServiceFrameRef(
                                        version='1.0',
                                        ref='rd:ride_sharing_example'
                                    ),
                                    SiteFrameRef(
                                        version='1.0',
                                        ref='rd:ride_sharing_example'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='ryde@single_trip',
                                        version='any',
                                        name=MultilingualString(
                                            value='ryde   - Tariff'
                                        ),
                                        document_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://ryde.eu/tariff.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.INFO,
                                                    ]
                                                ),
                                                InfoLink(
                                                    value='https://ryde.eu/tariffMap.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MAP,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:XRYD'
                                        ),
                                        choice_1=CarPoolingServiceRef(
                                            version='any',
                                            ref='ryde'
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='ryde@single_trip@access',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='A ride on the service -  '
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    choice_1=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='gamma_area+alphaville_centre'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ryde@single_trip@access',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:access',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            choice=[
                                                                OperatorRef(
                                                                    version='any',
                                                                    ref='noc:XRYD'
                                                                ),
                                                            ],
                                                            choice_2=[
                                                                CarPoolingServiceRef(
                                                                    version='any',
                                                                    ref='ryde'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ryde@single_trip@eligibility',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='eligible user types'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:eligibility',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ryde@single_trip@eligibility',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:eligible',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                VehiclePoolerProfile(
                                                                    id='smoker',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Adult'
                                                                    ),
                                                                    user_type=UserTypeEnumeration.ADULT,
                                                                    minimum_age=16,
                                                                    smoking_allowed=True,
                                                                    pets_allowed=True,
                                                                    detour_accepted=False
                                                                ),
                                                                VehiclePoolerProfile(
                                                                    id='non_smoker',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Adult'
                                                                    ),
                                                                    user_type=UserTypeEnumeration.ADULT,
                                                                    minimum_age=16,
                                                                    smoking_allowed=False,
                                                                    luggage_allowed=False,
                                                                    detour_accepted=True
                                                                ),
                                                                LuggageAllowance(
                                                                    id='non_smoker@skis',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Will accept up to one pair of skis'
                                                                    ),
                                                                    baggage_type=BaggageTypeEnumeration.SKIS,
                                                                    maximum_number_items=1
                                                                ),
                                                                LuggageAllowance(
                                                                    id='non_smoker@bag',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Will accept one suitcase'
                                                                    ),
                                                                    baggage_type=BaggageTypeEnumeration.SMALL_SUITCASE,
                                                                    maximum_number_items=1
                                                                ),
                                                                LuggageAllowance(
                                                                    id='non_smoker@wheelchair',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Will accept wheelchair up to stated dimensions'
                                                                    ),
                                                                    baggage_type=BaggageTypeEnumeration.WHEELCHAIR,
                                                                    maximum_number_items=1,
                                                                    maximum_bag_height=Decimal('1.5'),
                                                                    maximum_bag_width=Decimal('1.2'),
                                                                    maximum_bag_depth=Decimal('0.3')
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ryde@single_trip@conditions_of_travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='COnditions on travel'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:travel_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ryde@single_trip@conditions_of_travel',
                                                        version='any',
                                                        name=MultilingualString(
                                                            value='Conditions of travel'
                                                        ),
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:condition_of_use',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UsageValidityPeriod(
                                                                    id='ryde@single_trip@usageValidity',
                                                                    version='any',
                                                                    validity_period_type=UsageValidityTypeEnumeration.SINGLE_TRIP,
                                                                    usage_trigger=UsageTriggerEnumeration.START_OUTBOUND_RIDE,
                                                                    usage_end=UsageEndEnumeration.END_OF_TRIP
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='ryde@single_trip@frequency',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='One trip no transfers'
                                                                    ),
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.NONE,
                                                                    maximal_frequency=1
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ryde@single_trip@conditions_of_sale',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions of sale'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:sale_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ryde@single_trip@conditions_of_sale',
                                                        version='any',
                                                        name=MultilingualString(
                                                            value='Conditions of sale'
                                                        ),
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:condition_of_sale',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                Refunding(
                                                                    id='ryde@single_trip@refunding',
                                                                    version='any',
                                                                    refund_type=RefundTypeEnumeration.CANCELLATION,
                                                                    refund_policy=[
                                                                        RefundPolicyEnumeration.ANY,
                                                                    ],
                                                                    payment_method=[
                                                                        PaymentMethodEnumeration.EPAY_ACCOUNT,
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ryde@single_trip@accommodation',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Accomodation'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:condition_of_travel',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ryde@single_trip@facilities',
                                                        version='any',
                                                        name=MultilingualString(
                                                            value='facilities'
                                                        ),
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:condition_of_travel',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.OR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            facility_set_ref=[
                                                                ServiceFacilitySetRef(
                                                                    version='any',
                                                                    ref='smoking'
                                                                ),
                                                                ServiceFacilitySetRef(
                                                                    version='any',
                                                                    ref='no_smoking'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        ),
                                        distance_matrix_elements=DistanceMatrixElementsRelStructure(
                                            distance_matrix_element_ref_or_distance_matrix_element=[
                                                DistanceMatrixElement(
                                                    id='gamma_area+alphaville_centre',
                                                    version='any',
                                                    choice=PointRefStructure(
                                                        version='any',
                                                        ref='gamma_area'
                                                    ),
                                                    choice_1=PointRefStructure(
                                                        version='any',
                                                        ref='alphaville_centre'
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='gamma_area+alphaville_gare',
                                                    version='any',
                                                    choice=PointRefStructure(
                                                        version='any',
                                                        ref='gamma_area'
                                                    ),
                                                    choice_1=PointRefStructure(
                                                        version='any',
                                                        ref='alphaville_gare'
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='alphaville_centre+alphaville_gare',
                                                    version='any',
                                                    choice=PointRefStructure(
                                                        version='any',
                                                        ref='alphaville_centre'
                                                    ),
                                                    choice_1=PointRefStructure(
                                                        version='any',
                                                        ref='alphaville_gare'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_products=FareProductsInFrameRelStructure(
                                fare_product=[
                                    ThirdPartyProduct(
                                        id='ryde_online@membership',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Registered member of ryde online'
                                        ),
                                        info_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://tickettoryde/apps',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        )
                                    ),
                                    PreassignedFareProduct(
                                        id='ryde@single_trip',
                                        version='any',
                                        name=MultilingualString(
                                            value='One off trip'
                                        ),
                                        charging_moment_type=ChargingMomentEnumeration.BEFORE_TRAVEL_THEN_ADJUST_AT_END_OF_TRAVEL,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:XRYD'
                                        ),
                                        condition_summary=ConditionSummary(
                                            fare_structure_type=FareStructureTypeEnumeration.NETWORK_FLAT_FARE,
                                            tariff_basis=TariffBasisEnumeration.FLAT,
                                            is_refundable=False,
                                            has_discounted_fares=False,
                                            requires_deposit=True,
                                            no_cash_payment=True,
                                            requires_reservation=False
                                        ),
                                        validable_elements=ValidableElementsRelStructure(
                                            validable_element_ref_or_validable_element=[
                                                ValidableElement(
                                                    id='ryde@single_trip@travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Single  ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='ryde@single_trip@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='ryde@single_trip@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='ryde@single_trip@conditions_of_travel'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='ryde@single_trip@accommodation'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='ryde@single_trip',
                                                    version='any',
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='any',
                                                        ref='ryde@single_trip@travel'
                                                    )
                                                ),
                                            ]
                                        ),
                                        product_type=PreassignedFareProductEnumeration.SINGLE_TRIP
                                    ),
                                ]
                            ),
                            distribution_channels=DistributionChannelsInFrameRelStructure(
                                distribution_channel=[
                                    DistributionChannel(
                                        id='online',
                                        version='any',
                                        name=MultilingualString(
                                            value='Online'
                                        ),
                                        distribution_channel_type=DistributionChannelTypeEnumeration.ONLINE,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        ),
                                        payment_methods=[
                                            PaymentMethodEnumeration.DEBIT_CARD,
                                            PaymentMethodEnumeration.CREDIT_CARD,
                                        ],
                                        distribution_rights=[
                                            DistributionRightsEnumeration.SELL,
                                        ]
                                    ),
                                    DistributionChannel(
                                        id='mobile_application',
                                        version='any',
                                        name=MultilingualString(
                                            value='Mobile application'
                                        ),
                                        distribution_channel_type=DistributionChannelTypeEnumeration.MOBILE_DEVICE,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        ),
                                        payment_methods=[
                                            PaymentMethodEnumeration.DEBIT_CARD,
                                            PaymentMethodEnumeration.CREDIT_CARD,
                                        ],
                                        distribution_rights=[
                                            DistributionRightsEnumeration.SELL,
                                        ]
                                    ),
                                ]
                            ),
                            fulfilment_methods=FulfilmentMethodsInFrameRelStructure(
                                fulfilment_method=[
                                    FulfilmentMethod(
                                        id='mobile_device',
                                        version='any',
                                        name=MultilingualString(
                                            value='Collect from machine'
                                        ),
                                        fulfilment_method_type=FulfilmentMethodTypeEnumeration.MOBILE_APP,
                                        types_of_travel_document=TypeOfTravelDocumentRefsRelStructure(
                                            type_of_travel_document_ref=[
                                                TypeOfTravelDocumentRef(
                                                    version='any',
                                                    ref='mobile_application_data'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            types_of_travel_documents=TypesOfTravelDocumentInFrameRelStructure(
                                type_of_travel_document=[
                                    TypeOfTravelDocument(
                                        id='mobile_application_data',
                                        version='any',
                                        name=MultilingualString(
                                            value='Mobile app with access code'
                                        ),
                                        media_type=MediaTypeEnumeration.MOBILE_APP,
                                        machine_readable=[
                                            MachineReadableEnumeration.NFC,
                                        ]
                                    ),
                                ]
                            ),
                            sales_offer_packages=SalesOfferPackagesInFrameRelStructure(
                                sales_offer_package=[
                                    SalesOfferPackage(
                                        id='ryde@membership-SOP@mobileApp',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='ryde one off Mobile app purchase'
                                        ),
                                        condition_summary=ConditionSummary(
                                            requires_account=True
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='ryde@membership-SOP@online',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='By Mobile app'
                                                    ),
                                                    order=1,
                                                    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref=DistributionChannelRef(
                                                        version='any',
                                                        ref='online'
                                                    ),
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.ONLINE,
                                                    ticketing_service_facility_list=TicketingServiceFacilityList(
                                                        value=[
                                                            TicketingServiceFacilityEnumeration.PURCHASE,
                                                        ]
                                                    ),
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        version='any',
                                                        ref='mobile_device'
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='ryde@membership-SOP@mobileApp',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=ThirdPartyProductRef(
                                                        version='any',
                                                        ref='ryde_online@membership'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='ryde@single_trip-SOP@mobileApp',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='ryde one off Mobile app purchase'
                                        ),
                                        condition_summary=ConditionSummary(
                                            requires_account=True
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='ryde@single_trip-SOP@mobileApp',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Registered member of floggit '
                                                    ),
                                                    order=1,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            EntitlementRequired(
                                                                id='ryde@single_trip-SOP@mobileApp@registered',
                                                                version='any',
                                                                choice=ThirdPartyProductRef(
                                                                    version='any',
                                                                    ref='ryde_online@membership'
                                                                ),
                                                                entitlement_constraint=EntitlementConstraintStructure(
                                                                    user_constraint=SameUserEnumeration.SAME_PERSON
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameters=ValidityParametersRelStructure(
                                                        choice_2=[
                                                            OnlineServiceRef(
                                                                version='any',
                                                                ref='ryde_online'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='ryde@single_trip-SOP@mobileApp',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='By Mobile app'
                                                    ),
                                                    order=1,
                                                    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref=DistributionChannelRef(
                                                        version='any',
                                                        ref='mobile_application'
                                                    ),
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.MOBILE_DEVICE,
                                                    ticketing_service_facility_list=TicketingServiceFacilityList(
                                                        value=[
                                                            TicketingServiceFacilityEnumeration.PURCHASE,
                                                            TicketingServiceFacilityEnumeration.REFUND,
                                                        ]
                                                    ),
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        version='any',
                                                        ref='mobile_device'
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='ryde@single_trip-SOP@mobileApp',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='any',
                                                        ref='ryde@single_trip'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='rd:ride_sharing_example_Prices',
                            data_source_ref_attribute='rd:ryde',
                            version='1.0',
                            responsibility_set_ref_attribute='rd:tariffs',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_currency='EUR'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='rd:ride_sharing_example'
                                    ),
                                ]
                            ),
                            pricing_parameter_set=PricingParameterSet(
                                id='rd:ride_sharing_example_Prices',
                                version='any',
                                pricing_services=PricingServicesRelStructure(
                                    pricing_service=[
                                        PricingService(
                                            id='ryde_pricer',
                                            version='any',
                                            name=MultilingualString(
                                                value='Dynamic pricing engine'
                                            ),
                                            organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                                version='any',
                                                ref='noc:XRYD'
                                            ),
                                            url='https://ticketToRyde/engine'
                                        ),
                                    ]
                                )
                            ),
                            fare_tables=FareTablesInFrameRelStructure(
                                fare_table=[
                                    FareTable(
                                        id='ryde@single_trip',
                                        version='any',
                                        name=MultilingualString(
                                            value='ryde one off use prices'
                                        ),
                                        prices_for=PriceableObjectRefsRelStructure(
                                            choice=[
                                                SalesOfferPackageRef(
                                                    version='any',
                                                    ref='ryde@single_trip-SOP@mobileApp'
                                                ),
                                            ]
                                        ),
                                        used_in=UsedInRefsRelStructure(
                                            choice=[
                                                TariffRef(
                                                    version='any',
                                                    ref='ryde@single_trip'
                                                ),
                                            ]
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:XRYD'
                                        ),
                                        specifics=FareTableSpecificsStructure(
                                            choice_1=CarPoolingServiceRef(
                                                version='any',
                                                ref='ryde'
                                            )
                                        ),
                                        prices=FarePricesRelStructure(
                                            fare_price_ref_or_cell_ref_or_fare_price=[
                                                DistanceMatrixElementPrice(
                                                    id='gamma_area+alphaville_centre',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Dynamic Price'
                                                    ),
                                                    pricing_service_ref=PricingServiceRef(
                                                        version='any',
                                                        ref='ryde_pricer'
                                                    ),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='gamma_area+alphaville_centre'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ),
            CompositeFrame(
                id='rd:ride_sharing_example_transaction_examples',
                data_source_ref_attribute='rd:ryde',
                version='1.0',
                responsibility_set_ref_attribute='rd:transaction_data',
                name=MultilingualString(
                    value='Sample Transactions for ryde trips '
                ),
                prerequisites=VersionFrameRefsRelStructure(
                    version_frame_ref=[
                        CompositeFrameRef(
                            version='1.0',
                            ref='rd:ride_sharing_example'
                        ),
                    ]
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ResourceFrame(
                            id='rd:ride_sharing_example_data',
                            version='1.0',
                            name=MultilingualString(
                                value='Transaction common resources'
                            ),
                            vehicle_types=VehicleTypesInFrameRelStructure(
                                choice=[
                                    SimpleVehicleType(
                                        id='fast_car',
                                        version='any',
                                        self_propelled=True,
                                        propulsion_type=PropulsionTypeEnumeration.COMBUSTION,
                                        fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(
                                            value=FuelTypeEnumeration.PETROL_UNLEADED
                                        ),
                                        maximum_range=Decimal('400'),
                                        licence_requirements=LicenceRequirementsEnumeration.FULL,
                                        vehicle_category=SimpleVehicleCategoryEnumeration.MEDIUM_CAR,
                                        portable=False
                                    ),
                                ]
                            ),
                            vehicle_models=VehicleModelsInFrameRelStructure(
                                vehicle_model=[
                                    VehicleModel(
                                        id='porsche_404',
                                        version='any',
                                        manufacturer=MultilingualString(
                                            value='Porsche'
                                        ),
                                        vehicle_model_profile_ref=CarModelProfileRef(
                                            version='any',
                                            ref='porsche_404@A2'
                                        )
                                    ),
                                ]
                            ),
                            vehicle_model_profiles=VehicleModelProfilesInFrameRelStructure(
                                car_model_profile_or_cycle_model_profile=[
                                    CarModelProfile(
                                        id='porsche_404@A2',
                                        version='any',
                                        name=MultilingualString(
                                            value='Porsche 404 model A2'
                                        ),
                                        number_of_gears=6,
                                        child_seat=ChildSeatEnumeration.BABY,
                                        seats=4,
                                        doors=2,
                                        transmission=TransmissionEnumeration.AUTOMATIC,
                                        cruise_control=True,
                                        sat_nav=True,
                                        air_conditioning=True,
                                        convertible=True,
                                        usb_power_sockets=True,
                                        trailer_hitch=False,
                                        roof_rack=False,
                                        cycle_rack=False,
                                        ski_rack=True
                                    ),
                                ]
                            ),
                            vehicles=VehiclesInFrameRelStructure(
                                train_element_or_vehicle=[
                                    Vehicle(
                                        id='db54278',
                                        created=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value="Freddy's car"
                                        ),
                                        description=MultilingualString(
                                            value='Bright red Porsche convertible'
                                        ),
                                        registration_number='db54278',
                                        transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                            version='any',
                                            ref='fast_car'
                                        ),
                                        vehicle_model_ref=VehicleModelRef(
                                            version='any',
                                            ref='porsche_404'
                                        ),
                                        vehicle_model_profile_ref=CarModelProfileRef(
                                            version='any',
                                            ref='porsche_404@A2'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='rd:ride_sharing_example_data',
                            version='1.0',
                            operating_days=OperatingDaysInFrameRelStructure(
                                operating_day=[
                                    OperatingDay(
                                        id='2020-08-10',
                                        version='any',
                                        calendar_date=XmlDate(2020, 8, 10)
                                    ),
                                ]
                            )
                        ),
                        MobilityJourneyFrame(
                            id='rydt:sample_transactions',
                            version='1.2',
                            single_journey_paths=SingleJourneyPathsRelStructure(
                                single_journey_path=[
                                    SingleJourneyPath(
                                        id='rydt:Cust777@trans001@ride1234',
                                        version='any',
                                        name=MultilingualString(
                                            value='Path from Delta park and ride to Alphaville  hotel de ville.'
                                        ),
                                        distance=Decimal('25.00'),
                                        points_in_sequence=VehicleMeetingPointsInSequenceRelStructure(
                                            vehicle_meeting_point_in_path=[
                                                VehicleMeetingPointInPath(
                                                    id='rydt:Cust777@trans001@ride1234',
                                                    version='any',
                                                    order=1,
                                                    choice_1=VehicleMeetingPointRef(
                                                        version='any',
                                                        ref='gamma_area'
                                                    ),
                                                    onward_vehicle_meeting_link_ref=OnwardVehicleMeetingLinkRef(
                                                        version='any',
                                                        ref='gamma_area+alphaville_centre'
                                                    )
                                                ),
                                                VehicleMeetingPointInPath(
                                                    id='rydt:Cust777@trans001@ride1234',
                                                    version='any',
                                                    order=2,
                                                    choice_1=VehicleMeetingPointRef(
                                                        version='any',
                                                        ref='alphaville_centre'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            single_journeys=SingleJourneysRelStructure(
                                single_journey=[
                                    SingleJourney(
                                        id='rydt:Cust777@trans001@ride1234',
                                        version='any',
                                        name=MultilingualString(
                                            value='Offered Car pool journey from Delta, park and ride, to Alphaville,  hotel de ville'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.SELF_DRIVE,
                                        transport_submode=TransportSubmode(
                                            choice=SelfDriveSubmode(
                                                value=SelfDriveSubmodeEnumeration.OWN_CAR
                                            )
                                        ),
                                        common_vehicle_service_ref_or_vehicle_pooling_service_ref=CarPoolingServiceRef(
                                            version='any',
                                            ref='ryde'
                                        ),
                                        vehicle_ref=VehicleRef(
                                            version='any',
                                            ref='db54278'
                                        ),
                                        single_journey_path_ref=SingleJourneyPathRef(
                                            version='any',
                                            ref='rydt:Cust777@trans001@ride1234'
                                        ),
                                        departure_time=XmlTime(7, 0, 0, 0),
                                        operating_day_ref=OperatingDayRef(
                                            version='any',
                                            ref='2020-08-10'
                                        ),
                                        dated_passing_times=TargetPassingTimesRelStructure(
                                            target_passing_time=[
                                                TargetPassingTime(
                                                    id='rydt:Cust777@trans001@ride1234',
                                                    version='any',
                                                    point_in_journey_pattern_ref=PointInSingleJourneyPathRef(
                                                        version='any',
                                                        ref='rydt:Cust777@trans001@ride1234',
                                                        order=1
                                                    ),
                                                    choice_1=[
                                                        TargetPassingTimeVersionedChildStructure.AimedDepartureTime(
                                                            value=XmlTime(7, 0, 0, 0)
                                                        ),
                                                    ]
                                                ),
                                                TargetPassingTime(
                                                    id='rydt:Cust777@trans001@ride1234',
                                                    version='any',
                                                    point_in_journey_pattern_ref=PointInSingleJourneyPathRef(
                                                        version='any',
                                                        ref='rydt:Cust777@trans001@ride1234',
                                                        order=2
                                                    ),
                                                    choice_1=[
                                                        TargetPassingTimeVersionedChildStructure.AimedArrivalTime(
                                                            value=XmlTime(9, 15, 0, 0)
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),
                                        meeting_point_assignments=VehicleMeetingPointAssignmentsRelStructure(
                                            dynamic_vehicle_meeting_point_assignment_ref_or_vehicle_meeting_point_assignment_ref_or_vehicle_meeting_point_assignment=[
                                                VehicleMeetingPointAssignment1(
                                                    id='rydt:Cust777@trans001@ride1234',
                                                    version='any',
                                                    order=1,
                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                        version='any',
                                                        ref='gamma_area'
                                                    ),
                                                    choice=VehiclePoolingParkingAreaRef(
                                                        version='any',
                                                        ref='delta_park_and_ride@A1'
                                                    ),
                                                    usage=MeetingUsageEnumeration.PICK_UP
                                                ),
                                                VehicleMeetingPointAssignment1(
                                                    id='rydt:Cust777@trans001@ride1234',
                                                    version='any',
                                                    order=2,
                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                        version='any',
                                                        ref='alphaville_centre'
                                                    ),
                                                    choice=PointOfInterestRef(
                                                        version='any',
                                                        ref='alphaville_hdv'
                                                    ),
                                                    usage=MeetingUsageEnumeration.SET_DOWN
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            individual_travellers=IndividualTravellersInFrameRelStructure(
                                individual_traveller=[
                                    IndividualTraveller(
                                        id='rydt:Cust555',
                                        created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                        changed=XmlDateTime(2020, 8, 10, 9, 55, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Esmerelda'
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='rydt:Cust555'
                                        ),
                                        identity_verified=True,
                                        ranking=2,
                                        gender=GenderEnumeration.FEMALE,
                                        talkative=True,
                                        smoker=True,
                                        languages=[
                                            'fr',
                                            'de',
                                            'en',
                                            'ru',
                                            'it',
                                            'es',
                                            'nl',
                                        ],
                                        individual_passenger_infos=IndividualPassengerInfosRelStructure(
                                            individual_passenger_info=[
                                                IndividualPassengerInfo(
                                                    id='rydt:Cust555-01',
                                                    created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                    changed=XmlDateTime(2020, 8, 10, 9, 55, 0),
                                                    version='any',
                                                    individual_traveller_ref=IndividualTravellerRef(
                                                        version='any',
                                                        ref='rydt:Cust555'
                                                    ),
                                                    ranking=9,
                                                    last_trip_date=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                    comments_about=MultilingualString(
                                                        value='Never stopped talking, dog was sick everywhere'
                                                    ),
                                                    travelling_with_pet=True
                                                ),
                                            ]
                                        )
                                    ),
                                    IndividualTraveller(
                                        id='rydt:Cust777',
                                        created=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                        changed=XmlDateTime(2020, 8, 10, 14, 20, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Freddy'
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='rydt:Cust777'
                                        ),
                                        identity_verified=True,
                                        ranking=4,
                                        gender=GenderEnumeration.MALE,
                                        talkative=False,
                                        smoker=False,
                                        languages=[
                                            'ga',
                                            'en',
                                        ],
                                        vehicle_pooling_driver_infos=VehiclePoolingDriverInfosRelStructure(
                                            vehicle_pooling_driver_info=[
                                                VehiclePoolingDriverInfo(
                                                    id='rydt:Cust777-01',
                                                    created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                    changed=XmlDateTime(2020, 8, 10, 14, 20, 0),
                                                    version='any',
                                                    individual_traveller_ref=IndividualTravellerRef(
                                                        version='any',
                                                        ref='rydt:Cust777'
                                                    ),
                                                    ranking=5,
                                                    last_trip_date=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                    comments_about=MultilingualString(
                                                        value='Crazy, drove like a bat out of hell'
                                                    ),
                                                    travelling_with_pet=False,
                                                    driving_licence_verified=True,
                                                    insurance_verified=True,
                                                    driving_style=DrivingStyleEnumeration.FAST,
                                                    number_of_proposed_trips=3,
                                                    number_of_travellers_carried=5,
                                                    vehicle_ref=VehicleRef(
                                                        version='any',
                                                        ref='db54278'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SalesTransactionFrame(
                            id='rydt:sample_transactions',
                            version='1.2',
                            name=MultilingualString(
                                value='ryde Sample Transactions'
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    CodespaceRef(
                                        ref='ryd_data'
                                    ),
                                    Codespace(
                                        id='ryd_transactions',
                                        xmlns='rydt',
                                        xmlns_url='http://www.ryde.eu/transactions',
                                        description='Operator transaction data'
                                    ),
                                ]
                            ),
                            customers=CustomersInFrameRelStructure(
                                customer=[
                                    Customer(
                                        id='rydt:Cust555',
                                        created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                        version='any',
                                        surname='von Ritter',
                                        first_name='Esmerelda Z',
                                        title='Baronin',
                                        gender=GenderEnumeration.FEMALE,
                                        smoker=True,
                                        email='esmerelda@almanachdegotha.de',
                                        phone=TelephoneContactStructure(
                                            tel_national_number='078671234567',
                                            tel_country_code='41'
                                        ),
                                        customer_eligibilities=CustomerEligibilitiesRelStructure(
                                            customer_eligibility=[
                                                UserProfileEligibility(
                                                    id='rydt:Cust555@trans001@pooler',
                                                    version='any',
                                                    user_profile_ref=VehiclePoolerProfileRef(
                                                        version='any',
                                                        ref='non_smoker'
                                                    )
                                                ),
                                            ]
                                        ),
                                        customer_accounts=CustomerAccountsRelStructure(
                                            customer_account_ref_or_customer_account=[
                                                CustomerAccount(
                                                    id='rydt:Cust555@AC7651',
                                                    created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='hotrider'
                                                    ),
                                                    start_date=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                    customer_account_status_type=AccountStatusTypeEnumeration.ACTIVE,
                                                    customer_purchase_packages=CustomerPurchasePackageRefsRelStructure(
                                                        customer_purchase_package_ref=[
                                                            CustomerPurchasePackageRef(
                                                                version='any',
                                                                ref='rydt:CPP@Cust555@001'
                                                            ),
                                                            CustomerPurchasePackageRef(
                                                                version='any',
                                                                ref='rydt:CPP@Cust555@005'
                                                            ),
                                                        ]
                                                    ),
                                                    customer_payment_means_ref=CustomerPaymentMeansRef(
                                                        version='any',
                                                        ref='rydt:Cust555@AC7651@p1'
                                                    ),
                                                    payment_means=CustomerPaymentMeansRelStructure(
                                                        customer_payment_means=[
                                                            CustomerPaymentMeans(
                                                                id='rydt:Cust555@AC7651@p1',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='EZRitter Visa Card'
                                                                ),
                                                                medium_access_device_ref=EmvCardRef(
                                                                    version='any',
                                                                    ref='visa:47594444555666'
                                                                )
                                                            ),
                                                            CustomerPaymentMeans(
                                                                id='rydt:Cust555@AC7651@p2',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='EZRitter mobile device'
                                                                ),
                                                                medium_access_device_ref=MobileDeviceRef(
                                                                    version='any',
                                                                    ref='rydt:4178671234567'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    medium_access_devices=MediumAccessDeviceRefsRelStructure(
                                                        medium_access_device_ref=MobileDeviceRef(
                                                            version='any',
                                                            ref='rydt:4178671234567'
                                                        )
                                                    )
                                                ),
                                            ]
                                        ),
                                        fare_contracts=FareContractsRelStructure(
                                            fare_contract_ref_or_fare_contract=[
                                                FareContract(
                                                    id='rydt:Cust555@trans001',
                                                    created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                    version='any',
                                                    customer_ref=CustomerRef(
                                                        version='any',
                                                        ref='rydt:Cust555'
                                                    ),
                                                    fare_contract_entries=FareContractEntriesRelStructure(
                                                        choice=[
                                                            SalesTransaction(
                                                                id='rydt:Cust555@trans001@join_as_member',
                                                                created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Join AS Member'
                                                                ),
                                                                date=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                                type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                                    ref='fxc:product_purchase',
                                                                    version_ref='EXTERNAL'
                                                                ),
                                                                amount=Decimal('0'),
                                                                travel_specifications=TravelSpecificationsRelStructure(
                                                                    travel_specification_ref_or_travel_specification=[
                                                                        OfferedTravelSpecification(
                                                                            id='rydt:Cust555@trans001@join_as_member',
                                                                            version='any',
                                                                            date=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='any',
                                                                                ref='rydt:Cust555@trans001@join_as_member'
                                                                            ),
                                                                            amount=Decimal('0'),
                                                                            start_of_validity=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                                            travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                                start=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                                                authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                                    version='any',
                                                                                    ref='noc:XRYD'
                                                                                ),
                                                                                user_profile_ref=VehiclePoolerProfileRef(
                                                                                    version='any',
                                                                                    ref='non_smoker'
                                                                                ),
                                                                                choice=CarPoolingServiceRef(
                                                                                    version='any',
                                                                                    ref='ryde'
                                                                                )
                                                                            ),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='rydt:Cust555@trans001@purchase_member',
                                                                                        version='any',
                                                                                        name=MultilingualString(
                                                                                            value='Join as member'
                                                                                        ),
                                                                                        order=1,
                                                                                        preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=ThirdPartyProductRef(
                                                                                            version='any',
                                                                                            ref='ryde_online@membership'
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                travel_documents=TravelDocumentsRelStructure(
                                                                    choice=[
                                                                        TravelDocument(
                                                                            id='rydt:ticket@765452230',
                                                                            validity_conditions_or_valid_between=[
                                                                                ValidBetween(
                                                                                    from_date=XmlDateTime(2020, 2, 28, 13, 0, 0)
                                                                                ),
                                                                            ],
                                                                            version='any',
                                                                            type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                                                version='any',
                                                                                ref='mobile_application_data'
                                                                            ),
                                                                            customer_purchase_package_ref=CustomerPurchasePackageRef(
                                                                                version='any',
                                                                                ref='rydt:CPP@Cust555@001'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            SalesTransaction(
                                                                id='rydt:Cust555@trans005@purchase_ride',
                                                                created=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Buy Single   ride Adult'
                                                                ),
                                                                description=MultilingualString(
                                                                    value='Cust555 pays for ride from Cust777. For simplicity we show  as a single  prepaid. If payment waslaterm e.g. completion, could have separate transactiosn for reservation and payment. '
                                                                ),
                                                                date=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                                                type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                                    ref='fxc:product_purchase',
                                                                    version_ref='EXTERNAL'
                                                                ),
                                                                amount=Decimal('10.00'),
                                                                payment_method=PaymentMethodEnumeration.CASH,
                                                                travel_specifications=TravelSpecificationsRelStructure(
                                                                    travel_specification_ref_or_travel_specification=[
                                                                        OfferedTravelSpecification(
                                                                            id='rydt:Cust555@trans005@purchase_ride',
                                                                            created=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                                                            version='any',
                                                                            date=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='any',
                                                                                ref='rydt:Cust555@trans005@purchase_ride'
                                                                            ),
                                                                            fare_price_ref_or_cell_ref=DistanceMatrixElementPriceRef(
                                                                                version='any',
                                                                                ref='gamma_area+alphaville_centre'
                                                                            ),
                                                                            amount=Decimal('10.00'),
                                                                            start_of_validity=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                            travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                                origin=TravelSpecificationSummaryEndpointStructure(
                                                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                                                        version='any',
                                                                                        ref='gamma_area'
                                                                                    )
                                                                                ),
                                                                                destination=TravelSpecificationSummaryEndpointStructure(
                                                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                                                        version='any',
                                                                                        ref='alphaville_centre'
                                                                                    )
                                                                                ),
                                                                                start=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                                duration=XmlDuration("PT45M"),
                                                                                authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                                    version='any',
                                                                                    ref='noc:XRYD'
                                                                                ),
                                                                                user_profile_ref=VehiclePoolerProfileRef(
                                                                                    version='any',
                                                                                    ref='non_smoker'
                                                                                ),
                                                                                choice=CarPoolingServiceRef(
                                                                                    version='any',
                                                                                    ref='ryde'
                                                                                )
                                                                            ),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='rydt:Cust555@trans005@purchase_ride',
                                                                                        version='any',
                                                                                        name=MultilingualString(
                                                                                            value='Single ride'
                                                                                        ),
                                                                                        order=1,
                                                                                        validable_element_ref=ValidableElementRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip@travel'
                                                                                        ),
                                                                                        preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip'
                                                                                        ),
                                                                                        fare_structure_element_ref=FareStructureElementRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip@access'
                                                                                        ),
                                                                                        sales_offer_package_ref=SalesOfferPackageRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip-SOP@mobileApp'
                                                                                        ),
                                                                                        limitations=UsageParametersRelStructure(
                                                                                            choice=[
                                                                                                VehiclePoolerProfileRef(
                                                                                                    version='any',
                                                                                                    ref='non_smoker'
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                        validity_parameters=ValidityParametersRelStructure(
                                                                                            mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                                                VehiclePoolingRef(
                                                                                                    version='any',
                                                                                                    ref='ride_share'
                                                                                                ),
                                                                                            ],
                                                                                            choice=[
                                                                                                OperatorRef(
                                                                                                    version='any',
                                                                                                    ref='noc:XRYD'
                                                                                                ),
                                                                                            ],
                                                                                            vehicle_meeting_point_ref=[
                                                                                                VehicleMeetingPointRef(
                                                                                                    version='any',
                                                                                                    ref='gamma_area'
                                                                                                ),
                                                                                                VehicleMeetingPointRef(
                                                                                                    version='any',
                                                                                                    ref='alphaville_centre'
                                                                                                ),
                                                                                            ],
                                                                                            vehicle_meeting_place_ref=[
                                                                                                VehiclePoolingMeetingPlaceRef(
                                                                                                    version='any',
                                                                                                    ref='delta_park_and_ride'
                                                                                                ),
                                                                                                VehiclePoolingMeetingPlaceRef(
                                                                                                    version='any',
                                                                                                    ref='town_hall'
                                                                                                ),
                                                                                            ],
                                                                                            choice_1=[
                                                                                                VehiclePoolingParkingAreaRef(
                                                                                                    version='any',
                                                                                                    ref='delta_park_and_ride@A1'
                                                                                                ),
                                                                                            ],
                                                                                            facility_set_ref=[
                                                                                                ServiceFacilitySetRef(
                                                                                                    version='any',
                                                                                                    ref='no_smoking'
                                                                                                ),
                                                                                            ],
                                                                                            single_journey_ref=[
                                                                                                SingleJourneyRef(
                                                                                                    version='any',
                                                                                                    ref='rydt:Cust777@trans001@ride1234'
                                                                                                ),
                                                                                            ],
                                                                                            choice_2=[
                                                                                                CarPoolingServiceRef(
                                                                                                    version='any',
                                                                                                    ref='ryde'
                                                                                                ),
                                                                                            ],
                                                                                            vehicle_ref=[
                                                                                                VehicleRef(
                                                                                                    version='any',
                                                                                                    ref='db54278'
                                                                                                ),
                                                                                            ],
                                                                                            type_of_travel_document_ref=[
                                                                                                TypeOfTravelDocumentRef(
                                                                                                    version='any',
                                                                                                    ref='mobile_application_data'
                                                                                                ),
                                                                                            ],
                                                                                            distribution_channel_ref_or_group_of_distribution_channels_ref=[
                                                                                                DistributionChannelRef(
                                                                                                    version='any',
                                                                                                    ref='mobile_application'
                                                                                                ),
                                                                                            ],
                                                                                            fulfilment_method_ref=[
                                                                                                FulfilmentMethodRef(
                                                                                                    version='any',
                                                                                                    ref='mobile_device'
                                                                                                ),
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                travel_documents=TravelDocumentsRelStructure(
                                                                    choice=[
                                                                        TravelDocument(
                                                                            id='rydt:ticket@765452234',
                                                                            validity_conditions_or_valid_between=[
                                                                                ValidBetween(
                                                                                    from_date=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                                    to_date=XmlDateTime(2020, 8, 10, 8, 0, 0)
                                                                                ),
                                                                            ],
                                                                            created=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                                                            version='any',
                                                                            type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                                                version='any',
                                                                                ref='mobile_application_data'
                                                                            ),
                                                                            customer_purchase_package_ref=CustomerPurchasePackageRef(
                                                                                version='any',
                                                                                ref='rydt:CPP@Cust555@005'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    Customer(
                                        id='rydt:Cust777',
                                        created=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                        version='any',
                                        surname='Gonzalez',
                                        first_name='Freddy',
                                        gender=GenderEnumeration.MALE,
                                        smoker=True,
                                        email='freddy@gofast.fr',
                                        phone=TelephoneContactStructure(
                                            tel_national_number='078672020202',
                                            tel_country_code='31'
                                        ),
                                        customer_eligibilities=CustomerEligibilitiesRelStructure(
                                            customer_eligibility=[
                                                UserProfileEligibility(
                                                    id='rydt:Cust777@trans001@pooler',
                                                    version='any',
                                                    user_profile_ref=VehiclePoolerProfileRef(
                                                        version='any',
                                                        ref='non_smoker'
                                                    )
                                                ),
                                            ]
                                        ),
                                        customer_accounts=CustomerAccountsRelStructure(
                                            customer_account_ref_or_customer_account=[
                                                CustomerAccount(
                                                    id='rydt:Cust777@AC8145',
                                                    created=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='fastrunner'
                                                    ),
                                                    start_date=XmlDateTime(2018, 1, 28, 12, 0, 0),
                                                    customer_account_status_type=AccountStatusTypeEnumeration.ACTIVE,
                                                    customer_purchase_packages=CustomerPurchasePackageRefsRelStructure(
                                                        customer_purchase_package_ref=[
                                                            CustomerPurchasePackageRef(
                                                                value='Join',
                                                                version='any',
                                                                ref='rydt:CPP@Cust777@001'
                                                            ),
                                                            CustomerPurchasePackageRef(
                                                                value='sell ride',
                                                                version='any',
                                                                ref='rydt:CPP@Cust777@021'
                                                            ),
                                                        ]
                                                    ),
                                                    customer_payment_means_ref=CustomerPaymentMeansRef(
                                                        version='any',
                                                        ref='rydt:Cust777@AC8145@p1'
                                                    ),
                                                    payment_means=CustomerPaymentMeansRelStructure(
                                                        customer_payment_means=[
                                                            CustomerPaymentMeans(
                                                                id='rydt:Cust777@AC8145@p1',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Freddy master Card'
                                                                ),
                                                                medium_access_device_ref=EmvCardRef(
                                                                    ref='mc:47594444555666',
                                                                    version_ref='ETXERNAL'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        fare_contracts=FareContractsRelStructure(
                                            fare_contract_ref_or_fare_contract=[
                                                FareContract(
                                                    id='rydt:Cust777@trans001',
                                                    created=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                                    version='any',
                                                    customer_ref=CustomerRef(
                                                        ref='rydt:Cust777'
                                                    ),
                                                    fare_contract_entries=FareContractEntriesRelStructure(
                                                        choice=[
                                                            SalesTransaction(
                                                                id='rydt:Cust777@trans001@join_as_member',
                                                                created=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Join AS Member'
                                                                ),
                                                                date=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                                                type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                                    ref='fxc:product_purchase',
                                                                    version_ref='EXTERNAL'
                                                                ),
                                                                amount=Decimal('0'),
                                                                travel_specifications=TravelSpecificationsRelStructure(
                                                                    travel_specification_ref_or_travel_specification=[
                                                                        OfferedTravelSpecification(
                                                                            id='rydt:Cust777@trans001@join_as_member',
                                                                            version='any',
                                                                            date=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='any',
                                                                                ref='rydt:Cust777@trans001@join_as_member'
                                                                            ),
                                                                            amount=Decimal('0'),
                                                                            start_of_validity=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                                                            travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                                start=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                                                                authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                                    version='any',
                                                                                    ref='noc:XRYD'
                                                                                ),
                                                                                user_profile_ref=VehiclePoolerProfileRef(
                                                                                    version='any',
                                                                                    ref='non_smoker'
                                                                                ),
                                                                                choice=CarPoolingServiceRef(
                                                                                    version='any',
                                                                                    ref='ryde'
                                                                                )
                                                                            ),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='rydt:Cust777@trans001@purchase_member',
                                                                                        version='any',
                                                                                        name=MultilingualString(
                                                                                            value='Join as member'
                                                                                        ),
                                                                                        order=1,
                                                                                        preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=ThirdPartyProductRef(
                                                                                            version='any',
                                                                                            ref='ryde_online@membership'
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            SalesTransaction(
                                                                id='rydt:Cust777@trans005@offer_ride',
                                                                created=XmlDateTime(2020, 8, 6, 16, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Offer a Single  ride Adult beteen gamma and alphavile on 2020-08-10T07:00:00 '
                                                                ),
                                                                description=MultilingualString(
                                                                    value='Cust777 a offers ride. '
                                                                ),
                                                                date=XmlDateTime(2020, 8, 6, 16, 0, 0),
                                                                type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                                    ref='fxc:offer_ride',
                                                                    version_ref='EXTERNAL'
                                                                ),
                                                                amount=Decimal('-8.00'),
                                                                payment_method=PaymentMethodEnumeration.CASH,
                                                                travel_specifications=TravelSpecificationsRelStructure(
                                                                    travel_specification_ref_or_travel_specification=[
                                                                        OfferedTravelSpecification(
                                                                            id='rydt:Cust777@trans005@offer_ride',
                                                                            created=XmlDateTime(2020, 8, 6, 16, 0, 0),
                                                                            version='any',
                                                                            date=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='any',
                                                                                ref='rydt:Cust777@trans005@sell_ride'
                                                                            ),
                                                                            fare_price_ref_or_cell_ref=DistanceMatrixElementPriceRef(
                                                                                version='any',
                                                                                ref='gamma_area+alphaville_centre'
                                                                            ),
                                                                            amount=Decimal('10.00'),
                                                                            travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                                origin=TravelSpecificationSummaryEndpointStructure(
                                                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                                                        version='any',
                                                                                        ref='gamma_area'
                                                                                    )
                                                                                ),
                                                                                destination=TravelSpecificationSummaryEndpointStructure(
                                                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                                                        version='any',
                                                                                        ref='alphaville_centre'
                                                                                    )
                                                                                ),
                                                                                start=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                                duration=XmlDuration("PT45M"),
                                                                                authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                                    version='any',
                                                                                    ref='noc:XRYD'
                                                                                ),
                                                                                user_profile_ref=VehiclePoolerProfileRef(
                                                                                    version='any',
                                                                                    ref='non_smoker'
                                                                                ),
                                                                                choice=CarPoolingServiceRef(
                                                                                    version='any',
                                                                                    ref='ryde'
                                                                                )
                                                                            ),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='rydt:Cust777@trans005@offer_ride',
                                                                                        version='any',
                                                                                        name=MultilingualString(
                                                                                            value='Single ride'
                                                                                        ),
                                                                                        order=1,
                                                                                        validable_element_ref=ValidableElementRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip@travel'
                                                                                        ),
                                                                                        preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip'
                                                                                        ),
                                                                                        fare_structure_element_ref=FareStructureElementRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip@access'
                                                                                        ),
                                                                                        sales_offer_package_ref=SalesOfferPackageRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip-SOP@mobileApp'
                                                                                        ),
                                                                                        limitations=UsageParametersRelStructure(
                                                                                            choice=[
                                                                                                VehiclePoolerProfileRef(
                                                                                                    version='any',
                                                                                                    ref='non_smoker'
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                        validity_parameters=ValidityParametersRelStructure(
                                                                                            mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                                                VehiclePoolingRef(
                                                                                                    version='any',
                                                                                                    ref='ride_share'
                                                                                                ),
                                                                                            ],
                                                                                            choice=[
                                                                                                OperatorRef(
                                                                                                    version='any',
                                                                                                    ref='noc:XRYD'
                                                                                                ),
                                                                                            ],
                                                                                            facility_set_ref=[
                                                                                                ServiceFacilitySetRef(
                                                                                                    version='any',
                                                                                                    ref='no_smoking'
                                                                                                ),
                                                                                            ],
                                                                                            single_journey_ref=[
                                                                                                SingleJourneyRef(
                                                                                                    version='any',
                                                                                                    ref='rydt:Cust777@trans001@ride1234'
                                                                                                ),
                                                                                            ],
                                                                                            choice_2=[
                                                                                                CarPoolingServiceRef(
                                                                                                    version='any',
                                                                                                    ref='ryde'
                                                                                                ),
                                                                                            ],
                                                                                            vehicle_ref=[
                                                                                                VehicleRef(
                                                                                                    version='any',
                                                                                                    ref='db54278'
                                                                                                ),
                                                                                            ],
                                                                                            type_of_travel_document_ref=[
                                                                                                TypeOfTravelDocumentRef(
                                                                                                    version='any',
                                                                                                    ref='mobile_application_data'
                                                                                                ),
                                                                                            ],
                                                                                            distribution_channel_ref_or_group_of_distribution_channels_ref=[
                                                                                                DistributionChannelRef(
                                                                                                    version='any',
                                                                                                    ref='mobile_application'
                                                                                                ),
                                                                                            ],
                                                                                            fulfilment_method_ref=[
                                                                                                FulfilmentMethodRef(
                                                                                                    version='any',
                                                                                                    ref='mobile_device'
                                                                                                ),
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            SalesTransaction(
                                                                id='rydt:Cust777@trans005@sell_ride',
                                                                created=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Sell Single  ride Adult'
                                                                ),
                                                                description=MultilingualString(
                                                                    value='Cust777 accepts to provides ride by  Cust555. For simplicity we show  as a single  prepaid. If payment was later e.g.  on completion, could have separate transactions for reservation and payment. '
                                                                ),
                                                                date=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                                                type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                                    ref='fxc:sell_ride',
                                                                    version_ref='EXTERNAL'
                                                                ),
                                                                amount=Decimal('-8.00'),
                                                                payment_method=PaymentMethodEnumeration.CASH,
                                                                travel_specifications=TravelSpecificationsRelStructure(
                                                                    travel_specification_ref_or_travel_specification=[
                                                                        OfferedTravelSpecification(
                                                                            id='rydt:Cust777@trans005@sell_ride',
                                                                            version='any',
                                                                            date=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='any',
                                                                                ref='rydt:Cust777@trans005@sell_ride'
                                                                            ),
                                                                            fare_price_ref_or_cell_ref=DistanceMatrixElementPriceRef(
                                                                                version='any',
                                                                                ref='gamma_area+alphaville_centre'
                                                                            ),
                                                                            amount=Decimal('-8.00'),
                                                                            rule_step_results=PriceRuleStepResultsRelStructure(
                                                                                rule_step_result=[
                                                                                    PriceRuleStepResultStructure(
                                                                                        amount=Decimal('-10'),
                                                                                        adjustment_amount=Decimal('2.00'),
                                                                                        discounting_rule_ref_or_pricing_rule_ref=PricingRuleRef(
                                                                                            ref='ryde_fee'
                                                                                        ),
                                                                                        narrative=MultilingualString(
                                                                                            value='10 charge less Â£2 Ryde fee'
                                                                                        ),
                                                                                        id='rydt:Cust777@trans005@sell_ride',
                                                                                        order=1
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                            start_of_validity=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                            travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                                origin=TravelSpecificationSummaryEndpointStructure(
                                                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                                                        version='any',
                                                                                        ref='gamma_area'
                                                                                    )
                                                                                ),
                                                                                destination=TravelSpecificationSummaryEndpointStructure(
                                                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                                                        version='any',
                                                                                        ref='alphaville_centre'
                                                                                    )
                                                                                ),
                                                                                start=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                                duration=XmlDuration("PT45M"),
                                                                                authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                                    version='any',
                                                                                    ref='noc:XRYD'
                                                                                ),
                                                                                user_profile_ref=VehiclePoolerProfileRef(
                                                                                    version='any',
                                                                                    ref='non_smoker'
                                                                                ),
                                                                                choice=CarPoolingServiceRef(
                                                                                    version='any',
                                                                                    ref='ryde'
                                                                                )
                                                                            ),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='rydt:Cust777@trans005@sell_ride',
                                                                                        version='any',
                                                                                        name=MultilingualString(
                                                                                            value='Single ride'
                                                                                        ),
                                                                                        order=1,
                                                                                        validable_element_ref=ValidableElementRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip@travel'
                                                                                        ),
                                                                                        preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip'
                                                                                        ),
                                                                                        fare_structure_element_ref=FareStructureElementRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip@access'
                                                                                        ),
                                                                                        sales_offer_package_ref=SalesOfferPackageRef(
                                                                                            version='any',
                                                                                            ref='ryde@single_trip-SOP@mobileApp'
                                                                                        ),
                                                                                        limitations=UsageParametersRelStructure(
                                                                                            choice=[
                                                                                                VehiclePoolerProfileRef(
                                                                                                    version='any',
                                                                                                    ref='non_smoker'
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                        validity_parameters=ValidityParametersRelStructure(
                                                                                            mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                                                VehiclePoolingRef(
                                                                                                    version='any',
                                                                                                    ref='ride_share'
                                                                                                ),
                                                                                            ],
                                                                                            choice=[
                                                                                                OperatorRef(
                                                                                                    version='any',
                                                                                                    ref='noc:XRYD'
                                                                                                ),
                                                                                            ],
                                                                                            vehicle_meeting_point_ref=[
                                                                                                VehicleMeetingPointRef(
                                                                                                    version='any',
                                                                                                    ref='gamma_area'
                                                                                                ),
                                                                                                VehicleMeetingPointRef(
                                                                                                    version='any',
                                                                                                    ref='alphaville_centre'
                                                                                                ),
                                                                                            ],
                                                                                            vehicle_meeting_place_ref=[
                                                                                                VehiclePoolingMeetingPlaceRef(
                                                                                                    version='any',
                                                                                                    ref='delta_park_and_ride'
                                                                                                ),
                                                                                                VehiclePoolingMeetingPlaceRef(
                                                                                                    version='any',
                                                                                                    ref='town_hall'
                                                                                                ),
                                                                                            ],
                                                                                            choice_1=[
                                                                                                VehiclePoolingParkingAreaRef(
                                                                                                    version='any',
                                                                                                    ref='delta_park_and_ride@A1'
                                                                                                ),
                                                                                            ],
                                                                                            facility_set_ref=[
                                                                                                ServiceFacilitySetRef(
                                                                                                    version='any',
                                                                                                    ref='no_smoking'
                                                                                                ),
                                                                                            ],
                                                                                            single_journey_ref=[
                                                                                                SingleJourneyRef(
                                                                                                    version='any',
                                                                                                    ref='rydt:Cust777@trans001@ride1234'
                                                                                                ),
                                                                                            ],
                                                                                            choice_2=[
                                                                                                CarPoolingServiceRef(
                                                                                                    version='any',
                                                                                                    ref='ryde'
                                                                                                ),
                                                                                            ],
                                                                                            vehicle_ref=[
                                                                                                VehicleRef(
                                                                                                    version='any',
                                                                                                    ref='db54278'
                                                                                                ),
                                                                                            ],
                                                                                            type_of_travel_document_ref=[
                                                                                                TypeOfTravelDocumentRef(
                                                                                                    version='any',
                                                                                                    ref='mobile_application_data'
                                                                                                ),
                                                                                            ],
                                                                                            distribution_channel_ref_or_group_of_distribution_channels_ref=[
                                                                                                DistributionChannelRef(
                                                                                                    version='any',
                                                                                                    ref='mobile_application'
                                                                                                ),
                                                                                            ],
                                                                                            fulfilment_method_ref=[
                                                                                                FulfilmentMethodRef(
                                                                                                    version='any',
                                                                                                    ref='mobile_device'
                                                                                                ),
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                travel_documents=TravelDocumentsRelStructure(
                                                                    choice=[
                                                                        TravelDocument(
                                                                            id='rydt:ticket@765452235',
                                                                            validity_conditions_or_valid_between=[
                                                                                ValidBetween(
                                                                                    from_date=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                                    to_date=XmlDateTime(2020, 8, 10, 8, 0, 0)
                                                                                ),
                                                                            ],
                                                                            created=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                                                            version='any',
                                                                            type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                                                version='any',
                                                                                ref='mobile_application_data'
                                                                            ),
                                                                            customer_purchase_package_ref=CustomerPurchasePackageRef(
                                                                                version='any',
                                                                                ref='rydt:CPP@Cust777@021'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            medium_access_devices=MediumAccessDevicesInFrameRelStructure(
                                emv_card_or_smartcard_or_mobile_device=[
                                    EmvCard(
                                        id='visa:47594444555666',
                                        created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='E.von Ritter - Visa card'
                                        )
                                    ),
                                    MobileDevice(
                                        id='rydt:4178671234567',
                                        created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value="Esmerelda's phone"
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='rydt:Cust555'
                                        ),
                                        application_instances=MediumApplicationInstanceRelStructure(
                                            medium_application_instance=[
                                                MediumApplicationInstance(
                                                    id='rydt:4178671234567@Ryde',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Ryde app'
                                                    ),
                                                    travel_document_ref=TravelDocumentRef(
                                                        version='any',
                                                        ref='rydt:ticket@765452234'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    MobileDevice(
                                        id='rydt:3178672020202',
                                        created=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value="Freddy's phone"
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='rydt:Cust777'
                                        ),
                                        application_instances=MediumApplicationInstanceRelStructure(
                                            medium_application_instance=[
                                                MediumApplicationInstance(
                                                    id='rydt:3178672020202@Ryde',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Ryde app'
                                                    ),
                                                    travel_document_ref=TravelDocumentRef(
                                                        version='any',
                                                        ref='rydt:ticket@765452234'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            blacklists=BlacklistsInFrameRelStructure(
                                blacklist=[
                                    Blacklist(
                                        id='rydt:Bad',
                                        version='any',
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:XRYD'
                                        ),
                                        security_listings=SecurityListingsRelStructure(
                                            security_listing=[
                                                MediumAccessDeviceSecurityListing(
                                                    id='rydt:Bad@visa@47594444555666',
                                                    version='any',
                                                    order=1,
                                                    medium_access_device_ref=EmvCardRef(
                                                        version='any',
                                                        ref='visa:47594444555666'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            whitelists=WhitelistsInFrameRelStructure(
                                whitelist=[
                                    Whitelist(
                                        id='rydt:Good',
                                        version='any',
                                        name=MultilingualString(
                                            value='Approved listimgs>'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:XRYD'
                                        ),
                                        security_listings=SecurityListingsRelStructure(
                                            security_listing=[
                                                CustomerSecurityListing(
                                                    id='rydt:Good@Cust555',
                                                    version='any',
                                                    order=1,
                                                    customer_ref=CustomerRef(
                                                        version='any',
                                                        ref='rydt:Cust555'
                                                    )
                                                ),
                                                MediumAccessDeviceSecurityListing(
                                                    id='rydt:Good@4178671234567',
                                                    version='any',
                                                    order=1,
                                                    medium_access_device_ref=MobileDeviceRef(
                                                        version='any',
                                                        ref='rydt:4178671234567'
                                                    )
                                                ),
                                                CustomerSecurityListing(
                                                    id='rydt:Good@Cust777',
                                                    version='any',
                                                    order=1,
                                                    customer_ref=CustomerRef(
                                                        version='any',
                                                        ref='rydt:Cust777'
                                                    )
                                                ),
                                                MediumAccessDeviceSecurityListing(
                                                    id='rydt:Good@47594444555666',
                                                    version='any',
                                                    order=1,
                                                    medium_access_device_ref=EmvCardRef(
                                                        ref='mc:47594444555666',
                                                        version_ref='ETXERNAL'
                                                    )
                                                ),
                                                MediumAccessDeviceSecurityListing(
                                                    id='rydt:Good@3178672020202',
                                                    version='any',
                                                    order=1,
                                                    medium_access_device_ref=MobileDeviceRef(
                                                        version='any',
                                                        ref='rydt:3178672020202'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            customer_purchase_packages=CustomerPurchasePackagesInFrameRelStructure(
                                customer_purchase_package=[
                                    CustomerPurchasePackage(
                                        id='rydt:CPP@Cust555@001',
                                        validity_conditions_or_valid_between=[
                                            ValidBetween(
                                                from_date=XmlDateTime(2020, 2, 28, 13, 0, 0)
                                            ),
                                        ],
                                        created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Membership'
                                        ),
                                        description=MultilingualString(
                                            value='Cust555 joins ride schem as a member'
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='rydt:Cust555'
                                        ),
                                        customer_account_ref=CustomerAccountRef(
                                            version='any',
                                            ref='rydt:Cust555@AC7651'
                                        ),
                                        customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                            customer_purchase_package_element=[
                                                CustomerPurchasePackageElement(
                                                    id='rydt:CPP@Cust555@001',
                                                    version='any',
                                                    sales_offer_package_element_ref=SalesOfferPackageElementRef(
                                                        version='any',
                                                        ref='ryde@membership-SOP@mobileApp'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        ),
                                        sales_transaction_ref=SalesTransactionRef(
                                            version='any',
                                            ref='rydt:Cust555@trans001@join_as_member'
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            version='any',
                                            ref='rydt:4178671234567'
                                        ),
                                        medium_application_instance_ref=MediumApplicationInstanceRef(
                                            version='any',
                                            ref='rydt:4178671234567@Ryde'
                                        )
                                    ),
                                    CustomerPurchasePackage(
                                        id='rydt:CPP@Cust555@005',
                                        created=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                        changed=XmlDateTime(2020, 8, 10, 11, 50, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Book Single ride, prepaid'
                                        ),
                                        description=MultilingualString(
                                            value='Cust555 Purchase of ride from CUST777 to be made on   2020-08-10 at - 07:00:00  '
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='rydt:Cust555'
                                        ),
                                        customer_account_ref=CustomerAccountRef(
                                            version='any',
                                            ref='rydt:Cust555@AC7651'
                                        ),
                                        travel_specifications=TravelSpecificationsRelStructure(
                                            travel_specification_ref_or_travel_specification=[
                                                OfferedTravelSpecificationRef(
                                                    version='any',
                                                    ref='rydt:Cust555@trans005@purchase_ride'
                                                ),
                                            ]
                                        ),
                                        customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                            customer_purchase_package_element=[
                                                CustomerPurchasePackageElement(
                                                    id='rydt:CPP@Cust555@005',
                                                    created=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                                    changed=XmlDateTime(2020, 8, 10, 11, 50, 0),
                                                    version='any',
                                                    sales_offer_package_element_ref=SalesOfferPackageElementRef(
                                                        version='any',
                                                        ref='ryde@single_trip-SOP@mobileApp'
                                                    ),
                                                    marked_as=MarkedAsEnumeration.USED,
                                                    element_accesses=CustomerPurchasePackageElementAccessesRelStructure(
                                                        customer_purchase_package_element_access=[
                                                            CustomerPurchasePackageElementAccess(
                                                                id='rydt:CPP@Cust555@005@001',
                                                                created=XmlDateTime(2020, 8, 8, 12, 0, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.UNUSED
                                                            ),
                                                            CustomerPurchasePackageElementAccess(
                                                                id='rydt:CPP@Cust555@005@002',
                                                                changed=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.ACTIVATED,
                                                                validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                                    customer_purchase_parameter_assignment=[
                                                                        CustomerPurchaseParameterAssignment(
                                                                            id='rydt:Cust555@trans005@002',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Pick up at designated point'
                                                                            ),
                                                                            order=1,
                                                                            validity_parameters=ValidityParametersRelStructure(
                                                                                vehicle_meeting_point_ref=[
                                                                                    VehicleMeetingPointRef(
                                                                                        version='any',
                                                                                        ref='gamma_area'
                                                                                    ),
                                                                                ],
                                                                                vehicle_meeting_place_ref=[
                                                                                    VehiclePoolingMeetingPlaceRef(
                                                                                        version='any',
                                                                                        ref='delta_park_and_ride'
                                                                                    ),
                                                                                ],
                                                                                choice_1=[
                                                                                    VehiclePoolingParkingAreaRef(
                                                                                        version='any',
                                                                                        ref='delta_park_and_ride@A1'
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CustomerPurchasePackageElementAccess(
                                                                id='rydt:CPP@Cust555@005@003',
                                                                changed=XmlDateTime(2020, 8, 10, 7, 55, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.USED,
                                                                validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                                    customer_purchase_parameter_assignment=[
                                                                        CustomerPurchaseParameterAssignment(
                                                                            id='rydt:Cust555@trans005@003',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Set down at designated point'
                                                                            ),
                                                                            order=1,
                                                                            validity_parameters=ValidityParametersRelStructure(
                                                                                vehicle_meeting_point_ref=[
                                                                                    VehicleMeetingPointRef(
                                                                                        version='any',
                                                                                        ref='alphaville_centre'
                                                                                    ),
                                                                                ],
                                                                                vehicle_meeting_place_ref=[
                                                                                    VehiclePoolingMeetingPlaceRef(
                                                                                        version='any',
                                                                                        ref='town_hall'
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                        customer_purchase_parameter_assignment=[
                                                            CustomerPurchaseParameterAssignment(
                                                                id='rydt:CPP@Cust555@005',
                                                                version='any',
                                                                order=1,
                                                                limitations=UsageParametersRelStructure(
                                                                    choice=[
                                                                        VehiclePoolerProfileRef(
                                                                            version='any',
                                                                            ref='non_smoker'
                                                                        ),
                                                                    ]
                                                                ),
                                                                validity_parameters=ValidityParametersRelStructure(
                                                                    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                        VehiclePoolingRef(
                                                                            version='any',
                                                                            ref='ride_share'
                                                                        ),
                                                                    ],
                                                                    choice=[
                                                                        OperatorRef(
                                                                            version='any',
                                                                            ref='noc:XRYD'
                                                                        ),
                                                                    ],
                                                                    facility_set_ref=[
                                                                        ServiceFacilitySetRef(
                                                                            version='any',
                                                                            ref='no_smoking'
                                                                        ),
                                                                    ],
                                                                    single_journey_ref=[
                                                                        SingleJourneyRef(
                                                                            version='any',
                                                                            ref='rydt:Cust777@trans001@ride1234'
                                                                        ),
                                                                    ],
                                                                    choice_2=[
                                                                        CarPoolingServiceRef(
                                                                            version='any',
                                                                            ref='ryde'
                                                                        ),
                                                                    ],
                                                                    vehicle_ref=[
                                                                        VehicleRef(
                                                                            version='any',
                                                                            ref='db54278'
                                                                        ),
                                                                    ],
                                                                    type_of_travel_document_ref=[
                                                                        TypeOfTravelDocumentRef(
                                                                            version='any',
                                                                            ref='mobile_application_data'
                                                                        ),
                                                                    ],
                                                                    distribution_channel_ref_or_group_of_distribution_channels_ref=[
                                                                        DistributionChannelRef(
                                                                            version='any',
                                                                            ref='mobile_application'
                                                                        ),
                                                                    ],
                                                                    fulfilment_method_ref=[
                                                                        FulfilmentMethodRef(
                                                                            version='any',
                                                                            ref='mobile_device'
                                                                        ),
                                                                    ]
                                                                ),
                                                                individual_traveller_ref=IndividualTravellerRef(
                                                                    version='any',
                                                                    ref='rydt:Cust555'
                                                                ),
                                                                vehicle_pooling_driver_info_ref=VehiclePoolingDriverInfoRef(
                                                                    version='any',
                                                                    ref='rydt:Cust777-01'
                                                                ),
                                                                trip_ref=TripRef(
                                                                    ref='123456'
                                                                ),
                                                                trip_leg_ref=TripLegRef(
                                                                    ref='123456-1'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        ),
                                        sales_transaction_ref=SalesTransactionRef(
                                            version='any',
                                            ref='rydt:Cust555@trans005@purchase_ride'
                                        ),
                                        prices=CustomerPurchasePackagePricesRelStructure(
                                            customer_purchase_package_price_ref_or_customer_purchase_package_price_or_cell_ref=[
                                                CustomerPurchasePackagePriceVersionedChildStructure(
                                                    id='rydt:CPP@Cust555@005',
                                                    version='any',
                                                    amount=Decimal('8.00'),
                                                    pricing_service_ref=PricingServiceRef(
                                                        version='any',
                                                        ref='ryde_pricer'
                                                    )
                                                ),
                                            ]
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            version='any',
                                            ref='rydt:4178671234567'
                                        ),
                                        medium_application_instance_ref=MediumApplicationInstanceRef(
                                            version='any',
                                            ref='rydt:4178671234567@Ryde'
                                        )
                                    ),
                                    CustomerPurchasePackage(
                                        id='rydt:CPP@Cust777@001',
                                        validity_conditions_or_valid_between=[
                                            ValidBetween(
                                                from_date=XmlDateTime(2019, 1, 5, 12, 0, 0)
                                            ),
                                        ],
                                        created=XmlDateTime(2019, 1, 5, 12, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Membership'
                                        ),
                                        description=MultilingualString(
                                            value='Cust777 joins ride scheme'
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='rydt:Cust777'
                                        ),
                                        customer_account_ref=CustomerAccountRef(
                                            version='any',
                                            ref='rydt:Cust777@AC8145'
                                        ),
                                        customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                            customer_purchase_package_element=[
                                                CustomerPurchasePackageElement(
                                                    id='rydt:CPP@Cust777@001',
                                                    version='any',
                                                    sales_offer_package_element_ref=SalesOfferPackageElementRef(
                                                        version='any',
                                                        ref='ryde@membership-SOP@mobileApp'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        ),
                                        sales_transaction_ref=SalesTransactionRef(
                                            version='any',
                                            ref='rydt:Cust777@trans001@join_as_member'
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            version='any',
                                            ref='rydt:3178672020202'
                                        ),
                                        medium_application_instance_ref=MediumApplicationInstanceRef(
                                            version='any',
                                            ref='rydt:3178672020202@Ryde'
                                        )
                                    ),
                                    CustomerPurchasePackage(
                                        id='rydt:CPP@Cust777@021',
                                        created=XmlDateTime(2020, 8, 6, 16, 0, 0),
                                        changed=XmlDateTime(2020, 8, 10, 11, 50, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Provide Single ride'
                                        ),
                                        description=MultilingualString(
                                            value='Cust777 to provide a ride to CUst555 on 2020-08-10'
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='rydt:Cust777'
                                        ),
                                        customer_account_ref=CustomerAccountRef(
                                            version='any',
                                            ref='rydt:Cust777@AC8145'
                                        ),
                                        travel_specifications=TravelSpecificationsRelStructure(
                                            travel_specification_ref_or_travel_specification=[
                                                OfferedTravelSpecificationRef(
                                                    version='any',
                                                    ref='rydt:Cust777@trans005@sell_ride'
                                                ),
                                            ]
                                        ),
                                        customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                            customer_purchase_package_element=[
                                                CustomerPurchasePackageElement(
                                                    id='rydt:CPP@Cust777@021',
                                                    version='any',
                                                    sales_offer_package_element_ref=SalesOfferPackageElementRef(
                                                        version='any',
                                                        ref='ryde@single_trip-SOP@mobileApp'
                                                    ),
                                                    element_accesses=CustomerPurchasePackageElementAccessesRelStructure(
                                                        customer_purchase_package_element_access=[
                                                            CustomerPurchasePackageElementAccess(
                                                                id='rydt:CPP@Cust777@005@001',
                                                                created=XmlDateTime(2020, 8, 6, 16, 0, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.UNUSED
                                                            ),
                                                            CustomerPurchasePackageElementAccess(
                                                                id='rydt:CPP@Cust777@005@002',
                                                                changed=XmlDateTime(2020, 8, 10, 7, 0, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.ACTIVATED
                                                            ),
                                                            CustomerPurchasePackageElementAccess(
                                                                id='rydt:CPP@Cust777@005@003',
                                                                changed=XmlDateTime(2020, 8, 10, 7, 55, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.USED
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                        customer_purchase_parameter_assignment=[
                                                            CustomerPurchaseParameterAssignment(
                                                                id='rydt:CPP@Cust777@021',
                                                                version='any',
                                                                order=1,
                                                                limitations=UsageParametersRelStructure(
                                                                    choice=[
                                                                        VehiclePoolerProfileRef(
                                                                            version='any',
                                                                            ref='non_smoker'
                                                                        ),
                                                                    ]
                                                                ),
                                                                validity_parameters=ValidityParametersRelStructure(
                                                                    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                        VehiclePoolingRef(
                                                                            version='any',
                                                                            ref='ride_share'
                                                                        ),
                                                                    ],
                                                                    choice=[
                                                                        OperatorRef(
                                                                            version='any',
                                                                            ref='noc:XRYD'
                                                                        ),
                                                                    ],
                                                                    facility_set_ref=[
                                                                        ServiceFacilitySetRef(
                                                                            version='any',
                                                                            ref='no_smoking'
                                                                        ),
                                                                    ],
                                                                    single_journey_ref=[
                                                                        SingleJourneyRef(
                                                                            version='any',
                                                                            ref='rydt:Cust777@trans001@ride1234'
                                                                        ),
                                                                    ],
                                                                    choice_2=[
                                                                        CarPoolingServiceRef(
                                                                            version='any',
                                                                            ref='ryde'
                                                                        ),
                                                                    ],
                                                                    vehicle_ref=[
                                                                        VehicleRef(
                                                                            version='any',
                                                                            ref='db54278'
                                                                        ),
                                                                    ],
                                                                    type_of_travel_document_ref=[
                                                                        TypeOfTravelDocumentRef(
                                                                            version='any',
                                                                            ref='mobile_application_data'
                                                                        ),
                                                                    ],
                                                                    distribution_channel_ref_or_group_of_distribution_channels_ref=[
                                                                        DistributionChannelRef(
                                                                            version='any',
                                                                            ref='mobile_application'
                                                                        ),
                                                                    ],
                                                                    fulfilment_method_ref=[
                                                                        FulfilmentMethodRef(
                                                                            version='any',
                                                                            ref='mobile_device'
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        ),
                                        sales_transaction_ref=SalesTransactionRef(
                                            version='any',
                                            ref='rydt:Cust777@trans005@sell_ride'
                                        ),
                                        prices=CustomerPurchasePackagePricesRelStructure(
                                            customer_purchase_package_price_ref_or_customer_purchase_package_price_or_cell_ref=[
                                                CustomerPurchasePackagePriceVersionedChildStructure(
                                                    id='rydt:CPP@Cust777@021',
                                                    version='any',
                                                    amount=Decimal('8.00'),
                                                    pricing_service_ref=PricingServiceRef(
                                                        version='any',
                                                        ref='ryde_pricer'
                                                    )
                                                ),
                                            ]
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            version='any',
                                            ref='rydt:3178672020202'
                                        ),
                                        medium_application_instance_ref=MediumApplicationInstanceRef(
                                            version='any',
                                            ref='rydt:3178672020202@Ryde'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    ),
    version='1.2.2'
)
