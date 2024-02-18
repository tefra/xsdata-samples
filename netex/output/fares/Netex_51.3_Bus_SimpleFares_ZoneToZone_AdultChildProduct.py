from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import ValidBetween
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.cell_versioned_child_structure import CellsRelStructure
from netex.models.cell_versioned_child_structure import FarePricesRelStructure
from netex.models.cell_versioned_child_structure import FareTable1
from netex.models.cell_versioned_child_structure import FareTablesRelStructure
from netex.models.cell_versioned_child_structure import PriceGroup1
from netex.models.cell_versioned_child_structure import PriceGroupsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.discounting_rule import DiscountingRule
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.distance_matrix_element import DistanceMatrixElement
from netex.models.distance_matrix_element_price import DistanceMatrixElementPrice
from netex.models.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.models.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.models.distribution_assignment import DistributionAssignment
from netex.models.distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from netex.models.distribution_channel_ref import DistributionChannelRef
from netex.models.distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.fare_frame import FareFrame
from netex.models.fare_frame_ref import FareFrameRef
from netex.models.fare_prices_in_frame_rel_structure import FarePricesInFrameRelStructure
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
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignment
from netex.models.group_of_lines import GroupOfLines
from netex.models.groups_of_lines_in_frame_rel_structure import GroupsOfLinesInFrameRelStructure
from netex.models.interchanging import Interchanging
from netex.models.line_1 import Line1
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
from netex.models.price_group_ref import PriceGroupRef
from netex.models.priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.pricing_rules_rel_structure import PricingRulesRelStructure
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.round_trip import RoundTrip
from netex.models.round_trip_type_enumeration import RoundTripTypeEnumeration
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.tariff import Tariff
from netex.models.tariff_ref import TariffRef
from netex.models.tariff_zone_1 import TariffZone1
from netex.models.tariff_zone_ref_1 import TariffZoneRef1
from netex.models.tariff_zone_ref_structure import TariffZoneRefStructure
from netex.models.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.models.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.ticketing_service_facility_list import TicketingServiceFacilityList
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_concession import TypeOfConcession
from netex.models.type_of_concession_ref import TypeOfConcessionRef
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_parameter_price import UsageParameterPrice
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
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


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
                                id='hde:range',
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
        value='Example  of simple point to point fares'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='myfares:DTA@z2Z',
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
                            description='My buses'
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
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='mybus:DTA@z2Z@network',
                            version='1',
                            name=MultilingualString(
                                value='Stops for Winter timetable for Network'
                            ),
                            network=Network(
                                id='mybus:DTA',
                                version='any',
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
                                        TariffZoneRef1(
                                            version='any',
                                            ref='myfares:1'
                                        ),
                                        TariffZoneRef1(
                                            version='any',
                                            ref='myfares:2'
                                        ),
                                        TariffZoneRef1(
                                            version='any',
                                            ref='myfares:3'
                                        ),
                                    ]
                                )
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line1(
                                        id='mybus:Line_24',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line  24'
                                        )
                                    ),
                                    Line1(
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
                                                TariffZoneRef1(
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
                                                TariffZoneRef1(
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
                                                TariffZoneRef1(
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
                                                TariffZoneRef1(
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
                                                TariffZoneRef1(
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
                                ]
                            ),
                            tariff_zones=TariffZonesInFrameRelStructure(
                                tariff_zone=[
                                    TariffZone1(
                                        id='myfares:1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Zone 1'
                                        )
                                    ),
                                    TariffZone1(
                                        id='myfares:2',
                                        version='any',
                                        name=MultilingualString(
                                            value='Zone 2'
                                        )
                                    ),
                                    TariffZone1(
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
                            id='myfares:DTA@z2Z@products',
                            version='1.0',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_currency='EUR'
                            ),
                            pricing_parameter_set=PricingParameterSet(
                                id='myfares:myfares',
                                version='1.0',
                                pricing_rules=PricingRulesRelStructure(
                                    pricing_rule=[
                                        DiscountingRule(
                                            id='myfares:0%',
                                            version='any',
                                            discount_as_percentage=Decimal('0')
                                        ),
                                        DiscountingRule(
                                            id='myfares:50%',
                                            version='any',
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
                                            value='Zone tozone tariff'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='myfares:Tz2z@access',
                                                    version='1.0',
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
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.XOR,
                                                        validity_parameters=ValidityParametersRelStructure(
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
                                                                    id='myfares:Tz2z@conditions_of_travel@trip',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='Single Trip'
                                                                    ),
                                                                    trip_type=RoundTripTypeEnumeration.SINGLE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='myfares:Tz2z@conditions_of_travel@frequency',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='One trip no transfers'
                                                                    ),
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    maximal_frequency=1
                                                                ),
                                                                Interchanging(
                                                                    id='myfares:Tz2z@conditions_of_travel@interchanging',
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
                                                        value='Zone 1  to  Zone 1'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:1'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:1'
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z1+Z2',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 1  to  Zone 2'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:1'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:2'
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z1+Z3',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 1  to  Zone 3'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:1'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:3'
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z2+Z2',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 2  to  Zone 2'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:2'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:2'
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z2+Z3',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 2  to  Zone 3'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:2'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:3'
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:Z3+Z3',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Zone 3  to  Zone 3'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:3'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='myfares:3'
                                                    )
                                                ),
                                            ]
                                        ),
                                        price_groups=PriceGroupsRelStructure(
                                            price_group_ref_or_price_group=[
                                                PriceGroupRef(
                                                    version='1.0',
                                                    ref='myfares:DTA@discounts'
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
                                            value='Adult Zone to zone  Trip   '
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
                                                        value='Single  ride'
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
                                                    id='myfares:SingleTrip',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='First ride'
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

                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
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
                            id='myfares:DTA@z2Z@prices',
                            version='1.0',
                            pricing_parameter_set=PricingParameterSet(
                                id='myfares:DTA@rules',
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
                            price_groups=FarePricesInFrameRelStructure(
                                price_group=[
                                    PriceGroup1(
                                        id='myfares:DTA@discounts',
                                        version='1.0',
                                        members=FarePricesRelStructure(
                                            fare_price_ref_or_cell_ref_or_fare_price=[
                                                UsageParameterPrice(
                                                    id='myfares:adult',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Adult price'
                                                    ),
                                                    discounting_rule_ref_or_pricing_rule_ref_or_pricing_rule=DiscountingRuleRef(
                                                        version='1.0',
                                                        ref='myfares:0%'
                                                    ),
                                                    choice=UserProfileRef(
                                                        version='any',
                                                        ref='myfares:adult'
                                                    )
                                                ),
                                                UsageParameterPrice(
                                                    id='myfares:child',
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
                                        )
                                    ),
                                ]
                            ),
                            fare_tables=FareTablesInFrameRelStructure(
                                fare_table=[
                                    FareTable1(
                                        id='myfares:DTA',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Prices for Zonal Trip Product  '
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
                                        cells=CellsRelStructure(
                                            choice=[
                                                DistanceMatrixElementPrice(
                                                    id='myfares:Tz2z@Z1+Z1',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Zone 1  to  Zone 1'
                                                    ),
                                                    amount=Decimal('0.50'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='myfares:Z1+Z2'
                                                    )
                                                ),
                                                DistanceMatrixElementPrice(
                                                    id='myfares:Tz2z@Z1+Z2',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Zone 1  to  Zone 2'
                                                    ),
                                                    amount=Decimal('1.00'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='myfares:Z1+Z2'
                                                    )
                                                ),
                                                DistanceMatrixElementPrice(
                                                    id='myfares:Tz2z@Z1+Z3',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Zone 1  to  Zone 3'
                                                    ),
                                                    amount=Decimal('3.00'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='myfares:Z1+Z3'
                                                    )
                                                ),
                                                DistanceMatrixElementPrice(
                                                    id='myfares:Tz2z@Z2+Z2',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Zone 2  to  Zone 3'
                                                    ),
                                                    amount=Decimal('0.50'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='myfares:Z2+Z2'
                                                    )
                                                ),
                                                DistanceMatrixElementPrice(
                                                    id='myfares:Tz2z@Z2+Z3',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Zone 2  to  Zone 3'
                                                    ),
                                                    amount=Decimal('2.00'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='any',
                                                        ref='myfares:Z2+Z3'
                                                    )
                                                ),
                                                DistanceMatrixElementPrice(
                                                    id='myfares:Tz2z@Z3+Z3',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Zone 2  to  Zone 3'
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
                                ]
                            )
                        ),
                        ResourceFrame(
                            id='myfares:DTA@Common Resources',
                            version='any',
                            name=MultilingualString(
                                value='Common resources'
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    Codespace(
                                        id='ntx',
                                        xmlns='ntx',
                                        xmlns_url='http://www.netex.org.uk',
                                        description='Netex profile'
                                    ),
                                ]
                            ),
                            types_of_value=TypesOfValueInFrameRelStructure(
                                choice=[
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
            ),
        ]
    )
)
