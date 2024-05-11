from decimal import Decimal
from netex.models.accepted_driver_permit import AcceptedDriverPermit
from netex.models.accepted_driver_permits_rel_structure import AcceptedDriverPermitsRelStructure
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.account_status_type_enumeration import AccountStatusTypeEnumeration
from netex.models.activation_means_enumeration import ActivationMeansEnumeration
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.battery_equipment import BatteryEquipment
from netex.models.branding import Branding
from netex.models.branding_ref import BrandingRef
from netex.models.car_service_facility_enumeration import CarServiceFacilityEnumeration
from netex.models.car_service_facility_list import CarServiceFacilityList
from netex.models.charging_equipment_profile import ChargingEquipmentProfile
from netex.models.charging_equipment_profile_ref import ChargingEquipmentProfileRef
from netex.models.charging_moment_enumeration import ChargingMomentEnumeration
from netex.models.charging_policy import ChargingPolicy
from netex.models.charging_policy_ref import ChargingPolicyRef
from netex.models.codespace import Codespace
from netex.models.codespace_ref import CodespaceRef
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.composite_frame_ref import CompositeFrameRef
from netex.models.condition_summary import ConditionSummary
from netex.models.contact import Contact
from netex.models.contact_details_structure import ContactDetailsStructure
from netex.models.contact_ref import ContactRef
from netex.models.contact_structure import ContactStructure
from netex.models.contact_type_enumeration import ContactTypeEnumeration
from netex.models.contacts_rel_structure import ContactsRelStructure
from netex.models.coupling_type_enumeration import CouplingTypeEnumeration
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.current_type_enumeration import CurrentTypeEnumeration
from netex.models.customer import Customer
from netex.models.customer_account import CustomerAccount
from netex.models.customer_account_ref import CustomerAccountRef
from netex.models.customer_accounts_rel_structure import CustomerAccountsRelStructure
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
from netex.models.customer_purchase_packages_rel_structure import CustomerPurchasePackagesRelStructure
from netex.models.customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment
from netex.models.customer_purchase_parameter_assignments_rel_structure import CustomerPurchaseParameterAssignmentsRelStructure
from netex.models.customer_ref import CustomerRef
from netex.models.customers_in_frame_rel_structure import CustomersInFrameRelStructure
from netex.models.cycle_model_profile import CycleModelProfile
from netex.models.cycle_model_profile_ref import CycleModelProfileRef
from netex.models.cycle_storage_enumeration import CycleStorageEnumeration
from netex.models.cycle_storage_equipment import CycleStorageEquipment
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.data_role_type_enumeration import DataRoleTypeEnumeration
from netex.models.data_source import DataSource
from netex.models.data_source_ref_structure import DataSourceRefStructure
from netex.models.data_sources_in_frame_rel_structure import DataSourcesInFrameRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.deposit_policy_enumeration import DepositPolicyEnumeration
from netex.models.distribution_assignment import DistributionAssignment
from netex.models.distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from netex.models.distribution_channel import DistributionChannel
from netex.models.distribution_channel_ref import DistributionChannelRef
from netex.models.distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from netex.models.distribution_channels_in_frame_rel_structure import DistributionChannelsInFrameRelStructure
from netex.models.distribution_rights_enumeration import DistributionRightsEnumeration
from netex.models.emv_card_ref import EmvCardRef
from netex.models.entitlement_constraint_structure import EntitlementConstraintStructure
from netex.models.entitlement_required import EntitlementRequired
from netex.models.entitlement_required_ref import EntitlementRequiredRef
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import DayType
from netex.models.entity_in_version_structure import DayTypesRelStructure
from netex.models.entity_in_version_structure import TimebandVersionedChildStructure
from netex.models.entity_in_version_structure import TimebandsRelStructure
from netex.models.entity_in_version_structure import ValidBetween
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.equipment_place import EquipmentPlace
from netex.models.equipment_places_rel_structure import EquipmentPlacesRelStructure
from netex.models.equipments_rel_structure import EquipmentsRelStructure
from netex.models.exterior import Exterior
from netex.models.fare_contract import FareContract
from netex.models.fare_contract_entries_rel_structure import FareContractEntriesRelStructure
from netex.models.fare_contracts_in_frame_rel_structure import FareContractsInFrameRelStructure
from netex.models.fare_contracts_rel_structure import FareContractsRelStructure
from netex.models.fare_frame import FareFrame
from netex.models.fare_frame_ref import FareFrameRef
from netex.models.fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from netex.models.fare_structure_element import FareStructureElement
from netex.models.fare_structure_element_in_sequence import FareStructureElementInSequence
from netex.models.fare_structure_element_ref import FareStructureElementRef
from netex.models.fare_structure_element_refs_rel_structure import FareStructureElementRefsRelStructure
from netex.models.fare_structure_elements_in_sequence_rel_structure import FareStructureElementsInSequenceRelStructure
from netex.models.fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from netex.models.fare_structure_type_enumeration import FareStructureTypeEnumeration
from netex.models.fare_table_specifics_structure import FareTableSpecificsStructure
from netex.models.fare_tables_in_frame_rel_structure import FareTablesInFrameRelStructure
from netex.models.fleet import Fleet
from netex.models.fleet_ref import FleetRef
from netex.models.fleet_refs_rel_structure import FleetRefsRelStructure
from netex.models.fleets_rel_structure import FleetsRelStructure
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.models.fuel_type_enumeration import FuelTypeEnumeration
from netex.models.fulfilment_method import FulfilmentMethod
from netex.models.fulfilment_method_ref import FulfilmentMethodRef
from netex.models.fulfilment_method_type_enumeration import FulfilmentMethodTypeEnumeration
from netex.models.fulfilment_methods_in_frame_rel_structure import FulfilmentMethodsInFrameRelStructure
from netex.models.gated_enumeration import GatedEnumeration
from netex.models.gender_enumeration import GenderEnumeration
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.generic_parameter_assignments_rel_structure import GenericParameterAssignment
from netex.models.generic_parameter_assignments_rel_structure import GenericParameterAssignmentsRelStructure
from netex.models.hire_facility_enumeration import HireFacilityEnumeration
from netex.models.hire_facility_list import HireFacilityList
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.info_link import InfoLink
from netex.models.info_links_rel_structure import InfoLinksRelStructure
from netex.models.layer_ref import LayerRef
from netex.models.licence_requirements_enumeration import LicenceRequirementsEnumeration
from netex.models.lighting_enumeration import LightingEnumeration
from netex.models.linear_ring import LinearRing
from netex.models.location_structure_2 import LocationStructure2
from netex.models.locking_mechanism_enumeration import LockingMechanismEnumeration
from netex.models.logical_operation_enumeration import LogicalOperationEnumeration
from netex.models.machine_readable_enumeration import MachineReadableEnumeration
from netex.models.marked_as_enumeration import MarkedAsEnumeration
from netex.models.media_type_enumeration import MediaTypeEnumeration
from netex.models.medium_access_device_refs_rel_structure import MediumAccessDeviceRefsRelStructure
from netex.models.medium_application_instance_ref import MediumApplicationInstanceRef
from netex.models.mobile_device_ref import MobileDeviceRef
from netex.models.mobility_journey_frame import MobilityJourneyFrame
from netex.models.mobility_service_constraint_zone import MobilityServiceConstraintZone
from netex.models.mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from netex.models.mobility_service_constraint_zones_in_frame_rel_structure import MobilityServiceConstraintZonesInFrameRelStructure
from netex.models.mobility_service_frame import MobilityServiceFrame
from netex.models.mobility_service_frame_ref import MobilityServiceFrameRef
from netex.models.mobility_service_refs_rel_structure import MobilityServiceRefsRelStructure
from netex.models.mobility_services_rel_structure import MobilityServicesRelStructure
from netex.models.modes_of_operation_rel_structure import ModesOfOperationRelStructure
from netex.models.monitored_vehicle_sharing_parking_bay import MonitoredVehicleSharingParkingBay
from netex.models.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.models.multilingual_string import MultilingualString
from netex.models.network_filter_by_value_structure import NetworkFilterByValueStructure
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.object_filter_by_value_structure import ObjectFilterByValueStructure
from netex.models.offered_travel_specification import OfferedTravelSpecification
from netex.models.online_service import OnlineService
from netex.models.online_service_operator import OnlineServiceOperator
from netex.models.online_service_operator_ref import OnlineServiceOperatorRef
from netex.models.online_service_operator_version_structure import OnlineServiceOperatorVersionStructure
from netex.models.online_service_ref import OnlineServiceRef
from netex.models.online_service_refs_rel_structure import OnlineServiceRefsRelStructure
from netex.models.online_services_rel_structure import OnlineServicesRelStructure
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.organisation_role_enumeration import OrganisationRoleEnumeration
from netex.models.organisation_type_enumeration import OrganisationTypeEnumeration
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.parking import Parking
from netex.models.parking_areas_rel_structure import ParkingAreasRelStructure
from netex.models.parking_bay_condition import ParkingBayCondition
from netex.models.parking_bay_status_enumeration import ParkingBayStatusEnumeration
from netex.models.parking_bays_rel_structure import ParkingBaysRelStructure
from netex.models.parking_component_refs_rel_structure import ParkingComponentRefsRelStructure
from netex.models.parking_layout_enumeration import ParkingLayoutEnumeration
from netex.models.parking_log_entries_in_frame_rel_structure import ParkingLogEntriesInFrameRelStructure
from netex.models.parking_properties import ParkingProperties
from netex.models.parking_properties_rel_structure import ParkingPropertiesRelStructure
from netex.models.parking_ref import ParkingRef
from netex.models.parking_type_enumeration import ParkingTypeEnumeration
from netex.models.parking_user_enumeration import ParkingUserEnumeration
from netex.models.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.models.parking_visibility_enumeration import ParkingVisibilityEnumeration
from netex.models.parkings_in_frame_rel_structure import ParkingsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.passenger_capacity_structure import PassengerCapacityStructure
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.place_equipments_rel_structure import PlaceEquipmentsRelStructure
from netex.models.plug_type_enumeration import PlugTypeEnumeration
from netex.models.polygon import Polygon
from netex.models.pool_of_vehicles import PoolOfVehicles
from netex.models.pool_of_vehicles_rel_structure import PoolOfVehiclesRelStructure
from netex.models.pos import Pos
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.preassigned_fare_product_enumeration import PreassignedFareProductEnumeration
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.price_rule_step_result_structure import PriceRuleStepResultStructure
from netex.models.price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from netex.models.priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from netex.models.priceable_object_version_structure import FarePricesRelStructure
from netex.models.priceable_object_version_structure import FareTable
from netex.models.priceable_object_version_structure import FareTablesRelStructure
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.pricing_rule import PricingRule
from netex.models.pricing_rule_ref import PricingRuleRef
from netex.models.pricing_rules_rel_structure import PricingRulesRelStructure
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.propulsion_type_enumeration import PropulsionTypeEnumeration
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.refuelling_equipment import RefuellingEquipment
from netex.models.related_organisation import RelatedOrganisation
from netex.models.related_organisations_rel_structure import RelatedOrganisationsRelStructure
from netex.models.rental_availability import RentalAvailability
from netex.models.rental_penalty_policy import RentalPenaltyPolicy
from netex.models.rental_penalty_policy_ref import RentalPenaltyPolicyRef
from netex.models.rental_penalty_policy_type_enumeration import RentalPenaltyPolicyTypeEnumeration
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.responsibility_role_assignment import ResponsibilityRoleAssignment
from netex.models.responsibility_role_assignments_rel_structure import ResponsibilityRoleAssignmentsRelStructure
from netex.models.responsibility_set import ResponsibilitySet
from netex.models.responsibility_sets_in_frame_rel_structure import ResponsibilitySetsInFrameRelStructure
from netex.models.sale_discount_right import SaleDiscountRight
from netex.models.sale_discount_right_ref import SaleDiscountRightRef
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_element_ref import SalesOfferPackageElementRef
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.sales_transaction import SalesTransaction
from netex.models.sales_transaction_frame import SalesTransactionFrame
from netex.models.sales_transaction_ref import SalesTransactionRef
from netex.models.sales_transaction_refs_rel_structure import SalesTransactionRefsRelStructure
from netex.models.same_user_enumeration import SameUserEnumeration
from netex.models.self_drive_submode import SelfDriveSubmode
from netex.models.self_drive_submode_enumeration import SelfDriveSubmodeEnumeration
from netex.models.service_access_code import ServiceAccessCode
from netex.models.service_access_code_ref import ServiceAccessCodeRef
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.models.shared_usage_enumeration import SharedUsageEnumeration
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.simple_vehicle_category_enumeration import SimpleVehicleCategoryEnumeration
from netex.models.simple_vehicle_type import SimpleVehicleType
from netex.models.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.models.site_facility_set import SiteFacilitySet
from netex.models.site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from netex.models.site_frame import SiteFrame
from netex.models.site_frame_ref import SiteFrameRef
from netex.models.specific_parameter_assignments_rel_structure import SpecificParameterAssignment
from netex.models.specific_parameter_assignments_rel_structure import SpecificParameterAssignmentsRelStructure
from netex.models.staffing import Staffing
from netex.models.staffing_enumeration import StaffingEnumeration
from netex.models.stakeholder_role_type_enumeration import StakeholderRoleTypeEnumeration
from netex.models.submode import Submode
from netex.models.submodes_rel_structure import SubmodesRelStructure
from netex.models.tariff import Tariff
from netex.models.tariff_basis_enumeration import TariffBasisEnumeration
from netex.models.tariff_ref import TariffRef
from netex.models.tariff_zone import TariffZone
from netex.models.tariff_zone_ref import TariffZoneRef
from netex.models.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.telephone_contact_structure import TelephoneContactStructure
from netex.models.ticket_type_enumeration import TicketTypeEnumeration
from netex.models.ticketing_equipment import TicketingEquipment
from netex.models.ticketing_facility_enumeration import TicketingFacilityEnumeration
from netex.models.ticketing_facility_list import TicketingFacilityList
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.ticketing_service_facility_list import TicketingServiceFacilityList
from netex.models.time_interval import TimeInterval
from netex.models.time_interval_price import TimeIntervalPrice
from netex.models.time_interval_price_ref import TimeIntervalPriceRef
from netex.models.time_interval_ref import TimeIntervalRef
from netex.models.time_intervals_rel_structure import TimeIntervalsRelStructure
from netex.models.topographic_place import TopographicPlace
from netex.models.topographic_place_descriptor_versioned_child_structure import TopographicPlaceDescriptorVersionedChildStructure
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.topographic_places_in_frame_rel_structure import TopographicPlacesInFrameRelStructure
from netex.models.transferability import Transferability
from netex.models.transport_organisation_version_structure import TransportOrganisationVersionStructure
from netex.models.transport_type_refs_rel_structure import TransportTypeRefsRelStructure
from netex.models.transport_type_version_structure import TransportTypeVersionStructure
from netex.models.transport_zone_use_enumeration import TransportZoneUseEnumeration
from netex.models.travel_document import TravelDocument
from netex.models.travel_documents_rel_structure import TravelDocumentsRelStructure
from netex.models.travel_specification_summary_endpoint_structure import TravelSpecificationSummaryEndpointStructure
from netex.models.travel_specification_summary_view import TravelSpecificationSummaryView
from netex.models.travel_specifications_rel_structure import TravelSpecificationsRelStructure
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_driver_permit import TypeOfDriverPermit
from netex.models.type_of_driver_permit_ref import TypeOfDriverPermitRef
from netex.models.type_of_equipment import TypeOfEquipment
from netex.models.type_of_equipment_ref import TypeOfEquipmentRef
from netex.models.type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef
from netex.models.type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from netex.models.type_of_info_link_enumeration import TypeOfInfoLinkEnumeration
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.type_of_travel_document_refs_rel_structure import TypeOfTravelDocumentRefsRelStructure
from netex.models.types_of_travel_document_in_frame_rel_structure import TypesOfTravelDocumentInFrameRelStructure
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_end_enumeration import UsageEndEnumeration
from netex.models.usage_parameter_price import UsageParameterPrice
from netex.models.usage_parameter_refs_rel_structure import UsageParameterRefsRelStructure
from netex.models.usage_parameters_rel_structure import UsageParametersRelStructure
from netex.models.usage_start_constraint_type_enumeration import UsageStartConstraintTypeEnumeration
from netex.models.usage_trigger_enumeration import UsageTriggerEnumeration
from netex.models.usage_validity_period import UsageValidityPeriod
from netex.models.usage_validity_type_enumeration import UsageValidityTypeEnumeration
from netex.models.used_in_refs_rel_structure import UsedInRefsRelStructure
from netex.models.user_profile import UserProfile
from netex.models.user_profile_ref import UserProfileRef
from netex.models.user_type_enumeration import UserTypeEnumeration
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_ref import ValidableElementRef
from netex.models.validable_elements_rel_structure import ValidableElementsRelStructure
from netex.models.validity_parameters_rel_structure import ValidityParametersRelStructure
from netex.models.value_set import ValueSet
from netex.models.vehicle import Vehicle
from netex.models.vehicle_access_credential_assignments_rel_structure import VehicleAccessCredentialAssignmentsRelStructure
from netex.models.vehicle_access_credentials_assignment import VehicleAccessCredentialsAssignment
from netex.models.vehicle_access_credentials_assignment_ref import VehicleAccessCredentialsAssignmentRef
from netex.models.vehicle_equipmen_profiles_in_frame_rel_structure import VehicleEquipmenProfilesInFrameRelStructure
from netex.models.vehicle_equipment_profile import VehicleEquipmentProfile
from netex.models.vehicle_equipment_profile_member import VehicleEquipmentProfileMember
from netex.models.vehicle_equipment_profile_members_rel_structure import VehicleEquipmentProfileMembersRelStructure
from netex.models.vehicle_equipment_profile_refs_rel_structure import VehicleEquipmentProfileRefsRelStructure
from netex.models.vehicle_model import VehicleModel
from netex.models.vehicle_model_profiles_in_frame_rel_structure import VehicleModelProfilesInFrameRelStructure
from netex.models.vehicle_model_ref import VehicleModelRef
from netex.models.vehicle_models_in_frame_rel_structure import VehicleModelsInFrameRelStructure
from netex.models.vehicle_ref import VehicleRef
from netex.models.vehicle_refs_rel_structure import VehicleRefsRelStructure
from netex.models.vehicle_release_equipment import VehicleReleaseEquipment
from netex.models.vehicle_service_place_assignments_rel_structure import VehicleServicePlaceAssignmentsRelStructure
from netex.models.vehicle_sharing import VehicleSharing
from netex.models.vehicle_sharing_parking_area import VehicleSharingParkingArea
from netex.models.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from netex.models.vehicle_sharing_place_assignment import VehicleSharingPlaceAssignment
from netex.models.vehicle_sharing_ref import VehicleSharingRef
from netex.models.vehicle_sharing_service import VehicleSharingService
from netex.models.vehicle_sharing_service_ref import VehicleSharingServiceRef
from netex.models.vehicle_sharing_type_enumeration import VehicleSharingTypeEnumeration
from netex.models.vehicle_type_zone_restriction import VehicleTypeZoneRestriction
from netex.models.vehicle_type_zone_restrictions_rel_structure import VehicleTypeZoneRestrictionsRelStructure
from netex.models.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure
from netex.models.vehicles_rel_structure import VehiclesRelStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from netex.models.zone_rule_applicability_enumeration import ZoneRuleApplicabilityEnumeration
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
            value='Request for Metrobike 1 tariff'
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
                                        ref='noc:MBIKE'
                                    ),
                                    VehicleSharingRef(
                                        version='any',
                                        ref='cycle_share'
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
        value='Example of Cycle Sharing schem with prices'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='mb:cycle_sharing_example',
                validity_conditions_or_valid_between=[
                    ValidBetween(
                        from_date=XmlDateTime(2020, 1, 1, 0, 0, 0),
                        to_date=XmlDateTime(2020, 12, 31, 12, 0, 0)
                    ),
                ],
                data_source_ref_attribute='mb:metrobike',
                version='1.0',
                responsibility_set_ref_attribute='mb:tariffs',
                name=MultilingualString(
                    value='Cycle Sharing Example'
                ),
                description=MultilingualString(
                    value='This is an example showing how one might encode a cycle sharings scheme " Metrobike" in NeTEx. It includes some prices.'
                ),
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        CodespaceRef(
                            ref='mb_data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='mb_data'
                    ),
                    default_data_source_ref=DataSourceRefStructure(
                        version='1.0',
                        ref='mb:metrobike'
                    ),
                    default_currency='EUR'
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ResourceFrame(
                            id='mb:cycle_sharing_example',
                            version='1.0',
                            responsibility_set_ref_attribute='mb:network_data',
                            name=MultilingualString(
                                value='Metrobike Operator specific common resources'
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    Codespace(
                                        id='mb_data',
                                        xmlns='mb',
                                        xmlns_url='http://www.metrobike.eu/',
                                        description='Metrobike data'
                                    ),
                                ]
                            ),
                            data_sources=DataSourcesInFrameRelStructure(
                                data_source=[
                                    DataSource(
                                        id='mb:metrobike',
                                        version='1.0',
                                        email='feedback@metrobike.eu'
                                    ),
                                ]
                            ),
                            responsibility_sets=ResponsibilitySetsInFrameRelStructure(
                                responsibility_set=[
                                    ResponsibilitySet(
                                        id='mb:tariffs',
                                        version='any',
                                        name=MultilingualString(
                                            value='Operator Tariffs'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='mb:tariff_data@creates',
                                                    version='any',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.CREATES,
                                                    ],
                                                    stakeholder_role_type=[
                                                        StakeholderRoleTypeEnumeration.FARE_MANAGEMENT,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        value='Metrobike',
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ResponsibilitySet(
                                        id='mb:network_data',
                                        version='any',
                                        name=MultilingualString(
                                            value='Operator data'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='mb:network_data@creates',
                                                    version='any',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.CREATES,
                                                    ],
                                                    stakeholder_role_type=[
                                                        StakeholderRoleTypeEnumeration.PLANNING,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        value='Metrobike',
                                                        version='any',
                                                        ref='noc:MBIKE'
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
                                        id='AllBranding',
                                        version='any',
                                        name=MultilingualString(
                                            value='Velo sailor'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                Branding(
                                                    id='myBrand',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Metrobike'
                                                    ),
                                                    url='https://www.metrobike.eu/static/images/colorways/metrobike/logo.png'
                                                ),
                                            ]
                                        ),
                                        class_of_values='Branding'
                                    ),
                                    ValueSet(
                                        id='BikeEquip',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bike equipment'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfEquipment(
                                                    id='battery',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Battery'
                                                    )
                                                ),
                                                TypeOfEquipment(
                                                    id='charger',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Charger'
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='TypeOfEquipment'
                                    ),
                                    ValueSet(
                                        id='DriverPermits',
                                        version='any',
                                        name=MultilingualString(
                                            value='Driving licence types'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfDriverPermit(
                                                    id='ecycle_permit',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='ecycle'
                                                    )
                                                ),
                                                TypeOfDriverPermit(
                                                    id='car_permit',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='car'
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='TypeOfDriverPermit'
                                    ),
                                ]
                            ),
                            contacts=ContactsRelStructure(
                                contact=Contact(
                                    id='mbike',
                                    version='any',
                                    contact_details=ContactDetailsStructure(
                                        email='info@metrobike.eu',
                                        phone='+32 1293 449191'
                                    ),
                                    contact_type=ContactTypeEnumeration.INFORMATION
                                )
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    Operator(
                                        id='noc:MBIKE',
                                        version='any',
                                        public_code=PrivateCodeStructure(
                                            value='MBK'
                                        ),
                                        name=MultilingualString(
                                            value='Metrobike'
                                        ),
                                        short_name=MultilingualString(
                                            value='Metrobike'
                                        ),
                                        trading_name=MultilingualString(
                                            value='Metrobike SA'
                                        ),
                                        contact_details=ContactStructure(
                                            contact_ref=ContactRef(
                                                version='any',
                                                ref='mbike'
                                            )
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.OPERATOR,
                                        ],
                                        related_organisations=RelatedOrganisationsRelStructure(
                                            related_organisation=[
                                                RelatedOrganisation(
                                                    id='noc:MBIKE',
                                                    version='any',
                                                    organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                                        version='any',
                                                        ref='floggit'
                                                    ),
                                                    organisation_role_type=OrganisationRoleEnumeration.DISTRIBUTOR
                                                ),
                                            ]
                                        ),
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
                                            value=SelfDriveSubmodeEnumeration.HIRE_CYCLE
                                        ),
                                        mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=VehicleSharingRef(
                                            version='any',
                                            ref='cycle_share'
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
                                    VehicleSharing(
                                        id='cycle_share',
                                        version='any',
                                        name=MultilingualString(
                                            value='Cycle Hire'
                                        ),
                                        description=MultilingualString(
                                            value='Cycles available from fixed stations charge per hour'
                                        ),
                                        submodes=SubmodesRelStructure(
                                            submode=[
                                                Submode(
                                                    id='cycle_share',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.SELF_DRIVE,
                                                    choice=SelfDriveSubmode(
                                                        value=SelfDriveSubmodeEnumeration.HIRE_CYCLE
                                                    )
                                                ),
                                            ]
                                        ),
                                        vehicle_sharing_type=VehicleSharingTypeEnumeration.VEHICLE_SHARING
                                    ),
                                ]
                            ),
                            vehicle_types=VehicleTypesInFrameRelStructure(
                                choice=[
                                    SimpleVehicleType(
                                        id='pedal_cycle',
                                        version='any',
                                        name=MultilingualString(
                                            value='Pedal cycle'
                                        ),
                                        reversing_direction=False,
                                        self_propelled=False,
                                        propulsion_type=PropulsionTypeEnumeration.HUMAN,
                                        fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(
                                            value=FuelTypeEnumeration.NONE
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.SELF_DRIVE,
                                        passenger_capacity=PassengerCapacityStructure(
                                            id='pedal_cycle',
                                            version='any',
                                            seating_capacity=1
                                        ),
                                        length=Decimal('2'),
                                        height=Decimal('1.6'),
                                        weight=Decimal('40'),
                                        licence_requirements=LicenceRequirementsEnumeration.NONE,
                                        vehicle_category=SimpleVehicleCategoryEnumeration.CYCLE,
                                        minimum_age=14
                                    ),
                                    SimpleVehicleType(
                                        id='electric_cycle',
                                        version='any',
                                        name=MultilingualString(
                                            value='Electric cycle'
                                        ),
                                        reversing_direction=False,
                                        self_propelled=True,
                                        propulsion_type=PropulsionTypeEnumeration.ELECTRIC_ASSIST,
                                        fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(
                                            value=FuelTypeEnumeration.BATTERY
                                        ),
                                        maximum_range=Decimal('15'),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.SELF_DRIVE,
                                        passenger_capacity=PassengerCapacityStructure(
                                            id='electric_cycle',
                                            version='any',
                                            seating_capacity=1
                                        ),
                                        length=Decimal('2.2'),
                                        height=Decimal('1.5'),
                                        weight=Decimal('60'),
                                        licence_requirements=LicenceRequirementsEnumeration.NONE,
                                        vehicle_category=SimpleVehicleCategoryEnumeration.CYCLE,
                                        minimum_age=14,
                                        accepted_driver_permits=AcceptedDriverPermitsRelStructure(
                                            accepted_driver_permit=[
                                                AcceptedDriverPermit(
                                                    id='electric_cycle@scooter',
                                                    version='any',
                                                    type_of_driver_permit_ref=TypeOfDriverPermitRef(
                                                        version='any',
                                                        ref='ecycle_permit'
                                                    )
                                                ),
                                                AcceptedDriverPermit(
                                                    id='electric_cycle@car',
                                                    version='any',
                                                    type_of_driver_permit_ref=TypeOfDriverPermitRef(
                                                        version='any',
                                                        ref='car_permit'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            vehicle_models=VehicleModelsInFrameRelStructure(
                                vehicle_model=[
                                    VehicleModel(
                                        id='penny_farthing',
                                        version='any',
                                        name=MultilingualString(
                                            value='Old Model Bike'
                                        ),
                                        transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                            version='any',
                                            ref='pedal_cycle'
                                        ),
                                        vehicle_model_profile_ref=CycleModelProfileRef(
                                            version='any',
                                            ref='boneKitA'
                                        )
                                    ),
                                    VehicleModel(
                                        id='boneShaker',
                                        version='any',
                                        name=MultilingualString(
                                            value='New Model Bike'
                                        ),
                                        transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                            version='any',
                                            ref='pedal_cycle'
                                        ),
                                        vehicle_model_profile_ref=CycleModelProfileRef(
                                            version='any',
                                            ref='boneKitA'
                                        )
                                    ),
                                    VehicleModel(
                                        id='electric_boneshaker',
                                        version='any',
                                        name=MultilingualString(
                                            value='New Model Bike v2'
                                        ),
                                        transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                            version='any',
                                            ref='electric_cycle'
                                        ),
                                        equipment_profiles=VehicleEquipmentProfileRefsRelStructure(
                                            vehicle_equipment_profile_ref=[
                                                ChargingEquipmentProfileRef(
                                                    version='any',
                                                    ref='ebike_charging'
                                                ),
                                            ]
                                        ),
                                        vehicle_model_profile_ref=CycleModelProfileRef(
                                            version='any',
                                            ref='boneKitB'
                                        )
                                    ),
                                ]
                            ),
                            vehicle_equipment_profiles=VehicleEquipmenProfilesInFrameRelStructure(
                                vehicle_equipment_profile_or_charging_equipment_profile=[
                                    VehicleEquipmentProfile(
                                        id='ebike',
                                        version='any',
                                        units=2,
                                        vehicle_equipment_profile_members=VehicleEquipmentProfileMembersRelStructure(
                                            vehicle_equipment_profile_member=[
                                                VehicleEquipmentProfileMember(
                                                    id='ebike@battery',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Batteries'
                                                    ),
                                                    minimum_units=2,
                                                    type_of_equipment_ref=TypeOfEquipmentRef(
                                                        version='any',
                                                        ref='battery'
                                                    )
                                                ),
                                                VehicleEquipmentProfileMember(
                                                    id='ebike@charger',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Charger'
                                                    ),
                                                    minimum_units=1,
                                                    type_of_equipment_ref=TypeOfEquipmentRef(
                                                        version='any',
                                                        ref='charger'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ChargingEquipmentProfile(
                                        id='ebike_charging',
                                        version='any',
                                        coupling_type=CouplingTypeEnumeration.PLUG,
                                        plug_type=PlugTypeEnumeration.TYPE2,
                                        current_type=CurrentTypeEnumeration.VALUE_1_PHASE_AC,
                                        maximum_charging_power=Decimal('240'),
                                        preparation_duration=XmlDuration("PT1M"),
                                        finalisation_duration=XmlDuration("PT1M")
                                    ),
                                ]
                            ),
                            vehicle_model_profiles=VehicleModelProfilesInFrameRelStructure(
                                car_model_profile_or_cycle_model_profile=[
                                    CycleModelProfile(
                                        id='boneKitA',
                                        version='any',
                                        battery=False,
                                        lamps=True,
                                        helmet=False,
                                        pump=False,
                                        locker=False,
                                        basket=False,
                                        lock=True
                                    ),
                                    CycleModelProfile(
                                        id='boneKitB',
                                        version='any',
                                        battery=False,
                                        lamps=True,
                                        helmet=False,
                                        pump=False,
                                        locker=False,
                                        basket=True,
                                        lock=True
                                    ),
                                    CycleModelProfile(
                                        id='ebike',
                                        version='any',
                                        battery=True,
                                        lamps=True,
                                        helmet=False,
                                        pump=False,
                                        locker=False,
                                        basket=True,
                                        lock=True
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='mb:cycle_sharing_example',
                            version='1.0',
                            responsibility_set_ref_attribute='mb:network_data',
                            name=MultilingualString(
                                value='Network data used by Metrobike 1'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='mb:cycle_sharing_example'
                                    ),
                                ]
                            ),
                            topographic_places=TopographicPlacesInFrameRelStructure(
                                topographic_place=[
                                    TopographicPlace(
                                        id='Alphaville',
                                        version='any',
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal('1.35250'),
                                                latitude=Decimal('52.44692'),
                                                pos=Pos(
                                                    value=[
                                                        376748.0,
                                                        167119.0,
                                                    ],
                                                    srs_name='UKOS'
                                                ),
                                                id='Alphaville'
                                            )
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='Alphaville'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            parkings=ParkingsInFrameRelStructure(
                                parking=[
                                    Parking(
                                        id='bike_station_alpha',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bike Station Alpha',
                                            lang='en'
                                        ),
                                        info_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='http:metrobike.eu/ios/bike_station_alpha',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.INFO,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='http:metrobike.eu/android/bike_station_alpha',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.INFO,
                                                    ],
                                                    target_platform='android'
                                                ),
                                                InfoLink(
                                                    value='http:metrobike.eu/web/bike_station_alpha',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.INFO,
                                                    ],
                                                    target_platform='eb'
                                                ),
                                            ]
                                        ),
                                        cross_road=MultilingualString(
                                            value='Main Street'
                                        ),
                                        landmark=MultilingualString(
                                            value='Main Railway Station'
                                        ),
                                        covered=CoveredEnumeration.COVERED,
                                        gated=GatedEnumeration.OPEN_AREA,
                                        lighting=LightingEnumeration.WELL_LIT,
                                        facilities=SiteFacilitySetsRelStructure(
                                            site_facility_set_ref_or_site_facility_set=[
                                                SiteFacilitySet(
                                                    id='bike_station_alpha',
                                                    version='any',
                                                    car_service_facility_list=CarServiceFacilityList(
                                                        value=[
                                                            CarServiceFacilityEnumeration.VALET_PARKING,
                                                        ]
                                                    ),
                                                    ticketing_service_facility_list=TicketingServiceFacilityList(
                                                        value=[
                                                            TicketingServiceFacilityEnumeration.PURCHASE,
                                                        ]
                                                    ),
                                                    hire_facility_list=HireFacilityList(
                                                        value=[
                                                            HireFacilityEnumeration.CYCLE_HIRE,
                                                        ]
                                                    ),
                                                    staffing=Staffing(
                                                        value=StaffingEnumeration.PART_TIME
                                                    )
                                                ),
                                            ]
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='Alphaville'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
                                        ),
                                        parking_type=ParkingTypeEnumeration.CYCLE_RENTAL,
                                        parking_vehicle_types=[
                                            ParkingVehicleEnumeration.PEDAL_CYCLE,
                                        ],
                                        vehicle_types=TransportTypeRefsRelStructure(
                                            transport_type_ref_or_vehicle_type_ref=[
                                                SimpleVehicleTypeRef(
                                                    version='any',
                                                    ref='pedal_cycle'
                                                ),
                                            ]
                                        ),
                                        parking_areas=ParkingAreasRelStructure(
                                            parking_area_ref_or_parking_area=[
                                                VehicleSharingParkingArea(
                                                    id='bike_station_alpha_A1',
                                                    version='any',
                                                    equipment_places=EquipmentPlacesRelStructure(
                                                        equipment_place_ref_or_equipment_place=[
                                                            EquipmentPlace(
                                                                id='bike_station_alpha_A1@rack',
                                                                version='any'
                                                            ),
                                                        ]
                                                    ),
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            VehicleReleaseEquipment(
                                                                id='bike_station_alpha_A1@rack',
                                                                version='any',
                                                                local_control=True,
                                                                locking_mechanism=LockingMechanismEnumeration.DOCK
                                                            ),
                                                            CycleStorageEquipment(
                                                                id='bike_station_alpha_A1@rack',
                                                                version='any',
                                                                number_of_spaces=10,
                                                                cycle_storage_type=CycleStorageEnumeration.DOCKS
                                                            ),
                                                            TicketingEquipment(
                                                                id='bike_station_alpha',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Ticket Machine s at Bike Station Alpha'
                                                                ),
                                                                ticket_machines=True,
                                                                number_of_machines=2,
                                                                ticketing_facility_list=TicketingFacilityList(
                                                                    value=[
                                                                        TicketingFacilityEnumeration.TICKET_MACHINES,
                                                                    ]
                                                                ),
                                                                payment_methods=[
                                                                    PaymentMethodEnumeration.DEBIT_CARD,
                                                                    PaymentMethodEnumeration.CREDIT_CARD,
                                                                    PaymentMethodEnumeration.CONTACTLESS_PAYMENT_CARD,
                                                                    PaymentMethodEnumeration.EPAY_DEVICE,
                                                                    PaymentMethodEnumeration.EPAY_ACCOUNT,
                                                                ],
                                                                ticket_types_available=[
                                                                    TicketTypeEnumeration.STANDARD,
                                                                ]
                                                            ),
                                                        ]
                                                    ),
                                                    total_capacity=10,
                                                    bays=ParkingBaysRelStructure(
                                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref_or_parking_bay=[
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@01',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@02',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@03',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@04',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@05',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@06',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@07',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@08',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@09',
                                                                version='any',
                                                                place_equipments=PlaceEquipmentsRelStructure(
                                                                    choice=[
                                                                        VehicleReleaseEquipment(
                                                                            id='bike_station_alpha_A109',
                                                                            version='any',
                                                                            local_control=True,
                                                                            locking_mechanism=LockingMechanismEnumeration.DOCK
                                                                        ),
                                                                        RefuellingEquipment(
                                                                            id='bike_station_alpha_A1@09',
                                                                            version='any',
                                                                            fuel_type=FuelTypeEnumeration.ELECTRICITY
                                                                        ),
                                                                    ]
                                                                ),
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE,
                                                                transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                                    version='any',
                                                                    ref='electric_cycle'
                                                                ),
                                                                recharging_available=True
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_alpha_A1@10',
                                                                version='any',
                                                                equipment_places=EquipmentPlacesRelStructure(
                                                                    equipment_place_ref_or_equipment_place=[
                                                                        EquipmentPlace(
                                                                            id='bike_station_alpha_A1@10',
                                                                            version='any'
                                                                        ),
                                                                    ]
                                                                ),
                                                                place_equipments=PlaceEquipmentsRelStructure(
                                                                    choice=[
                                                                        VehicleReleaseEquipment(
                                                                            id='bike_station_alpha_A1k@10',
                                                                            version='any',
                                                                            local_control=True,
                                                                            locking_mechanism=LockingMechanismEnumeration.DOCK
                                                                        ),
                                                                        RefuellingEquipment(
                                                                            id='bike_station_alpha_A1@10',
                                                                            version='any',
                                                                            fuel_type=FuelTypeEnumeration.ELECTRICITY
                                                                        ),
                                                                    ]
                                                                ),
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE,
                                                                transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                                    version='any',
                                                                    ref='electric_cycle'
                                                                ),
                                                                recharging_available=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    Parking(
                                        id='bike_station_beta',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bike Station Beta',
                                            lang='en'
                                        ),
                                        cross_road=MultilingualString(
                                            value='Main Street'
                                        ),
                                        landmark=MultilingualString(
                                            value='Town Hall'
                                        ),
                                        covered=CoveredEnumeration.OUTDOORS,
                                        facilities=SiteFacilitySetsRelStructure(
                                            site_facility_set_ref_or_site_facility_set=[
                                                SiteFacilitySet(
                                                    id='bike_station_beta',
                                                    version='any',
                                                    ticketing_service_facility_list=TicketingServiceFacilityList(
                                                        value=[
                                                            TicketingServiceFacilityEnumeration.PURCHASE,
                                                        ]
                                                    ),
                                                    hire_facility_list=HireFacilityList(
                                                        value=[
                                                            HireFacilityEnumeration.CYCLE_HIRE,
                                                        ]
                                                    ),
                                                    staffing=Staffing(
                                                        value=StaffingEnumeration.UNMANNED
                                                    )
                                                ),
                                            ]
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='Alphaville'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
                                        ),
                                        parking_type=ParkingTypeEnumeration.CYCLE_RENTAL,
                                        parking_vehicle_types=[
                                            ParkingVehicleEnumeration.PEDAL_CYCLE,
                                        ],
                                        vehicle_types=TransportTypeRefsRelStructure(
                                            transport_type_ref_or_vehicle_type_ref=[
                                                SimpleVehicleTypeRef(
                                                    version='any',
                                                    ref='pedal_cycle'
                                                ),
                                            ]
                                        ),
                                        parking_layout=ParkingLayoutEnumeration.ON_PAVEMENT,
                                        total_capacity=5,
                                        parking_properties=ParkingPropertiesRelStructure(
                                            parking_properties=[
                                                ParkingProperties(
                                                    id='bike_station_beta',
                                                    version='any',
                                                    parking_user_types=[
                                                        ParkingUserEnumeration.RENTAL,
                                                    ],
                                                    parking_vehicle_types=[
                                                        ParkingVehicleEnumeration.PEDAL_CYCLE,
                                                    ],
                                                    parking_visibility=ParkingVisibilityEnumeration.DOCKS
                                                ),
                                            ]
                                        ),
                                        parking_areas=ParkingAreasRelStructure(
                                            parking_area_ref_or_parking_area=[
                                                VehicleSharingParkingArea(
                                                    id='bike_station_beta_B1',
                                                    version='any',
                                                    equipment_places=EquipmentPlacesRelStructure(
                                                        equipment_place_ref_or_equipment_place=[
                                                            EquipmentPlace(
                                                                id='bike_station_beta_B1@rack',
                                                                version='any'
                                                            ),
                                                        ]
                                                    ),
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            CycleStorageEquipment(
                                                                id='bike_station_beta_B1@rack',
                                                                version='any',
                                                                number_of_spaces=10,
                                                                cycle_storage_type=CycleStorageEnumeration.DOCKS
                                                            ),
                                                            TicketingEquipment(
                                                                id='bike_station_beta_B1@rack',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Ticket Machine at Bike Station Beta'
                                                                ),
                                                                ticket_machines=True,
                                                                number_of_machines=1,
                                                                ticketing_facility_list=TicketingFacilityList(
                                                                    value=[
                                                                        TicketingFacilityEnumeration.TICKET_MACHINES,
                                                                    ]
                                                                ),
                                                                payment_methods=[
                                                                    PaymentMethodEnumeration.DEBIT_CARD,
                                                                    PaymentMethodEnumeration.CREDIT_CARD,
                                                                    PaymentMethodEnumeration.CONTACTLESS_PAYMENT_CARD,
                                                                ],
                                                                ticket_types_available=[
                                                                    TicketTypeEnumeration.STANDARD,
                                                                ]
                                                            ),
                                                        ]
                                                    ),
                                                    total_capacity=5,
                                                    bays=ParkingBaysRelStructure(
                                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref_or_parking_bay=[
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_beta_B1@01',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_beta_B1@02',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_beta_B1@03',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_beta_B1@04',
                                                                version='any',
                                                                place_equipments=PlaceEquipmentsRelStructure(
                                                                    choice=[
                                                                        VehicleReleaseEquipment(
                                                                            id='bike_station_beta_B1@04',
                                                                            version='any',
                                                                            local_control=True,
                                                                            locking_mechanism=LockingMechanismEnumeration.DOCK
                                                                        ),
                                                                        RefuellingEquipment(
                                                                            id='bike_station_beta_B1@04',
                                                                            version='any',
                                                                            fuel_type=FuelTypeEnumeration.ELECTRICITY
                                                                        ),
                                                                    ]
                                                                ),
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE,
                                                                transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                                    version='any',
                                                                    ref='electric_cycle'
                                                                ),
                                                                recharging_available=True
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='bike_station_beta_B1@05',
                                                                version='any',
                                                                place_equipments=PlaceEquipmentsRelStructure(
                                                                    choice=[
                                                                        VehicleReleaseEquipment(
                                                                            id='bike_station_beta_B1@05',
                                                                            version='any',
                                                                            local_control=True,
                                                                            locking_mechanism=LockingMechanismEnumeration.DOCK
                                                                        ),
                                                                        RefuellingEquipment(
                                                                            id='bike_station_beta_B1@05',
                                                                            version='any',
                                                                            fuel_type=FuelTypeEnumeration.ELECTRICITY
                                                                        ),
                                                                    ]
                                                                ),
                                                                parking_vehicle_type=ParkingVehicleEnumeration.PEDAL_CYCLE,
                                                                transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                                    version='any',
                                                                    ref='electric_cycle'
                                                                ),
                                                                recharging_available=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    Parking(
                                        id='bike_station_omega',
                                        version='any',
                                        name=MultilingualString(
                                            value='Virtual bike station',
                                            lang='en'
                                        ),
                                        cross_road=MultilingualString(
                                            value='Union Street'
                                        ),
                                        landmark=MultilingualString(
                                            value='University'
                                        ),
                                        covered=CoveredEnumeration.OUTDOORS,
                                        facilities=SiteFacilitySetsRelStructure(
                                            site_facility_set_ref_or_site_facility_set=[
                                                SiteFacilitySet(
                                                    id='bike_station_omega',
                                                    version='any',
                                                    hire_facility_list=HireFacilityList(
                                                        value=[
                                                            HireFacilityEnumeration.CYCLE_HIRE,
                                                        ]
                                                    ),
                                                    staffing=Staffing(
                                                        value=StaffingEnumeration.UNMANNED
                                                    )
                                                ),
                                            ]
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='Alphaville'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
                                        ),
                                        parking_type=ParkingTypeEnumeration.CYCLE_RENTAL,
                                        parking_layout=ParkingLayoutEnumeration.CYCLE_HIRE,
                                        parking_properties=ParkingPropertiesRelStructure(
                                            parking_properties=[
                                                ParkingProperties(
                                                    id='bike_station_omega',
                                                    version='any',
                                                    parking_vehicle_types=[
                                                        ParkingVehicleEnumeration.CYCLE,
                                                        ParkingVehicleEnumeration.E_CYCLE,
                                                    ],
                                                    parking_visibility=ParkingVisibilityEnumeration.UNMARKED
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            tariff_zones=TariffZonesInFrameRelStructure(
                                tariff_zone=[
                                    TariffZone(
                                        id='all_metropolis',
                                        version='any',
                                        name=MultilingualString(
                                            value='All Metropolis',
                                            lang='en'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='mb:cycle_sharing_example',
                            version='1.0',
                            responsibility_set_ref_attribute='mb:network_data',
                            name=MultilingualString(
                                value='Day Type devinitions'
                            ),
                            service_calendar=ServiceCalendar(
                                id='cycle_sharing_example',
                                version='any',
                                day_types=DayTypesRelStructure(
                                    day_type_ref_or_day_type=[
                                        DayType(
                                            id='working_day',
                                            version='any',
                                            name=MultilingualString(
                                                value='Working Day'
                                            ),
                                            properties=PropertiesOfDayRelStructure(
                                                property_of_day=[
                                                    PropertyOfDay(
                                                        days_of_week=[
                                                            DayOfWeekEnumeration.WEEKDAYS,
                                                        ],
                                                        holiday_types=[
                                                            HolidayTypeEnumeration.WORKING_DAY,
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                )
                            )
                        ),
                        MobilityServiceFrame(
                            id='mb:cycle_sharing_example',
                            version='1.0',
                            responsibility_set_ref_attribute='mb:network_data',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='mb:cycle_sharing_example'
                                    ),
                                    ServiceCalendarFrameRef(
                                        version='1.0',
                                        ref='mb:cycle_sharing_example'
                                    ),
                                ]
                            ),
                            fleets=FleetsRelStructure(
                                fleet=[
                                    Fleet(
                                        id='metrobike_fleet',
                                        version='any',
                                        name=MultilingualString(
                                            value='The metrobike fleet'
                                        ),
                                        members=VehiclesRelStructure(
                                            vehicle_ref_or_vehicle=[
                                                Vehicle(
                                                    id='P01',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='penny_farthing'
                                                    ),
                                                    actual_vehicle_equipments=EquipmentsRelStructure(
                                                        choice=[
                                                            VehicleReleaseEquipment(
                                                                id='P01@release',
                                                                version='any',
                                                                out_of_service=False,
                                                                remote_control=True,
                                                                local_control=True,
                                                                locking_mechanism=LockingMechanismEnumeration.IMMOBILISING_LOCK
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                Vehicle(
                                                    id='P02',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='penny_farthing'
                                                    ),
                                                    actual_vehicle_equipments=EquipmentsRelStructure(
                                                        choice=[
                                                            VehicleReleaseEquipment(
                                                                id='P02@release',
                                                                version='any',
                                                                out_of_service=False,
                                                                remote_control=False,
                                                                local_control=True,
                                                                locking_mechanism=LockingMechanismEnumeration.DOCK
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                Vehicle(
                                                    id='P03',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='penny_farthing'
                                                    ),
                                                    actual_vehicle_equipments=EquipmentsRelStructure(
                                                        choice=[
                                                            VehicleReleaseEquipment(
                                                                id='P03@release',
                                                                version='any',
                                                                out_of_service=True,
                                                                remote_control=True,
                                                                local_control=False,
                                                                locking_mechanism=LockingMechanismEnumeration.DOCK
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                Vehicle(
                                                    id='P04',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='penny_farthing'
                                                    )
                                                ),
                                                Vehicle(
                                                    id='B01',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='boneShaker'
                                                    )
                                                ),
                                                Vehicle(
                                                    id='N02',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='boneShaker'
                                                    )
                                                ),
                                                Vehicle(
                                                    id='B03',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='boneShaker'
                                                    )
                                                ),
                                                Vehicle(
                                                    id='B04',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='boneShaker'
                                                    )
                                                ),
                                                Vehicle(
                                                    id='B05',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='boneShaker'
                                                    )
                                                ),
                                                Vehicle(
                                                    id='C01',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='electric_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='electric_boneshaker'
                                                    ),
                                                    actual_vehicle_equipments=EquipmentsRelStructure(
                                                        choice=[
                                                            BatteryEquipment(
                                                                id='C01_battery_1',
                                                                version='any',
                                                                type_of_equipment_ref=TypeOfEquipmentRef(
                                                                    version='any',
                                                                    ref='battery'
                                                                ),
                                                                battery_capacity=Decimal('1000'),
                                                                maximum_charging_power=Decimal('240')
                                                            ),
                                                            BatteryEquipment(
                                                                id='C01_battery_2',
                                                                version='any',
                                                                type_of_equipment_ref=TypeOfEquipmentRef(
                                                                    version='any',
                                                                    ref='battery'
                                                                ),
                                                                battery_capacity=Decimal('1000'),
                                                                maximum_charging_power=Decimal('240')
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                Vehicle(
                                                    id='C02',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='electric_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='electric_boneshaker'
                                                    ),
                                                    actual_vehicle_equipments=EquipmentsRelStructure(
                                                        choice=[
                                                            BatteryEquipment(
                                                                id='C02_battery_1',
                                                                version='any',
                                                                type_of_equipment_ref=TypeOfEquipmentRef(
                                                                    version='any',
                                                                    ref='battery'
                                                                ),
                                                                battery_capacity=Decimal('1000'),
                                                                maximum_charging_power=Decimal('240')
                                                            ),
                                                            BatteryEquipment(
                                                                id='C02_battery_2',
                                                                version='any',
                                                                type_of_equipment_ref=TypeOfEquipmentRef(
                                                                    version='any',
                                                                    ref='battery'
                                                                ),
                                                                battery_capacity=Decimal('1000'),
                                                                maximum_charging_power=Decimal('240')
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                Vehicle(
                                                    id='C03',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:MBIKE'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='electric_cycle'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='electric_boneshaker'
                                                    ),
                                                    actual_vehicle_equipments=EquipmentsRelStructure(
                                                        choice=[
                                                            BatteryEquipment(
                                                                id='C03_battery_1',
                                                                version='any',
                                                                type_of_equipment_ref=TypeOfEquipmentRef(
                                                                    version='any',
                                                                    ref='battery'
                                                                ),
                                                                battery_capacity=Decimal('1000'),
                                                                maximum_charging_power=Decimal('240')
                                                            ),
                                                            BatteryEquipment(
                                                                id='C03_battery_2',
                                                                version='any',
                                                                type_of_equipment_ref=TypeOfEquipmentRef(
                                                                    version='any',
                                                                    ref='battery'
                                                                ),
                                                                battery_capacity=Decimal('1000'),
                                                                maximum_charging_power=Decimal('240')
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            pools_of_vehicles=PoolOfVehiclesRelStructure(
                                pool_of_vehicles=[
                                    PoolOfVehicles(
                                        id='metrobike_pool_1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Restricted Pool -zone'
                                        ),
                                        mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        mobility_service_constraint_zone_ref=MobilityServiceConstraintZoneRef(
                                            version='any',
                                            ref='bring_back_to_zone'
                                        ),
                                        vehicles=VehicleRefsRelStructure(
                                            vehicle_ref=[
                                                VehicleRef(
                                                    version='any',
                                                    ref='B01'
                                                ),
                                                VehicleRef(
                                                    version='any',
                                                    ref='B03'
                                                ),
                                                VehicleRef(
                                                    version='any',
                                                    ref='B05'
                                                ),
                                            ]
                                        )
                                    ),
                                    PoolOfVehicles(
                                        id='metrobike_pool_2',
                                        version='any',
                                        name=MultilingualString(
                                            value='Restricted Pool - parking'
                                        ),
                                        mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        parking_ref=ParkingRef(
                                            version='any',
                                            ref='bike_station_beta'
                                        ),
                                        parking_components=ParkingComponentRefsRelStructure(
                                            parking_area_ref_or_parking_bay_ref_or_vehicle_sharing_parking_bay_ref=[
                                                VehicleSharingParkingAreaRef(
                                                    version='any',
                                                    ref='bike_station_beta_B1'
                                                ),
                                            ]
                                        ),
                                        vehicles=VehicleRefsRelStructure(
                                            vehicle_ref=[
                                                VehicleRef(
                                                    version='any',
                                                    ref='P03'
                                                ),
                                                VehicleRef(
                                                    version='any',
                                                    ref='P04'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            mobility_services=MobilityServicesRelStructure(
                                mobility_service_or_common_vehicle_service_or_vehicle_pooling_service=[
                                    VehicleSharingService(
                                        id='metrobike',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Metro Bike Cycle share scheme'
                                        ),
                                        info_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='http:metrobike.eu/info',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.INFO,
                                                    ]
                                                ),
                                                InfoLink(
                                                    value='http:metrobike.eu/ios',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='http:metrobike.eu/android',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='android'
                                                ),
                                                InfoLink(
                                                    value='http:metrobike.eu/ios',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='http:metrobike.eu/android',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='android'
                                                ),
                                            ]
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
                                        ),
                                        booking_required=False,
                                        registration_required=False,
                                        proposed_by_services=OnlineServiceRefsRelStructure(
                                            online_service_ref=[
                                                OnlineServiceRef(
                                                    version='any',
                                                    ref='metrobike_online'
                                                ),
                                            ]
                                        ),
                                        vehicle_sharing_ref=VehicleSharingRef(
                                            version='any',
                                            ref='cycle_share'
                                        ),
                                        sharing_policy_url='http:metrobike.eu/policy',
                                        minimum_sharing_period=XmlDuration("PT30M"),
                                        maximum_sharing_period=XmlDuration("PT24H"),
                                        fleets=FleetRefsRelStructure(
                                            fleet_ref=[
                                                FleetRef(
                                                    version='any',
                                                    ref='metrobike_fleet'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            online_services=OnlineServicesRelStructure(
                                online_service=[
                                    OnlineService(
                                        id='metrobike_online',
                                        version='any',
                                        name=MultilingualString(
                                            value='Online registration for metrobike'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        ),
                                        proposing_services=MobilityServiceRefsRelStructure(
                                            mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref=[
                                                VehicleSharingServiceRef(
                                                    version='any',
                                                    ref='metrobike'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            vehicle_meeting_place_assignments=VehicleServicePlaceAssignmentsRelStructure(
                                vehicle_sharing_place_assignment_or_vehicle_pooling_place_assignment_or_taxi_service_place_assignment=[
                                    VehicleSharingPlaceAssignment(
                                        id='metrobik@bike_station_alpha_A1@rack',
                                        version='any',
                                        order=1,
                                        common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        vehicle_sharing_parking_area_ref=VehicleSharingParkingAreaRef(
                                            version='any',
                                            ref='bike_station_alpha_A1'
                                        )
                                    ),
                                    VehicleSharingPlaceAssignment(
                                        id='bike_station_beta',
                                        version='any',
                                        order=1,
                                        common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        vehicle_sharing_parking_area_ref=VehicleSharingParkingAreaRef(
                                            version='any',
                                            ref='bike_station_beta_B1'
                                        )
                                    ),
                                ]
                            ),
                            mobility_service_constraint_zones=MobilityServiceConstraintZonesInFrameRelStructure(
                                mobility_service_constraint_zone=[
                                    MobilityServiceConstraintZone(
                                        id='no_cycling_peak_hours',
                                        validity_conditions_or_valid_between=[
                                            ValidityConditionsRelStructure(
                                                choice=[
                                                    AvailabilityCondition(
                                                        id='peak_hours',
                                                        version='any',
                                                        day_types=DayTypesRelStructure(
                                                            day_type_ref_or_day_type=[
                                                                DayTypeRef(
                                                                    ref='working_day'
                                                                ),
                                                            ]
                                                        ),
                                                        timebands=TimebandsRelStructure(
                                                            timeband_ref_or_timeband=[
                                                                TimebandVersionedChildStructure(
                                                                    id='peak_hours@morning',
                                                                    version='any',
                                                                    start_time_or_start_event=XmlTime(8, 0, 0, 0),
                                                                    choice=[
                                                                        XmlTime(10, 0, 0, 0),
                                                                    ]
                                                                ),
                                                                TimebandVersionedChildStructure(
                                                                    id='peak_hours@evening',
                                                                    version='any',
                                                                    start_time_or_start_event=XmlTime(17, 0, 0, 0),
                                                                    choice=[
                                                                        XmlTime(19, 0, 0, 0),
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            ),
                                        ],
                                        version='any',
                                        name=MultilingualString(
                                            value='Use of zone in peak hours'
                                        ),
                                        polygon_or_multi_surface=Polygon(
                                            id='PB44_A01_B001',
                                            exterior=Exterior(
                                                linear_ring=LinearRing(
                                                    pos_or_point_property_or_pos_list=[
                                                        Pos(
                                                            value=[
                                                                3.14159265358979,
                                                                3.14159265358979,
                                                            ],
                                                            srs_name='wgs84',
                                                            srs_dimension=2
                                                        ),
                                                        Pos(
                                                            value=[
                                                                3.14159265358979,
                                                                3.14159265358979,
                                                            ],
                                                            srs_name='wgs84',
                                                            srs_dimension=2
                                                        ),
                                                        Pos(
                                                            value=[
                                                                3.14159265358979,
                                                                3.14159265358979,
                                                            ],
                                                            srs_name='wgs84',
                                                            srs_dimension=2
                                                        ),
                                                        Pos(
                                                            value=[
                                                                3.14159265358979,
                                                                3.14159265358979,
                                                            ],
                                                            srs_name='wgs84',
                                                            srs_dimension=2
                                                        ),
                                                    ]
                                                )
                                            )
                                        ),
                                        rule_applicability=ZoneRuleApplicabilityEnumeration.INSIDE,
                                        mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        vehicle_restrictions=VehicleTypeZoneRestrictionsRelStructure(
                                            vehicle_type_zone_restriction=[
                                                VehicleTypeZoneRestriction(
                                                    id='no_cycling_peak_hours',
                                                    version='any',
                                                    zone_use=TransportZoneUseEnumeration.FORBIDDEN_ZONE,
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    MobilityServiceConstraintZone(
                                        id='general_uses',
                                        version='any',
                                        name=MultilingualString(
                                            value='Normal Use of zone'
                                        ),
                                        mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        vehicle_restrictions=VehicleTypeZoneRestrictionsRelStructure(
                                            vehicle_type_zone_restriction=[
                                                VehicleTypeZoneRestriction(
                                                    id='general_use',
                                                    version='any',
                                                    zone_use=TransportZoneUseEnumeration.ALL_USES_ALLOWED,
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='pedal_cycle'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    MobilityServiceConstraintZone(
                                        id='bring_back_to_zone',
                                        version='any',
                                        name=MultilingualString(
                                            value='Must bring back to same zone'
                                        ),
                                        mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        vehicle_restrictions=VehicleTypeZoneRestrictionsRelStructure(
                                            vehicle_type_zone_restriction=[
                                                VehicleTypeZoneRestriction(
                                                    id='bring_back',
                                                    version='any',
                                                    zone_use=TransportZoneUseEnumeration.MUST_PICK_UP_AND_DROP_OFF_IN_SAME_ZONE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='mb:cycle_sharing_example-single_session',
                            data_source_ref_attribute='mb:metrobike',
                            version='1.0',
                            responsibility_set_ref_attribute='mb:tariffs',
                            name=MultilingualString(
                                value='Metrobike single session '
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    MobilityServiceFrameRef(
                                        version='1.0',
                                        ref='mb:cycle_sharing_example'
                                    ),
                                    SiteFrameRef(
                                        version='1.0',
                                        ref='mb:cycle_sharing_example'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='metrobike@single_session',
                                        version='any',
                                        name=MultilingualString(
                                            value='Metrobike 1 - Tariff'
                                        ),
                                        document_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://metrobike.eu/tariff.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.INFO,
                                                    ]
                                                ),
                                                InfoLink(
                                                    value='https://metrobike.eu/tariffMap.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MAP,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
                                        ),
                                        choice_1=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        time_intervals=TimeIntervalsRelStructure(
                                            time_interval_ref_or_time_interval=[
                                                TimeInterval(
                                                    id='metrobike@M0+M45',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='First 45 minutes'
                                                    ),
                                                    duration=XmlDuration("PT45M")
                                                ),
                                                TimeInterval(
                                                    id='metrobike@M45+M90',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='45 - 90 minutes'
                                                    ),
                                                    duration=XmlDuration("PT45M")
                                                ),
                                                TimeInterval(
                                                    id='metrobike@M90-eachM60',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='90 - 600 minutes, per hour'
                                                    ),
                                                    duration=XmlDuration("PT60M")
                                                ),
                                                TimeInterval(
                                                    id='metrobike@M600+',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='More than 5 hours 600 minutes'
                                                    ),
                                                    duration=XmlDuration("P1D")
                                                ),
                                            ]
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='metrobike@single_session@access',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Anywhere in Zone'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='metrobike@single_session@access',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:can_access',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.AND,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            tariff_zone_ref=[
                                                                TariffZoneRef(
                                                                    version='any',
                                                                    ref='all_metropolis'
                                                                ),
                                                            ],
                                                            choice_2=[
                                                                VehicleSharingServiceRef(
                                                                    version='any',
                                                                    ref='metrobike'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='metrobike@single_session@durations',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Any where in Zone'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access_when'
                                                    ),
                                                    fare_structure_elements_in_sequence=FareStructureElementsInSequenceRelStructure(
                                                        fare_structure_element_in_sequence_or_controllable_element_in_sequence=[
                                                            FareStructureElementInSequence(
                                                                id='metrobike@single_session@durations',
                                                                version='any',
                                                                is_first_in_sequence=True,
                                                                minimum_access=1,
                                                                maximum_access=1,
                                                                order=1,
                                                                validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                                    id='metrobike@single_session@durations@M0+M45',
                                                                    version='any',
                                                                    order=1,
                                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                                        ref='fxc:can_access_during',
                                                                        version_ref='EXTERNAL'
                                                                    ),
                                                                    time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref=TimeIntervalRef(
                                                                        version='any',
                                                                        ref='metrobike@M0+M45'
                                                                    )
                                                                )
                                                            ),
                                                            FareStructureElementInSequence(
                                                                id='metrobike@single_session@durations',
                                                                version='any',
                                                                minimum_access=0,
                                                                maximum_access=1,
                                                                order=2,
                                                                validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                                    id='metrobike@single_session@durations@M45+M90',
                                                                    version='any',
                                                                    order=1,
                                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                                        ref='fxc:can_access_during',
                                                                        version_ref='EXTERNAL'
                                                                    ),
                                                                    time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref=TimeIntervalRef(
                                                                        version='any',
                                                                        ref='metrobike@M45+M90'
                                                                    )
                                                                )
                                                            ),
                                                            FareStructureElementInSequence(
                                                                id='metrobike@single_session@durations',
                                                                version='any',
                                                                minimum_access=0,
                                                                maximum_access=4,
                                                                order=3,
                                                                validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                                    id='metrobike@single_session@durations@M90-eachM60',
                                                                    version='any',
                                                                    order=1,
                                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                                        ref='fxc:can_access_during',
                                                                        version_ref='EXTERNAL'
                                                                    ),
                                                                    time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref=TimeIntervalRef(
                                                                        version='any',
                                                                        ref='metrobike@M90-eachM60'
                                                                    )
                                                                )
                                                            ),
                                                            FareStructureElementInSequence(
                                                                id='metrobike@single_session@durations@M600+',
                                                                version='any',
                                                                is_last_in_sequence=True,
                                                                minimum_access=0,
                                                                maximum_access=1,
                                                                order=4,
                                                                validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                                    id='metrobike@single_session@durations',
                                                                    version='any',
                                                                    order=1,
                                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                                        ref='fxc:can_access_during',
                                                                        version_ref='EXTERNAL'
                                                                    ),
                                                                    time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref=TimeIntervalRef(
                                                                        version='any',
                                                                        ref='metrobike@M600+'
                                                                    )
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='metrobike@single_session@eligibility',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Eligible user types'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:eligibility',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='metrobike@single_session@eligibility',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:eligible',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UserProfile(
                                                                    id='notATot',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Anyone over 14'
                                                                    ),
                                                                    user_type=UserTypeEnumeration.ANYONE,
                                                                    minimum_age=14
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='metrobike@single_session@conditions_of_travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions on travel'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:travel_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='metrobike@single_session@conditions_of_travel',
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
                                                                    id='metrobike@single_session@usageValidity',
                                                                    version='any',
                                                                    validity_period_type=UsageValidityTypeEnumeration.SINGLE_TRIP,
                                                                    usage_trigger=UsageTriggerEnumeration.ACTIVATION,
                                                                    usage_end=UsageEndEnumeration.END_OF_TRIP,
                                                                    activation_means=ActivationMeansEnumeration.ACCESS_CODE,
                                                                    usage_start_constraint_type=UsageStartConstraintTypeEnumeration.VARIABLE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='metrobike@single_session@frequency',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='One trip no transfers'
                                                                    ),
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    maximal_frequency=1
                                                                ),
                                                                Transferability(
                                                                    id='metrobike@single_session@transferability',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Is Transferable to one user at a time - NB Transferee must also be eligible'
                                                                    ),
                                                                    can_transfer=True,
                                                                    shared_usage=SharedUsageEnumeration.SINGLE_USER
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='metrobike@single_session@conditions_of_sale',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions of sale'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:sale_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='metrobike@single_session@conditions_of_sale',
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
                                                                ChargingPolicy(
                                                                    id='metrobike@single_session@charging_policy@Deposit',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Deposit'
                                                                    ),
                                                                    deposit_policy=DepositPolicyEnumeration.DEPOSIT_BLOCKED
                                                                ),
                                                                RentalPenaltyPolicy(
                                                                    id='metrobike@single_session@hire_penalty@late_return',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Charge for late return'
                                                                    ),
                                                                    rental_penalty_policy_type=RentalPenaltyPolicyTypeEnumeration.LATE_VEHICLE_RETURN
                                                                ),
                                                                RentalPenaltyPolicy(
                                                                    id='metrobike@single_session@hire_penalty@zone_transgression',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Charge for taking out of zone'
                                                                    ),
                                                                    rental_penalty_policy_type=RentalPenaltyPolicyTypeEnumeration.ZONE_TRANSGRESSION
                                                                ),
                                                                RentalPenaltyPolicy(
                                                                    id='metrobike@single_session@hire_penalty@lost_vehicle',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Charge for no return'
                                                                    ),
                                                                    rental_penalty_policy_type=RentalPenaltyPolicyTypeEnumeration.NO_VEHICLE_RETURN
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_products=FareProductsInFrameRelStructure(
                                fare_product=[
                                    SaleDiscountRight(
                                        id='metrobike_online@membership',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Registered member of Metrobike online'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        )
                                    ),
                                    PreassignedFareProduct(
                                        id='metrobike@single_session',
                                        version='any',
                                        name=MultilingualString(
                                            value='One off trip'
                                        ),
                                        info_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://metrobike.com/hirecheck_ios.htm',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MOBILE_APP_INSTALL_CHECK,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='https://metrobike.com/hirecheck_android.htm ',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MOBILE_APP_INSTALL_CHECK,
                                                    ],
                                                    target_platform='android'
                                                ),
                                                InfoLink(
                                                    value='https://metrobike.com/hire_ios.htm',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='https://metrobike.com/hire_android.htm ',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='android'
                                                ),
                                            ]
                                        ),
                                        charging_moment_type=ChargingMomentEnumeration.BEFORE_TRAVEL_THEN_ADJUST_AT_END_OF_TRAVEL,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
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
                                                    id='metrobike@single_session@travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Single ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@single_session@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@single_session@durations'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@single_session@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@single_session@conditions_of_travel'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@single_session@conditions_of_sale'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='metrobike@single_session',
                                                    version='any',
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='any',
                                                        ref='metrobike@single_session@travel'
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
                                        id='ticket_machine',
                                        version='any',
                                        name=MultilingualString(
                                            value='On street ticket machine'
                                        ),
                                        distribution_channel_type=DistributionChannelTypeEnumeration.AT_STOP,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
                                        ),
                                        payment_methods=[
                                            PaymentMethodEnumeration.DEBIT_CARD,
                                            PaymentMethodEnumeration.CREDIT_CARD,
                                            PaymentMethodEnumeration.CONTACTLESS_PAYMENT_CARD,
                                            PaymentMethodEnumeration.EPAY_DEVICE,
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
                                    DistributionChannel(
                                        id='online',
                                        version='any',
                                        name=MultilingualString(
                                            value='internet web acces'
                                        ),
                                        distribution_channel_type=DistributionChannelTypeEnumeration.ONLINE,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        ),
                                        payment_methods=[
                                            PaymentMethodEnumeration.DEBIT_CARD,
                                            PaymentMethodEnumeration.CREDIT_CARD,
                                            PaymentMethodEnumeration.CONTACTLESS_PAYMENT_CARD,
                                        ],
                                        distribution_rights=[
                                            DistributionRightsEnumeration.SELL,
                                            DistributionRightsEnumeration.INFORM,
                                        ]
                                    ),
                                ]
                            ),
                            fulfilment_methods=FulfilmentMethodsInFrameRelStructure(
                                fulfilment_method=[
                                    FulfilmentMethod(
                                        id='collect_from_machine',
                                        version='any',
                                        name=MultilingualString(
                                            value='Collect from machine'
                                        ),
                                        fulfilment_method_type=FulfilmentMethodTypeEnumeration.TICKET_MACHINE,
                                        types_of_travel_document=TypeOfTravelDocumentRefsRelStructure(
                                            type_of_travel_document_ref=[
                                                TypeOfTravelDocumentRef(
                                                    version='any',
                                                    ref='printed_ticket'
                                                ),
                                            ]
                                        )
                                    ),
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
                                        id='printed_ticket',
                                        version='any',
                                        name=MultilingualString(
                                            value='Printed ticket with access code'
                                        ),
                                        media_type=MediaTypeEnumeration.PAPER_TICKET,
                                        machine_readable=[
                                            MachineReadableEnumeration.NONE,
                                        ]
                                    ),
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
                                        id='metrobike_online@membership-SOP@mobile_app',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Metrobike membership'
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='metrobike_online@membership-SOP@mobile_app',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=SaleDiscountRightRef(
                                                        version='any',
                                                        ref='metrobike_online@membership'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='metrobike@single_session-SOP@p-ticket',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Metrobike one-session purchase from ticket machine'
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='metrobike@single_session-SOP@p-ticket@onStreet',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='On street ticket machine'
                                                    ),
                                                    order=1,
                                                    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref=DistributionChannelRef(
                                                        version='any',
                                                        ref='ticket_machine'
                                                    ),
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.AT_STOP,
                                                    ticketing_service_facility_list=TicketingServiceFacilityList(
                                                        value=[
                                                            TicketingServiceFacilityEnumeration.PURCHASE,
                                                        ]
                                                    ),
                                                    payment_methods=[
                                                        PaymentMethodEnumeration.DEBIT_CARD,
                                                        PaymentMethodEnumeration.CREDIT_CARD,
                                                        PaymentMethodEnumeration.CONTACTLESS_PAYMENT_CARD,
                                                        PaymentMethodEnumeration.EPAY_DEVICE,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        version='any',
                                                        ref='collect_from_machine'
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='metrobike@single_session-SOP@p-ticket',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='printed_ticket'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='any',
                                                        ref='metrobike@single_session'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='metrobike@single_session-SOP@mobileApp',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Metrobike one off Mobile app purchase'
                                        ),
                                        condition_summary=ConditionSummary(
                                            requires_account=True
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='metrobike@single_session-SOP@mobileApp',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Must be Registered member of floggit'
                                                    ),
                                                    order=1,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            EntitlementRequired(
                                                                id='metrobike@single_session-SOP@mobileApp@registered',
                                                                version='any',
                                                                choice=SaleDiscountRightRef(
                                                                    version='any',
                                                                    ref='metrobike_online@membership'
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
                                                                ref='metrobike_online'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='metrobike@single_session-SOP@mobileApp',
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
                                                    id='metrobike@single_session-SOP@mobileApp',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='any',
                                                        ref='metrobike@single_session'
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
                            id='mb:cycle_sharing_example-day_pass',
                            data_source_ref_attribute='mb:metrobike',
                            version='1.0',
                            responsibility_set_ref_attribute='mb:tariffs',
                            name=MultilingualString(
                                value='Metrobike day Pass1'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    MobilityServiceFrameRef(
                                        version='1.0',
                                        ref='mb:cycle_sharing_example'
                                    ),
                                    SiteFrameRef(
                                        version='1.0',
                                        ref='mb:cycle_sharing_example'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='metrobike@day_pass',
                                        version='any',
                                        name=MultilingualString(
                                            value='Metrobike Day Pass - Tariff'
                                        ),
                                        document_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://metrobike.eu/tariff.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.INFO,
                                                    ]
                                                ),
                                                InfoLink(
                                                    value='https://metrobike.eu/tariffMap.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfoLinkEnumeration.MAP,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
                                        ),
                                        choice_1=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        time_intervals=TimeIntervalsRelStructure(
                                            time_interval_ref_or_time_interval=[
                                                TimeInterval(
                                                    id='metrobike@1D',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Metrobike Day Pass'
                                                    ),
                                                    minimum_duration=XmlDuration("P1D")
                                                ),
                                            ]
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='metrobike@day_pass@access',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Any where in Zone'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='metrobike@day_pass@@access',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:can_access',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.AND,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            tariff_zone_ref=[
                                                                TariffZoneRef(
                                                                    version='any',
                                                                    ref='all_metropolis'
                                                                ),
                                                            ],
                                                            choice_2=[
                                                                VehicleSharingServiceRef(
                                                                    version='any',
                                                                    ref='metrobike'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='metrobike@day_pass@durations',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Access up to end of fare day'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access_when'
                                                    ),
                                                    time_interval_ref_or_time_intervals_or_time_structure_factors=TimeIntervalRef(
                                                        version='any',
                                                        ref='metrobike@1D'
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='metrobike@day_pass@eligibility',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Eligible user types'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:eligibility',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='metrobike@day_pass@eligibility',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:eligible',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UserProfileRef(
                                                                    version='any',
                                                                    ref='notATot'
                                                                ),
                                                                EntitlementRequiredRef(
                                                                    version='any',
                                                                    ref='metrobike_registered'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='metrobike@day_pass@conditions_of_travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='COnditions on travel'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:travel_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='metrobike@day_pass@conditions_of_travel',
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
                                                                    id='metrobike@day_pass@usagValidity',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Valid till end of fare day.'
                                                                    ),
                                                                    validity_period_type=UsageValidityTypeEnumeration.DAY_PASS,
                                                                    usage_trigger=UsageTriggerEnumeration.PURCHASE,
                                                                    usage_end=UsageEndEnumeration.END_OF_FARE_DAY,
                                                                    activation_means=ActivationMeansEnumeration.USE_OF_MOBILE_DEVICE,
                                                                    usage_start_constraint_type=UsageStartConstraintTypeEnumeration.VARIABLE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='metrobike@day_pass@frequency',
                                                                    version='any',
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.UNLIMITED
                                                                ),
                                                                Transferability(
                                                                    id='metrobike@day_pass@transferability',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Is Transferable - Transferee must be eligible'
                                                                    ),
                                                                    can_transfer=True,
                                                                    shared_usage=SharedUsageEnumeration.SINGLE_USER
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_products=FareProductsInFrameRelStructure(
                                fare_product=[
                                    PreassignedFareProduct(
                                        id='metrobike@day_pass',
                                        version='any',
                                        name=MultilingualString(
                                            value='Metrobike day pass'
                                        ),
                                        charging_moment_type=ChargingMomentEnumeration.BEFORE_TRAVEL,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
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
                                                    id='metrobike@day_pass@travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Single ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@day_pass@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@day_pass@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@day_pass@durations'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@day_pass@conditions_of_travel'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='metrobike@single_session@conditions_of_sale'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='metrobike@day_pass',
                                                    version='any',
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='any',
                                                        ref='metrobike@day_pass@travel'
                                                    )
                                                ),
                                            ]
                                        ),
                                        product_type=PreassignedFareProductEnumeration.SINGLE_TRIP
                                    ),
                                ]
                            ),
                            sales_offer_packages=SalesOfferPackagesInFrameRelStructure(
                                sales_offer_package=[
                                    SalesOfferPackage(
                                        id='metrobike@day_pass-SOP@mobileApp',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Metrobike day pass Mobile (app purchase only)'
                                        ),
                                        condition_summary=ConditionSummary(
                                            requires_account=True
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='metrobike@day_pass-SOP@mobileApp',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Registered member of floggit '
                                                    ),
                                                    order=1,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            EntitlementRequired(
                                                                id='metrobike_registered',
                                                                version='any',
                                                                choice=SaleDiscountRightRef(
                                                                    version='any',
                                                                    ref='metrobike_online@membership'
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
                                                                ref='metrobike_online'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='metrobike@day_pass-SOP@mobileApp',
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
                                                    id='metrobike@day_pass-SOP@mobileApp',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='any',
                                                        ref='metrobike@day_pass'
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
                            id='mb:cycle_sharing_example_prices',
                            data_source_ref_attribute='mb:metrobike',
                            version='1.0',
                            responsibility_set_ref_attribute='mb:tariffs',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_currency='EUR'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='mb:cycle_sharing_example-single_session'
                                    ),
                                ]
                            ),
                            pricing_parameter_set=PricingParameterSet(
                                id='mb:cycle_sharing_example_Prices',
                                version='any',
                                pricing_rules=PricingRulesRelStructure(
                                    pricing_rule=[
                                        PricingRule(
                                            id='cumulative_total',
                                            version='any',
                                            name=MultilingualString(
                                                value='Excess charge is sum of additional '
                                            )
                                        ),
                                        PricingRule(
                                            id='per_hour',
                                            version='any',
                                            name=MultilingualString(
                                                value='Multiply by number of hours'
                                            )
                                        ),
                                    ]
                                )
                            ),
                            fare_tables=FareTablesInFrameRelStructure(
                                fare_table=[
                                    FareTable(
                                        id='metrobike',
                                        version='any',
                                        name=MultilingualString(
                                            value='Metrobike prices'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:MBIKE'
                                        ),
                                        limitations=UsageParameterRefsRelStructure(
                                            choice=[
                                                UserProfileRef(
                                                    version='any',
                                                    ref='notATot'
                                                ),
                                            ]
                                        ),
                                        specifics=FareTableSpecificsStructure(
                                            tariff_zone_ref=TariffZoneRef(
                                                version='any',
                                                ref='all_metropolis'
                                            ),
                                            choice_1=VehicleSharingServiceRef(
                                                version='any',
                                                ref='metrobike'
                                            )
                                        ),
                                        includes=FareTablesRelStructure(
                                            fare_table_ref_or_fare_table=[
                                                FareTable(
                                                    id='metrobike@single_session',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Metrobike one off use prices'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            SalesOfferPackageRef(
                                                                version='any',
                                                                ref='metrobike@single_session-SOP@p-ticket'
                                                            ),
                                                            SalesOfferPackageRef(
                                                                version='any',
                                                                ref='metrobike@single_session-SOP@mobileApp'
                                                            ),
                                                        ]
                                                    ),
                                                    used_in=UsedInRefsRelStructure(
                                                        choice=[
                                                            TariffRef(
                                                                version='any',
                                                                ref='metrobike@single_session'
                                                            ),
                                                        ]
                                                    ),
                                                    includes=FareTablesRelStructure(
                                                        fare_table_ref_or_fare_table=[
                                                            FareTable(
                                                                id='metrobike@single_session@rental',
                                                                version='any',
                                                                prices=FarePricesRelStructure(
                                                                    fare_price_ref_or_cell_ref_or_fare_price=[
                                                                        UsageParameterPrice(
                                                                            id='metrobike@single_session@charging_policy@Deposit',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Deposit - blocked'
                                                                            ),
                                                                            amount=Decimal('300.00'),
                                                                            choice=ChargingPolicyRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session@charging_policy@Deposit'
                                                                            )
                                                                        ),
                                                                        UsageParameterPrice(
                                                                            id='metrobike@single_session@charging_policy@Deposit_Refund',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Deposit - unblocked'
                                                                            ),
                                                                            amount=Decimal('-300.00'),
                                                                            choice=ChargingPolicyRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session@charging_policy@Deposit'
                                                                            )
                                                                        ),
                                                                        TimeIntervalPrice(
                                                                            id='metrobike@M0+M45',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='First 45 minutes'
                                                                            ),
                                                                            amount=Decimal('2.10'),
                                                                            units=Decimal('45'),
                                                                            time_interval_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='metrobike@M0+M45'
                                                                            )
                                                                        ),
                                                                        TimeIntervalPrice(
                                                                            id='metrobike@M45+M90',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='45 to 90 minutes extra charge'
                                                                            ),
                                                                            amount=Decimal('3.00'),
                                                                            units=Decimal('45'),
                                                                            time_interval_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='metrobike@M45+M90'
                                                                            )
                                                                        ),
                                                                        TimeIntervalPrice(
                                                                            id='metrobike@M90-eachM60',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='90 to 600 minutes, charge per hour e'
                                                                            ),
                                                                            amount=Decimal('4.00'),
                                                                            units=Decimal('60'),
                                                                            time_interval_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='metrobike@M90-eachM60'
                                                                            )
                                                                        ),
                                                                        TimeIntervalPrice(
                                                                            id='metrobike@M600+',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Over 600 minutes'
                                                                            ),
                                                                            amount=Decimal('40.00'),
                                                                            units=Decimal('600'),
                                                                            time_interval_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='metrobike@M600+'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            FareTable(
                                                                id='metrobike@hire_penalty',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Metrobike penalty fees'
                                                                ),
                                                                limitations=UsageParameterRefsRelStructure(
                                                                    choice=[
                                                                        UserProfileRef(
                                                                            version='any',
                                                                            ref='notATot'
                                                                        ),
                                                                    ]
                                                                ),
                                                                prices=FarePricesRelStructure(
                                                                    fare_price_ref_or_cell_ref_or_fare_price=[
                                                                        UsageParameterPrice(
                                                                            id='metrobike@single_session@hire_penalty@late_return',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Late return'
                                                                            ),
                                                                            amount=Decimal('100.00'),
                                                                            choice=RentalPenaltyPolicyRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session@hire_penalty@late_return'
                                                                            )
                                                                        ),
                                                                        UsageParameterPrice(
                                                                            id='metrobike@single_session@hire_penalty@lost_vehicle',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Late retrun'
                                                                            ),
                                                                            amount=Decimal('900.00'),
                                                                            choice=RentalPenaltyPolicyRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session@hire_penalty@lost_vehicle'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareTable(
                                                    id='metrobike@day_pass',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Metrobike day pass prices'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            SalesOfferPackageRef(
                                                                version='any',
                                                                ref='metrobike@day_pass-SOP@mobileApp'
                                                            ),
                                                        ]
                                                    ),
                                                    used_in=UsedInRefsRelStructure(
                                                        choice=[
                                                            TariffRef(
                                                                version='any',
                                                                ref='metrobike@day_pass'
                                                            ),
                                                        ]
                                                    ),
                                                    includes=FareTablesRelStructure(
                                                        fare_table_ref_or_fare_table=[
                                                            FareTable(
                                                                id='metrobike@day_pass@rental',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Metrobike Day PAss fees'
                                                                ),
                                                                limitations=UsageParameterRefsRelStructure(
                                                                    choice=[
                                                                        UserProfileRef(
                                                                            version='any',
                                                                            ref='notATot'
                                                                        ),
                                                                    ]
                                                                ),
                                                                prices=FarePricesRelStructure(
                                                                    fare_price_ref_or_cell_ref_or_fare_price=[
                                                                        TimeIntervalPrice(
                                                                            id='metrobike@1D',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='day pass'
                                                                            ),
                                                                            amount=Decimal('12.00'),
                                                                            time_interval_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='metrobike@1D'
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
                            )
                        ),
                    ]
                )
            ),
            CompositeFrame(
                id='mb:cycle_sharing_example_transaction_examples',
                data_source_ref_attribute='mb:metrobike',
                version='1.0',
                responsibility_set_ref_attribute='mb:transaction_data',
                name=MultilingualString(
                    value='Sample Transactions for Metrobike trips '
                ),
                prerequisites=VersionFrameRefsRelStructure(
                    version_frame_ref=[
                        CompositeFrameRef(
                            version='1.0',
                            ref='mb:cycle_sharing_example'
                        ),
                    ]
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        MobilityJourneyFrame(
                            id='mbt:sample_transactions',
                            version='1.2',
                            vehicle_access_credentials=VehicleAccessCredentialAssignmentsRelStructure(
                                vehicle_access_credentials_assignment=[
                                    VehicleAccessCredentialsAssignment(
                                        id='mbt:Anon001@trans069@purchase_single_session@one_time',
                                        version='any',
                                        order=1,
                                        common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        vehicle_ref=VehicleRef(
                                            version='any',
                                            ref='C01'
                                        ),
                                        service_access_code_ref=ServiceAccessCodeRef(
                                            version='any',
                                            ref='mbt:Anon001@027@purchase_single_session'
                                        )
                                    ),
                                    VehicleAccessCredentialsAssignment(
                                        id='mbt:Cust444@trans005@purchase_day_pass',
                                        version='any',
                                        order=1,
                                        common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='metrobike'
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            ref='mbt:317867122222',
                                            version_ref='External'
                                        ),
                                        service_access_code_ref=ServiceAccessCodeRef(
                                            version='any',
                                            ref='mbt:Good@Cust444@005@purchase_day_pass'
                                        )
                                    ),
                                ]
                            ),
                            parking_log_entries=ParkingLogEntriesInFrameRelStructure(
                                parking_log_entry=[
                                    RentalAvailability(
                                        id='bike_station_alpha@2020-10-08T11:07:00',
                                        version='any',
                                        name=MultilingualString(
                                            value='Before Checkout '
                                        ),
                                        date=XmlDateTime(2020, 10, 8, 11, 6, 55),
                                        parking_ref=ParkingRef(
                                            version='any',
                                            ref='bike_station_alpha'
                                        ),
                                        is_operational=True,
                                        is_renting=True,
                                        is_accepting_returns=True,
                                        available_vehicles=5,
                                        disabled_vehicles=2,
                                        available_docks=3,
                                        disabled_docks=2
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@01@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@01'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@02@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@02'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@03@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@03'
                                        ),
                                        status=ParkingBayStatusEnumeration.AVAILABLE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@04@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@04'
                                        ),
                                        status=ParkingBayStatusEnumeration.AVAILABLE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@05@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@05'
                                        ),
                                        status=ParkingBayStatusEnumeration.AVAILABLE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@06@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@06'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@07@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@07'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@08@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@08'
                                        ),
                                        status=ParkingBayStatusEnumeration.OUT_OF_SERVICE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@09@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@09'
                                        ),
                                        status=ParkingBayStatusEnumeration.OUT_OF_SERVICE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@10@2020-10-08T11:07:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@10'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                    RentalAvailability(
                                        id='bike_station_alpha@2020-10-08T11:07:20',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Checkout '
                                        ),
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 20),
                                        parking_ref=ParkingRef(
                                            version='any',
                                            ref='bike_station_alpha'
                                        ),
                                        is_operational=True,
                                        is_renting=True,
                                        is_accepting_returns=True,
                                        available_vehicles=4,
                                        disabled_vehicles=2,
                                        available_docks=4,
                                        disabled_docks=2
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_alpha_A1@10@2020-10-08T11:07:20',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 11, 7, 20),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_alpha_A1@10'
                                        ),
                                        status=ParkingBayStatusEnumeration.AVAILABLE
                                    ),
                                    RentalAvailability(
                                        id='bike_station_beta@2020-10-08T13:10:00',
                                        version='any',
                                        name=MultilingualString(
                                            value='Before Return'
                                        ),
                                        date=XmlDateTime(2020, 10, 8, 13, 10, 0),
                                        parking_ref=ParkingRef(
                                            version='any',
                                            ref='bike_station_beta'
                                        ),
                                        is_operational=True,
                                        is_renting=True,
                                        is_accepting_returns=True,
                                        available_vehicles=3,
                                        available_docks=2
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_beta_B1@01@2020-10-08T13:10:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 13, 10, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_beta_B1@01'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_beta_B1@02@2020-10-08T13:10:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 13, 10, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_beta_B1@02'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_beta_B1@03@2020-10-08T13:10:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 13, 10, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_beta_B1@03'
                                        ),
                                        status=ParkingBayStatusEnumeration.AVAILABLE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_beta_B1@04@2020-10-08T13:10:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 13, 10, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_beta_B1@04'
                                        ),
                                        status=ParkingBayStatusEnumeration.AVAILABLE
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_beta_B1@05@2020-10-08T13:10:00',
                                        version='any',
                                        date=XmlDateTime(2020, 10, 8, 13, 10, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_beta_B1@05'
                                        ),
                                        status=ParkingBayStatusEnumeration.AVAILABLE
                                    ),
                                    RentalAvailability(
                                        id='bike_station_beta@2020-10-08T13:10:05',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Return'
                                        ),
                                        date=XmlDateTime(2020, 10, 8, 13, 10, 5),
                                        parking_ref=ParkingRef(
                                            version='any',
                                            ref='bike_station_beta'
                                        ),
                                        is_operational=True,
                                        is_renting=True,
                                        is_accepting_returns=True,
                                        available_vehicles=4,
                                        available_docks=1
                                    ),
                                    ParkingBayCondition(
                                        id='bike_station_beta_B1@04@2020-10-08T13:10:05',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Return'
                                        ),
                                        date=XmlDateTime(2020, 10, 8, 13, 10, 5),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='bike_station_beta_B1@04'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                ]
                            )
                        ),
                        SalesTransactionFrame(
                            id='mbt:sample_transactions',
                            version='1.2',
                            name=MultilingualString(
                                value='Metrobike Sample Transactions'
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    CodespaceRef(
                                        ref='mb_data'
                                    ),
                                    Codespace(
                                        id='mb_transactions',
                                        xmlns='mbt',
                                        xmlns_url='http://www.metrobike.eu/transactions',
                                        description='Operator transaction data'
                                    ),
                                ]
                            ),
                            customers=CustomersInFrameRelStructure(
                                customer=[
                                    Customer(
                                        id='mbt:Cust444',
                                        created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                        version='any',
                                        surname='Johnson',
                                        first_name='Boris',
                                        title='Mr',
                                        gender=GenderEnumeration.MALE,
                                        email='boris@brexit.eu',
                                        email_verified=XmlDateTime(2020, 2, 28, 15, 0, 0),
                                        phone=TelephoneContactStructure(
                                            tel_national_number='07867122222',
                                            tel_country_code='31'
                                        ),
                                        phone_verified=XmlDateTime(2020, 2, 28, 16, 0, 0),
                                        customer_accounts=CustomerAccountsRelStructure(
                                            customer_account_ref_or_customer_account=[
                                                CustomerAccount(
                                                    id='mbt:Cust444@AC7651',
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
                                                                ref='mbt:Good@Cust444@005'
                                                            ),
                                                        ]
                                                    ),
                                                    customer_payment_means_ref=CustomerPaymentMeansRef(
                                                        version='any',
                                                        ref='mbt:Cust444@AC7651@p1'
                                                    ),
                                                    payment_means=CustomerPaymentMeansRelStructure(
                                                        customer_payment_means=[
                                                            CustomerPaymentMeans(
                                                                id='mbt:Cust444@AC7651@p1',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='B.Johnson Visa Card'
                                                                ),
                                                                medium_access_device_ref=EmvCardRef(
                                                                    ref='visa:47594444555666',
                                                                    version_ref='external'
                                                                )
                                                            ),
                                                            CustomerPaymentMeans(
                                                                id='mbt:Cust444@AC7651@p2',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='B.Johnson mobile device'
                                                                ),
                                                                medium_access_device_ref=MobileDeviceRef(
                                                                    ref='mbt:317867122222',
                                                                    version_ref='external'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    medium_access_devices=MediumAccessDeviceRefsRelStructure(
                                                        medium_access_device_ref=MobileDeviceRef(
                                                            ref='mbt:317867122222',
                                                            version_ref='External'
                                                        )
                                                    )
                                                ),
                                            ]
                                        ),
                                        fare_contracts=FareContractsRelStructure(
                                            fare_contract_ref_or_fare_contract=[
                                                FareContract(
                                                    id='mbt:Cust444@contract001',
                                                    version='any',
                                                    customer_ref=CustomerRef(
                                                        ref='mbt:Cust444',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    fare_contract_entries=FareContractEntriesRelStructure(
                                                        choice=[
                                                            SalesTransaction(
                                                                id='mbt:Cust444@contract001@t001@join_as_member',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Join As Member'
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
                                                                            id='mbt:Cust444@contract001@t001@join_as_member',
                                                                            version='any',
                                                                            date=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='any',
                                                                                ref='mbt:Cust444@contract001@t001@join_as_member'
                                                                            ),
                                                                            amount=Decimal('0'),
                                                                            start_of_validity=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                                            travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                                start=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                                                authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                                    version='any',
                                                                                    ref='noc:MBIKE'
                                                                                ),
                                                                                choice=VehicleSharingServiceRef(
                                                                                    version='any',
                                                                                    ref='metrobike'
                                                                                )
                                                                            ),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='mbt:Cust444@contract001@t001@purchase_member',
                                                                                        version='any',
                                                                                        name=MultilingualString(
                                                                                            value='Join as member'
                                                                                        ),
                                                                                        order=1,
                                                                                        preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=SaleDiscountRightRef(
                                                                                            version='any',
                                                                                            ref='metrobike_online@membership'
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                customer_purchase_packages=CustomerPurchasePackagesRelStructure(
                                                                    customer_purchase_package_or_customer_purchase_package_ref=[
                                                                        CustomerPurchasePackageRef(
                                                                            version='any',
                                                                            ref='mbt:Good@Cust444@001'
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            SalesTransaction(
                                                                id='mbt:Cust444@trans005@purchase_day_pass',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Buy Dap PAss'
                                                                ),
                                                                date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                                type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                                    ref='fxc:product_purchase',
                                                                    version_ref='EXTERNAL'
                                                                ),
                                                                amount=Decimal('12.00'),
                                                                payment_method=PaymentMethodEnumeration.CREDIT_CARD,
                                                                travel_specifications=TravelSpecificationsRelStructure(
                                                                    travel_specification_ref_or_travel_specification=[
                                                                        OfferedTravelSpecification(
                                                                            id='mbt:Cust444@trans005@purchase_day_pass',
                                                                            version='any',
                                                                            date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='any',
                                                                                ref='mbt:Cust444@trans005@purchase_day_pass'
                                                                            ),
                                                                            fare_price_ref_or_cell_ref=TimeIntervalPriceRef(
                                                                                version='any',
                                                                                ref='metrobike@1D'
                                                                            ),
                                                                            amount=Decimal('12.00'),
                                                                            start_of_validity=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                                            travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                                start=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                                                duration=XmlDuration("P1D"),
                                                                                choice=VehicleSharingServiceRef(
                                                                                    version='any',
                                                                                    ref='metrobike'
                                                                                )
                                                                            ),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='mbt:Cust444@trans005@purchase_day_pass',
                                                                                        version='any',
                                                                                        name=MultilingualString(
                                                                                            value='Single ride'
                                                                                        ),
                                                                                        order=1,
                                                                                        validable_element_ref=ValidableElementRef(
                                                                                            version='any',
                                                                                            ref='metrobike@day_pass@travel'
                                                                                        ),
                                                                                        preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                                                            version='any',
                                                                                            ref='metrobike@day_pass'
                                                                                        ),
                                                                                        fare_structure_element_ref=FareStructureElementRef(
                                                                                            version='any',
                                                                                            ref='metrobike@day_pass@access'
                                                                                        ),
                                                                                        sales_offer_package_ref=SalesOfferPackageRef(
                                                                                            version='any',
                                                                                            ref='metrobike@day_pass-SOP@mobileApp'
                                                                                        ),
                                                                                        validity_parameters=ValidityParametersRelStructure(
                                                                                            mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                                                VehicleSharingRef(
                                                                                                    version='any',
                                                                                                    ref='cycle_share'
                                                                                                ),
                                                                                            ],
                                                                                            choice=[
                                                                                                OperatorRef(
                                                                                                    version='any',
                                                                                                    ref='noc:MBIKE'
                                                                                                ),
                                                                                                OnlineServiceOperatorRef(
                                                                                                    version='any',
                                                                                                    ref='floggit'
                                                                                                ),
                                                                                            ],
                                                                                            choice_2=[
                                                                                                VehicleSharingServiceRef(
                                                                                                    version='any',
                                                                                                    ref='metrobike'
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
                                                                                        time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref=TimeIntervalRef(
                                                                                            version='any',
                                                                                            ref='metrobike@1D'
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                customer_purchase_packages=CustomerPurchasePackagesRelStructure(
                                                                    customer_purchase_package_or_customer_purchase_package_ref=[
                                                                        CustomerPurchasePackageRef(
                                                                            version='any',
                                                                            ref='mbt:Good@Cust444@005'
                                                                        ),
                                                                    ]
                                                                ),
                                                                travel_documents=TravelDocumentsRelStructure(
                                                                    choice=[
                                                                        ServiceAccessCodeRef(
                                                                            version='any',
                                                                            ref='mbt:Good@Cust444@005@purchase_day_pass'
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
                            fare_contracts=FareContractsInFrameRelStructure(
                                fare_contract=[
                                    FareContract(
                                        id='mbt:Anon001@trans069',
                                        version='any',
                                        customer_ref=CustomerRef(
                                            ref='mbt:Anon001',
                                            version_ref='EXTERNAL'
                                        ),
                                        fare_contract_entries=FareContractEntriesRelStructure(
                                            choice=[
                                                SalesTransaction(
                                                    id='mbt:Anon001@trans069@purchase_single_session@checkout',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Buy Single ticket Adult'
                                                    ),
                                                    date=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                    type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                        ref='fxc:product_purchase',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    amount=Decimal('2.10'),
                                                    payment_method=PaymentMethodEnumeration.CASH,
                                                    travel_specifications=TravelSpecificationsRelStructure(
                                                        travel_specification_ref_or_travel_specification=[
                                                            OfferedTravelSpecification(
                                                                id='mbt:Anon001@trans069@purchase_single_session@checkout',
                                                                version='any',
                                                                date=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                                sales_transaction_ref=SalesTransactionRef(
                                                                    version='any',
                                                                    ref='mbt:Anon001@trans069@purchase_single_session@checkout'
                                                                ),
                                                                fare_price_ref_or_cell_ref=TimeIntervalPriceRef(
                                                                    version='any',
                                                                    ref='metrobike@M0+M45'
                                                                ),
                                                                amount=Decimal('2.10'),
                                                                start_of_validity=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                                travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                    origin=TravelSpecificationSummaryEndpointStructure(
                                                                        stop_place_ref_or_site_ref=ParkingRef(
                                                                            version='any',
                                                                            ref='bike_station_alpha'
                                                                        )
                                                                    ),
                                                                    start=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                                    duration=XmlDuration("PT45M"),
                                                                    authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                        version='any',
                                                                        ref='noc:MBIKE'
                                                                    ),
                                                                    user_profile_ref=UserProfileRef(
                                                                        version='any',
                                                                        ref='notATot'
                                                                    ),
                                                                    choice=VehicleSharingServiceRef(
                                                                        version='any',
                                                                        ref='metrobike'
                                                                    )
                                                                ),
                                                                specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                    specific_parameter_assignment=[
                                                                        SpecificParameterAssignment(
                                                                            id='mbt:Anon001@trans069@purchase_single_session@checkout',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='One off cycle hire'
                                                                            ),
                                                                            order=1,
                                                                            validable_element_ref=ValidableElementRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session@travel'
                                                                            ),
                                                                            preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session'
                                                                            ),
                                                                            fare_structure_element_ref=FareStructureElementRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session@access'
                                                                            ),
                                                                            sales_offer_package_ref=SalesOfferPackageRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session-SOP@p-ticket'
                                                                            ),
                                                                            limitations=UsageParametersRelStructure(
                                                                                choice=[
                                                                                    UserProfileRef(
                                                                                        version='any',
                                                                                        ref='notATot'
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                            validity_parameters=ValidityParametersRelStructure(
                                                                                mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                                    VehicleSharingRef(
                                                                                        version='any',
                                                                                        ref='cycle_share'
                                                                                    ),
                                                                                ],
                                                                                choice=[
                                                                                    OperatorRef(
                                                                                        version='any',
                                                                                        ref='noc:MBIKE'
                                                                                    ),
                                                                                ],
                                                                                tariff_zone_ref=[
                                                                                    TariffZoneRef(
                                                                                        version='any',
                                                                                        ref='all_metropolis'
                                                                                    ),
                                                                                ],
                                                                                choice_1=[
                                                                                    MonitoredVehicleSharingParkingBayRef(
                                                                                        version='any',
                                                                                        ref='bike_station_alpha_A1@02'
                                                                                    ),
                                                                                    VehicleSharingParkingAreaRef(
                                                                                        version='any',
                                                                                        ref='bike_station_alpha_A1'
                                                                                    ),
                                                                                    MonitoredVehicleSharingParkingBayRef(
                                                                                        version='any',
                                                                                        ref='bike_station_alpha_A1@10'
                                                                                    ),
                                                                                ],
                                                                                transport_type_ref_or_vehicle_type_ref=[
                                                                                    SimpleVehicleTypeRef(
                                                                                        version='any',
                                                                                        ref='electric_cycle'
                                                                                    ),
                                                                                ],
                                                                                vehicle_model_ref=[
                                                                                    VehicleModelRef(
                                                                                        version='any',
                                                                                        ref='electric_boneshaker'
                                                                                    ),
                                                                                ],
                                                                                vehicle_model_profile_ref=[
                                                                                    CycleModelProfileRef(
                                                                                        version='any',
                                                                                        ref='boneKitB'
                                                                                    ),
                                                                                ],
                                                                                choice_2=[
                                                                                    VehicleSharingServiceRef(
                                                                                        version='any',
                                                                                        ref='metrobike'
                                                                                    ),
                                                                                ],
                                                                                vehicle_ref=[
                                                                                    VehicleRef(
                                                                                        version='any',
                                                                                        ref='C01'
                                                                                    ),
                                                                                ],
                                                                                type_of_travel_document_ref=[
                                                                                    TypeOfTravelDocumentRef(
                                                                                        version='any',
                                                                                        ref='printed_ticket'
                                                                                    ),
                                                                                ],
                                                                                distribution_channel_ref_or_group_of_distribution_channels_ref=[
                                                                                    DistributionChannelRef(
                                                                                        version='any',
                                                                                        ref='ticket_machine'
                                                                                    ),
                                                                                ],
                                                                                fulfilment_method_ref=[
                                                                                    FulfilmentMethodRef(
                                                                                        version='any',
                                                                                        ref='collect_from_machine'
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                            time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='metrobike@M0+M45'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    customer_purchase_packages=CustomerPurchasePackagesRelStructure(
                                                        customer_purchase_package_or_customer_purchase_package_ref=[
                                                            CustomerPurchasePackageRef(
                                                                version='any',
                                                                ref='mbt:Anon001@027'
                                                            ),
                                                        ]
                                                    ),
                                                    travel_documents=TravelDocumentsRelStructure(
                                                        choice=[
                                                            TravelDocument(
                                                                id='mbt:ticket@765452234',
                                                                validity_conditions_or_valid_between=[
                                                                    ValidBetween(
                                                                        from_date=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                                        to_date=XmlDateTime(2020, 12, 8, 14, 1, 0)
                                                                    ),
                                                                ],
                                                                version='any',
                                                                type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                                    version='any',
                                                                    ref='printed_ticket'
                                                                )
                                                            ),
                                                            ServiceAccessCodeRef(
                                                                version='any',
                                                                ref='mbt:Anon001@027@purchase_single_session'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                SalesTransaction(
                                                    id='mbt:Anon001@trans069@purchase_single_session@return',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Return and pay additional charge'
                                                    ),
                                                    date=XmlDateTime(2020, 12, 8, 14, 47, 0),
                                                    type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                        ref='fxc:product_purchase',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    payment_method=PaymentMethodEnumeration.CASH,
                                                    travel_specifications=TravelSpecificationsRelStructure(
                                                        travel_specification_ref_or_travel_specification=[
                                                            OfferedTravelSpecification(
                                                                id='mbt:Anon001@trans069@purchase_single_session@return',
                                                                version='any',
                                                                date=XmlDateTime(2020, 10, 8, 13, 10, 0),
                                                                sales_transaction_ref=SalesTransactionRef(
                                                                    version='any',
                                                                    ref='mbt:Anon001@trans069@purchase_single_session@return'
                                                                ),
                                                                amount=Decimal('7.00'),
                                                                rule_step_results=PriceRuleStepResultsRelStructure(
                                                                    rule_step_result=[
                                                                        PriceRuleStepResultStructure(
                                                                            fare_price_ref=TimeIntervalPriceRef(
                                                                                version='any',
                                                                                ref='metrobike@M45+M90'
                                                                            ),
                                                                            amount=Decimal('3.00'),
                                                                            adjustment_amount=Decimal('3.00'),
                                                                            discounting_rule_ref_or_pricing_rule_ref=PricingRuleRef(
                                                                                version='any',
                                                                                ref='cumulative_total'
                                                                            ),
                                                                            narrative=MultilingualString(
                                                                                value='46 minutes to 90 minutes'
                                                                            ),
                                                                            id='mbt:Anon001@trans069@purchase_single_session@return',
                                                                            order=1
                                                                        ),
                                                                        PriceRuleStepResultStructure(
                                                                            fare_price_ref=TimeIntervalPriceRef(
                                                                                version='any',
                                                                                ref='metrobike@M90-eachM60'
                                                                            ),
                                                                            amount=Decimal('4.00'),
                                                                            adjustment_amount=Decimal('8.00'),
                                                                            adjustment_units=Decimal('120'),
                                                                            discounting_rule_ref_or_pricing_rule_ref=PricingRuleRef(
                                                                                version='any',
                                                                                ref='per_hour'
                                                                            ),
                                                                            narrative=MultilingualString(
                                                                                value='91 minutes to 600 minutes'
                                                                            ),
                                                                            id='mbt:Anon001@trans069@purchase_single_session@return',
                                                                            order=2
                                                                        ),
                                                                    ]
                                                                ),
                                                                end_of_validity=XmlDateTime(2020, 10, 8, 13, 10, 0),
                                                                travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                    destination=TravelSpecificationSummaryEndpointStructure(
                                                                        stop_place_ref_or_site_ref=ParkingRef(
                                                                            version='any',
                                                                            ref='bike_station_beta'
                                                                        )
                                                                    ),
                                                                    start=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                                    duration=XmlDuration("PT45M"),
                                                                    authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                        version='any',
                                                                        ref='noc:MBIKE'
                                                                    ),
                                                                    user_profile_ref=UserProfileRef(
                                                                        version='any',
                                                                        ref='notATot'
                                                                    ),
                                                                    choice=VehicleSharingServiceRef(
                                                                        version='any',
                                                                        ref='metrobike'
                                                                    )
                                                                ),
                                                                specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                    specific_parameter_assignment=[
                                                                        SpecificParameterAssignment(
                                                                            id='mbt:Anon001@trans069@purchase_single_session@return',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='One off cycle hire - return'
                                                                            ),
                                                                            order=1,
                                                                            validable_element_ref=ValidableElementRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session@travel'
                                                                            ),
                                                                            preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session'
                                                                            ),
                                                                            fare_structure_element_ref=FareStructureElementRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session@access'
                                                                            ),
                                                                            sales_offer_package_ref=SalesOfferPackageRef(
                                                                                version='any',
                                                                                ref='metrobike@single_session-SOP@p-ticket'
                                                                            ),
                                                                            validity_parameters=ValidityParametersRelStructure(
                                                                                mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                                    VehicleSharingRef(
                                                                                        version='any',
                                                                                        ref='cycle_share'
                                                                                    ),
                                                                                ],
                                                                                choice=[
                                                                                    OperatorRef(
                                                                                        version='any',
                                                                                        ref='noc:MBIKE'
                                                                                    ),
                                                                                ],
                                                                                tariff_zone_ref=[
                                                                                    TariffZoneRef(
                                                                                        version='any',
                                                                                        ref='all_metropolis'
                                                                                    ),
                                                                                ],
                                                                                choice_1=[
                                                                                    VehicleSharingParkingAreaRef(
                                                                                        version='any',
                                                                                        ref='bike_station_beta_B1'
                                                                                    ),
                                                                                    MonitoredVehicleSharingParkingBayRef(
                                                                                        version='any',
                                                                                        ref='bike_station_beta_B1@04'
                                                                                    ),
                                                                                ],
                                                                                transport_type_ref_or_vehicle_type_ref=[
                                                                                    SimpleVehicleTypeRef(
                                                                                        version='any',
                                                                                        ref='electric_cycle'
                                                                                    ),
                                                                                ],
                                                                                vehicle_model_ref=[
                                                                                    VehicleModelRef(
                                                                                        version='any',
                                                                                        ref='electric_boneshaker'
                                                                                    ),
                                                                                ],
                                                                                vehicle_model_profile_ref=[
                                                                                    CycleModelProfileRef(
                                                                                        version='any',
                                                                                        ref='boneKitB'
                                                                                    ),
                                                                                ],
                                                                                choice_2=[
                                                                                    VehicleSharingServiceRef(
                                                                                        version='any',
                                                                                        ref='metrobike'
                                                                                    ),
                                                                                ],
                                                                                vehicle_ref=[
                                                                                    VehicleRef(
                                                                                        version='any',
                                                                                        ref='C01'
                                                                                    ),
                                                                                ],
                                                                                distribution_channel_ref_or_group_of_distribution_channels_ref=[
                                                                                    DistributionChannelRef(
                                                                                        version='any',
                                                                                        ref='online'
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                            time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='metrobike@M90-eachM60'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    customer_purchase_packages=CustomerPurchasePackagesRelStructure(
                                                        customer_purchase_package_or_customer_purchase_package_ref=[
                                                            CustomerPurchasePackageRef(
                                                                version='any',
                                                                ref='mbt:Anon001@027'
                                                            ),
                                                        ]
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
                                        id='mbt:Good@Cust444@001',
                                        validity_conditions_or_valid_between=[
                                            ValidBetween(
                                                from_date=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                to_date=XmlDateTime(2023, 2, 28, 13, 0, 0)
                                            ),
                                        ],
                                        created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Membership'
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='mbt:Cust444'
                                        ),
                                        customer_account_ref=CustomerAccountRef(
                                            version='any',
                                            ref='mbt:Cust444@AC7651'
                                        ),
                                        customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                            customer_purchase_package_element=[
                                                CustomerPurchasePackageElement(
                                                    id='mbt:Good@Cust444@001',
                                                    created=XmlDateTime(2020, 2, 28, 13, 0, 0),
                                                    version='any',
                                                    sales_offer_package_element_ref=SalesOfferPackageElementRef(
                                                        version='any',
                                                        ref='metrobike_online@membership-SOP@mobile_app'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        ),
                                        sales_transaction_ref=SalesTransactionRef(
                                            version='any',
                                            ref='mbt:Cust444@contract001@t001@join_as_member'
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            ref='mbt:317867122222',
                                            version_ref='external'
                                        ),
                                        medium_application_instance_ref=MediumApplicationInstanceRef(
                                            ref='mbt:317867122222@mboik',
                                            version_ref='external'
                                        )
                                    ),
                                    CustomerPurchasePackage(
                                        id='mbt:Good@Cust444@005',
                                        validity_conditions_or_valid_between=[
                                            ValidBetween(
                                                from_date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                to_date=XmlDateTime(2020, 10, 8, 23, 59, 59)
                                            ),
                                        ],
                                        created=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                        changed=XmlDateTime(2020, 10, 8, 18, 35, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Day Pass'
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='mbt:Cust444'
                                        ),
                                        customer_account_ref=CustomerAccountRef(
                                            version='any',
                                            ref='mbt:Cust444@AC7651'
                                        ),
                                        customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                            customer_purchase_package_element=[
                                                CustomerPurchasePackageElement(
                                                    id='mbt:Good@Cust444@005',
                                                    created=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                    version='any',
                                                    sales_offer_package_element_ref=SalesOfferPackageElementRef(
                                                        version='any',
                                                        ref='metrobike@day_pass-SOP@mobileApp'
                                                    ),
                                                    element_accesses=CustomerPurchasePackageElementAccessesRelStructure(
                                                        customer_purchase_package_element_access=[
                                                            CustomerPurchasePackageElementAccess(
                                                                id='mbt:Good@Cust444@005@02',
                                                                created=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                                version='any',
                                                                access_number=1
                                                            ),
                                                            CustomerPurchasePackageElementAccess(
                                                                id='mbt:Good@Cust444@005@02',
                                                                created=XmlDateTime(2020, 10, 8, 15, 3, 0),
                                                                version='any',
                                                                access_number=2
                                                            ),
                                                            CustomerPurchasePackageElementAccess(
                                                                id='mbt:Good@Cust444@005@02',
                                                                created=XmlDateTime(2020, 10, 8, 18, 35, 0),
                                                                version='any',
                                                                access_number=2
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                        customer_purchase_parameter_assignment=[
                                                            CustomerPurchaseParameterAssignment(
                                                                id='mbt:Good@Cust444@005',
                                                                version='any',
                                                                order=1,
                                                                validity_parameters=ValidityParametersRelStructure(
                                                                    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                        VehicleSharingRef(
                                                                            version='any',
                                                                            ref='cycle_share'
                                                                        ),
                                                                    ],
                                                                    choice=[
                                                                        OperatorRef(
                                                                            version='any',
                                                                            ref='noc:MBIKE'
                                                                        ),
                                                                    ],
                                                                    choice_2=[
                                                                        VehicleSharingServiceRef(
                                                                            version='any',
                                                                            ref='metrobike'
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
                                            ref='mbt:Cust444@trans005@purchase_day_pass'
                                        ),
                                        prices=CustomerPurchasePackagePricesRelStructure(
                                            customer_purchase_package_price_ref_or_customer_purchase_package_price_or_cell_ref=[
                                                CustomerPurchasePackagePriceVersionedChildStructure(
                                                    id='mbt:Good@Cust444@005',
                                                    created=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                    version='any',
                                                    amount=Decimal('12.00'),
                                                    customer_purchase_package_ref_or_customer_purchase_package_element_ref=CustomerPurchasePackageRef(
                                                        version='any',
                                                        ref='mbt:Good@Cust444@005'
                                                    )
                                                ),
                                            ]
                                        ),
                                        travel_documents=TravelDocumentsRelStructure(
                                            choice=[
                                                ServiceAccessCode(
                                                    id='mbt:Good@Cust444@005@purchase_day_pass',
                                                    validity_conditions_or_valid_between=[
                                                        ValidBetween(
                                                            from_date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                            to_date=XmlDateTime(2020, 10, 9, 11, 2, 0)
                                                        ),
                                                    ],
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    customer_purchase_package_ref=CustomerPurchasePackageRef(
                                                        version='any',
                                                        ref='mbt:Good@Cust444@005'
                                                    ),
                                                    access_code='9876',
                                                    vehicle_access_credentials_assignment_ref=VehicleAccessCredentialsAssignmentRef(
                                                        version='any',
                                                        ref='mbt:Cust444@trans005@purchase_day_pase'
                                                    )
                                                ),
                                            ]
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            ref='mbt:317867122222',
                                            version_ref='external'
                                        ),
                                        medium_application_instance_ref=MediumApplicationInstanceRef(
                                            ref='mbt:317867122222@mboik',
                                            version_ref='external'
                                        )
                                    ),
                                    CustomerPurchasePackage(
                                        id='mbt:Anon001@027',
                                        validity_conditions_or_valid_between=[
                                            ValidBetween(
                                                from_date=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                to_date=XmlDateTime(2020, 12, 8, 14, 1, 0)
                                            ),
                                        ],
                                        created=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                        changed=XmlDateTime(2020, 12, 8, 14, 47, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Single session cycle use'
                                        ),
                                        customer_ref=CustomerRef(
                                            ref='mbt:Anon001',
                                            version_ref='EXTERNAL'
                                        ),
                                        customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                            customer_purchase_package_element=[
                                                CustomerPurchasePackageElement(
                                                    id='mbt:Anon001@027',
                                                    created=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                    version='any',
                                                    sales_offer_package_element_ref=SalesOfferPackageElementRef(
                                                        version='any',
                                                        ref='metrobike@day_pass-SOP@mobileApp'
                                                    ),
                                                    element_accesses=CustomerPurchasePackageElementAccessesRelStructure(
                                                        customer_purchase_package_element_access=[
                                                            CustomerPurchasePackageElementAccess(
                                                                id='mbt:Anon001@027@001',
                                                                created=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.ACTIVATED,
                                                                validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                                    customer_purchase_parameter_assignment=[
                                                                        CustomerPurchaseParameterAssignment(
                                                                            id='mbt:Anon001@027@001',
                                                                            created=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Checkout from station alpha_a1_001'
                                                                            ),
                                                                            order=1,
                                                                            validity_parameters=ValidityParametersRelStructure(
                                                                                choice_1=[
                                                                                    MonitoredVehicleSharingParkingBayRef(
                                                                                        version='any',
                                                                                        ref='bike_station_alpha_A1@01'
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CustomerPurchasePackageElementAccess(
                                                                id='mbt:Anon001@027@002',
                                                                created=XmlDateTime(2020, 12, 8, 14, 47, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.USED,
                                                                validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                                    customer_purchase_parameter_assignment=[
                                                                        CustomerPurchaseParameterAssignment(
                                                                            id='mbt:Anon001@027@002',
                                                                            created=XmlDateTime(2020, 12, 8, 14, 47, 0),
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Check back in to station beta_b1_004'
                                                                            ),
                                                                            order=1,
                                                                            validity_parameters=ValidityParametersRelStructure(
                                                                                choice_1=[
                                                                                    MonitoredVehicleSharingParkingBayRef(
                                                                                        version='any',
                                                                                        ref='bike_station_beta_B1@04'
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
                                                                id='mbt:Anon001@027',
                                                                version='any',
                                                                order=1,
                                                                validity_parameters=ValidityParametersRelStructure(
                                                                    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                        VehicleSharingRef(
                                                                            version='any',
                                                                            ref='cycle_share'
                                                                        ),
                                                                    ],
                                                                    choice=[
                                                                        OperatorRef(
                                                                            version='any',
                                                                            ref='noc:MBIKE'
                                                                        ),
                                                                    ],
                                                                    choice_2=[
                                                                        VehicleSharingServiceRef(
                                                                            version='any',
                                                                            ref='metrobike'
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
                                            ref='mbt:Anon001@trans069@purchase_single_session@checkout'
                                        ),
                                        sales_transactions=SalesTransactionRefsRelStructure(
                                            sales_transaction_ref=[
                                                SalesTransactionRef(
                                                    version='any',
                                                    ref='mbt:Anon001@trans069@purchase_single_session@return'
                                                ),
                                            ]
                                        ),
                                        prices=CustomerPurchasePackagePricesRelStructure(
                                            customer_purchase_package_price_ref_or_customer_purchase_package_price_or_cell_ref=[
                                                CustomerPurchasePackagePriceVersionedChildStructure(
                                                    id='mbt:Anon001@027',
                                                    created=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Intial prepayment'
                                                    ),
                                                    amount=Decimal('2.10'),
                                                    customer_purchase_package_ref_or_customer_purchase_package_element_ref=CustomerPurchasePackageRef(
                                                        version='any',
                                                        ref='mbt:Anon001@027'
                                                    )
                                                ),
                                                CustomerPurchasePackagePriceVersionedChildStructure(
                                                    id='mbt:Anon001@027',
                                                    created=XmlDateTime(2020, 12, 8, 14, 47, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Additional charge 3 + 4'
                                                    ),
                                                    amount=Decimal('7.00'),
                                                    customer_purchase_package_ref_or_customer_purchase_package_element_ref=CustomerPurchasePackageRef(
                                                        version='any',
                                                        ref='mbt:Anon001@027'
                                                    )
                                                ),
                                            ]
                                        ),
                                        travel_documents=TravelDocumentsRelStructure(
                                            choice=[
                                                ServiceAccessCode(
                                                    id='mbt:Anon001@027@purchase_single_session',
                                                    validity_conditions_or_valid_between=[
                                                        ValidBetween(
                                                            from_date=XmlDateTime(2020, 12, 8, 12, 1, 0),
                                                            to_date=XmlDateTime(2020, 12, 8, 12, 15, 0)
                                                        ),
                                                    ],
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    access_code='1234',
                                                    vehicle_access_credentials_assignment_ref=VehicleAccessCredentialsAssignmentRef(
                                                        version='any',
                                                        ref='mbt:Anon001@trans069@purchase_single_session@one_time'
                                                    )
                                                ),
                                            ]
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            ref='mbt:317867122222',
                                            version_ref='external'
                                        ),
                                        medium_application_instance_ref=MediumApplicationInstanceRef(
                                            ref='mbt:317867122222@mboik',
                                            version_ref='external'
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
