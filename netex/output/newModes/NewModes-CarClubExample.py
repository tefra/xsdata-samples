from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.account_status_type_enumeration import AccountStatusTypeEnumeration
from netex.models.activation_means_enumeration import ActivationMeansEnumeration
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType1
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import ValidBetween
from netex.models.branding import Branding
from netex.models.branding_ref import BrandingRef
from netex.models.car_model_profile import CarModelProfile
from netex.models.car_model_profile_ref import CarModelProfileRef
from netex.models.cell_versioned_child_structure import FarePricesRelStructure
from netex.models.cell_versioned_child_structure import FareTable1
from netex.models.cell_versioned_child_structure import FareTablesRelStructure
from netex.models.charging_moment_enumeration import ChargingMomentEnumeration
from netex.models.charging_policy import ChargingPolicy
from netex.models.charging_policy_ref import ChargingPolicyRef
from netex.models.child_seat_enumeration import ChildSeatEnumeration
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
from netex.models.covered_enumeration import CoveredEnumeration
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
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.data_role_type_enumeration import DataRoleTypeEnumeration
from netex.models.data_source import DataSource
from netex.models.data_source_ref_structure import DataSourceRefStructure
from netex.models.data_sources_in_frame_rel_structure import DataSourcesInFrameRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.deposit_policy_enumeration import DepositPolicyEnumeration
from netex.models.discounting_rule import DiscountingRule
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.distribution_assignment import DistributionAssignment
from netex.models.distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from netex.models.distribution_channel import DistributionChannel
from netex.models.distribution_channel_ref import DistributionChannelRef
from netex.models.distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from netex.models.distribution_channels_in_frame_rel_structure import DistributionChannelsInFrameRelStructure
from netex.models.distribution_rights_enumeration import DistributionRightsEnumeration
from netex.models.emv_card_ref import EmvCardRef
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.entitlement_constraint_structure import EntitlementConstraintStructure
from netex.models.entitlement_given import EntitlementGiven
from netex.models.entitlement_required import EntitlementRequired
from netex.models.entitlement_type_enumeration import EntitlementTypeEnumeration
from netex.models.equipments_rel_structure import EquipmentsRelStructure
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
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignment
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignmentsRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.info_link import InfoLink
from netex.models.info_links_rel_structure import InfoLinksRelStructure
from netex.models.layer_ref import LayerRef
from netex.models.licence_requirements_enumeration import LicenceRequirementsEnumeration
from netex.models.lighting_enumeration import LightingEnumeration
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
from netex.models.pos import Pos
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.preassigned_fare_product_enumeration import PreassignedFareProductEnumeration
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.price_rule_step_result_structure import PriceRuleStepResultStructure
from netex.models.price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from netex.models.priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.pricing_rules_rel_structure import PricingRulesRelStructure
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.propulsion_type_enumeration import PropulsionTypeEnumeration
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.refunding import Refunding
from netex.models.related_organisation import RelatedOrganisation
from netex.models.related_organisations_rel_structure import RelatedOrganisationsRelStructure
from netex.models.rental_availability import RentalAvailability
from netex.models.rental_penalty_policy import RentalPenaltyPolicy
from netex.models.rental_penalty_policy_ref import RentalPenaltyPolicyRef
from netex.models.rental_penalty_policy_type_enumeration import RentalPenaltyPolicyTypeEnumeration
from netex.models.resell_type_enumeration import ResellTypeEnumeration
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
from netex.models.sales_offer_package_price import SalesOfferPackagePrice
from netex.models.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.sales_transaction import SalesTransaction
from netex.models.sales_transaction_frame import SalesTransactionFrame
from netex.models.sales_transaction_ref import SalesTransactionRef
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
from netex.models.site_frame import SiteFrame
from netex.models.site_frame_ref import SiteFrameRef
from netex.models.specific_parameter_assignment_version_structure import SpecificParameterAssignment
from netex.models.specific_parameter_assignment_version_structure import SpecificParameterAssignmentsRelStructure
from netex.models.stakeholder_role_type_enumeration import StakeholderRoleTypeEnumeration
from netex.models.submode import Submode
from netex.models.submodes_rel_structure import SubmodesRelStructure
from netex.models.tariff import Tariff
from netex.models.tariff_basis_enumeration import TariffBasisEnumeration
from netex.models.tariff_ref import TariffRef
from netex.models.tariff_zone_1 import TariffZone1
from netex.models.tariff_zone_ref_1 import TariffZoneRef1
from netex.models.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.telephone_contact_structure import TelephoneContactStructure
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
from netex.models.transmission_enumeration import TransmissionEnumeration
from netex.models.transport_organisation_version_structure import TransportOrganisationVersionStructure
from netex.models.transport_type_refs_rel_structure import TransportTypeRefsRelStructure
from netex.models.transport_type_version_structure import TransportTypeVersionStructure
from netex.models.travel_document import TravelDocument
from netex.models.travel_documents_rel_structure import TravelDocumentsRelStructure
from netex.models.travel_specification_summary_view import TravelSpecificationSummaryView
from netex.models.travel_specifications_rel_structure import TravelSpecificationsRelStructure
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef
from netex.models.type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from netex.models.type_of_infolink_enumeration import TypeOfInfolinkEnumeration
from netex.models.type_of_proof_ref import TypeOfProofRef
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.type_of_travel_document_refs_rel_structure import TypeOfTravelDocumentRefsRelStructure
from netex.models.types_of_proof_refs_rel_structure import TypesOfProofRefsRelStructure
from netex.models.types_of_travel_document_in_frame_rel_structure import TypesOfTravelDocumentInFrameRelStructure
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_end_enumeration import UsageEndEnumeration
from netex.models.usage_parameter_price import UsageParameterPrice
from netex.models.usage_parameter_refs_rel_structure import UsageParameterRefsRelStructure
from netex.models.usage_parameters_rel_structure import UsageParametersRelStructure
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
from netex.models.vehicle_model import VehicleModel
from netex.models.vehicle_model_profiles_in_frame_rel_structure import VehicleModelProfilesInFrameRelStructure
from netex.models.vehicle_model_ref import VehicleModelRef
from netex.models.vehicle_models_in_frame_rel_structure import VehicleModelsInFrameRelStructure
from netex.models.vehicle_ref import VehicleRef
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
from netex.models.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure
from netex.models.vehicles_rel_structure import VehiclesRelStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2021, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2021, 12, 17, 9, 30, 46, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        ),
        description=MultilingualString(
            value='Request for Carclub tariff'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        validity_condition=[
                            AvailabilityCondition(
                                id='r1',
                                version='any',
                                from_date=XmlDateTime(2021, 1, 1, 0, 0, 0, 0, 0)
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
                                        ref='coc:MCR'
                                    ),
                                    VehicleSharingRef(
                                        version='any',
                                        ref='car_club'
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
        value='Example of Car Club   with prices'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='mc:car_club_example',
                validity_conditions_or_valid_between=[
                    ValidBetween(
                        from_date=XmlDateTime(2021, 1, 1, 0, 0, 0),
                        to_date=XmlDateTime(2021, 12, 31, 12, 0, 0)
                    ),
                ],
                data_source_ref_attribute='mc:my_car',
                version='1.0',
                responsibility_set_ref_attribute='mc:tariffs',
                name=MultilingualString(
                    value='Car Club  Example'
                ),
                description=MultilingualString(
                    value='This is an example showing how one might encode   a Car Club scheme "My Car"  in NeTEx.  It includes some  prices.'
                ),
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        CodespaceRef(
                            ref='mc_data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='mc_data'
                    ),
                    default_data_source_ref=DataSourceRefStructure(
                        version='any',
                        ref='mc:my_car'
                    ),
                    default_currency='EUR'
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ResourceFrame(
                            id='mc:car_club_example',
                            version='1.0',
                            responsibility_set_ref_attribute='mc:network_data',
                            name=MultilingualString(
                                value='Operator specific  common resources'
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    Codespace(
                                        id='mc_data',
                                        xmlns='mc',
                                        xmlns_url='http://www.mycar.com',
                                        description='Mycar data'
                                    ),
                                ]
                            ),
                            data_sources=DataSourcesInFrameRelStructure(
                                data_source=[
                                    DataSource(
                                        id='mc:my_car',
                                        version='any',
                                        email='feedback@mycar.com'
                                    ),
                                ]
                            ),
                            responsibility_sets=ResponsibilitySetsInFrameRelStructure(
                                responsibility_set=[
                                    ResponsibilitySet(
                                        id='mc:tariffs',
                                        version='any',
                                        name=MultilingualString(
                                            value='Operator Tariffs'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='mc:tariff_data@creates',
                                                    version='any',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.CREATES,
                                                    ],
                                                    stakeholder_role_type=[
                                                        StakeholderRoleTypeEnumeration.FARE_MANAGEMENT,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        value='My Car',
                                                        version='any',
                                                        ref='coc:MCR'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ResponsibilitySet(
                                        id='mc:network_data',
                                        version='any',
                                        name=MultilingualString(
                                            value='Operator data'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='mc:network_data@creates',
                                                    version='any',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.CREATES,
                                                    ],
                                                    stakeholder_role_type=[
                                                        StakeholderRoleTypeEnumeration.PLANNING,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        value='My Car',
                                                        version='any',
                                                        ref='coc:MCR'
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
                                            value='MyCar'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                Branding(
                                                    id='myBrand',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='My Car'
                                                    ),
                                                    url='https://www.mycar.com/static/images/colorways/myc/logo.png'
                                                ),
                                            ]
                                        ),
                                        class_of_values='Branding'
                                    ),
                                ]
                            ),
                            contacts=ContactsRelStructure(
                                contact=Contact(
                                    id='MCR',
                                    version='any',
                                    contact_details=ContactDetailsStructure(
                                        email='info@mycar.com',
                                        phone='+32 1293 449191'
                                    ),
                                    contact_type=ContactTypeEnumeration.INFORMATION
                                )
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    Operator(
                                        id='coc:MCR',
                                        version='any',
                                        public_code=PrivateCodeStructure(
                                            value='MBK'
                                        ),
                                        name=MultilingualString(
                                            value='My Car'
                                        ),
                                        short_name=MultilingualString(
                                            value='My Car'
                                        ),
                                        trading_name=MultilingualString(
                                            value='My Car Gmbh'
                                        ),
                                        contact_details=ContactStructure(
                                            contact_ref=ContactRef(
                                                version='any',
                                                ref='MCR'
                                            )
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.OPERATOR,
                                        ],
                                        related_organisations=RelatedOrganisationsRelStructure(
                                            related_organisation=[
                                                RelatedOrganisation(
                                                    id='coc:MCR',
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
                                            value=SelfDriveSubmodeEnumeration.HIRE_CAR
                                        ),
                                        mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=VehicleSharingRef(
                                            version='any',
                                            ref='car_club'
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
                                        id='car_club',
                                        version='any',
                                        name=MultilingualString(
                                            value='Car Club'
                                        ),
                                        description=MultilingualString(
                                            value='Cars available from fixed stations charge per period'
                                        ),
                                        submodes=SubmodesRelStructure(
                                            submode=[
                                                Submode(
                                                    id='car_club',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.SELF_DRIVE,
                                                    choice=SelfDriveSubmode(
                                                        value=SelfDriveSubmodeEnumeration.HIRE_CAR
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
                                        id='small_car',
                                        version='any',
                                        name=MultilingualString(
                                            value='Small car'
                                        ),
                                        reversing_direction=False,
                                        self_propelled=True,
                                        propulsion_type=PropulsionTypeEnumeration.ELECTRIC,
                                        fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(
                                            value=FuelTypeEnumeration.BATTERY
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.SELF_DRIVE,
                                        passenger_capacity=PassengerCapacityStructure(
                                            id='car_club',
                                            version='any',
                                            seating_capacity=4
                                        ),
                                        length=Decimal('3.5'),
                                        height=Decimal('1.6'),
                                        weight=Decimal('600'),
                                        licence_requirements=LicenceRequirementsEnumeration.FULL,
                                        vehicle_category=SimpleVehicleCategoryEnumeration.SMALL_CAR,
                                        minimum_age=18
                                    ),
                                ]
                            ),
                            vehicle_models=VehicleModelsInFrameRelStructure(
                                vehicle_model=[
                                    VehicleModel(
                                        id='mini_whiz',
                                        version='any',
                                        name=MultilingualString(
                                            value='Model A'
                                        ),
                                        transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                            version='any',
                                            ref='small_car'
                                        ),
                                        vehicle_model_profile_ref=CarModelProfileRef(
                                            version='any',
                                            ref='model_a'
                                        )
                                    ),
                                ]
                            ),
                            vehicle_model_profiles=VehicleModelProfilesInFrameRelStructure(
                                car_model_profile_or_cycle_model_profile=[
                                    CarModelProfile(
                                        id='model_a',
                                        version='any',
                                        child_seat=ChildSeatEnumeration.NONE,
                                        seats=4,
                                        doors=2,
                                        transmission=TransmissionEnumeration.AUTOMATIC,
                                        sat_nav=True,
                                        air_conditioning=True,
                                        convertible=False,
                                        usb_power_sockets=False,
                                        roof_rack=False,
                                        ski_rack=False
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='mc:car_club_example',
                            version='1.0',
                            responsibility_set_ref_attribute='mc:network_data',
                            name=MultilingualString(
                                value='Network data used by My Car 1'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='mc:car_club_example'
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
                                        id='car_station_alpha',
                                        version='any',
                                        name=MultilingualString(
                                            value='Car Station Alpha',
                                            lang='en'
                                        ),
                                        info_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='http:mycar.com/ios/car_station_alpha',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.INFO,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='http:mycar.com/android/car_station_alpha',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.INFO,
                                                    ],
                                                    target_platform='android'
                                                ),
                                                InfoLink(
                                                    value='http:mycar.com/web/car_station_alpha',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.INFO,
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
                                        covered=CoveredEnumeration.OUTDOORS,
                                        gated=GatedEnumeration.OPEN_AREA,
                                        lighting=LightingEnumeration.WELL_LIT,
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='Alphaville'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='coc:MCR'
                                        ),
                                        parking_type=ParkingTypeEnumeration.RENTAL_CAR_PARKING,
                                        parking_vehicle_types=[
                                            ParkingVehicleEnumeration.CAR,
                                        ],
                                        vehicle_types=TransportTypeRefsRelStructure(
                                            transport_type_ref_or_vehicle_type_ref=[
                                                SimpleVehicleTypeRef(
                                                    version='any',
                                                    ref='small_car'
                                                ),
                                            ]
                                        ),
                                        parking_layout=ParkingLayoutEnumeration.ROADSIDE,
                                        total_capacity=2,
                                        parking_properties=ParkingPropertiesRelStructure(
                                            parking_properties=[
                                                ParkingProperties(
                                                    id='car_station_alpha',
                                                    version='any',
                                                    parking_user_types=[
                                                        ParkingUserEnumeration.RENTAL,
                                                    ],
                                                    parking_vehicle_types=[
                                                        ParkingVehicleEnumeration.CAR,
                                                    ],
                                                    parking_visibility=ParkingVisibilityEnumeration.DEMARCATED
                                                ),
                                            ]
                                        ),
                                        parking_areas=ParkingAreasRelStructure(
                                            parking_area_ref_or_parking_area=[
                                                VehicleSharingParkingArea(
                                                    id='car_station_alpha_A1',
                                                    version='any',
                                                    total_capacity=2,
                                                    bays=ParkingBaysRelStructure(
                                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref_or_parking_bay=[
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='car_station_alpha_A1@01',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.CAR,
                                                                transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                                    version='any',
                                                                    ref='small_car'
                                                                ),
                                                                recharging_available=True
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='car_station_alpha_A1@02',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.CAR,
                                                                transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                                    version='any',
                                                                    ref='small_car'
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
                                        id='car_station_beta',
                                        version='any',
                                        name=MultilingualString(
                                            value='Car Station Beta',
                                            lang='en'
                                        ),
                                        cross_road=MultilingualString(
                                            value='Main Street'
                                        ),
                                        landmark=MultilingualString(
                                            value='Town Hall'
                                        ),
                                        covered=CoveredEnumeration.OUTDOORS,
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='Alphaville'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='coc:MCR'
                                        ),
                                        parking_type=ParkingTypeEnumeration.RENTAL_CAR_PARKING,
                                        parking_vehicle_types=[
                                            ParkingVehicleEnumeration.CAR,
                                        ],
                                        vehicle_types=TransportTypeRefsRelStructure(
                                            transport_type_ref_or_vehicle_type_ref=[
                                                SimpleVehicleTypeRef(
                                                    version='any',
                                                    ref='small_car'
                                                ),
                                            ]
                                        ),
                                        parking_layout=ParkingLayoutEnumeration.ROADSIDE,
                                        total_capacity=2,
                                        parking_properties=ParkingPropertiesRelStructure(
                                            parking_properties=[
                                                ParkingProperties(
                                                    id='car_station_beta',
                                                    version='any',
                                                    parking_user_types=[
                                                        ParkingUserEnumeration.RENTAL,
                                                    ],
                                                    parking_vehicle_types=[
                                                        ParkingVehicleEnumeration.CAR,
                                                    ],
                                                    parking_visibility=ParkingVisibilityEnumeration.DEMARCATED
                                                ),
                                            ]
                                        ),
                                        parking_areas=ParkingAreasRelStructure(
                                            parking_area_ref_or_parking_area=[
                                                VehicleSharingParkingArea(
                                                    id='car_station_beta_B1',
                                                    version='any',
                                                    total_capacity=2,
                                                    bays=ParkingBaysRelStructure(
                                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref_or_parking_bay=[
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='car_station_beta_B1@01',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.CAR,
                                                                transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                                    version='any',
                                                                    ref='small_car'
                                                                ),
                                                                recharging_available=True
                                                            ),
                                                            MonitoredVehicleSharingParkingBay(
                                                                id='car_station_beta_B1@02',
                                                                version='any',
                                                                parking_vehicle_type=ParkingVehicleEnumeration.CAR,
                                                                transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                                    version='any',
                                                                    ref='small_car'
                                                                ),
                                                                recharging_available=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            tariff_zones=TariffZonesInFrameRelStructure(
                                tariff_zone=[
                                    TariffZone1(
                                        id='AllMetropolis',
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
                            id='mc:car_club_example',
                            version='1.0',
                            responsibility_set_ref_attribute='mc:network_data',
                            name=MultilingualString(
                                value='Day Type devinitions'
                            ),
                            service_calendar=ServiceCalendar(
                                id='car_club_example',
                                version='any',
                                day_types=DayTypesRelStructure(
                                    day_type_ref_or_day_type=[
                                        DayType1(
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
                                        DayType1(
                                            id='non_working_day',
                                            version='any',
                                            name=MultilingualString(
                                                value='Working Day'
                                            ),
                                            properties=PropertiesOfDayRelStructure(
                                                property_of_day=[
                                                    PropertyOfDay(
                                                        days_of_week=[
                                                            DayOfWeekEnumeration.SATURDAY,
                                                            DayOfWeekEnumeration.SUNDAY,
                                                        ],
                                                        holiday_types=[
                                                            HolidayTypeEnumeration.ANY_DAY,
                                                        ]
                                                    ),
                                                    PropertyOfDay(
                                                        days_of_week=[
                                                            DayOfWeekEnumeration.WEEKDAYS,
                                                        ],
                                                        holiday_types=[
                                                            HolidayTypeEnumeration.ANY_HOLIDAY,
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
                            id='mc:car_club_example',
                            version='1.0',
                            responsibility_set_ref_attribute='mc:network_data',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='mc:car_club_example'
                                    ),
                                    ServiceCalendarFrameRef(
                                        version='1.0',
                                        ref='mc:car_club_example'
                                    ),
                                ]
                            ),
                            fleets=FleetsRelStructure(
                                fleet=[
                                    Fleet(
                                        id='mycar_fleet',
                                        version='any',
                                        name=MultilingualString(
                                            value='The My Car fleet'
                                        ),
                                        members=VehiclesRelStructure(
                                            vehicle_ref_or_vehicle=[
                                                Vehicle(
                                                    id='car_01',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='coc:MCR'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='small_car'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='mini_whiz'
                                                    ),
                                                    vehicle_model_profile_ref=CarModelProfileRef(
                                                        version='any',
                                                        ref='model_a'
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
                                                    id='car_02',
                                                    version='any',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='coc:MCR'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=SimpleVehicleTypeRef(
                                                        version='any',
                                                        ref='small_car'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='mini_whiz'
                                                    ),
                                                    vehicle_model_profile_ref=CarModelProfileRef(
                                                        version='any',
                                                        ref='model_a'
                                                    ),
                                                    actual_vehicle_equipments=EquipmentsRelStructure(
                                                        choice=[
                                                            VehicleReleaseEquipment(
                                                                id='P02@release',
                                                                version='any',
                                                                out_of_service=False,
                                                                remote_control=False,
                                                                local_control=True,
                                                                locking_mechanism=LockingMechanismEnumeration.IMMOBILISING_LOCK
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            mobility_services=MobilityServicesRelStructure(
                                mobility_service_or_common_vehicle_service_or_vehicle_pooling_service=[
                                    VehicleSharingService(
                                        id='my_car_club',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='My Car Club'
                                        ),
                                        info_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='http:mycar.com/info',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.INFO,
                                                    ]
                                                ),
                                                InfoLink(
                                                    value='http:mycar.com/ios',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='http:mycar.com/android',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='android'
                                                ),
                                                InfoLink(
                                                    value='http:mycar.com/ios',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='http:mycar.com/android',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='android'
                                                ),
                                            ]
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='coc:MCR'
                                        ),
                                        booking_required=False,
                                        registration_required=False,
                                        proposed_by_services=OnlineServiceRefsRelStructure(
                                            online_service_ref=[
                                                OnlineServiceRef(
                                                    version='any',
                                                    ref='mycar_online'
                                                ),
                                            ]
                                        ),
                                        vehicle_sharing_ref=VehicleSharingRef(
                                            version='any',
                                            ref='car_club'
                                        ),
                                        minimum_sharing_period=XmlDuration("PT30M"),
                                        maximum_sharing_period=XmlDuration("PT24H"),
                                        fleets=FleetRefsRelStructure(
                                            fleet_ref=[
                                                FleetRef(
                                                    version='any',
                                                    ref='mycar_fleet'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            online_services=OnlineServicesRelStructure(
                                online_service=[
                                    OnlineService(
                                        id='mycar_online',
                                        version='any',
                                        name=MultilingualString(
                                            value='Online registration for My Car'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        ),
                                        proposing_services=MobilityServiceRefsRelStructure(
                                            mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref=[
                                                VehicleSharingServiceRef(
                                                    version='any',
                                                    ref='my_car_club'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            vehicle_meeting_place_assignments=VehicleServicePlaceAssignmentsRelStructure(
                                vehicle_sharing_place_assignment_or_vehicle_pooling_place_assignment_or_taxi_service_place_assignment=[
                                    VehicleSharingPlaceAssignment(
                                        id='metrobik@car_station_alpha_A1',
                                        version='any',
                                        order=1,
                                        common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='my_car_club'
                                        ),
                                        vehicle_sharing_parking_area_ref=VehicleSharingParkingAreaRef(
                                            version='any',
                                            ref='car_station_alpha_A1'
                                        )
                                    ),
                                    VehicleSharingPlaceAssignment(
                                        id='car_station_beta',
                                        version='any',
                                        order=1,
                                        common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='my_car_club'
                                        ),
                                        vehicle_sharing_parking_area_ref=VehicleSharingParkingAreaRef(
                                            version='any',
                                            ref='car_station_beta_B1'
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='mc:car_club_example-single_session',
                            data_source_ref_attribute='mc:my_car',
                            version='1.0',
                            responsibility_set_ref_attribute='mc:tariffs',
                            name=MultilingualString(
                                value='My Car single session '
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    MobilityServiceFrameRef(
                                        version='1.0',
                                        ref='mc:car_club_example'
                                    ),
                                    SiteFrameRef(
                                        version='1.0',
                                        ref='mc:car_club_example'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='my_car@membership',
                                        version='any',
                                        name=MultilingualString(
                                            value='My Car Club Membership - Tariff'
                                        ),
                                        document_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://mycar.com/membership.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.INFO,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='coc:MCR'
                                        ),
                                        choice_1=VehicleSharingServiceRef(
                                            version='any',
                                            ref='my_car_club'
                                        ),
                                        time_intervals=TimeIntervalsRelStructure(
                                            time_interval_ref_or_time_interval=[
                                                TimeInterval(
                                                    id='my_car@1-year',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='One Year'
                                                    ),
                                                    duration=XmlDuration("P1Y")
                                                ),
                                            ]
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='my_car@membership@access',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Access rights'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:can_access',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='my_car@membership@access',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:condition_of_use',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                EntitlementGiven(
                                                                    id='mycar_online@membership@entitlements_given',
                                                                    version='any',
                                                                    choice=PreassignedFareProductRef(
                                                                        version='any',
                                                                        ref='my_car@single_session'
                                                                    ),
                                                                    entitlement_constraint=EntitlementConstraintStructure(
                                                                        user_constraint=SameUserEnumeration.SAME_PERSON
                                                                    ),
                                                                    entitlement_type=EntitlementTypeEnumeration.PURCHASE
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='my_car@membership@durations',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Any where in Zone'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access_when'
                                                    ),
                                                    time_interval_ref_or_time_intervals_or_time_structure_factors=TimeIntervalsRelStructure(
                                                        time_interval_ref_or_time_interval=[
                                                            TimeIntervalRef(
                                                                version='any',
                                                                ref='my_car@1-year'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='my_car@membership@eligibility',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Eligible user types'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:eligibility',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='my_car@membership@eligibility',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:eligible',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UserProfile(
                                                                    id='adult_driver',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Qualified driver'
                                                                    ),
                                                                    user_type=UserTypeEnumeration.ADULT,
                                                                    minimum_age=18,
                                                                    types_of_proof_required_ref=TypesOfProofRefsRelStructure(
                                                                        type_of_proof_ref=[
                                                                            TypeOfProofRef(
                                                                                ref='driving_licence',
                                                                                version_ref='external'
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='my_car@membership@conditions_of_travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions on travel'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:travel_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='my_car@membership@conditions_of_travel',
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
                                                                Transferability(
                                                                    id='my_car@membership@transferability',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Not Transferable  '
                                                                    ),
                                                                    can_transfer=False
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='my_car@membership@conditions_of_sale',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions of sale'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:sale_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='my_car@membership@conditions_of_sale',
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
                                                                    id='my_car@membership@charging_policy@refunding',
                                                                    version='any',
                                                                    allowed=ResellTypeEnumeration.NONE
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    Tariff(
                                        id='my_car@single_session',
                                        version='any',
                                        name=MultilingualString(
                                            value='My Car 1 - Tariff'
                                        ),
                                        document_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://mycar.com/tariff.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.INFO,
                                                    ]
                                                ),
                                                InfoLink(
                                                    value='https://mycar.com/tariffMap.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MAP,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='coc:MCR'
                                        ),
                                        choice_1=VehicleSharingServiceRef(
                                            version='any',
                                            ref='my_car_club'
                                        ),
                                        time_intervals=TimeIntervalsRelStructure(
                                            time_interval_ref_or_time_interval=[
                                                TimeInterval(
                                                    id='my_car@2-hours',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='First 2hours'
                                                    ),
                                                    duration=XmlDuration("PT2H")
                                                ),
                                                TimeInterval(
                                                    id='my_car@12-hours',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Half day'
                                                    ),
                                                    duration=XmlDuration("PT12H")
                                                ),
                                                TimeInterval(
                                                    id='my_car@1-day',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='1 dayr'
                                                    ),
                                                    duration=XmlDuration("P1D")
                                                ),
                                            ]
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='my_car@single_session@access',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Anywhere in Zone'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='my_car@single_session@access',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:can_access',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.AND,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            tariff_zone_ref=[
                                                                TariffZoneRef1(
                                                                    version='any',
                                                                    ref='AllMetropolis'
                                                                ),
                                                            ],
                                                            choice_2=[
                                                                VehicleSharingServiceRef(
                                                                    version='any',
                                                                    ref='my_car_club'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='my_car@single_session@durations',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Any where in Zone'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access_when'
                                                    ),
                                                    time_interval_ref_or_time_intervals_or_time_structure_factors=TimeIntervalsRelStructure(
                                                        time_interval_ref_or_time_interval=[
                                                            TimeIntervalRef(
                                                                version='any',
                                                                ref='my_car@2-hours'
                                                            ),
                                                            TimeIntervalRef(
                                                                version='any',
                                                                ref='my_car@12-hours'
                                                            ),
                                                            TimeIntervalRef(
                                                                version='any',
                                                                ref='my_car@1-day'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='my_car@single_session@eligibility',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Eligible user types'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:eligibility',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='my_car@single_session@eligibility',
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
                                                                    ref='adult_driver'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='my_car@single_session@conditions_of_travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions on travel'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:travel_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='my_car@single_session@conditions_of_travel',
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
                                                                    id='my_car@single_session@usageValidity',
                                                                    version='any',
                                                                    validity_period_type=UsageValidityTypeEnumeration.SINGLE_TRIP,
                                                                    usage_trigger=UsageTriggerEnumeration.ACTIVATION,
                                                                    usage_end=UsageEndEnumeration.PRODUCT_EXPIRY,
                                                                    activation_means=ActivationMeansEnumeration.ACCESS_CODE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='my_car@single_session@frequency',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='One trip  '
                                                                    ),
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    maximal_frequency=1
                                                                ),
                                                                Transferability(
                                                                    id='my_car@single_session@transferability',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Is Transferable - Transferee bust be eligible'
                                                                    ),
                                                                    can_transfer=False,
                                                                    shared_usage=SharedUsageEnumeration.SINGLE_USER
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='my_car@single_session@conditions_of_sale',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions of sale'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:sale_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='my_car@single_session@conditions_of_sale',
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
                                                                    id='my_car@single_session@charging_policy@Deposit',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Deposit'
                                                                    ),
                                                                    deposit_policy=DepositPolicyEnumeration.DEPOSIT_BLOCKED
                                                                ),
                                                                RentalPenaltyPolicy(
                                                                    id='my_car@single_session@hire_penalty@late_return',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Charge for late return'
                                                                    ),
                                                                    rental_penalty_policy_type=RentalPenaltyPolicyTypeEnumeration.LATE_VEHICLE_RETURN
                                                                ),
                                                                Refunding(
                                                                    id='my_car@single_session@refunding',
                                                                    version='any',
                                                                    allowed=ResellTypeEnumeration.PARTIAL
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
                                        id='mycar_online@membership',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='1 years membership of My Car online'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        ),
                                        validable_elements=ValidableElementsRelStructure(
                                            validable_element_ref_or_validable_element=[
                                                ValidableElement(
                                                    id='my_car@membership@travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Single  ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@membership@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@membership@durations'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@membership@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@membership@conditions_of_travel'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@membership@conditions_of_sale'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    PreassignedFareProduct(
                                        id='my_car@single_session',
                                        version='any',
                                        name=MultilingualString(
                                            value='One off care hire session'
                                        ),
                                        info_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://mycar.com/hirecheck_ios.htm',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MOBILE_APP_INSTALL_CHECK,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='https://mycar.com/hirecheck_android.htm ',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MOBILE_APP_INSTALL_CHECK,
                                                    ],
                                                    target_platform='android'
                                                ),
                                                InfoLink(
                                                    value='https://mycar.com/hire_ios.htm',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='ios'
                                                ),
                                                InfoLink(
                                                    value='https://mycar.com/hire_android.htm ',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MOBILE_APP_DOWNLOAD,
                                                    ],
                                                    target_platform='android'
                                                ),
                                            ]
                                        ),
                                        charging_moment_type=ChargingMomentEnumeration.BEFORE_TRAVEL_THEN_ADJUST_AT_END_OF_TRAVEL,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='coc:MCR'
                                        ),
                                        condition_summary=ConditionSummary(
                                            fare_structure_type=FareStructureTypeEnumeration.NETWORK_FLAT_FARE,
                                            tariff_basis=TariffBasisEnumeration.FLAT,
                                            is_refundable=False,
                                            requires_deposit=True,
                                            no_cash_payment=True,
                                            requires_reservation=True
                                        ),
                                        validable_elements=ValidableElementsRelStructure(
                                            validable_element_ref_or_validable_element=[
                                                ValidableElement(
                                                    id='my_car@single_session@travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Single  ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@single_session@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@single_session@durations'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@single_session@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@single_session@conditions_of_travel'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='my_car@single_session@conditions_of_sale'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='my_car@single_session',
                                                    version='any',
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='any',
                                                        ref='my_car@single_session@travel'
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
                                            PaymentMethodEnumeration.DIRECT_DEBIT,
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
                                        id='mycar_online@membership-SOP@mobile_app',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='My Car club membership'
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='mycar_online@membership-SOP@mobile_app',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=SaleDiscountRightRef(
                                                        version='any',
                                                        ref='mycar_online@membership'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='my_car@single_session-SOP@mobileApp',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='My Car one off Mobile app purchase'
                                        ),
                                        condition_summary=ConditionSummary(
                                            requires_account=True
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='my_car@single_session-SOP@mobileApp',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Must be Registered member of floggit'
                                                    ),
                                                    order=1,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            EntitlementRequired(
                                                                id='my_car@single_session-SOP@mobileApp@registered',
                                                                version='any',
                                                                choice=SaleDiscountRightRef(
                                                                    version='any',
                                                                    ref='mycar_online@membership'
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
                                                                ref='mycar_online'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='my_car@single_session-SOP@mobileApp',
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
                                                    id='my_car@single_session-SOP@mobileApp',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='any',
                                                        ref='my_car@single_session'
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
                            id='mc:car_club_example_prices',
                            data_source_ref_attribute='mc:my_car',
                            version='1.0',
                            responsibility_set_ref_attribute='mc:tariffs',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_currency='EUR'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='mc:car_club_example-single_session'
                                    ),
                                ]
                            ),
                            pricing_parameter_set=PricingParameterSet(
                                id='mc:car_club_example_Prices',
                                version='any',
                                pricing_rules=PricingRulesRelStructure(
                                    pricing_rule=[
                                        DiscountingRule(
                                            id='vat',
                                            version='any',
                                            name=MultilingualString(
                                                value='Vat '
                                            ),
                                            method_name='tax',
                                            discount_as_percentage=Decimal('-15')
                                        ),
                                    ]
                                )
                            ),
                            fare_tables=FareTablesInFrameRelStructure(
                                fare_table=[
                                    FareTable1(
                                        id='my_car_club',
                                        version='any',
                                        name=MultilingualString(
                                            value='My Car  prices'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='coc:MCR'
                                        ),
                                        limitations=UsageParameterRefsRelStructure(
                                            choice=[
                                                UserProfileRef(
                                                    version='any',
                                                    ref='adult_driver'
                                                ),
                                            ]
                                        ),
                                        specifics=FareTableSpecificsStructure(
                                            tariff_zone_ref=TariffZoneRef1(
                                                version='any',
                                                ref='AllMetropolis'
                                            ),
                                            choice_1=VehicleSharingServiceRef(
                                                version='any',
                                                ref='my_car_club'
                                            )
                                        ),
                                        includes=FareTablesRelStructure(
                                            fare_table_ref_or_fare_table=[
                                                FareTable1(
                                                    id='my_car@single_session',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='My Car one off use prices'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            SalesOfferPackageRef(
                                                                version='any',
                                                                ref='my_car@single_session-SOP@mobileApp'
                                                            ),
                                                        ]
                                                    ),
                                                    used_in=UsedInRefsRelStructure(
                                                        choice=[
                                                            TariffRef(
                                                                version='any',
                                                                ref='my_car@single_session'
                                                            ),
                                                        ]
                                                    ),
                                                    includes=FareTablesRelStructure(
                                                        fare_table_ref_or_fare_table=[
                                                            FareTable1(
                                                                id='my_car@single_session@rental',
                                                                version='any',
                                                                prices=FarePricesRelStructure(
                                                                    fare_price_ref_or_cell_ref_or_fare_price=[
                                                                        SalesOfferPackagePrice(
                                                                            id='mycar_online@membership-SOP@mobile_app',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Membership 1 year'
                                                                            ),
                                                                            amount=Decimal('30.00'),
                                                                            sales_offer_package_ref_or_sales_offer_package_element_ref=SalesOfferPackageRef(
                                                                                version='any',
                                                                                ref='mycar_online@membership-SOP@mobile_app'
                                                                            )
                                                                        ),
                                                                        UsageParameterPrice(
                                                                            id='my_car@single_session@charging_policy@Deposit',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Deposit - blocked'
                                                                            ),
                                                                            amount=Decimal('300.00'),
                                                                            choice=ChargingPolicyRef(
                                                                                version='any',
                                                                                ref='my_car@single_session@charging_policy@Deposit'
                                                                            )
                                                                        ),
                                                                        UsageParameterPrice(
                                                                            id='my_car@single_session@charging_policy@Deposit_Refund',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Deposit - unblocked'
                                                                            ),
                                                                            amount=Decimal('-300.00'),
                                                                            choice=ChargingPolicyRef(
                                                                                version='any',
                                                                                ref='my_car@single_session@charging_policy@Deposit'
                                                                            )
                                                                        ),
                                                                        TimeIntervalPrice(
                                                                            id='my_car@2-hours',
                                                                            version='any',
                                                                            amount=Decimal('45.00'),
                                                                            time_interval_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='my_car@2-hours'
                                                                            )
                                                                        ),
                                                                        TimeIntervalPrice(
                                                                            id='my_car@12-hours',
                                                                            version='any',
                                                                            amount=Decimal('60.00'),
                                                                            time_interval_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='my_car@12-hours'
                                                                            )
                                                                        ),
                                                                        TimeIntervalPrice(
                                                                            id='my_car@1-day',
                                                                            version='any',
                                                                            amount=Decimal('90.00'),
                                                                            time_interval_ref=TimeIntervalRef(
                                                                                version='any',
                                                                                ref='my_car@1-day'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            FareTable1(
                                                                id='my_car@hire_penalty',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='My Car penalty fees'
                                                                ),
                                                                limitations=UsageParameterRefsRelStructure(
                                                                    choice=[
                                                                        UserProfileRef(
                                                                            version='any',
                                                                            ref='adult_driver'
                                                                        ),
                                                                    ]
                                                                ),
                                                                prices=FarePricesRelStructure(
                                                                    fare_price_ref_or_cell_ref_or_fare_price=[
                                                                        UsageParameterPrice(
                                                                            id='my_car@single_session@hire_penalty@late_return',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Late return'
                                                                            ),
                                                                            amount=Decimal('100.00'),
                                                                            choice=RentalPenaltyPolicyRef(
                                                                                version='any',
                                                                                ref='my_car@single_session@hire_penalty@late_return'
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
                id='mc:car_club_example_transaction_examples',
                data_source_ref_attribute='mc:my_car',
                version='1.0',
                responsibility_set_ref_attribute='mc:transaction_data',
                name=MultilingualString(
                    value='Sample Transactions for My Car trips '
                ),
                prerequisites=VersionFrameRefsRelStructure(
                    version_frame_ref=[
                        CompositeFrameRef(
                            version='1.0',
                            ref='mc:car_club_example'
                        ),
                    ]
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        MobilityJourneyFrame(
                            id='mct:sample_transactions',
                            version='1.2',
                            vehicle_access_credentials=VehicleAccessCredentialAssignmentsRelStructure(
                                vehicle_access_credentials_assignment=[
                                    VehicleAccessCredentialsAssignment(
                                        id='mct:Cust444@trans005@purchase_single_session',
                                        version='any',
                                        order=1,
                                        common_vehicle_service_ref_or_vehicle_pooling_service_ref=VehicleSharingServiceRef(
                                            version='any',
                                            ref='my_car_club'
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            ref='mct:317867122222',
                                            version_ref='External'
                                        ),
                                        service_access_code_ref=ServiceAccessCodeRef(
                                            version='any',
                                            ref='mct:Good@Cust444@005@purchase_single_session'
                                        )
                                    ),
                                ]
                            ),
                            parking_log_entries=ParkingLogEntriesInFrameRelStructure(
                                parking_log_entry=[
                                    RentalAvailability(
                                        id='car_station_alpha@2021-10-08T11:15:00',
                                        version='any',
                                        name=MultilingualString(
                                            value='Before Checkout '
                                        ),
                                        date=XmlDateTime(2021, 10, 8, 11, 6, 55),
                                        parking_ref=ParkingRef(
                                            version='any',
                                            ref='car_station_alpha'
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
                                        id='car_station_alpha_A1@01@2021-10-08T11:15:00',
                                        version='any',
                                        date=XmlDateTime(2021, 10, 8, 11, 15, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='car_station_alpha_A1@01'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                    ParkingBayCondition(
                                        id='car_station_alpha_A1@02@2021-10-08T11:15:00',
                                        version='any',
                                        date=XmlDateTime(2021, 10, 8, 11, 15, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='car_station_alpha_A1@02'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                    RentalAvailability(
                                        id='car_station_alpha@2021-10-08T11:07:20',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Checkout '
                                        ),
                                        date=XmlDateTime(2021, 10, 8, 11, 7, 20),
                                        parking_ref=ParkingRef(
                                            version='any',
                                            ref='car_station_alpha'
                                        ),
                                        is_operational=True,
                                        is_renting=True,
                                        is_accepting_returns=True,
                                        available_vehicles=1,
                                        available_docks=1
                                    ),
                                    ParkingBayCondition(
                                        id='car_station_alpha_A1@01@2021-10-08T11:07:20',
                                        version='any',
                                        date=XmlDateTime(2021, 10, 8, 11, 7, 20),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='car_station_alpha_A1@01'
                                        ),
                                        status=ParkingBayStatusEnumeration.AVAILABLE
                                    ),
                                    RentalAvailability(
                                        id='car_station_alpha_A1@20@21-10-08T23:10:00',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Return'
                                        ),
                                        date=XmlDateTime(2021, 10, 8, 23, 10, 0),
                                        parking_ref=ParkingRef(
                                            version='any',
                                            ref='car_station_alpha'
                                        ),
                                        is_operational=True,
                                        is_renting=True,
                                        is_accepting_returns=True,
                                        available_vehicles=2,
                                        available_docks=0
                                    ),
                                    ParkingBayCondition(
                                        id='car_station_alpha_A1@01@2021-10-08T23:10:00',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Return'
                                        ),
                                        date=XmlDateTime(2021, 10, 8, 23, 10, 0),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=MonitoredVehicleSharingParkingBayRef(
                                            version='any',
                                            ref='car_station_alpha_A1@01'
                                        ),
                                        status=ParkingBayStatusEnumeration.IN_USE
                                    ),
                                ]
                            )
                        ),
                        SalesTransactionFrame(
                            id='mct:sample_transactions',
                            version='1.2',
                            name=MultilingualString(
                                value='My Car Sample Transactions'
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    CodespaceRef(
                                        ref='mc_data'
                                    ),
                                    Codespace(
                                        id='mc_transactions',
                                        xmlns='mct',
                                        xmlns_url='http://www.mycar.com/transactions',
                                        description='Operator transaction data'
                                    ),
                                ]
                            ),
                            customers=CustomersInFrameRelStructure(
                                customer=[
                                    Customer(
                                        id='mct:Cust444',
                                        version='any',
                                        surname='Johnson',
                                        first_name='Boris',
                                        title='Mr',
                                        gender=GenderEnumeration.MALE,
                                        email='boris@brexit.eu',
                                        email_verified=XmlDateTime(2021, 2, 28, 15, 0, 0),
                                        phone=TelephoneContactStructure(
                                            tel_national_number='07867122222',
                                            tel_country_code='41'
                                        ),
                                        phone_verified=XmlDateTime(2021, 2, 28, 16, 0, 0),
                                        customer_accounts=CustomerAccountsRelStructure(
                                            customer_account_ref_or_customer_account=[
                                                CustomerAccount(
                                                    id='mct:Cust444@AC7651',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bojo'
                                                    ),
                                                    start_date=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                                    customer_account_status_type=AccountStatusTypeEnumeration.ACTIVE,
                                                    customer_purchase_packages=CustomerPurchasePackageRefsRelStructure(
                                                        customer_purchase_package_ref=[
                                                            CustomerPurchasePackageRef(
                                                                version='any',
                                                                ref='mct:Good@Cust444@005'
                                                            ),
                                                        ]
                                                    ),
                                                    customer_payment_means_ref=CustomerPaymentMeansRef(
                                                        version='any',
                                                        ref='mct:Cust444@AC7651@p1'
                                                    ),
                                                    payment_means=CustomerPaymentMeansRelStructure(
                                                        customer_payment_means=[
                                                            CustomerPaymentMeans(
                                                                id='mct:Cust444@AC7651@p1',
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
                                                                id='mct:Cust444@AC7651@p2',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='B.Johnson mobile device'
                                                                ),
                                                                medium_access_device_ref=MobileDeviceRef(
                                                                    ref='mct:317867122222',
                                                                    version_ref='external'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    medium_access_devices=MediumAccessDeviceRefsRelStructure(
                                                        medium_access_device_ref=MobileDeviceRef(
                                                            ref='mct:317867122222',
                                                            version_ref='External'
                                                        )
                                                    )
                                                ),
                                            ]
                                        ),
                                        fare_contracts=FareContractsRelStructure(
                                            fare_contract_ref_or_fare_contract=[
                                                FareContract(
                                                    id='mct:Cust444@contract001',
                                                    version='any',
                                                    customer_ref=CustomerRef(
                                                        ref='mct:Cust444',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    fare_contract_entries=FareContractEntriesRelStructure(
                                                        choice=[
                                                            SalesTransaction(
                                                                id='mct:Cust444@contract001@t001@join_as_member',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Join As Member'
                                                                ),
                                                                date=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                                                type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                                    ref='fxc:product_purchase',
                                                                    version_ref='EXTERNAL'
                                                                ),
                                                                amount=Decimal('30.00'),
                                                                travel_specifications=TravelSpecificationsRelStructure(
                                                                    travel_specification_ref_or_travel_specification=[
                                                                        OfferedTravelSpecification(
                                                                            id='mct:Cust444@contract001@t001@join_as_member',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='1 year membership'
                                                                            ),
                                                                            date=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='any',
                                                                                ref='mct:Cust444@contract001@t001@join_as_member'
                                                                            ),
                                                                            fare_price_ref_or_cell_ref=SalesOfferPackagePriceRef(
                                                                                version='any',
                                                                                ref='mycar_online@membership-SOP@mobile_app'
                                                                            ),
                                                                            amount=Decimal('34.50'),
                                                                            rule_step_results=PriceRuleStepResultsRelStructure(
                                                                                rule_step_result=[
                                                                                    PriceRuleStepResultStructure(
                                                                                        fare_price_ref=SalesOfferPackagePriceRef(
                                                                                            version='any',
                                                                                            ref='mycar_online@membership-SOP@mobile_app'
                                                                                        ),
                                                                                        amount=Decimal('30.00'),
                                                                                        adjustment_amount=Decimal('4.50'),
                                                                                        discounting_rule_ref_or_pricing_rule_ref=DiscountingRuleRef(
                                                                                            version='any',
                                                                                            ref='vat'
                                                                                        ),
                                                                                        narrative=MultilingualString(
                                                                                            value='Add 15% VAT'
                                                                                        ),
                                                                                        id='mct:Cust444@contract001@t001@join_as_member@tax',
                                                                                        order=1
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                            start_of_validity=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                                                            end_of_validity=XmlDateTime(2022, 2, 28, 13, 0, 0),
                                                                            travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                                start=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                                                                authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                                    version='any',
                                                                                    ref='coc:MCR'
                                                                                ),
                                                                                choice=VehicleSharingServiceRef(
                                                                                    version='any',
                                                                                    ref='my_car_club'
                                                                                )
                                                                            ),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='mct:Cust444@contract001@t001@purchase_member',
                                                                                        version='any',
                                                                                        name=MultilingualString(
                                                                                            value='Join as member'
                                                                                        ),
                                                                                        order=1,
                                                                                        sales_offer_package_ref=SalesOfferPackageRef(
                                                                                            version='any',
                                                                                            ref='mycar_online@membership-SOP@mobile_app'
                                                                                        ),
                                                                                        time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref=TimeIntervalRef(
                                                                                            version='any',
                                                                                            ref='my_car@1-day'
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
                                                                            ref='mct:Good@Cust444@001'
                                                                        ),
                                                                    ]
                                                                ),
                                                                travel_documents=TravelDocumentsRelStructure(
                                                                    choice=[
                                                                        TravelDocument(
                                                                            id='mbt:ticket@m-0345',
                                                                            validity_conditions_or_valid_between=[
                                                                                ValidBetween(
                                                                                    from_date=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                                                                    to_date=XmlDateTime(2022, 2, 28, 12, 59, 59)
                                                                                ),
                                                                            ],
                                                                            version='any',
                                                                            type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                                                version='any',
                                                                                ref='mobile_application_data'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            SalesTransaction(
                                                                id='mct:Cust444@trans005@purchase_single_session',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Book and pay for  1-day use of a car'
                                                                ),
                                                                date=XmlDateTime(2021, 10, 1, 10, 10, 0),
                                                                type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                                    ref='fxc:product_purchase',
                                                                    version_ref='EXTERNAL'
                                                                ),
                                                                amount=Decimal('103.50'),
                                                                rule_step_results=PriceRuleStepResultsRelStructure(
                                                                    rule_step_result=[
                                                                        PriceRuleStepResultStructure(
                                                                            fare_price_ref=TimeIntervalPriceRef(
                                                                                version='any',
                                                                                ref='my_car@1-day'
                                                                            ),
                                                                            amount=Decimal('90.00'),
                                                                            adjustment_amount=Decimal('13.50'),
                                                                            discounting_rule_ref_or_pricing_rule_ref=DiscountingRuleRef(
                                                                                version='any',
                                                                                ref='vat'
                                                                            ),
                                                                            narrative=MultilingualString(
                                                                                value='Add 15% VAT'
                                                                            ),
                                                                            id='mct:Cust444@trans005@purchase_single_session@tax',
                                                                            order=1
                                                                        ),
                                                                    ]
                                                                ),
                                                                payment_method=PaymentMethodEnumeration.CREDIT_CARD,
                                                                travel_specifications=TravelSpecificationsRelStructure(
                                                                    travel_specification_ref_or_travel_specification=[
                                                                        OfferedTravelSpecification(
                                                                            id='mct:Cust444@trans005@purchase_single_session',
                                                                            version='any',
                                                                            date=XmlDateTime(2021, 10, 8, 11, 15, 0),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='any',
                                                                                ref='mct:Cust444@trans005@purchase_single_session'
                                                                            ),
                                                                            fare_price_ref_or_cell_ref=TimeIntervalPriceRef(
                                                                                version='any',
                                                                                ref='my_car@1-day'
                                                                            ),
                                                                            amount=Decimal('90.00'),
                                                                            start_of_validity=XmlDateTime(2021, 10, 8, 11, 15, 0),
                                                                            travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                                start=XmlDateTime(2021, 10, 8, 11, 15, 0),
                                                                                end=XmlDateTime(2021, 10, 9, 11, 14, 59),
                                                                                duration=XmlDuration("P1D"),
                                                                                choice=VehicleSharingServiceRef(
                                                                                    version='any',
                                                                                    ref='my_car_club'
                                                                                )
                                                                            ),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='mct:Cust444@trans005@purchase_single_session',
                                                                                        version='any',
                                                                                        name=MultilingualString(
                                                                                            value='Single session'
                                                                                        ),
                                                                                        order=1,
                                                                                        validable_element_ref=ValidableElementRef(
                                                                                            version='any',
                                                                                            ref='my_car@single_session@travel'
                                                                                        ),
                                                                                        preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                                                            version='any',
                                                                                            ref='my_car@single_session'
                                                                                        ),
                                                                                        fare_structure_element_ref=FareStructureElementRef(
                                                                                            version='any',
                                                                                            ref='my_car@single_session@access'
                                                                                        ),
                                                                                        sales_offer_package_ref=SalesOfferPackageRef(
                                                                                            version='any',
                                                                                            ref='my_car@single_session-SOP@mobileApp'
                                                                                        ),
                                                                                        validity_parameters=ValidityParametersRelStructure(
                                                                                            mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                                                VehicleSharingRef(
                                                                                                    version='any',
                                                                                                    ref='car_club'
                                                                                                ),
                                                                                            ],
                                                                                            choice=[
                                                                                                OperatorRef(
                                                                                                    version='any',
                                                                                                    ref='coc:MCR'
                                                                                                ),
                                                                                                OnlineServiceOperatorRef(
                                                                                                    version='any',
                                                                                                    ref='floggit'
                                                                                                ),
                                                                                            ],
                                                                                            choice_1=[
                                                                                                VehicleSharingParkingAreaRef(
                                                                                                    version='any',
                                                                                                    ref='car_station_alpha_A1'
                                                                                                ),
                                                                                                MonitoredVehicleSharingParkingBayRef(
                                                                                                    version='any',
                                                                                                    ref='car_station_alpha_A1@01'
                                                                                                ),
                                                                                            ],
                                                                                            vehicle_model_profile_ref=[
                                                                                                CarModelProfileRef(
                                                                                                    version='any',
                                                                                                    ref='model_a'
                                                                                                ),
                                                                                            ],
                                                                                            choice_2=[
                                                                                                VehicleSharingServiceRef(
                                                                                                    version='any',
                                                                                                    ref='my_car_club'
                                                                                                ),
                                                                                            ],
                                                                                            vehicle_ref=[
                                                                                                VehicleRef(
                                                                                                    version='any',
                                                                                                    ref='car_01'
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
                                                                                            ref='my_car@1-day'
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
                                                                            ref='mct:Good@Cust444@005'
                                                                        ),
                                                                    ]
                                                                ),
                                                                travel_documents=TravelDocumentsRelStructure(
                                                                    choice=[
                                                                        ServiceAccessCodeRef(
                                                                            version='any',
                                                                            ref='mct:Good@Cust444@005@purchase_single_session'
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
                            customer_purchase_packages=CustomerPurchasePackagesInFrameRelStructure(
                                customer_purchase_package=[
                                    CustomerPurchasePackage(
                                        id='mct:Good@Cust444@001',
                                        validity_conditions_or_valid_between=[
                                            ValidBetween(
                                                from_date=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                                to_date=XmlDateTime(2022, 2, 28, 13, 0, 0)
                                            ),
                                        ],
                                        created=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Membership'
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='mct:Cust444'
                                        ),
                                        customer_account_ref=CustomerAccountRef(
                                            version='any',
                                            ref='mct:Cust444@AC7651'
                                        ),
                                        customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                            customer_purchase_package_element=[
                                                CustomerPurchasePackageElement(
                                                    id='mct:Good@Cust444@001',
                                                    created=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                                    version='any',
                                                    sales_offer_package_element_ref=SalesOfferPackageElementRef(
                                                        version='any',
                                                        ref='mycar_online@membership-SOP@mobile_app'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        ),
                                        sales_transaction_ref=SalesTransactionRef(
                                            version='any',
                                            ref='mct:Cust444@contract001@t001@join_as_member'
                                        ),
                                        prices=CustomerPurchasePackagePricesRelStructure(
                                            customer_purchase_package_price_ref_or_customer_purchase_package_price_or_cell_ref=[
                                                CustomerPurchasePackagePriceVersionedChildStructure(
                                                    id='mct:Good@Cust444@001',
                                                    created=XmlDateTime(2021, 2, 28, 13, 0, 0),
                                                    version='any',
                                                    amount=Decimal('34.50'),
                                                    rule_step_results=PriceRuleStepResultsRelStructure(
                                                        rule_step_result=[
                                                            PriceRuleStepResultStructure(
                                                                fare_price_ref=SalesOfferPackagePriceRef(
                                                                    version='any',
                                                                    ref='mycar_online@membership-SOP@mobile_app'
                                                                ),
                                                                amount=Decimal('30.00'),
                                                                adjustment_amount=Decimal('4.50'),
                                                                discounting_rule_ref_or_pricing_rule_ref=DiscountingRuleRef(
                                                                    version='any',
                                                                    ref='vat'
                                                                ),
                                                                narrative=MultilingualString(
                                                                    value='Add 15% VAT'
                                                                ),
                                                                id='mct:Good@Cust444@001@tax',
                                                                order=1
                                                            ),
                                                        ]
                                                    ),
                                                    customer_purchase_package_ref_or_customer_purchase_package_element_ref=CustomerPurchasePackageRef(
                                                        version='any',
                                                        ref='mct:Good@Cust444@001'
                                                    )
                                                ),
                                            ]
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            ref='mct:317867122222',
                                            version_ref='external'
                                        ),
                                        medium_application_instance_ref=MediumApplicationInstanceRef(
                                            ref='mct:317867122222@mboik',
                                            version_ref='external'
                                        )
                                    ),
                                    CustomerPurchasePackage(
                                        id='mct:Good@Cust444@005',
                                        validity_conditions_or_valid_between=[
                                            ValidBetween(
                                                from_date=XmlDateTime(2021, 10, 8, 11, 15, 0),
                                                to_date=XmlDateTime(2021, 10, 8, 23, 59, 59)
                                            ),
                                        ],
                                        created=XmlDateTime(2021, 10, 1, 10, 10, 0),
                                        changed=XmlDateTime(2021, 10, 8, 23, 10, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Day Hire on  2021-10-08  at 11:15:00 '
                                        ),
                                        customer_ref=CustomerRef(
                                            version='any',
                                            ref='mct:Cust444'
                                        ),
                                        customer_account_ref=CustomerAccountRef(
                                            version='any',
                                            ref='mct:Cust444@AC7651'
                                        ),
                                        customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                            customer_purchase_package_element=[
                                                CustomerPurchasePackageElement(
                                                    id='mct:Good@Cust444@005',
                                                    created=XmlDateTime(2021, 10, 1, 10, 10, 0),
                                                    version='any',
                                                    sales_offer_package_element_ref=SalesOfferPackageElementRef(
                                                        version='any',
                                                        ref='my_car@single_session-SOP@mobileApp'
                                                    ),
                                                    element_accesses=CustomerPurchasePackageElementAccessesRelStructure(
                                                        customer_purchase_package_element_access=[
                                                            CustomerPurchasePackageElementAccess(
                                                                id='mct:Good@Cust444@005@02',
                                                                created=XmlDateTime(2021, 10, 1, 10, 10, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.UNUSED,
                                                                access_number=1
                                                            ),
                                                            CustomerPurchasePackageElementAccess(
                                                                id='mct:Good@Cust444@005@02',
                                                                created=XmlDateTime(2021, 10, 8, 11, 15, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.ACTIVATED,
                                                                access_number=1
                                                            ),
                                                            CustomerPurchasePackageElementAccess(
                                                                id='mct:Good@Cust444@005@02',
                                                                created=XmlDateTime(2021, 10, 8, 23, 10, 0),
                                                                version='any',
                                                                marked_as=MarkedAsEnumeration.EXPIRED,
                                                                access_number=1
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                        customer_purchase_parameter_assignment=[
                                                            CustomerPurchaseParameterAssignment(
                                                                id='mct:Good@Cust444@005',
                                                                version='any',
                                                                order=1,
                                                                validity_parameters=ValidityParametersRelStructure(
                                                                    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                        VehicleSharingRef(
                                                                            ref='car_club'
                                                                        ),
                                                                    ],
                                                                    choice=[
                                                                        OperatorRef(
                                                                            version='any',
                                                                            ref='coc:MCR'
                                                                        ),
                                                                    ],
                                                                    choice_2=[
                                                                        VehicleSharingServiceRef(
                                                                            version='any',
                                                                            ref='my_car_club'
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
                                                                    ref='my_car@1-day'
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
                                            ref='mct:Cust444@trans005@purchase_single_session'
                                        ),
                                        prices=CustomerPurchasePackagePricesRelStructure(
                                            customer_purchase_package_price_ref_or_customer_purchase_package_price_or_cell_ref=[
                                                CustomerPurchasePackagePriceVersionedChildStructure(
                                                    id='mct:Good@Cust444@005',
                                                    created=XmlDateTime(2021, 10, 1, 10, 10, 0),
                                                    version='any',
                                                    amount=Decimal('103.50'),
                                                    rule_step_results=PriceRuleStepResultsRelStructure(
                                                        rule_step_result=[
                                                            PriceRuleStepResultStructure(
                                                                fare_price_ref=TimeIntervalPriceRef(
                                                                    version='any',
                                                                    ref='my_car@1-day'
                                                                ),
                                                                amount=Decimal('90.00'),
                                                                adjustment_amount=Decimal('13.50'),
                                                                discounting_rule_ref_or_pricing_rule_ref=DiscountingRuleRef(
                                                                    version='any',
                                                                    ref='vat'
                                                                ),
                                                                narrative=MultilingualString(
                                                                    value='Add 15% VAT'
                                                                ),
                                                                id='mct:Good@Cust444@005@tax',
                                                                order=1
                                                            ),
                                                        ]
                                                    ),
                                                    customer_purchase_package_ref_or_customer_purchase_package_element_ref=CustomerPurchasePackageRef(
                                                        version='any',
                                                        ref='mct:Good@Cust444@005'
                                                    )
                                                ),
                                            ]
                                        ),
                                        travel_documents=TravelDocumentsRelStructure(
                                            choice=[
                                                ServiceAccessCode(
                                                    id='mct:Good@Cust444@005@purchase_single_session',
                                                    validity_conditions_or_valid_between=[
                                                        ValidBetween(
                                                            from_date=XmlDateTime(2021, 10, 8, 11, 15, 0),
                                                            to_date=XmlDateTime(2021, 10, 9, 11, 14, 59)
                                                        ),
                                                    ],
                                                    created=XmlDateTime(2021, 10, 1, 10, 10, 0),
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='mobile_application_data'
                                                    ),
                                                    customer_purchase_package_ref=CustomerPurchasePackageRef(
                                                        version='any',
                                                        ref='mct:Good@Cust444@005'
                                                    ),
                                                    access_code='9876',
                                                    vehicle_access_credentials_assignment_ref=VehicleAccessCredentialsAssignmentRef(
                                                        version='any',
                                                        ref='mct:Cust444@trans005@purchase_day_pase'
                                                    )
                                                ),
                                            ]
                                        ),
                                        medium_access_device_ref=MobileDeviceRef(
                                            ref='mct:317867122222',
                                            version_ref='external'
                                        ),
                                        medium_application_instance_ref=MediumApplicationInstanceRef(
                                            ref='mct:31786712244@mboik',
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
