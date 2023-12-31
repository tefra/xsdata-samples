from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.address_ref import AddressRef
from netex.models.addressable_place_ref import AddressablePlaceRef
from netex.models.addresses_in_frame_rel_structure import AddressesInFrameRelStructure
from netex.models.air_submode_enumeration import AirSubmodeEnumeration
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import ValidBetween
from netex.models.booking_access_enumeration import BookingAccessEnumeration
from netex.models.booking_arrangements_structure import BookingArrangementsStructure
from netex.models.booking_charge_type_enumeration import BookingChargeTypeEnumeration
from netex.models.booking_method_enumeration import BookingMethodEnumeration
from netex.models.branding import Branding
from netex.models.branding_ref import BrandingRef
from netex.models.cancelling import Cancelling
from netex.models.car_model_profile import CarModelProfile
from netex.models.car_model_profile_ref import CarModelProfileRef
from netex.models.catering_facility_enumeration import CateringFacilityEnumeration
from netex.models.cell_versioned_child_structure import FarePricesRelStructure
from netex.models.cell_versioned_child_structure import FareTable
from netex.models.charging_moment_enumeration import ChargingMomentEnumeration
from netex.models.chauffeured_vehicle_service import ChauffeuredVehicleService
from netex.models.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.models.codespace import Codespace
from netex.models.codespace_ref import CodespaceRef
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.companion_profile import CompanionProfile
from netex.models.companion_profiles_rel_structure import CompanionProfilesRelStructure
from netex.models.composite_frame_ref import CompositeFrameRef
from netex.models.condition_summary import ConditionSummary
from netex.models.contact_structure import ContactStructure
from netex.models.country_ref import CountryRef
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.customer_ref import CustomerRef
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.data_role_type_enumeration import DataRoleTypeEnumeration
from netex.models.data_source import DataSource
from netex.models.data_source_ref_structure import DataSourceRefStructure
from netex.models.data_sources_in_frame_rel_structure import DataSourcesInFrameRelStructure
from netex.models.discount_basis_enumeration import DiscountBasisEnumeration
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
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.fare_contract import FareContract
from netex.models.fare_contract_entries_rel_structure import FareContractEntriesRelStructure
from netex.models.fare_contracts_in_frame_rel_structure import FareContractsInFrameRelStructure
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
from netex.models.fleets_rel_structure import FleetsRelStructure
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.models.fuel_type_enumeration import FuelTypeEnumeration
from netex.models.fulfilment_method import FulfilmentMethod
from netex.models.fulfilment_method_ref import FulfilmentMethodRef
from netex.models.fulfilment_method_type_enumeration import FulfilmentMethodTypeEnumeration
from netex.models.fulfilment_methods_in_frame_rel_structure import FulfilmentMethodsInFrameRelStructure
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignment
from netex.models.iana_country_tld_enumeration import IanaCountryTldEnumeration
from netex.models.info_link import InfoLink
from netex.models.info_links_rel_structure import InfoLinksRelStructure
from netex.models.layer_ref import LayerRef
from netex.models.location_structure_2 import LocationStructure2
from netex.models.logical_operation_enumeration import LogicalOperationEnumeration
from netex.models.media_type_enumeration import MediaTypeEnumeration
from netex.models.meeting_usage_enumeration import MeetingUsageEnumeration
from netex.models.mobility_journey_frame import MobilityJourneyFrame
from netex.models.mobility_service_frame import MobilityServiceFrame
from netex.models.mobility_service_frame_ref import MobilityServiceFrameRef
from netex.models.mobility_service_refs_rel_structure import MobilityServiceRefsRelStructure
from netex.models.mobility_services_rel_structure import MobilityServicesRelStructure
from netex.models.modes_of_operation_rel_structure import ModesOfOperationRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.network_filter_by_value_structure import NetworkFilterByValueStructure
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from netex.models.object_filter_by_value_structure import ObjectFilterByValueStructure
from netex.models.offered_travel_specification import OfferedTravelSpecification
from netex.models.online_service import OnlineService
from netex.models.online_service_operator import OnlineServiceOperator
from netex.models.online_service_operator_ref import OnlineServiceOperatorRef
from netex.models.online_service_ref import OnlineServiceRef
from netex.models.online_service_refs_rel_structure import OnlineServiceRefsRelStructure
from netex.models.online_services_rel_structure import OnlineServicesRelStructure
from netex.models.onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from netex.models.operating_day_ref import OperatingDayRef
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.organisation_type_enumeration import OrganisationTypeEnumeration
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.parking import Parking
from netex.models.parking_areas_rel_structure import ParkingAreasRelStructure
from netex.models.parking_bay import ParkingBay
from netex.models.parking_bay_ref import ParkingBayRef
from netex.models.parking_bays_rel_structure import ParkingBaysRelStructure
from netex.models.parking_type_enumeration import ParkingTypeEnumeration
from netex.models.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.models.parkings_in_frame_rel_structure import ParkingsInFrameRelStructure
from netex.models.passenger_capacity_structure import PassengerCapacityStructure
from netex.models.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.point_in_single_journey_path_ref import PointInSingleJourneyPathRef
from netex.models.point_of_interest import PointOfInterest
from netex.models.point_of_interest_ref import PointOfInterestRef
from netex.models.point_ref_structure import PointRefStructure
from netex.models.points_of_interest_in_frame_rel_structure import PointsOfInterestInFrameRelStructure
from netex.models.postal_address import PostalAddress
from netex.models.postal_address_version_structure import PostalAddressVersionStructure
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.preassigned_fare_product_enumeration import PreassignedFareProductEnumeration
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from netex.models.propulsion_type_enumeration import PropulsionTypeEnumeration
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.models.purchase_when_enumeration import PurchaseWhenEnumeration
from netex.models.quay import Quay
from netex.models.quay_ref import QuayRef
from netex.models.quay_type_enumeration import QuayTypeEnumeration
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.rail_submode_enumeration import RailSubmodeEnumeration
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.responsibility_role_assignment import ResponsibilityRoleAssignment
from netex.models.responsibility_role_assignments_rel_structure import ResponsibilityRoleAssignmentsRelStructure
from netex.models.responsibility_set import ResponsibilitySet
from netex.models.responsibility_sets_in_frame_rel_structure import ResponsibilitySetsInFrameRelStructure
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.sales_transaction import SalesTransaction
from netex.models.sales_transaction_frame import SalesTransactionFrame
from netex.models.sales_transaction_ref import SalesTransactionRef
from netex.models.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.models.scheduled_operation import ScheduledOperation
from netex.models.scheduled_operation_type_enumeration import ScheduledOperationTypeEnumeration
from netex.models.service_booking_arrangements_structure import ServiceBookingArrangementsStructure
from netex.models.service_facility_set import ServiceFacilitySet
from netex.models.service_facility_set_ref import ServiceFacilitySetRef
from netex.models.service_facility_sets_in_frame_rel_structure import ServiceFacilitySetsInFrameRelStructure
from netex.models.service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.single_journey import SingleJourney
from netex.models.single_journey_path import SingleJourneyPath
from netex.models.single_journey_paths_rel_structure import SingleJourneyPathsRelStructure
from netex.models.single_journey_ref import SingleJourneyRef
from netex.models.single_journeys_rel_structure import SingleJourneysRelStructure
from netex.models.site_frame import SiteFrame
from netex.models.site_frame_ref import SiteFrameRef
from netex.models.site_ref_structure import SiteRefStructure
from netex.models.site_refs_rel_structure import SiteRefsRelStructure
from netex.models.site_type_enumeration import SiteTypeEnumeration
from netex.models.specific_parameter_assignment_version_structure import SpecificParameterAssignment
from netex.models.specific_parameter_assignment_version_structure import SpecificParameterAssignmentsRelStructure
from netex.models.stakeholder_role_type_enumeration import StakeholderRoleTypeEnumeration
from netex.models.stop_place import StopPlace
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.submode import Submode
from netex.models.submodes_rel_structure import SubmodesRelStructure
from netex.models.target_passing_time import TargetPassingTime
from netex.models.target_passing_times_rel_structure import TargetPassingTimesRelStructure
from netex.models.tariff import Tariff
from netex.models.tariff_basis_enumeration import TariffBasisEnumeration
from netex.models.tariff_ref import TariffRef
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.taxi_parking_area import TaxiParkingArea
from netex.models.taxi_rank import TaxiRank
from netex.models.taxi_stand import TaxiStand
from netex.models.taxi_stands_rel_structure import TaxiStandsRelStructure
from netex.models.taxi_submode_enumeration import TaxiSubmodeEnumeration
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.time_interval import TimeInterval
from netex.models.time_interval_price import TimeIntervalPrice
from netex.models.time_interval_ref import TimeIntervalRef
from netex.models.time_intervals_rel_structure import TimeIntervalsRelStructure
from netex.models.time_unit import TimeUnit
from netex.models.time_units_rel_structure import TimeUnitsRelStructure
from netex.models.topographic_place import TopographicPlace
from netex.models.topographic_place_descriptor_versioned_child_structure import TopographicPlaceDescriptorVersionedChildStructure
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.topographic_place_ref_structure import TopographicPlaceRefStructure
from netex.models.topographic_place_refs_rel_structure import TopographicPlaceRefsRelStructure
from netex.models.topographic_places_in_frame_rel_structure import TopographicPlacesInFrameRelStructure
from netex.models.transport_submode import TransportSubmode
from netex.models.travel_document import TravelDocument
from netex.models.travel_documents_rel_structure import TravelDocumentsRelStructure
from netex.models.travel_specification_summary_endpoint_structure import TravelSpecificationSummaryEndpointStructure
from netex.models.travel_specification_summary_view import TravelSpecificationSummaryView
from netex.models.travel_specifications_rel_structure import TravelSpecificationsRelStructure
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef
from netex.models.type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from netex.models.type_of_infolink_enumeration import TypeOfInfolinkEnumeration
from netex.models.type_of_parking import TypeOfParking
from netex.models.type_of_parking_ref import TypeOfParkingRef
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.type_of_travel_document_refs_rel_structure import TypeOfTravelDocumentRefsRelStructure
from netex.models.types_of_travel_document_in_frame_rel_structure import TypesOfTravelDocumentInFrameRelStructure
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_end_enumeration import UsageEndEnumeration
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
from netex.models.vehicle_meeting_link import VehicleMeetingLink
from netex.models.vehicle_meeting_link_ref import VehicleMeetingLinkRef
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
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.vehicle_model import VehicleModel
from netex.models.vehicle_model_profiles_in_frame_rel_structure import VehicleModelProfilesInFrameRelStructure
from netex.models.vehicle_model_ref import VehicleModelRef
from netex.models.vehicle_models_in_frame_rel_structure import VehicleModelsInFrameRelStructure
from netex.models.vehicle_pooling import VehiclePooling
from netex.models.vehicle_pooling_meeting_place import VehiclePoolingMeetingPlace
from netex.models.vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from netex.models.vehicle_pooling_place_assignment import VehiclePoolingPlaceAssignment
from netex.models.vehicle_pooling_ref import VehiclePoolingRef
from netex.models.vehicle_pooling_type_enumeration import VehiclePoolingTypeEnumeration
from netex.models.vehicle_ref import VehicleRef
from netex.models.vehicle_service_place_assignments_rel_structure import VehicleServicePlaceAssignmentsRelStructure
from netex.models.vehicle_type import VehicleType
from netex.models.vehicle_type_ref import VehicleTypeRef
from netex.models.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure
from netex.models.vehicles_in_frame_rel_structure import VehiclesInFrameRelStructure
from netex.models.vehicles_rel_structure import VehiclesRelStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2020, 12, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2020, 12, 17, 9, 30, 46, 0, 0),
        participant_ref='SYS002',
        description=MultilingualString(
            value='Request for hme james tariff'
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
                                        ref='noc:HJM'
                                    ),
                                    VehiclePoolingRef(
                                        ref='chauffeured_car'
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
        value='Example  of simple point to point fares'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='hjm:chauffeured_taxi_example',
                validity_conditions_or_valid_between=[
                    ValidBetween(
                        from_date=XmlDateTime(2020, 1, 1, 0, 0, 0),
                        to_date=XmlDateTime(2020, 12, 31, 12, 0, 0)
                    ),
                ],
                data_source_ref_attribute='hjm:home_james',
                version='1.0',
                responsibility_set_ref_attribute='hjm:tariffs',
                name=MultilingualString(
                    value='Chauffered car  Example'
                ),
                description=MultilingualString(
                    value='This is an example showing how one might encode  static aspects of a Chauffered car offering  "home james"  in NeTEx.  It includes some  prices.'
                ),
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        CodespaceRef(
                            ref='hjm_data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='hjm_data'
                    ),
                    default_data_source_ref=DataSourceRefStructure(
                        version='any',
                        ref='hjm:home_james'
                    ),
                    default_currency='GBP'
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ResourceFrame(
                            id='hjm:chauffeured_taxi_example',
                            version='1.0',
                            responsibility_set_ref_attribute='hjm:network_data',
                            name=MultilingualString(
                                value='Home James  Operator specific  common resources'
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    Codespace(
                                        id='hjm_data',
                                        xmlns='rd',
                                        xmlns_url='http://www.home_james.eu/data',
                                        description='ryde data'
                                    ),
                                ]
                            ),
                            data_sources=DataSourcesInFrameRelStructure(
                                data_source=[
                                    DataSource(
                                        id='hjm:home_james',
                                        version='any',
                                        email='feedback@homeJames.eu'
                                    ),
                                ]
                            ),
                            responsibility_sets=ResponsibilitySetsInFrameRelStructure(
                                responsibility_set=[
                                    ResponsibilitySet(
                                        id='hjm:tariffs',
                                        version='any',
                                        name=MultilingualString(
                                            value='Operator Tariffs'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='hjm:tariff_data@creates',
                                                    version='any',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.CREATES,
                                                    ],
                                                    stakeholder_role_type=[
                                                        StakeholderRoleTypeEnumeration.FARE_MANAGEMENT,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        value='noc:HJM',
                                                        version='any',
                                                        ref='noc:HJM'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ResponsibilitySet(
                                        id='hjm:network_data',
                                        version='any',
                                        name=MultilingualString(
                                            value='Operator data'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='hjm:network_data@creates',
                                                    version='any',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.CREATES,
                                                    ],
                                                    stakeholder_role_type=[
                                                        StakeholderRoleTypeEnumeration.PLANNING,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        value='noc:HJM',
                                                        version='any',
                                                        ref='noc:HJM'
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
                                            value='Brandingr'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                Branding(
                                                    id='myBrand',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Home James'
                                                    ),
                                                    url='https://www.home_james.eu/static/images//logo.png'
                                                ),
                                            ]
                                        ),
                                        class_of_values='Branding'
                                    ),
                                    ValueSet(
                                        id='TypeOfParking',
                                        version='any',
                                        name=MultilingualString(
                                            value='Types Of Parking'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfParking(
                                                    id='airport',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Airport Parking '
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='TypeOfParking'
                                    ),
                                ]
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    Operator(
                                        id='noc:HJM',
                                        version='any',
                                        name=MultilingualString(
                                            value='Home James Cars'
                                        ),
                                        short_name=MultilingualString(
                                            value='Home James'
                                        ),
                                        trading_name=MultilingualString(
                                            value='HJ Driver services Ltd.'
                                        ),
                                        description=MultilingualString(
                                            value='Chauffeured car service service'
                                        ),
                                        contact_details=ContactStructure(
                                            phone='+32 1293 449191'
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.OPERATOR,
                                        ],
                                        country_ref=CountryRef(
                                            ref=IanaCountryTldEnumeration.FR
                                        ),
                                        address=PostalAddressVersionStructure(
                                            street=MultilingualString(
                                                value='Alpha1'
                                            ),
                                            town=MultilingualString(
                                                value='Metropolis'
                                            ),
                                            post_code='RH10 9UA',
                                            postal_region='Metroland'
                                        ),
                                        primary_mode=AllModesEnumeration.TAXI,
                                        choice=TaxiSubmodeEnumeration.CHARTER_TAXI,
                                        mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=VehiclePoolingRef(
                                            version='any',
                                            ref='chauffeured_car'
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
                                            value='Thord  party providers of on;ine systems for HJ'
                                        ),
                                        contact_details=ContactStructure(
                                            email='barrowboy@floggit.com'
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.ONLINE_PROVIDER,
                                        ],
                                        address=PostalAddressVersionStructure(
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
                                        id='chauffeured_car',
                                        version='any',
                                        name=MultilingualString(
                                            value='Chauffeured car'
                                        ),
                                        description=MultilingualString(
                                            value='Prebooked car for  a period  or specific journey'
                                        ),
                                        submodes=SubmodesRelStructure(
                                            submode=[
                                                Submode(
                                                    id='chauffeured_car',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.TAXI,
                                                    choice=TaxiSubmodeEnumeration.CHARTER_TAXI
                                                ),
                                            ]
                                        ),
                                        vehicle_pooling_type=VehiclePoolingTypeEnumeration.CHAFFEURED_VEHICLE
                                    ),
                                    ScheduledOperation(
                                        id='scheduled_flights',
                                        version='any',
                                        name=MultilingualString(
                                            value='Scheduled flights'
                                        ),
                                        submodes=SubmodesRelStructure(
                                            submode=[
                                                Submode(
                                                    id='scheduled_flights@international',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.AIR,
                                                    choice=AirSubmodeEnumeration.INTERNATIONAL_FLIGHT
                                                ),
                                                Submode(
                                                    id='scheduled_flights@charter',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.AIR,
                                                    choice=AirSubmodeEnumeration.INTERNATIONAL_CHARTER_FLIGHT
                                                ),
                                                Submode(
                                                    id='scheduled_flights@domestic',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.AIR,
                                                    choice=AirSubmodeEnumeration.DOMESTIC_FLIGHT
                                                ),
                                            ]
                                        ),
                                        scheduled_operation_type=ScheduledOperationTypeEnumeration.SCHEDULED_SERVICE
                                    ),
                                    ScheduledOperation(
                                        id='scheduled_trains',
                                        version='any',
                                        name=MultilingualString(
                                            value='Scheduled trains'
                                        ),
                                        submodes=SubmodesRelStructure(
                                            submode=[
                                                Submode(
                                                    id='scheduled_trains@tgv',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.RAIL,
                                                    choice=RailSubmodeEnumeration.HIGH_SPEED_RAIL
                                                ),
                                                Submode(
                                                    id='scheduled_trains@regional',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.RAIL,
                                                    choice=RailSubmodeEnumeration.REGIONAL_RAIL
                                                ),
                                                Submode(
                                                    id='scheduled_trains@suburban',
                                                    version='any',
                                                    transport_mode=AllModesEnumeration.RAIL,
                                                    choice=RailSubmodeEnumeration.SUBURBAN_RAILWAY
                                                ),
                                            ]
                                        ),
                                        scheduled_operation_type=ScheduledOperationTypeEnumeration.SCHEDULED_SERVICE
                                    ),
                                ]
                            ),
                            service_facility_sets=ServiceFacilitySetsInFrameRelStructure(
                                service_facility_set=[
                                    ServiceFacilitySet(
                                        id='no_smoking',
                                        version='any',
                                        nuisance_facility_list=[
                                            NuisanceFacilityEnumeration.NO_SMOKING,
                                        ]
                                    ),
                                    ServiceFacilitySet(
                                        id='smoking',
                                        version='any',
                                        nuisance_facility_list=[
                                            NuisanceFacilityEnumeration.SMOKING,
                                        ]
                                    ),
                                    ServiceFacilitySet(
                                        id='wifi',
                                        version='any',
                                        passenger_comms_facility_list=[
                                            PassengerCommsFacilityEnumeration.FREE_WIFI,
                                        ]
                                    ),
                                ]
                            ),
                            vehicle_types=VehicleTypesInFrameRelStructure(
                                choice=[
                                    VehicleType(
                                        id='stretch_limo',
                                        version='any',
                                        name=MultilingualString(
                                            value='Strech limo'
                                        ),
                                        reversing_direction=True,
                                        self_propelled=True,
                                        propulsion_type=PropulsionTypeEnumeration.COMBUSTION,
                                        fuel_type_or_type_of_fuel=FuelTypeEnumeration.PETROL,
                                        transport_mode=AllVehicleModesOfTransportEnumeration.SELF_DRIVE,
                                        passenger_capacity=PassengerCapacityStructure(
                                            id='stretch_limo',
                                            version='any',
                                            seating_capacity=7
                                        ),
                                        length=Decimal('20'),
                                        height=Decimal('1.8'),
                                        weight=Decimal('1000'),
                                        first_axle_height=Decimal('0.25'),
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySet(
                                                    id='stretch_limo',
                                                    version='any',
                                                    catering_facility_list=[
                                                        CateringFacilityEnumeration.BAR,
                                                    ],
                                                    passenger_comms_facility_list=[
                                                        PassengerCommsFacilityEnumeration.VIDEO_ENTERTAINMENT,
                                                        PassengerCommsFacilityEnumeration.PUBLIC_WIFI,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            vehicle_models=VehicleModelsInFrameRelStructure(
                                vehicle_model=[
                                    VehicleModel(
                                        id='stretch_cadillac',
                                        version='any',
                                        name=MultilingualString(
                                            value='Strech Cadillac'
                                        ),
                                        manufacturer=MultilingualString(
                                            value='Cadillac'
                                        ),
                                        transport_type_ref_or_vehicle_type_ref=VehicleTypeRef(
                                            version='any',
                                            ref='stretch_limo'
                                        ),
                                        vehicle_model_profile_ref=CarModelProfileRef(
                                            version='any',
                                            ref='stretch_model'
                                        )
                                    ),
                                ]
                            ),
                            vehicle_model_profiles=VehicleModelProfilesInFrameRelStructure(
                                car_model_profile_or_cycle_model_profile=[
                                    CarModelProfile(
                                        id='stretch_model',
                                        version='any',
                                        air_conditioning=True,
                                        usb_power_sockets=True
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='hjm:chauffeured_taxi_example',
                            version='1.0',
                            responsibility_set_ref_attribute='hjm:network_data',
                            name=MultilingualString(
                                value='Places used by services.'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='hjm:chauffeured_taxi_example'
                                    ),
                                ]
                            ),
                            topographic_places=TopographicPlacesInFrameRelStructure(
                                topographic_place=[
                                    TopographicPlace(
                                        id='pays_de_soleil',
                                        version='any',
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='Pays de soleil'
                                            )
                                        )
                                    ),
                                    TopographicPlace(
                                        id='alphaville',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alphaville, Pays de soleil'
                                        ),
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
                                            ),
                                            qualify=TopographicPlaceDescriptorVersionedChildStructure.Qualify(
                                                qualifier_name=MultilingualString(
                                                    value='en soleil'
                                                ),
                                                topographic_place_ref=TopographicPlaceRef(
                                                    version='any',
                                                    ref='pays_de_soleil'
                                                )
                                            )
                                        ),
                                        parent_topographic_place_ref=TopographicPlaceRefStructure(
                                            version='any',
                                            ref='pays_de_soleil'
                                        )
                                    ),
                                    TopographicPlace(
                                        id='belaire',
                                        version='any',
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal('1.40250'),
                                                latitude=Decimal('52.74692'),
                                                id='belaire'
                                            )
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='Belaire'
                                            )
                                        ),
                                        parent_topographic_place_ref=TopographicPlaceRefStructure(
                                            version='any',
                                            ref='pays_de_soleil'
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
                                                id='gamma_sur_me'
                                            )
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='Gamma-sur-mer'
                                            )
                                        ),
                                        parent_topographic_place_ref=TopographicPlaceRefStructure(
                                            version='any',
                                            ref='pays_de_soleil'
                                        )
                                    ),
                                ]
                            ),
                            addresses=AddressesInFrameRelStructure(
                                address=[
                                    PostalAddress(
                                        id='chez_ritter',
                                        version='any',
                                        name=MultilingualString(
                                            value='Chez Ritter'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal('2.35250'),
                                                latitude=Decimal('53.44692'),
                                                id='chez_ritter'
                                            )
                                        ),
                                        building_name=MultilingualString(
                                            value='Chateau Ritter'
                                        ),
                                        street=MultilingualString(
                                            value='Rue de Ritter'
                                        ),
                                        town=MultilingualString(
                                            value='Gamma-sur-mer'
                                        ),
                                        province=MultilingualString(
                                            value='Pays de soleil'
                                        )
                                    ),
                                ]
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace(
                                        id='alphaville_aeroport',
                                        version='any',
                                        name=MultilingualString(
                                            value="Aeroporte Internationale d'Alphaville",
                                            lang='fr'
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='belaire'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.AIR,
                                        mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=ScheduledModeOfOperationRef(
                                            version='any',
                                            ref='scheduled_flights'
                                        ),
                                        other_transport_modes=[
                                            VehicleModeEnumeration.RAIL,
                                        ],
                                        served_places=TopographicPlaceRefsRelStructure(
                                            topographic_place_ref=[
                                                TopographicPlaceRefStructure(
                                                    version='any',
                                                    ref='alphaville'
                                                ),
                                                TopographicPlaceRefStructure(
                                                    version='any',
                                                    ref='gamma_sur_mer'
                                                ),
                                                TopographicPlaceRefStructure(
                                                    version='any',
                                                    ref='pays_de_soleil'
                                                ),
                                            ]
                                        ),
                                        main_terminus_for_places=TopographicPlaceRefsRelStructure(
                                            topographic_place_ref=[
                                                TopographicPlaceRefStructure(
                                                    version='any',
                                                    ref='alphaville'
                                                ),
                                            ]
                                        ),
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='alphaville_aeroport@taxi_set_down',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='set down Aeea'
                                                    ),
                                                    covered=CoveredEnumeration.COVERED,
                                                    transport_mode=AllVehicleModesOfTransportEnumeration.TAXI,
                                                    boarding_use=False,
                                                    alighting_use=True
                                                ),
                                                Quay(
                                                    id='alphaville_aeroport@taxi_pick_up',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Pick up   Area'
                                                    ),
                                                    covered=CoveredEnumeration.COVERED,
                                                    transport_mode=AllVehicleModesOfTransportEnumeration.TAXI,
                                                    boarding_use=True,
                                                    alighting_use=False
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='alphaville_gare',
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
                                        mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=ScheduledModeOfOperationRef(
                                            version='any',
                                            ref='scheduled_flights'
                                        ),
                                        main_terminus_for_places=TopographicPlaceRefsRelStructure(
                                            topographic_place_ref=[
                                                TopographicPlaceRefStructure(
                                                    version='any',
                                                    ref='alphaville'
                                                ),
                                            ]
                                        ),
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='alphaville_gare@platform_1',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 1'
                                                    ),
                                                    covered=CoveredEnumeration.INDOORS,
                                                    boarding_use=True,
                                                    alighting_use=True
                                                ),
                                                Quay(
                                                    id='alphaville_gare@platform_2',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 2'
                                                    ),
                                                    covered=CoveredEnumeration.INDOORS,
                                                    boarding_use=True,
                                                    alighting_use=False
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='alphaville_gare@taxi',
                                        version='any',
                                        name=MultilingualString(
                                            value="Taxi Rank at the Gare d'Alphaville",
                                            lang='fr'
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='alphaville'
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='alphaville_gare'
                                        ),
                                        contained_in_place_ref=TopographicPlaceRefStructure(
                                            version='any',
                                            ref='alphaville'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.TAXI,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='alphaville_gare@taxi_set_down',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Set down Aeea'
                                                    ),
                                                    covered=CoveredEnumeration.COVERED,
                                                    boarding_use=False,
                                                    alighting_use=True
                                                ),
                                                Quay(
                                                    id='alphaville_gare@taxi_pick_up',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Pick up   Area'
                                                    ),
                                                    covered=CoveredEnumeration.COVERED,
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
                                            value='Alphaville Hotel de Ville'
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
                                        id='alphaville_airport_taxi_parking',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alphaville Airport taxi parking',
                                            lang='en'
                                        ),
                                        cross_road=MultilingualString(
                                            value='Delta road'
                                        ),
                                        landmark=MultilingualString(
                                            value='Alphaville airports'
                                        ),
                                        covered=CoveredEnumeration.OUTDOORS,
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='belaire'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:HJM'
                                        ),
                                        parking_type=ParkingTypeEnumeration.AIRPORT_PARKING,
                                        type_of_parking_ref=TypeOfParkingRef(
                                            version='any',
                                            ref='airport'
                                        ),
                                        parking_vehicle_types=[
                                            ParkingVehicleEnumeration.TAXI,
                                        ],
                                        parking_areas=ParkingAreasRelStructure(
                                            parking_area_ref_or_parking_area=[
                                                TaxiParkingArea(
                                                    id='alphaville_airport_taxi_parking@A1',
                                                    version='any',
                                                    total_capacity=20,
                                                    bays=ParkingBaysRelStructure(
                                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref_or_parking_bay=[
                                                            ParkingBay(
                                                                id='alphaville_airport_taxi_parking@A1@chauff_1',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Chauffeured service pickup Bay'
                                                                ),
                                                                label=MultilingualString(
                                                                    value='Chauffeur 1'
                                                                )
                                                            ),
                                                            ParkingBay(
                                                                id='alphaville_airport_taxi_parking@A1@chauff_2',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Chauffeured service pickup Bay'
                                                                ),
                                                                label=MultilingualString(
                                                                    value='Chauffeur 1'
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
                        MobilityServiceFrame(
                            id='hjm:chauffeured_taxi_example',
                            version='1.0',
                            responsibility_set_ref_attribute='hjm:network_data',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='hjm:chauffeured_taxi_example'
                                    ),
                                ]
                            ),
                            fleets=FleetsRelStructure(
                                fleet=[
                                    Fleet(
                                        id='MetrobikeFleet',
                                        version='any',
                                        name=MultilingualString(
                                            value='The metrobike fleet'
                                        ),
                                        members=VehiclesRelStructure(
                                            vehicle_ref_or_vehicle=[
                                                Vehicle(
                                                    id='SWK007',
                                                    version='any',
                                                    registration_number='SWK007',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:HJM'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=VehicleTypeRef(
                                                        version='any',
                                                        ref='stretch_limo'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='stretch_cadillac'
                                                    ),
                                                    vehicle_model_profile_ref=CarModelProfileRef(
                                                        version='any',
                                                        ref='stretch_model'
                                                    )
                                                ),
                                                Vehicle(
                                                    id='SWK044',
                                                    version='any',
                                                    registration_number='SWK044',
                                                    transport_organisation_ref=OperatorRef(
                                                        version='any',
                                                        ref='noc:HJM'
                                                    ),
                                                    transport_type_ref_or_vehicle_type_ref=VehicleTypeRef(
                                                        version='any',
                                                        ref='stretch_limo'
                                                    ),
                                                    vehicle_model_ref=VehicleModelRef(
                                                        version='any',
                                                        ref='stretch_cadillac'
                                                    ),
                                                    vehicle_model_profile_ref=CarModelProfileRef(
                                                        version='any',
                                                        ref='stretch_model'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            mobility_services=MobilityServicesRelStructure(
                                mobility_service_or_common_vehicle_service_or_vehicle_pooling_service=[
                                    ChauffeuredVehicleService(
                                        id='hj_cars',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Home James Cars.'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:HJM'
                                        ),
                                        service_booking_arrangements=ServiceBookingArrangementsStructure(
                                            booking_contact=ContactStructure(
                                                phone='=31666777',
                                                url='https://www.homeJames.eu/booking'
                                            ),
                                            booking_methods=[
                                                BookingMethodEnumeration.MOBILE_APP,
                                                BookingMethodEnumeration.ONLINE,
                                            ],
                                            booking_access=BookingAccessEnumeration.AUTHORISED_PUBLIC,
                                            book_when=PurchaseWhenEnumeration.ADVANCE_ONLY,
                                            buy_when=[
                                                PurchaseMomentEnumeration.ON_CHECK_OUT,
                                            ],
                                            latest_booking_time=XmlTime(20, 0, 0, 0),
                                            minimum_booking_period=XmlDuration("P1D"),
                                            booking_url='https://www.homeJames.eu/booking',
                                            booking_note=MultilingualString(
                                                value='Booklings made online or by pyone  Bookings can be made up to two hour before travel. '
                                            ),
                                            minimum_booking_duration=XmlDuration("PT2H"),
                                            deposit_required=True,
                                            booking_charge_type=BookingChargeTypeEnumeration.NONE
                                        ),
                                        booking_required=True,
                                        registration_required=True,
                                        proposed_by_services=OnlineServiceRefsRelStructure(
                                            online_service_ref=[
                                                OnlineServiceRef(
                                                    version='any',
                                                    ref='hjm_online'
                                                ),
                                            ]
                                        ),
                                        vehicle_pooling_ref=VehiclePoolingRef(
                                            version='any',
                                            ref='chauffeured_car'
                                        )
                                    ),
                                ]
                            ),
                            online_services=OnlineServicesRelStructure(
                                online_service=[
                                    OnlineService(
                                        id='hjm_online',
                                        version='any',
                                        name=MultilingualString(
                                            value='Online booking for HJ Cars'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OnlineServiceOperatorRef(
                                            version='any',
                                            ref='floggit'
                                        ),
                                        proposing_services=MobilityServiceRefsRelStructure(
                                            mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref=[
                                                ChauffeuredVehicleServiceRef(
                                                    version='any',
                                                    ref='hj_cars'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            vehicle_meeting_points=VehicleMeetingPointsInFrameRelStructure(
                                vehicle_meeting_point=[
                                    VehicleMeetingPoint(
                                        id='alphaville_airport',
                                        version='any',
                                        name=MultilingualString(
                                            value='Pick up/Set down Alphaville airport'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('1.65250'),
                                            latitude=Decimal('53.54692')
                                        )
                                    ),
                                    VehicleMeetingPoint(
                                        id='gamma_area',
                                        version='any',
                                        name=MultilingualString(
                                            value='Pick up/Set down Gamma area'
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
                                            value='Pick up/Set down  in Alphaville centre'
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
                                            value='Pick up/Set down  at Alphaville station'
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
                                        id='gamma_area+alphaville_airport',
                                        version='any',
                                        distance=Decimal('40'),
                                        from_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='gamma_area'
                                        ),
                                        to_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_airport'
                                        )
                                    ),
                                    VehicleMeetingLink(
                                        id='alphaville_airport+gamma_area',
                                        version='any',
                                        distance=Decimal('40'),
                                        from_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_airport'
                                        ),
                                        to_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='gamma_area'
                                        )
                                    ),
                                    VehicleMeetingLink(
                                        id='gamma_area+alphaville_gare',
                                        version='any',
                                        distance=Decimal('15'),
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
                                        id='alphaville_gare+gamma_area',
                                        version='any',
                                        distance=Decimal('15'),
                                        from_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_gare'
                                        ),
                                        to_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='gamma_area'
                                        )
                                    ),
                                    VehicleMeetingLink(
                                        id='alphaville_airport+alphaville_centre',
                                        version='any',
                                        distance=Decimal('20'),
                                        from_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_airport'
                                        ),
                                        to_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_centre'
                                        )
                                    ),
                                    VehicleMeetingLink(
                                        id='alphaville_centre+alphaville_airport',
                                        version='any',
                                        distance=Decimal('20'),
                                        from_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_centre'
                                        ),
                                        to_point_ref=VehicleMeetingPointRefStructure(
                                            version='any',
                                            ref='alphaville_airport'
                                        )
                                    ),
                                ]
                            ),
                            vehicle_meeting_places=VehicleMeetingPlacesRelStructure(
                                vehicle_meeting_place=[
                                    VehiclePoolingMeetingPlace(
                                        id='alphaville_airport_set_down',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alphaville pick up'
                                        ),
                                        topographic_place_ref=TopographicPlaceRef(
                                            value=' ',
                                            version='any',
                                            ref='belaire'
                                        ),
                                        choice=QuayRef(
                                            version='any',
                                            ref='alphaville_gare@taxi_set_down'
                                        )
                                    ),
                                    VehiclePoolingMeetingPlace(
                                        id='alphaville_airport_pick_up',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alphaville pick up'
                                        ),
                                        topographic_place_ref=TopographicPlaceRef(
                                            value=' ',
                                            version='any',
                                            ref='belaire'
                                        ),
                                        choice=QuayRef(
                                            version='any',
                                            ref='alphaville_gare@taxi_pick_up'
                                        )
                                    ),
                                ]
                            ),
                            vehicle_meeting_place_assignments=VehicleServicePlaceAssignmentsRelStructure(
                                vehicle_sharing_place_assignment_or_vehicle_pooling_place_assignment_or_taxi_service_place_assignment=[
                                    VehiclePoolingPlaceAssignment(
                                        id='alphaville_airport_taxi_parking@pick_up',
                                        version='any',
                                        order=1,
                                        vehicle_pooling_service_ref=ChauffeuredVehicleServiceRef(
                                            version='any',
                                            ref='hj_cars'
                                        ),
                                        vehicle_pooling_meeting_place_ref_or_vehicle_pooling_parking_area_ref=VehiclePoolingMeetingPlaceRef(
                                            version='any',
                                            ref='alphaville_airport_pick_up'
                                        ),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=ParkingBayRef(
                                            version='any',
                                            ref='alphaville_airport_taxi_parking@A1@chauff_1'
                                        )
                                    ),
                                    VehiclePoolingPlaceAssignment(
                                        id='alphaville_airport_taxi_parking@set_down',
                                        version='any',
                                        order=1,
                                        vehicle_pooling_service_ref=ChauffeuredVehicleServiceRef(
                                            version='any',
                                            ref='hj_cars'
                                        ),
                                        vehicle_pooling_meeting_place_ref_or_vehicle_pooling_parking_area_ref=VehiclePoolingMeetingPlaceRef(
                                            version='any',
                                            ref='alphaville_airport_set_down'
                                        ),
                                        parking_bay_ref_or_vehicle_sharing_parking_bay_ref=ParkingBayRef(
                                            version='any',
                                            ref='alphaville_airport_taxi_parking@A1@chauff_2'
                                        )
                                    ),
                                    VehiclePoolingPlaceAssignment(
                                        id='alphaville_gare_taxi_parking@pick_up',
                                        version='any',
                                        order=1,
                                        vehicle_pooling_service_ref=ChauffeuredVehicleServiceRef(
                                            version='any',
                                            ref='hj_cars'
                                        ),
                                        vehicle_pooling_meeting_place_ref_or_vehicle_pooling_parking_area_ref=VehiclePoolingMeetingPlaceRef(
                                            version='any',
                                            ref='alphaville_gare_pick_up'
                                        )
                                    ),
                                    VehiclePoolingPlaceAssignment(
                                        id='alphaville_gare_taxi_parking@set_down',
                                        version='any',
                                        order=1,
                                        vehicle_pooling_service_ref=ChauffeuredVehicleServiceRef(
                                            version='any',
                                            ref='hj_cars'
                                        ),
                                        vehicle_pooling_meeting_place_ref_or_vehicle_pooling_parking_area_ref=VehiclePoolingMeetingPlaceRef(
                                            version='any',
                                            ref='alphaville_gare_set_down'
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='hjm:chauffeured_taxi_example-prepriced_trips',
                            data_source_ref_attribute='hjm:home_james',
                            version='1.0',
                            responsibility_set_ref_attribute='hjm:tariffs',
                            name=MultilingualString(
                                value='ome James - Chaufferred car hire - prepriced trips'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    MobilityServiceFrameRef(
                                        version='1.0',
                                        ref='hjm:chauffeured_taxi_example'
                                    ),
                                    SiteFrameRef(
                                        version='1.0',
                                        ref='hjm:chauffeured_taxi_example'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='home_james@prepriced_trip',
                                        version='any',
                                        name=MultilingualString(
                                            value='Tariff for standard trips'
                                        ),
                                        document_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://homeJames.eu/tariff.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.INFO,
                                                    ]
                                                ),
                                                InfoLink(
                                                    value='https://homeJames.eu/tariffMap.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MAP,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:HJM'
                                        ),
                                        choice_1=ChauffeuredVehicleServiceRef(
                                            version='any',
                                            ref='hj_cars'
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='home_james@prepriced_trip@access',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Access to one of the prepriced trips'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='home_james@prepriced_trip@access',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:access',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.OR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            vehicle_meeting_link_ref=[
                                                                VehicleMeetingLinkRef(
                                                                    version='any',
                                                                    ref='gamma_area+alphaville_airport'
                                                                ),
                                                                VehicleMeetingLinkRef(
                                                                    version='any',
                                                                    ref='alphaville_airport+gamma_area'
                                                                ),
                                                                VehicleMeetingLinkRef(
                                                                    version='any',
                                                                    ref='gamma_area+alphaville_gare'
                                                                ),
                                                                VehicleMeetingLinkRef(
                                                                    version='any',
                                                                    ref='alphaville_gare+gamma_area'
                                                                ),
                                                                VehicleMeetingLinkRef(
                                                                    version='any',
                                                                    ref='alphaville_airport+alphaville_centre'
                                                                ),
                                                                VehicleMeetingLinkRef(
                                                                    version='any',
                                                                    ref='alphaville_centre+alphaville_airport'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='home_james@prepriced_trip@eligibility',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Eligible user types'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:eligibility',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='home_james@prepriced_trip@eligibility',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:eligible',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UserProfile(
                                                                    id='person',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Person'
                                                                    ),
                                                                    user_type=UserTypeEnumeration.ANYONE,
                                                                    minimum_age=6,
                                                                    companion_profiles=CompanionProfilesRelStructure(
                                                                        companion_profile_ref_or_companion_profile=[
                                                                            CompanionProfile(
                                                                                id="'pet_with_person",
                                                                                version='any',
                                                                                user_profile_ref=UserProfileRef(
                                                                                    version='any',
                                                                                    ref='pet'
                                                                                ),
                                                                                maximum_number_of_persons=1,
                                                                                discount_basis=DiscountBasisEnumeration.FREE
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                                UserProfile(
                                                                    id='pet',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Pet '
                                                                    ),
                                                                    user_type=UserTypeEnumeration.ANIMAL
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='home_james@prepriced_trip@conditions_of_travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='COnditions on travel'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:travel_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='home_james@prepriced_trip@conditions_of_travel',
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
                                                                    id='home_james@prepriced_trip@usagValidity',
                                                                    version='any',
                                                                    validity_period_type=UsageValidityTypeEnumeration.SINGLE_TRIP,
                                                                    usage_trigger=UsageTriggerEnumeration.START_OUTBOUND_RIDE,
                                                                    usage_end=UsageEndEnumeration.END_OF_TRIP
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='home_james@prepriced_trip@frequency',
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
                                                    id='home_james@prepriced_trip@conditions_of_sale',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions of sale'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:sale_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='home_james@prepriced_trip@conditions_of_sale',
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
                                                                Cancelling(
                                                                    id='home_james@prepriced_trip@refunding',
                                                                    version='any',
                                                                    cancellation_allowed=True
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='home_james@prepriced_trip@accommodation',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions of sale'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:sale_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='home_james@prepriced_trip@facilities',
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
                                                    id='gamma_area+alphaville_airport',
                                                    version='any',
                                                    inverse_allowed=True,
                                                    choice=PointRefStructure(
                                                        version='any',
                                                        ref='gamma_area'
                                                    ),
                                                    choice_1=PointRefStructure(
                                                        version='any',
                                                        ref='alphaville_airport'
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='alphaville_airport+alphaville_centre',
                                                    version='any',
                                                    inverse_allowed=True,
                                                    choice=PointRefStructure(
                                                        version='any',
                                                        ref='alphaville_airport'
                                                    ),
                                                    choice_1=PointRefStructure(
                                                        version='any',
                                                        ref='alphaville_centre'
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='gamma_area+alphaville_gare',
                                                    version='any',
                                                    inverse_allowed=True,
                                                    choice=PointRefStructure(
                                                        version='any',
                                                        ref='gamma_area'
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
                                    PreassignedFareProduct(
                                        id='home_james@prepriced_trip',
                                        version='any',
                                        name=MultilingualString(
                                            value='One off trip for fixed price route '
                                        ),
                                        charging_moment_type=ChargingMomentEnumeration.AT_END_OF_TRAVEL,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:HJM'
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
                                                    id='home_james@prepriced_trip@travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Single  ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='home_james@prepriced_trip@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='home_james@prepriced_trip@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='home_james@prepriced_trip@conditions_of_travel'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='home_james@prepriced_trip@accommodation'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='home_james@prepriced_trip',
                                                    version='any',
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='any',
                                                        ref='home_james@prepriced_trip@travel'
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
                                        id='call_centre',
                                        version='any',
                                        name=MultilingualString(
                                            value='MCall centre'
                                        ),
                                        distribution_channel_type=DistributionChannelTypeEnumeration.TELEPHONE,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:HJM'
                                        ),
                                        payment_methods=[
                                            PaymentMethodEnumeration.DEBIT_CARD,
                                            PaymentMethodEnumeration.CREDIT_CARD,
                                        ]
                                    ),
                                ]
                            ),
                            fulfilment_methods=FulfilmentMethodsInFrameRelStructure(
                                fulfilment_method=[
                                    FulfilmentMethod(
                                        id='email',
                                        version='any',
                                        fulfilment_method_type=FulfilmentMethodTypeEnumeration.EMAIL,
                                        types_of_travel_document=TypeOfTravelDocumentRefsRelStructure(
                                            type_of_travel_document_ref=[
                                                TypeOfTravelDocumentRef(
                                                    version='any',
                                                    ref='email_confirmation'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            types_of_travel_documents=TypesOfTravelDocumentInFrameRelStructure(
                                type_of_travel_document=[
                                    TypeOfTravelDocument(
                                        id='email_confirmation',
                                        version='any',
                                        media_type=MediaTypeEnumeration.NONE
                                    ),
                                ]
                            ),
                            sales_offer_packages=SalesOfferPackagesInFrameRelStructure(
                                sales_offer_package=[
                                    SalesOfferPackage(
                                        id='home_james@prepriced_trip-SOP@online',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='One of prebooked, pay on completeion'
                                        ),
                                        condition_summary=ConditionSummary(
                                            requires_account=True
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='home_james@prepriced_trip-SOP@online',
                                                    version='any',
                                                    order=1,
                                                    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref=DistributionChannelRef(
                                                        version='any',
                                                        ref='online'
                                                    ),
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.ONLINE,
                                                    ticketing_service_facility_list=[
                                                        TicketingServiceFacilityEnumeration.RESERVATIONS,
                                                        TicketingServiceFacilityEnumeration.PURCHASE,
                                                        TicketingServiceFacilityEnumeration.REFUND,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        version='any',
                                                        ref='email'
                                                    )
                                                ),
                                                DistributionAssignment(
                                                    id='home_james@prepriced_trip-SOP@call_centre',
                                                    version='any',
                                                    order=1,
                                                    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref=DistributionChannelRef(
                                                        version='any',
                                                        ref='call_centre'
                                                    ),
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.TELEPHONE,
                                                    ticketing_service_facility_list=[
                                                        TicketingServiceFacilityEnumeration.RESERVATIONS,
                                                        TicketingServiceFacilityEnumeration.PURCHASE,
                                                        TicketingServiceFacilityEnumeration.REFUND,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        version='any',
                                                        ref='email'
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='home_james@prepriced_trip-SOP@online',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='email_confirmation'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='any',
                                                        ref='home_james@prepriced_trip'
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
                            id='hjm:chauffeured_taxi_example_prices-prepriced_trips',
                            data_source_ref_attribute='hjm:home_james',
                            version='1.0',
                            responsibility_set_ref_attribute='hjm:tariffs',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_currency='EUR'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='hjm:chauffeured_taxi_example-prepriced_trips'
                                    ),
                                ]
                            ),
                            fare_tables=FareTablesInFrameRelStructure(
                                fare_table=[
                                    FareTable(
                                        id='home_james@prepriced_trip',
                                        version='any',
                                        name=MultilingualString(
                                            value='Home james  prepriced trip  use prices'
                                        ),
                                        prices_for=PriceableObjectRefsRelStructure(
                                            choice=[
                                                SalesOfferPackageRef(
                                                    version='any',
                                                    ref='home_james@prepriced_trip-SOP@online'
                                                ),
                                            ]
                                        ),
                                        used_in=UsedInRefsRelStructure(
                                            choice=[
                                                TariffRef(
                                                    version='any',
                                                    ref='home_james@prepriced_trip'
                                                ),
                                            ]
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:HJM'
                                        ),
                                        specifics=FareTableSpecificsStructure(
                                            choice_1=ChauffeuredVehicleServiceRef(
                                                version='any',
                                                ref='hj_cars'
                                            )
                                        ),
                                        prices=FarePricesRelStructure(
                                            fare_price_ref_or_cell_ref_or_fare_price=[
                                                DistanceMatrixElementPrice(
                                                    id='gamma_area+alphaville_airport',
                                                    version='any',
                                                    amount=Decimal('80'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='gamma_area+alphaville_airport'
                                                    )
                                                ),
                                                DistanceMatrixElementPrice(
                                                    id='alphaville_airport+alphaville_centre',
                                                    version='any',
                                                    amount=Decimal('60'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='alphaville_airport+alphaville_centre'
                                                    )
                                                ),
                                                DistanceMatrixElementPrice(
                                                    id='gamma_area+alphaville_gare',
                                                    version='any',
                                                    amount=Decimal('40'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='gamma_area+alphaville_gare'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='hjm:chauffeured_taxi_example-charters',
                            data_source_ref_attribute='hjm:home_james',
                            version='1.0',
                            responsibility_set_ref_attribute='hjm:tariffs',
                            name=MultilingualString(
                                value='Home James - Chaufferred car hire by charter  period '
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    MobilityServiceFrameRef(
                                        version='1.0',
                                        ref='hjm:chauffeured_taxi_example'
                                    ),
                                    SiteFrameRef(
                                        version='1.0',
                                        ref='hjm:chauffeured_taxi_example'
                                    ),
                                ]
                            ),
                            time_units=TimeUnitsRelStructure(
                                time_unit_ref_or_time_unit=[
                                    TimeUnit(
                                        id='half_day',
                                        version='any'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='home_james@charter',
                                        version='any',
                                        name=MultilingualString(
                                            value='Tariff for time hired'
                                        ),
                                        document_links=InfoLinksRelStructure(
                                            info_link=[
                                                InfoLink(
                                                    value='https://homeJames.eu/tariffBespoke.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.INFO,
                                                    ]
                                                ),
                                                InfoLink(
                                                    value='https://homeJames.eu/tariffMap.pdf',
                                                    type_of_info_link=[
                                                        TypeOfInfolinkEnumeration.MAP,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='noc:HJM'
                                        ),
                                        choice_1=ChauffeuredVehicleServiceRef(
                                            version='any',
                                            ref='hj_cars'
                                        ),
                                        time_intervals=TimeIntervalsRelStructure(
                                            time_interval_ref_or_time_interval=[
                                                TimeInterval(
                                                    id='charter@4H',
                                                    version='any',
                                                    duration=XmlDuration("PT4H")
                                                ),
                                                TimeInterval(
                                                    id='charter@1D',
                                                    version='any',
                                                    duration=XmlDuration("P1D")
                                                ),
                                                TimeInterval(
                                                    id='charter@2D',
                                                    version='any',
                                                    duration=XmlDuration("P2D")
                                                ),
                                                TimeInterval(
                                                    id='charter@3D',
                                                    version='any',
                                                    duration=XmlDuration("P3D")
                                                ),
                                                TimeInterval(
                                                    id='charter@4D',
                                                    version='any',
                                                    duration=XmlDuration("P4D")
                                                ),
                                                TimeInterval(
                                                    id='charter@5D',
                                                    version='any',
                                                    duration=XmlDuration("P5D")
                                                ),
                                                TimeInterval(
                                                    id='charter@6D',
                                                    version='any',
                                                    duration=XmlDuration("P6D")
                                                ),
                                            ]
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='home_james@charter@access',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Access to one of the servic'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='home_james@charter@access',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:access',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.OR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            choice=[
                                                                OperatorRef(
                                                                    version='any',
                                                                    ref='noc:HJM'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='home_james@charter@durations',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Access to one of the servic'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:can_access_when',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='home_james@charter@durations',
                                                        version='any',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:can_access_when',
                                                            version_ref='EXTERNAL'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.OR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            choice=[
                                                                OperatorRef(
                                                                    version='any',
                                                                    ref='noc:HJM'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='home_james@charter@conditions_of_travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='COnditions on travel'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:travel_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='home_james@charter@conditions_of_travel',
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
                                                                    id='home_james@charter@usagValidity',
                                                                    version='any',
                                                                    validity_period_type=UsageValidityTypeEnumeration.OTHER,
                                                                    usage_trigger=UsageTriggerEnumeration.SPECIFIED_START_DATE,
                                                                    usage_end=UsageEndEnumeration.STANDARD_DURATION,
                                                                    usage_start_constraint_type=UsageStartConstraintTypeEnumeration.FIXED
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='home_james@charter@conditions_of_sale',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Conditions of sale'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:sale_conditions',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='home_james@charter@conditions_of_sale',
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
                                                                Cancelling(
                                                                    id='home_james@charter@refunding',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Can cancel up top 3 hours before'
                                                                    ),
                                                                    booking_arrangements=BookingArrangementsStructure(
                                                                        minimum_booking_period=XmlDuration("PT3H")
                                                                    ),
                                                                    cancellation_allowed=True
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
                                        id='home_james@charter',
                                        version='any',
                                        name=MultilingualString(
                                            value='One off trip for fixed price route '
                                        ),
                                        charging_moment_type=ChargingMomentEnumeration.AT_END_OF_TRAVEL,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:HJM'
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
                                                    id='home_james@charter@travel',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Single  ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='home_james@charter@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='home_james@prepriced_trip@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='home_james@charter@conditions_of_travel'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='any',
                                                                ref='home_james@prepriced_trip@accommodation'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='home_james@charter',
                                                    version='any',
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='any',
                                                        ref='home_james@charter@travel'
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
                                        id='home_james@charter-SOP@online',
                                        version='any',
                                        branding_ref=BrandingRef(
                                            version='any',
                                            ref='myBrand'
                                        ),
                                        name=MultilingualString(
                                            value='Chart for a specifed tome interval, pay on completion'
                                        ),
                                        condition_summary=ConditionSummary(
                                            requires_account=True
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='home_james@charter-SOP@online',
                                                    version='any',
                                                    order=1,
                                                    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref=DistributionChannelRef(
                                                        version='any',
                                                        ref='online'
                                                    ),
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.ONLINE,
                                                    ticketing_service_facility_list=[
                                                        TicketingServiceFacilityEnumeration.RESERVATIONS,
                                                        TicketingServiceFacilityEnumeration.PURCHASE,
                                                        TicketingServiceFacilityEnumeration.REFUND,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        version='any',
                                                        ref='email'
                                                    )
                                                ),
                                                DistributionAssignment(
                                                    id='home_james@charter-SOP@call_centre',
                                                    version='any',
                                                    order=1,
                                                    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref=DistributionChannelRef(
                                                        version='any',
                                                        ref='call_centre'
                                                    ),
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.TELEPHONE,
                                                    ticketing_service_facility_list=[
                                                        TicketingServiceFacilityEnumeration.RESERVATIONS,
                                                        TicketingServiceFacilityEnumeration.PURCHASE,
                                                        TicketingServiceFacilityEnumeration.REFUND,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        version='any',
                                                        ref='email'
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='home_james@charter-SOP@online',
                                                    version='any',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='email_confirmation'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='any',
                                                        ref='home_james@charter'
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
                            id='hjm:chauffeured_taxi_example_prices-charter',
                            data_source_ref_attribute='hjm:home_james',
                            version='1.0',
                            responsibility_set_ref_attribute='hjm:tariffs',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_currency='EUR'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='hjm:chauffeured_taxi_example-charters'
                                    ),
                                ]
                            ),
                            fare_tables=FareTablesInFrameRelStructure(
                                fare_table=[
                                    FareTable(
                                        id='home_james@charter',
                                        version='any',
                                        name=MultilingualString(
                                            value='Home james charter prices'
                                        ),
                                        prices_for=PriceableObjectRefsRelStructure(
                                            choice=[
                                                SalesOfferPackageRef(
                                                    version='any',
                                                    ref='home_james@charter-SOP@online'
                                                ),
                                            ]
                                        ),
                                        used_in=UsedInRefsRelStructure(
                                            choice=[
                                                TariffRef(
                                                    version='any',
                                                    ref='home_james@charter'
                                                ),
                                            ]
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='noc:HJM'
                                        ),
                                        specifics=FareTableSpecificsStructure(
                                            choice_1=ChauffeuredVehicleServiceRef(
                                                version='any',
                                                ref='hj_cars'
                                            )
                                        ),
                                        prices=FarePricesRelStructure(
                                            fare_price_ref_or_cell_ref_or_fare_price=[
                                                TimeIntervalPrice(
                                                    id='charter@4H',
                                                    version='any',
                                                    amount=Decimal('80'),
                                                    time_interval_ref=TimeIntervalRef(
                                                        version='any',
                                                        ref='charter@4H'
                                                    )
                                                ),
                                                TimeIntervalPrice(
                                                    id='charter@2D',
                                                    version='any',
                                                    amount=Decimal('120'),
                                                    time_interval_ref=TimeIntervalRef(
                                                        version='any',
                                                        ref='charter@1D'
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
                id='hjm:chauffeured_taxi_example_transaction_examples',
                data_source_ref_attribute='hjm:home_james',
                version='1.0',
                responsibility_set_ref_attribute='hjm:transaction_data',
                prerequisites=VersionFrameRefsRelStructure(
                    version_frame_ref=[
                        CompositeFrameRef(
                            version='1.0',
                            ref='hjm:chauffeured_taxi_example'
                        ),
                    ]
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ResourceFrame(
                            id='_data',
                            version='1.0',
                            name=MultilingualString(
                                value='Transaction common resources'
                            ),
                            vehicles=VehiclesInFrameRelStructure(
                                train_element_or_vehicle=[
                                    Vehicle(
                                        id='db54278',
                                        version='any',
                                        name=MultilingualString(
                                            value="Freddy's car"
                                        )
                                    ),
                                ]
                            )
                        ),
                        MobilityJourneyFrame(
                            id='hjmt:sample_transactions',
                            version='1.2',
                            single_journey_paths=SingleJourneyPathsRelStructure(
                                single_journey_path=[
                                    SingleJourneyPath(
                                        id='hmjt:anon@trans005@ride5163',
                                        version='any',
                                        name=MultilingualString(
                                            value='Path from Airportand   to Chez Ritter.'
                                        ),
                                        distance=Decimal('25.00'),
                                        points_in_sequence=VehicleMeetingPointsInSequenceRelStructure(
                                            vehicle_meeting_point_in_path=[
                                                VehicleMeetingPointInPath(
                                                    id='hmjt:anon@trans005@ride5163',
                                                    version='any',
                                                    order=1,
                                                    choice_1=VehicleMeetingPointRef(
                                                        version='any',
                                                        ref='alphaville_airport'
                                                    ),
                                                    onward_vehicle_meeting_link_ref=OnwardVehicleMeetingLinkRef(
                                                        version='any',
                                                        ref='alphaville_airport+alphaville_centre'
                                                    )
                                                ),
                                                VehicleMeetingPointInPath(
                                                    id='hmjt:anon@trans005@ride5163',
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
                                        id='hjmt:anon@trans005@ride5163',
                                        version='any',
                                        name=MultilingualString(
                                            value='Single journey from airport to Chez ritter'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.TAXI,
                                        transport_submode=TransportSubmode(
                                            choice=TaxiSubmodeEnumeration.CHARTER_TAXI
                                        ),
                                        common_vehicle_service_ref_or_vehicle_pooling_service_ref=ChauffeuredVehicleServiceRef(
                                            version='any',
                                            ref='hj_cars'
                                        ),
                                        vehicle_ref=VehicleRef(
                                            version='any',
                                            ref='SWK007'
                                        ),
                                        departure_time=XmlTime(10, 15, 0, 0),
                                        operating_day_ref=OperatingDayRef(
                                            ref='opday_7656',
                                            version_ref='EXTERNAL'
                                        ),
                                        dated_passing_times=TargetPassingTimesRelStructure(
                                            target_passing_time=[
                                                TargetPassingTime(
                                                    id='hjmt:anon@trans005@ride5163',
                                                    version='any',
                                                    point_in_journey_pattern_ref=PointInSingleJourneyPathRef(
                                                        version='any',
                                                        ref='hmjt:anon@trans005@ride5163',
                                                        order=1
                                                    ),
                                                    choice_1=[
                                                        DerivedElement(
                                                            qname='{http://www.netex.org.uk/netex}AimedDepartureTime',
                                                            value=XmlTime(10, 15, 0, 0)
                                                        ),
                                                    ]
                                                ),
                                                TargetPassingTime(
                                                    id='hjmt:anon@trans005@ride5163',
                                                    version='any',
                                                    point_in_journey_pattern_ref=PointInSingleJourneyPathRef(
                                                        version='any',
                                                        ref='hmjt:anon@trans005@ride5163',
                                                        order=2
                                                    ),
                                                    choice_1=[
                                                        XmlTime(11, 10, 0, 0),
                                                    ]
                                                ),
                                            ]
                                        ),
                                        meeting_point_assignments=VehicleMeetingPointAssignmentsRelStructure(
                                            dynamic_vehicle_meeting_point_assignment_ref_or_vehicle_meeting_point_assignment_ref_or_vehicle_meeting_point_assignment=[
                                                VehicleMeetingPointAssignment1(
                                                    id='hjmt:anon@trans005@ride5163',
                                                    version='any',
                                                    order=1,
                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                        version='any',
                                                        ref='alphaville_airport'
                                                    ),
                                                    choice=QuayRef(
                                                        version='any',
                                                        ref='alphaville_aeroport@taxi_pick_up'
                                                    ),
                                                    usage=MeetingUsageEnumeration.PICK_UP
                                                ),
                                                VehicleMeetingPointAssignment1(
                                                    id='hjmt:anon@trans005@ride5163',
                                                    version='any',
                                                    order=2,
                                                    vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                        version='any',
                                                        ref='gamma_area'
                                                    ),
                                                    choice=AddressablePlaceRef(
                                                        version='any',
                                                        ref='chez_ritter'
                                                    ),
                                                    usage=MeetingUsageEnumeration.SET_DOWN
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SalesTransactionFrame(
                            id='hjmt:sample_transactions',
                            version='1.2',
                            name=MultilingualString(
                                value='Home James  Sample Transactions'
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    CodespaceRef(
                                        ref='hjm_data'
                                    ),
                                    Codespace(
                                        id='hmj_transactions',
                                        xmlns='hmjt',
                                        xmlns_url='http://www.homeJames.eu/transactions',
                                        description='Operator transaction data'
                                    ),
                                ]
                            ),
                            fare_contracts=FareContractsInFrameRelStructure(
                                fare_contract=[
                                    FareContract(
                                        id='hjmt:anon@trans005',
                                        version='any',
                                        customer_ref=CustomerRef(
                                            ref='hjmt:Anon',
                                            version_ref='EXTERNAL'
                                        ),
                                        fare_contract_entries=FareContractEntriesRelStructure(
                                            choice=[
                                                SalesTransaction(
                                                    id='hjmt:anon@trans005@purchase_ride',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Buy Single   ride Adult'
                                                    ),
                                                    date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                    type_of_fare_contract_entry_ref=TypeOfFareContractEntryRef(
                                                        ref='fxc:product_purchase',
                                                        version_ref='EXTERNAL'
                                                    ),
                                                    amount=Decimal('10.00'),
                                                    payment_method=PaymentMethodEnumeration.CASH,
                                                    travel_specifications=TravelSpecificationsRelStructure(
                                                        travel_specification_ref_or_travel_specification=[
                                                            OfferedTravelSpecification(
                                                                id='hjmt:anon@trans005@purchase_ride',
                                                                version='any',
                                                                date=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                                sales_transaction_ref=SalesTransactionRef(
                                                                    version='any',
                                                                    ref='hjmt:anon@trans005@purchase_ride'
                                                                ),
                                                                fare_price_ref_or_cell_ref=DistanceMatrixElementPriceRef(
                                                                    version='any',
                                                                    ref='gamma_area+alphaville_airport'
                                                                ),
                                                                amount=Decimal('80.00'),
                                                                start_of_validity=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                                travel_specification_summary_view=TravelSpecificationSummaryView(
                                                                    origin=TravelSpecificationSummaryEndpointStructure(
                                                                        vehicle_meeting_point_ref=VehicleMeetingPointRef(
                                                                            version='any',
                                                                            ref='alphaville_airport'
                                                                        )
                                                                    ),
                                                                    destination=TravelSpecificationSummaryEndpointStructure(
                                                                        address_ref=AddressRef(
                                                                            version='any',
                                                                            ref='chez_ritter'
                                                                        )
                                                                    ),
                                                                    start=XmlDateTime(2020, 10, 8, 11, 7, 0),
                                                                    duration=XmlDuration("PT60M"),
                                                                    authority_ref_or_operator_ref_or_group_of_operators_ref=OperatorRef(
                                                                        version='any',
                                                                        ref='noc:HJM'
                                                                    ),
                                                                    choice=ChauffeuredVehicleServiceRef(
                                                                        version='any',
                                                                        ref='hj_cars'
                                                                    )
                                                                ),
                                                                specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                    specific_parameter_assignment=[
                                                                        SpecificParameterAssignment(
                                                                            id='hjmt:anon@trans005@purchase_ride',
                                                                            version='any',
                                                                            name=MultilingualString(
                                                                                value='Single ride'
                                                                            ),
                                                                            order=1,
                                                                            validable_element_ref=ValidableElementRef(
                                                                                version='any',
                                                                                ref='home_james@prepriced_trip@travel'
                                                                            ),
                                                                            preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                                                version='any',
                                                                                ref='home_james@prepriced_trip'
                                                                            ),
                                                                            fare_structure_element_ref=FareStructureElementRef(
                                                                                version='any',
                                                                                ref='home_james@prepriced_trip@access'
                                                                            ),
                                                                            sales_offer_package_ref=SalesOfferPackageRef(
                                                                                version='any',
                                                                                ref='home_james@prepriced_trip-SOP@online'
                                                                            ),
                                                                            validity_parameters=ValidityParametersRelStructure(
                                                                                mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref=[
                                                                                    VehiclePoolingRef(
                                                                                        version='any',
                                                                                        ref='chauffeured_car'
                                                                                    ),
                                                                                ],
                                                                                choice=[
                                                                                    OperatorRef(
                                                                                        version='any',
                                                                                        ref='noc:HJM'
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
                                                                                        ref='hjmt:anon@trans005@ride5163'
                                                                                    ),
                                                                                ],
                                                                                choice_2=[
                                                                                    ChauffeuredVehicleServiceRef(
                                                                                        version='any',
                                                                                        ref='hj_cars'
                                                                                    ),
                                                                                ],
                                                                                vehicle_ref=[
                                                                                    VehicleRef(
                                                                                        ref='CD886645',
                                                                                        version_ref='external'
                                                                                    ),
                                                                                ],
                                                                                type_of_travel_document_ref=[
                                                                                    TypeOfTravelDocumentRef(
                                                                                        version='any',
                                                                                        ref='email_confirmation'
                                                                                    ),
                                                                                ],
                                                                                distribution_channel_ref_or_group_of_distribution_channels_ref=[
                                                                                    DistributionChannelRef(
                                                                                        version='any',
                                                                                        ref='online'
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
                                                                id='hjmt:ticket@765452234',
                                                                validity_conditions_or_valid_between=[
                                                                    ValidBetween(
                                                                        from_date=XmlDateTime(2020, 10, 8, 11, 7, 0)
                                                                    ),
                                                                ],
                                                                version='any',
                                                                type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                                    version='any',
                                                                    ref='email_confirmation'
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
    ),
    version='1.2.2'
)
