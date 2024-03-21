from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.discounting_rule import DiscountingRule
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.distance_matrix_element import DistanceMatrixElement
from netex.models.distance_matrix_element_price import DistanceMatrixElementPrice
from netex.models.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.models.distance_matrix_element_prices_rel_structure import DistanceMatrixElementPricesRelStructure
from netex.models.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.models.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.models.distribution_assignment import DistributionAssignment
from netex.models.distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from netex.models.distribution_channel_ref import DistributionChannelRef
from netex.models.distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import DayType
from netex.models.entity_in_version_structure import ValidBetween
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.fare_demand_factor import FareDemandFactor
from netex.models.fare_demand_factor_ref import FareDemandFactorRef
from netex.models.fare_demand_type_enumeration import FareDemandTypeEnumeration
from netex.models.fare_frame import FareFrame
from netex.models.fare_frame_ref import FareFrameRef
from netex.models.fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from netex.models.fare_structure_element import FareStructureElement
from netex.models.fare_structure_element_ref import FareStructureElementRef
from netex.models.fare_structure_element_refs_rel_structure import FareStructureElementRefsRelStructure
from netex.models.fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from netex.models.fare_table_ref import FareTableRef
from netex.models.fare_tables_in_frame_rel_structure import FareTablesInFrameRelStructure
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.models.fulfilment_method_ref import FulfilmentMethodRef
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.generic_parameter_assignments_rel_structure import GenericParameterAssignment
from netex.models.generic_parameter_assignments_rel_structure import GenericParameterAssignmentsRelStructure
from netex.models.group_of_lines import GroupOfLines
from netex.models.group_of_timebands import GroupOfTimebands
from netex.models.group_of_timebands_in_frame_rel_structure import GroupOfTimebandsInFrameRelStructure
from netex.models.group_of_timebands_ref import GroupOfTimebandsRef
from netex.models.groups_of_lines_in_frame_rel_structure import GroupsOfLinesInFrameRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.interchanging import Interchanging
from netex.models.line import Line
from netex.models.line_ref import LineRef
from netex.models.line_refs_rel_structure import LineRefsRelStructure
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.logical_operation_enumeration import LogicalOperationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network import Network
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.network_ref import NetworkRef
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from netex.models.priceable_object_version_structure import CellsRelStructure
from netex.models.priceable_object_version_structure import FareTable
from netex.models.priceable_object_version_structure import FareTablesRelStructure
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.pricing_rules_rel_structure import PricingRulesRelStructure
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.round_trip import RoundTrip
from netex.models.round_trip_type_enumeration import RoundTripTypeEnumeration
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.models.service_frame import ServiceFrame
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.tariff import Tariff
from netex.models.tariff_ref import TariffRef
from netex.models.tariff_zone import TariffZone
from netex.models.tariff_zone_ref import TariffZoneRef
from netex.models.tariff_zone_ref_structure import TariffZoneRefStructure
from netex.models.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.models.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.temporal_validity_parameters_rel_structure import TemporalValidityParametersRelStructure
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.ticketing_service_facility_list import TicketingServiceFacilityList
from netex.models.timeband import Timeband
from netex.models.timeband_ref import TimebandRef
from netex.models.timeband_refs_rel_structure import TimebandRefsRelStructure
from netex.models.timebands_in_frame_rel_structure import TimebandsInFrameRelStructure
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_concession import TypeOfConcession
from netex.models.type_of_concession_ref import TypeOfConcessionRef
from netex.models.type_of_fare_product import TypeOfFareProduct
from netex.models.type_of_fare_product_ref import TypeOfFareProductRef
from netex.models.type_of_tariff import TypeOfTariff
from netex.models.type_of_tariff_ref import TypeOfTariffRef
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_parameter_price import UsageParameterPrice
from netex.models.usage_parameter_prices_rel_structure import UsageParameterPricesRelStructure
from netex.models.usage_parameter_refs_rel_structure import UsageParameterRefsRelStructure
from netex.models.usage_parameters_rel_structure import UsageParametersRelStructure
from netex.models.used_in_refs_rel_structure import UsedInRefsRelStructure
from netex.models.user_profile import UserProfile
from netex.models.user_profile_ref import UserProfileRef
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_ref import ValidableElementRef
from netex.models.validable_elements_rel_structure import ValidableElementsRelStructure
from netex.models.validity_parameters_rel_structure import ValidityParametersRelStructure
from netex.models.value_set import ValueSet
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        validity_condition=[
                            AvailabilityCondition(
                                id='hde:CAL_02',
                                version='any',
                                from_date=XmlDateTime(2011, 1, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        FareFrameRef(
                            value='REQUEST',
                            ref='myfares:FF01'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example of simple point to point fares'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='myfares:DTA@z2z_time_banded',
                validity_conditions_or_valid_between=[
                    ValidityConditionsRelStructure(
                        choice=[
                            ValidBetween(
                                from_date=XmlDateTime(2011, 1, 1, 0, 0, 0, 0, 0),
                                to_date=XmlDateTime(2011, 7, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                ],
                version='1',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='mybus',
                            xmlns='mybus',
                            xmlns_url='http://www.mybuses.eu/stuff',
                            description='My buse network description'
                        ),
                        Codespace(
                            id='myfares',
                            xmlns='myfares',
                            xmlns_url='http://www.myfares,com/fares',
                            description='Fare data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='myfares'
                    ),
                    default_currency='EUR'
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='mybus:DTA@z2z_time_banded@network',
                            version='1.0',
                            name=MultilingualString(
                                value='Stopss and tariff zones for   routes 24 and 46'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@Common_Resources'
                                    ),
                                ]
                            ),
                            network=Network(
                                id='mybus:DTA',
                                version='any',
                                transport_organisation_ref=OperatorRef(
                                    version='any',
                                    ref='mybus:DTA'
                                ),
                                groups_of_lines=GroupsOfLinesInFrameRelStructure(
                                    group_of_lines=[
                                        GroupOfLines(
                                            id='mybus:DTA@lines',
                                            version='any',
                                            members=LineRefsRelStructure(
                                                line_ref=[
                                                    LineRef(
                                                        version='any',
                                                        ref='mybus:Line_24'
                                                    ),
                                                    LineRef(
                                                        version='any',
                                                        ref='mybus:Line_48'
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                                tariff_zones=TariffZoneRefsRelStructure(
                                    tariff_zone_ref=[
                                        TariffZoneRef(
                                            version='any',
                                            ref='myfares:1'
                                        ),
                                        TariffZoneRef(
                                            version='any',
                                            ref='myfares:2'
                                        ),
                                        TariffZoneRef(
                                            version='any',
                                            ref='myfares:3'
                                        ),
                                    ]
                                )
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line(
                                        id='mybus:Line_24',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line  24'
                                        )
                                    ),
                                    Line(
                                        id='mybus:Line_48',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line  48'
                                        )
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='mybus:SSP_001',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha & Castle'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.0000'),
                                            latitude=Decimal('0.1000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        tariff_zones=TariffZoneRefsRelStructure(
                                            tariff_zone_ref=[
                                                TariffZoneRef(
                                                    version='any',
                                                    ref='myfares:1'
                                                ),
                                            ]
                                        ),
                                        short_name=MultilingualString(
                                            value='Alpha'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='EANDC'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        tariff_zones=TariffZoneRefsRelStructure(
                                            tariff_zone_ref=[
                                                TariffZoneRef(
                                                    version='any',
                                                    ref='myfares:2'
                                                ),
                                            ]
                                        ),
                                        short_name=MultilingualString(
                                            value='Bravo'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='MARCH'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.3000'),
                                            latitude=Decimal('0.3000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        tariff_zones=TariffZoneRefsRelStructure(
                                            tariff_zone_ref=[
                                                TariffZoneRef(
                                                    version='any',
                                                    ref='myfares:2'
                                                ),
                                            ]
                                        ),
                                        short_name=MultilingualString(
                                            value='Charley'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='KENG'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_022',
                                        version='any',
                                        name=MultilingualString(
                                            value='Quebec Street'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.34000'),
                                            latitude=Decimal('0.34000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        tariff_zones=TariffZoneRefsRelStructure(
                                            tariff_zone_ref=[
                                                TariffZoneRef(
                                                    version='any',
                                                    ref='myfares:2'
                                                ),
                                                TariffZoneRef(
                                                    version='any',
                                                    ref='myfares:3'
                                                ),
                                            ]
                                        ),
                                        short_name=MultilingualString(
                                            value='Quebec'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='QBC'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_021',
                                        version='any',
                                        name=MultilingualString(
                                            value='Romeo'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.34000'),
                                            latitude=Decimal('0.34000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        tariff_zones=TariffZoneRefsRelStructure(
                                            tariff_zone_ref=[
                                                TariffZoneRef(
                                                    version='any',
                                                    ref='myfares:3'
                                                ),
                                            ]
                                        ),
                                        short_name=MultilingualString(
                                            value='Romeo'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='ROM'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                ]
                            ),
                            tariff_zones=TariffZonesInFrameRelStructure(
                                tariff_zone=[
                                    TariffZone(
                                        id='myfares:1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Zone 1'
                                        )
                                    ),
                                    TariffZone(
                                        id='myfares:2',
                                        version='any',
                                        name=MultilingualString(
                                            value='Zone 2'
                                        )
                                    ),
                                    TariffZone(
                                        id='myfares:3',
                                        version='any',
                                        name=MultilingualString(
                                            value='Zone 3'
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='myfares:DTA@z2z_time_banded@products',
                            version='1.0',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ServiceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@z2z_time_banded@network'
                                    ),
                                    ServiceCalendarFrameRef(
                                        version='1.0',
                                        ref='myfares:DTA@z2z_time_banded@calendar'
                                    ),
                                ]
                            ),
                            pricing_parameter_set=PricingParameterSet(
                                id='myfares:price_rules',
                                version='1.0',
                                pricing_rules=PricingRulesRelStructure(
                                    pricing_rule=[
                                        DiscountingRule(
                                            id='myfares:0%',
                                            version='1.0',
                                            discount_as_percentage=Decimal('0')
                                        ),
                                        DiscountingRule(
                                            id='myfares:50%',
                                            version='1.0',
                                            discount_as_percentage=Decimal('50')
                                        ),
                                    ]
                                )
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='myfares:Tz2z',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Zone to Zone Trip tariff'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        type_of_tariff_ref=TypeOfTariffRef(
                                            version='ntx:v1.0',
                                            ref='ntx:zone_to_zone'
                                        ),
                                        quality_structure_factors=QualityStructureFactorsRelStructure(
                                            quality_structure_factor_ref_or_quality_structure_factor=[
                                                FareDemandFactor(
                                                    id='myfares:peak',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Any time'
                                                    ),
                                                    fare_demand_type=FareDemandTypeEnumeration.PEAK
                                                ),
                                                FareDemandFactor(
                                                    id='myfares:off_peak',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Off Peak'
                                                    ),
                                                    fare_demand_type=FareDemandTypeEnumeration.OFF_PEAK
                                                ),
                                            ]
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='myfares:Tz2z@access',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Allowed zone to zone transitions'
                                                    ),
                                                    choice_1=DistanceMatrixElementsRelStructure(
                                                        distance_matrix_element_ref_or_distance_matrix_element=[
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:Z1+Z2'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:Z1+Z3'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:Z2+Z3'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:Z1+Z1'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:Z2+Z2'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:Z3+Z3'
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Tz2z@access',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:can_access'
                                                        ),
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            choice=[
                                                                OperatorRef(
                                                                    version='any',
                                                                    ref='mybus:DTA'
                                                                ),
                                                            ],
                                                            group_of_lines_ref=[
                                                                NetworkRef(
                                                                    version='any',
                                                                    ref='mybus:DTA'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Tz2z@eligibility',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Eligible user types'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Tz2z@eligibility',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:eligible'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.XOR,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UserProfile(
                                                                    id='myfares:adult',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Child Fare'
                                                                    ),
                                                                    prices=UsageParameterPricesRelStructure(
                                                                        usage_parameter_price_ref_or_usage_parameter_price_or_cell_ref=[
                                                                            UsageParameterPrice(
                                                                                id='myfares:Tz2z@adult',
                                                                                version='1.0',
                                                                                name=MultilingualString(
                                                                                    value='Adult - full fare'
                                                                                ),
                                                                                choice=UserProfileRef(
                                                                                    version='any',
                                                                                    ref='myfares:adult'
                                                                                )
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    type_of_concession_ref=TypeOfConcessionRef(
                                                                        version='any',
                                                                        ref='myfares:adult'
                                                                    ),
                                                                    maximum_age=16
                                                                ),
                                                                UserProfile(
                                                                    id='myfares:child',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Child Fare'
                                                                    ),
                                                                    prices=UsageParameterPricesRelStructure(
                                                                        usage_parameter_price_ref_or_usage_parameter_price_or_cell_ref=[
                                                                            UsageParameterPrice(
                                                                                id='myfares:Tz2z@child',
                                                                                version='1.0',
                                                                                name=MultilingualString(
                                                                                    value='Child discount - all fares'
                                                                                ),
                                                                                discounting_rule_ref_or_pricing_rule_ref_or_pricing_rule=DiscountingRuleRef(
                                                                                    version='1.0',
                                                                                    ref='myfares:50%'
                                                                                ),
                                                                                choice=UserProfileRef(
                                                                                    version='any',
                                                                                    ref='myfares:child'
                                                                                )
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    type_of_concession_ref=TypeOfConcessionRef(
                                                                        version='any',
                                                                        ref='myfares:child'
                                                                    ),
                                                                    maximum_age=16
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Tz2z@demand_types',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Timebands for travel'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Tz2z@demand_types',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:can_access_when'
                                                        ),
                                                        includes_grouping_type=LogicalOperationEnumeration.XOR,
                                                        includes=GenericParameterAssignmentsRelStructure(
                                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                                GenericParameterAssignment(
                                                                    id='myfares:Tz2z@demand_types@peak',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='Peak Fare'
                                                                    ),
                                                                    order=1,
                                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                                        version='ntx:v1.0',
                                                                        ref='ntx:can_access_when'
                                                                    ),
                                                                    validity_parameter_grouping_type=LogicalOperationEnumeration.AND,
                                                                    temporal_validity_parameters=TemporalValidityParametersRelStructure(
                                                                        day_type_ref=[
                                                                            DayTypeRef(
                                                                                version='any',
                                                                                ref='myfares:DT_01-MF-NH'
                                                                            ),
                                                                        ],
                                                                        group_of_timebands_ref=[
                                                                            GroupOfTimebandsRef(
                                                                                version='any',
                                                                                ref='myfares:peak'
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    quality_structure_factor_ref=FareDemandFactorRef(
                                                                        version='1.0',
                                                                        ref='myfares:peak'
                                                                    )
                                                                ),
                                                                GenericParameterAssignment(
                                                                    id='myfares:Tz2z@demand_types@off_peak',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='Peak Fare'
                                                                    ),
                                                                    order=1,
                                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                                        version='ntx:v1.0',
                                                                        ref='ntx:can_access_when'
                                                                    ),
                                                                    temporal_validity_parameters=TemporalValidityParametersRelStructure(
                                                                        day_type_ref=[
                                                                            DayTypeRef(
                                                                                version='any',
                                                                                ref='myfares:DT_02-NotWorkingDay'
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    quality_structure_factor_ref=FareDemandFactorRef(
                                                                        version='1.0',
                                                                        ref='myfares:off_peak'
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Tz2z@conditions_of_travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='eligible user types'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Tz2z@conditions_of_travel',
                                                        version='1.0',
                                                        name=MultilingualString(
                                                            value='Conditions of travel'
                                                        ),
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:condition_of_use'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                RoundTrip(
                                                                    id='myfares:Tz2z@conditions_of_travel@direction',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='Single Trip'
                                                                    ),
                                                                    trip_type=RoundTripTypeEnumeration.SINGLE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='myfares:Tz2z@conditions_of_travel@one_trip',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='One trip only, any route, unlimited transfers'
                                                                    ),
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    maximal_frequency=1
                                                                ),
                                                                Interchanging(
                                                                    id='myfares:Tz2z@conditions_of_travel@no_transfers',
                                                                    version='1.0',
                                                                    maximum_number_of_interchanges=0
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
                                                    id='myfares:Z1+Z1',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 1 to Zone 1'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:1'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:1'
                                                    ),
                                                    prices=DistanceMatrixElementPricesRelStructure(
                                                        distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref=[
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z1+Z1@peak'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z1+Z1@offPeak'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z1+Z2',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 1 to Zone 2'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:1'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:2'
                                                    ),
                                                    prices=DistanceMatrixElementPricesRelStructure(
                                                        distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref=[
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z1+Z2@peak'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z1+Z2@offPeak'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z1+Z3',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 1 to Zone 3'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:1'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:3'
                                                    ),
                                                    prices=DistanceMatrixElementPricesRelStructure(
                                                        distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref=[
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z1+Z3@peak'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z1+Z3@offPeak'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z2+Z2',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 2 to Zone 2'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:2'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:2'
                                                    ),
                                                    prices=DistanceMatrixElementPricesRelStructure(
                                                        distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref=[
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z2+Z2@peak'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z2+Z2@offPeak'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z2+Z3',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 2 to Zone 3'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:2'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:3'
                                                    ),
                                                    prices=DistanceMatrixElementPricesRelStructure(
                                                        distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref=[
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z2+Z3@peak'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z2+Z3@offPeak'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z3+Z3',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 3 to Zone 3'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:3'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:3'
                                                    ),
                                                    prices=DistanceMatrixElementPricesRelStructure(
                                                        distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref=[
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z3+Z3@peak'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='any',
                                                                ref='myfares:SingleTrip@Z3+Z3@offPeak'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        fare_tables=FareTablesRelStructure(
                                            fare_table_ref_or_fare_table=[
                                                FareTableRef(
                                                    version='1.0',
                                                    ref='myfares:DTA'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_products=FareProductsInFrameRelStructure(
                                fare_product=[
                                    PreassignedFareProduct(
                                        id='myfares:SingleTrip',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Adult Standard Zone to zone - Peak'
                                        ),
                                        type_of_fare_product_ref_or_types_of_fare_product=TypeOfFareProductRef(
                                            version='ntx:v1.0',
                                            ref='ntx:trip'
                                        ),
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        validable_elements=ValidableElementsRelStructure(
                                            validable_element_ref_or_validable_element=[
                                                ValidableElement(
                                                    id='myfares:SingleTrip@travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Single ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Tz2z@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Tz2z@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Tz2z@demand_types'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Tz2z@conditions_of_travel'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='myfares:SingleTrip@access',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Single ride'
                                                    ),
                                                    is_first_in_sequence=True,
                                                    is_last_in_sequence=True,
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='1.0',
                                                        ref='myfares:SingleTrip@travel'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            sales_offer_packages=SalesOfferPackagesInFrameRelStructure(
                                sales_offer_package=[
                                    SalesOfferPackage(
                                        id='myfares:SingleTrip-SOP@p-ticket',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Single'
                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='myfares:SingleTrip-SOP@p-ticket@atStop',
                                                    version='10',
                                                    name=MultilingualString(
                                                        value='Onboard'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Pay for ticket onboard'
                                                    ),
                                                    order=1,
                                                    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref=DistributionChannelRef(
                                                        ref='ntx:on_board',
                                                        version_ref='ntx:v1.0'
                                                    ),
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.AT_STOP,
                                                    ticketing_service_facility_list=TicketingServiceFacilityList(
                                                        value=[
                                                            TicketingServiceFacilityEnumeration.PURCHASE,
                                                        ]
                                                    ),
                                                    payment_methods=[
                                                        PaymentMethodEnumeration.CASH_AND_CARD,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        ref='ntx:collect_on_board',
                                                        version_ref='ntx:v1.0'
                                                    )
                                                ),
                                                DistributionAssignment(
                                                    id='myfares:SingleTrip-SOP@p-ticket@onBoard',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Onboard'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Pay for ticket onboard'
                                                    ),
                                                    order=2,
                                                    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref=DistributionChannelRef(
                                                        ref='ntx:on_board',
                                                        version_ref='ntx:v1.0'
                                                    ),
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.ON_BOARD,
                                                    ticketing_service_facility_list=TicketingServiceFacilityList(
                                                        value=[
                                                            TicketingServiceFacilityEnumeration.PURCHASE,
                                                        ]
                                                    ),
                                                    payment_methods=[
                                                        PaymentMethodEnumeration.CASH_AND_CARD,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        ref='ntx:collect_on_board',
                                                        version_ref='ntx:v1.0'
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:SingleTrip-SOP@p-ticket',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        ref='ntx:printed_ticket',
                                                        version_ref='ntx:v1.0'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='1.0',
                                                        ref='myfares:SingleTrip'
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
                            id='myfares:DTA@z2z_time_banded@prices',
                            version='1.0',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='myfares:DTA@z2z_time_banded@products'
                                    ),
                                ]
                            ),
                            fare_tables=FareTablesInFrameRelStructure(
                                fare_table=[
                                    FareTable(
                                        id='myfares:DTA',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Prices for Zonal Tariff Trip Product'
                                        ),
                                        prices_for=PriceableObjectRefsRelStructure(
                                            choice=[
                                                SalesOfferPackageRef(
                                                    version='1.0',
                                                    ref='myfares:SingleTrip-SOP@p-ticket'
                                                ),
                                                PreassignedFareProductRef(
                                                    version='1.0',
                                                    ref='myfares:SingleTrip'
                                                ),
                                            ]
                                        ),
                                        used_in=UsedInRefsRelStructure(
                                            choice=[
                                                TariffRef(
                                                    version='1.0',
                                                    ref='myfares:Tz2z'
                                                ),
                                            ]
                                        ),
                                        limitations=UsageParameterRefsRelStructure(
                                            choice=[
                                                UserProfileRef(
                                                    version='any',
                                                    ref='myfares:adult'
                                                ),
                                            ]
                                        ),
                                        includes=FareTablesRelStructure(
                                            fare_table_ref_or_fare_table=[
                                                FareTable(
                                                    id='myfares:SingleTrip@off_peak',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Off Peak Prices for Zonal Tariff Product'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            FareDemandFactorRef(
                                                                version='1.0',
                                                                ref='myfares:off_peak'
                                                            ),
                                                        ]
                                                    ),
                                                    cells=CellsRelStructure(
                                                        choice=[
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z1+Z1@offPeak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 1 to Zone 2'
                                                                ),
                                                                amount=Decimal('0.50'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z1+Z1'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z1+Z2@offPeak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 1 to Zone 2'
                                                                ),
                                                                amount=Decimal('1.00'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z1+Z2'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z1+Z3@offPeak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 1 to Zone 3'
                                                                ),
                                                                amount=Decimal('3.00'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z1+Z3'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z2+Z2@offPeak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 2 to Zone 2'
                                                                ),
                                                                amount=Decimal('0.50'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z2+Z2'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z2+Z3@offPeak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 2 to Zone 3'
                                                                ),
                                                                amount=Decimal('2.00'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z2+Z3'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z3+Z3@offPeak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 3 to Zone 3'
                                                                ),
                                                                amount=Decimal('0.75'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z3+Z3'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareTable(
                                                    id='myfares:SingleTrip@peak',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Peak Fare Prices for Zonal Tariff Trip Product'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            FareDemandFactorRef(
                                                                version='1.0',
                                                                ref='myfares:peak'
                                                            ),
                                                        ]
                                                    ),
                                                    cells=CellsRelStructure(
                                                        choice=[
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z1+Z1@peak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 1 to Zone 1 Peak'
                                                                ),
                                                                amount=Decimal('1.00'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z1+Z1'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z1+Z2@peak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 1 to Zone 2 Peak'
                                                                ),
                                                                amount=Decimal('2.00'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z1+Z2'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z1+Z3@peak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 1 to Zone 3 Peak'
                                                                ),
                                                                amount=Decimal('4.00'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z1+Z3'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z2+Z2@peak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 2 to Zone 2 Peak'
                                                                ),
                                                                amount=Decimal('1.00'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z2+Z2'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z2+Z3@peak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 2 to Zone 3 Peak'
                                                                ),
                                                                amount=Decimal('2.50'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z2+Z3'
                                                                )
                                                            ),
                                                            DistanceMatrixElementPrice(
                                                                id='myfares:SingleTrip@Z3+Z3@peak',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Zone 3 to Zone 3 Peak'
                                                                ),
                                                                amount=Decimal('1.00'),
                                                                distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                    version='any',
                                                                    ref='myfares:Z3+Z3'
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
                        ServiceCalendarFrame(
                            id='myfares:DTA@z2z_time_banded@calendar',
                            version='1.0',
                            name=MultilingualString(
                                value='Service Calendar Coding'
                            ),
                            service_calendar=ServiceCalendar(
                                id='myfares:DTA@z2z_time_banded@calendar',
                                version='any',
                                from_date=XmlDate(2010, 11, 1),
                                to_date=XmlDate(2012, 11, 14)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType(
                                        id='myfares:DT_01-MF-NH',
                                        version='any',
                                        name=MultilingualString(
                                            value='Weekdays unless a holiday'
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.MONDAY,
                                                        DayOfWeekEnumeration.TUESDAY,
                                                        DayOfWeekEnumeration.WEDNESDAY,
                                                        DayOfWeekEnumeration.THURSDAY,
                                                        DayOfWeekEnumeration.FRIDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NOT_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType(
                                        id='myfares:DT_02-NotWorkingDay',
                                        version='any',
                                        name=MultilingualString(
                                            value='Not a working day'
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.EVERYDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NOT_WORKING_DAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            timebands=TimebandsInFrameRelStructure(
                                timeband=[
                                    Timeband(
                                        id='myfares:MorningPeak',
                                        version='any',
                                        name=MultilingualString(
                                            value='Morning Peak'
                                        ),
                                        start_time_or_start_event=XmlTime(8, 30, 0, 0),
                                        choice=[
                                            XmlTime(10, 0, 0, 0),
                                        ]
                                    ),
                                    Timeband(
                                        id='myfares:EveningPeak',
                                        version='any',
                                        name=MultilingualString(
                                            value='Evening Peak'
                                        ),
                                        start_time_or_start_event=XmlTime(17, 0, 0, 0),
                                        choice=[
                                            XmlTime(18, 30, 0, 0),
                                        ]
                                    ),
                                ]
                            ),
                            group_of_timebands=GroupOfTimebandsInFrameRelStructure(
                                group_of_timebands=[
                                    GroupOfTimebands(
                                        id='myfares:peak',
                                        version='any',
                                        name=MultilingualString(
                                            value='Peak Fare hours'
                                        ),
                                        timebands=TimebandRefsRelStructure(
                                            timeband_ref=[
                                                TimebandRef(
                                                    version='any',
                                                    ref='myfares:MorningPeak'
                                                ),
                                                TimebandRef(
                                                    version='any',
                                                    ref='myfares:EveningPeak'
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
            ResourceFrame(
                id='mybus:DTA@Common_Resources',
                version='1.0',
                name=MultilingualString(
                    value='Common resources'
                ),
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='ntx',
                            xmlns='ntx',
                            xmlns_url='http://netex.org.uk/',
                            description='Netex built in value'
                        ),
                    ]
                ),
                types_of_value=TypesOfValueInFrameRelStructure(
                    choice=[
                        ValueSet(
                            id='ntx:Types_of_Tariff',
                            version='ntx:v1.0',
                            name=MultilingualString(
                                value='Types of Tariff'
                            ),
                            values=TypesOfValueStructure(
                                type_of_value_or_type_of_entity=[
                                    TypeOfTariff(
                                        id='ntx:Distance_kilometers',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Kilometer Distance Kilometers'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:flat',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Flat'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:point_to_point',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Point to point'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:zone_to_zone',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Zone to Zone'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:zonal',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Zonal'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:section',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Section'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:banded',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Section'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:stored_value',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Stored value'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:discount',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Discount value'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:multitrip',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Multitrip carnet'
                                        )
                                    ),
                                    TypeOfTariff(
                                        id='ntx:identity_card',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='SIdentity'
                                        )
                                    ),
                                ]
                            ),
                            class_of_values='TypeOfTariff'
                        ),
                        ValueSet(
                            id='ntx:Types_of_FareProduct',
                            version='ntx:v1.0',
                            name=MultilingualString(
                                value='Types of Fare Product'
                            ),
                            values=TypesOfValueStructure(
                                type_of_value_or_type_of_entity=[
                                    TypeOfFareProduct(
                                        id='ntx:trip',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Trip product'
                                        )
                                    ),
                                    TypeOfFareProduct(
                                        id='ntx:multi_trip',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Multitrip / carnet  product'
                                        )
                                    ),
                                    TypeOfFareProduct(
                                        id='ntx:period_pass',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Peroid pass product'
                                        )
                                    ),
                                    TypeOfFareProduct(
                                        id='ntx:day_pass',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Day pass product'
                                        )
                                    ),
                                    TypeOfFareProduct(
                                        id='ntx:discount_card',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Discount  product'
                                        )
                                    ),
                                ]
                            ),
                            class_of_values='TypeOfFareProduct'
                        ),
                        ValueSet(
                            id='myfares:Types_of_Concession',
                            version='any',
                            name=MultilingualString(
                                value='Types of concession'
                            ),
                            values=TypesOfValueStructure(
                                type_of_value_or_type_of_entity=[
                                    TypeOfConcession(
                                        id='myfares:adult',
                                        version='any',
                                        name=MultilingualString(
                                            value='Adult'
                                        )
                                    ),
                                    TypeOfConcession(
                                        id='myfares:child',
                                        version='any',
                                        name=MultilingualString(
                                            value='Student'
                                        )
                                    ),
                                ]
                            ),
                            class_of_values='TypeOfConcession'
                        ),
                        ValueSet(
                            id='ntx:Types_of_AccessRightAssignment',
                            version='ntx:v1.0',
                            name=MultilingualString(
                                value='Types of Access Right Assignment'
                            ),
                            values=TypesOfValueStructure(
                                type_of_value_or_type_of_entity=[
                                    TypeOfAccessRightAssignment(
                                        id='ntx:eligible',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Eligible for a product or discount'
                                        )
                                    ),
                                    TypeOfAccessRightAssignment(
                                        id='ntx:can_access',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Grants access rights to use or travel on'
                                        )
                                    ),
                                    TypeOfAccessRightAssignment(
                                        id='ntx:can_access_when',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Grants access rights to use or travel during some period'
                                        )
                                    ),
                                    TypeOfAccessRightAssignment(
                                        id='ntx:condition_of_use',
                                        version='ntx:v1.0',
                                        name=MultilingualString(
                                            value='Defines a condition or restriction on use'
                                        )
                                    ),
                                ]
                            ),
                            class_of_values='TypeOfAccessRightAssignment'
                        ),
                    ]
                ),
                organisations=OrganisationsInFrameRelStructure(
                    organisation_or_transport_organisation=[
                        Operator(
                            id='mybus:DTA',
                            version='any',
                            name=MultilingualString(
                                value='Demo Transit Authority'
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
