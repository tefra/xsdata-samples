from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.distance_matrix_element import DistanceMatrixElement
from netex.models.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.models.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import ValidBetween
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.fare_frame import FareFrame
from netex.models.fare_frame_ref import FareFrameRef
from netex.models.fare_prices_in_frame_rel_structure import FarePricesInFrameRelStructure
from netex.models.fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from netex.models.fare_structure_element import FareStructureElement
from netex.models.fare_structure_element_ref import FareStructureElementRef
from netex.models.fare_structure_element_refs_rel_structure import FareStructureElementRefsRelStructure
from netex.models.fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from netex.models.fare_zone import FareZone
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.generic_parameter_assignments_rel_structure import GenericParameterAssignment
from netex.models.geographical_interval import GeographicalInterval
from netex.models.geographical_interval_price import GeographicalIntervalPrice
from netex.models.geographical_interval_price_ref import GeographicalIntervalPriceRef
from netex.models.geographical_interval_prices_rel_structure import GeographicalIntervalPricesRelStructure
from netex.models.geographical_interval_ref import GeographicalIntervalRef
from netex.models.geographical_intervals_rel_structure import GeographicalIntervalsRelStructure
from netex.models.geographical_structure_factor import GeographicalStructureFactor
from netex.models.geographical_structure_factor_ref import GeographicalStructureFactorRef
from netex.models.geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from netex.models.geographical_unit import GeographicalUnit
from netex.models.geographical_unit_ref import GeographicalUnitRef
from netex.models.geographical_units_rel_structure import GeographicalUnitsRelStructure
from netex.models.interchanging import Interchanging
from netex.models.interval_type_enumeration import IntervalTypeEnumeration
from netex.models.logical_operation_enumeration import LogicalOperationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network import Network
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.network_ref import NetworkRef
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.price_group_ref import PriceGroupRef
from netex.models.price_unit import PriceUnit
from netex.models.price_unit_ref import PriceUnitRef
from netex.models.price_units_rel_structure import PriceUnitsRelStructure
from netex.models.priceable_object_version_structure import FarePricesRelStructure
from netex.models.priceable_object_version_structure import PriceGroup1
from netex.models.priceable_object_version_structure import PriceGroupsRelStructure
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.round_trip import RoundTrip
from netex.models.round_trip_type_enumeration import RoundTripTypeEnumeration
from netex.models.service_frame import ServiceFrame
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.tariff import Tariff
from netex.models.tariff_zone_ref_1 import TariffZoneRef1
from netex.models.tariff_zone_ref_structure import TariffZoneRefStructure
from netex.models.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.models.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_concession import TypeOfConcession
from netex.models.type_of_fare_product import TypeOfFareProduct
from netex.models.type_of_fare_product_ref import TypeOfFareProductRef
from netex.models.type_of_tariff import TypeOfTariff
from netex.models.type_of_tariff_ref import TypeOfTariffRef
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_end_enumeration import UsageEndEnumeration
from netex.models.usage_parameters_rel_structure import UsageParametersRelStructure
from netex.models.usage_validity_period import UsageValidityPeriod
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_ref import ValidableElementRef
from netex.models.validable_elements_rel_structure import ValidableElementsRelStructure
from netex.models.validity_parameters_rel_structure import ValidityParametersRelStructure
from netex.models.value_set import ValueSet
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from netex.models.zone_ref_structure import ZoneRefStructure
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
                            ref='myfares:any'
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
                id='myfares:DTA@Nested_Zone',
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
                version='1.0',
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
                    ),
                    default_currency='EUR'
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='mybus:DTA@Nested_Zone@network',
                            version='1.0',
                            name=MultilingualString(
                                value='Stops for Fare network '
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
                                tariff_zones=TariffZoneRefsRelStructure(
                                    tariff_zone_ref=[
                                        TariffZoneRef1(
                                            version='any',
                                            ref='mybus:A'
                                        ),
                                        TariffZoneRef1(
                                            version='any',
                                            ref='mybus:B'
                                        ),
                                        TariffZoneRef1(
                                            version='any',
                                            ref='mybus:C'
                                        ),
                                    ]
                                )
                            ),
                            tariff_zones=TariffZonesInFrameRelStructure(
                                tariff_zone=[
                                    FareZone(
                                        id='mybus:A',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha '
                                        ),
                                        short_name=MultilingualString(
                                            value='A'
                                        ),
                                        parent_zone_ref=ZoneRefStructure(
                                            version='any',
                                            ref='mybus:B'
                                        )
                                    ),
                                    FareZone(
                                        id='mybus:B',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo  '
                                        ),
                                        short_name=MultilingualString(
                                            value='B'
                                        ),
                                        parent_zone_ref=ZoneRefStructure(
                                            version='any',
                                            ref='mybus:C'
                                        ),
                                        contains=TariffZoneRefsRelStructure(
                                            tariff_zone_ref=[
                                                TariffZoneRef1(
                                                    version='any',
                                                    ref='mybus:A'
                                                ),
                                            ]
                                        )
                                    ),
                                    FareZone(
                                        id='mybus:C',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley  '
                                        ),
                                        short_name=MultilingualString(
                                            value='C'
                                        ),
                                        contains=TariffZoneRefsRelStructure(
                                            tariff_zone_ref=[
                                                TariffZoneRef1(
                                                    version='any',
                                                    ref='mybus:B'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='myfares:DTA@Nested_Zone@products',
                            version='1.0',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ServiceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@Nested_Zone@network'
                                    ),
                                ]
                            ),
                            geographical_units=GeographicalUnitsRelStructure(
                                geographical_unit_ref_or_geographical_unit=[
                                    GeographicalUnit(
                                        id='myfares:gu',
                                        version='any',
                                        name=MultilingualString(
                                            value='Arbitrary Quantized Unit of Transport Usage - One zone to zone hop'
                                        )
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='myfares:Nested_Zone',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Zonal fares - Nested zones'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        type_of_tariff_ref=TypeOfTariffRef(
                                            version='ntx:v1.0',
                                            ref='ntx:zonal'
                                        ),
                                        geographical_unit_ref=GeographicalUnitRef(
                                            version='any',
                                            ref='myfares:gu'
                                        ),
                                        geographical_intervals=GeographicalIntervalsRelStructure(
                                            geographical_interval_ref_or_geographical_interval=[
                                                GeographicalInterval(
                                                    id='myfares:gi_1zone',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Same zone'
                                                    ),
                                                    number_of_units=1,
                                                    interval_type=IntervalTypeEnumeration.TARIFF_ZONE,
                                                    prices=GeographicalIntervalPricesRelStructure(
                                                        geographical_interval_price_ref_or_geographical_interval_price_or_cell_ref=[
                                                            GeographicalIntervalPriceRef(
                                                                version='1.0',
                                                                ref='myfares:Nested_Zone@gi_1'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                GeographicalInterval(
                                                    id='myfares:gi_2zone',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Two Zones'
                                                    ),
                                                    number_of_units=2,
                                                    interval_type=IntervalTypeEnumeration.TARIFF_ZONE,
                                                    prices=GeographicalIntervalPricesRelStructure(
                                                        geographical_interval_price_ref_or_geographical_interval_price_or_cell_ref=[
                                                            GeographicalIntervalPriceRef(
                                                                version='1.0',
                                                                ref='myfares:Nested_Zone@gi_2'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                GeographicalInterval(
                                                    id='myfares:gi_3zone',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Three Zones'
                                                    ),
                                                    number_of_units=3,
                                                    interval_type=IntervalTypeEnumeration.TARIFF_ZONE,
                                                    prices=GeographicalIntervalPricesRelStructure(
                                                        geographical_interval_price_ref_or_geographical_interval_price_or_cell_ref=[
                                                            GeographicalIntervalPriceRef(
                                                                version='1.0',
                                                                ref='myfares:Nested_Zone@gi_3'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        geographical_structure_factors=GeographicalStructureFactorsRelStructure(
                                            geographical_structure_factor_ref_or_geographical_structure_factor=[
                                                GeographicalStructureFactor(
                                                    id='myfares:1zone',
                                                    version='1.0',
                                                    geographical_interval_ref=GeographicalIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:gi_1zone'
                                                    ),
                                                    geographical_unit_ref=GeographicalUnitRef(
                                                        version='any',
                                                        ref='myfares:gu'
                                                    )
                                                ),
                                                GeographicalStructureFactor(
                                                    id='myfares:2zone',
                                                    version='1.0',
                                                    geographical_interval_ref=GeographicalIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:gi_2zone'
                                                    ),
                                                    geographical_unit_ref=GeographicalUnitRef(
                                                        version='any',
                                                        ref='myfares:gu'
                                                    )
                                                ),
                                                GeographicalStructureFactor(
                                                    id='myfares:3zone',
                                                    version='1.0',
                                                    geographical_interval_ref=GeographicalIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:gi_3zone'
                                                    ),
                                                    geographical_unit_ref=GeographicalUnitRef(
                                                        version='any',
                                                        ref='myfares:gu'
                                                    )
                                                ),
                                            ]
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='myfares:Nested_Zone@access',
                                                    version='1.0',
                                                    choice_1=DistanceMatrixElementsRelStructure(
                                                        distance_matrix_element_ref_or_distance_matrix_element=[
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:A+A'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:A+B'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:A+C'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:B+B'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:B+C'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:C+C'
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Nested_Zone@access',
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
                                                    id='myfares:Nested_Zone@conditions_of_travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='eligible user types'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Nested_Zone@conditions_of_travel',
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
                                                                    id='myfares:Nested_Zone@conditions_of_travel@direction',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='Single Trip'
                                                                    ),
                                                                    trip_type=RoundTripTypeEnumeration.SINGLE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='myfares:Nested_Zone@conditions_of_travel@frequency',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='One trip  '
                                                                    ),
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    minimal_frequency=1,
                                                                    maximal_frequency=1
                                                                ),
                                                                Interchanging(
                                                                    id='myfares:Nested_Zone@conditions_of_travel@interchanging',
                                                                    version='1.0',
                                                                    can_interchange=True,
                                                                    can_break_journey=False
                                                                ),
                                                                UsageValidityPeriod(
                                                                    id='myfares:Nested_Zone@conditions_of_travel@until',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Valid untile ride complete'
                                                                    ),
                                                                    usage_end=UsageEndEnumeration.END_OF_RIDE
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
                                                    id='myfares:A+A',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Alpha to Alpha'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:A'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:A'
                                                    ),
                                                    structure_factors=GeographicalStructureFactorsRelStructure(
                                                        geographical_structure_factor_ref_or_geographical_structure_factor=[
                                                            GeographicalStructureFactorRef(
                                                                version='1.0',
                                                                ref='myfares:1zone'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:A+B',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Alpha to Bravo'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:A'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:B'
                                                    ),
                                                    structure_factors=GeographicalStructureFactorsRelStructure(
                                                        geographical_structure_factor_ref_or_geographical_structure_factor=[
                                                            GeographicalStructureFactorRef(
                                                                version='1.0',
                                                                ref='myfares:2zone'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:A+C',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Alpha to Charley'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:A'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:C'
                                                    ),
                                                    structure_factors=GeographicalStructureFactorsRelStructure(
                                                        geographical_structure_factor_ref_or_geographical_structure_factor=[
                                                            GeographicalStructureFactorRef(
                                                                version='1.0',
                                                                ref='myfares:3zone'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:B+B',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bravo to Charley'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:B'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:B'
                                                    ),
                                                    structure_factors=GeographicalStructureFactorsRelStructure(
                                                        geographical_structure_factor_ref_or_geographical_structure_factor=[
                                                            GeographicalStructureFactorRef(
                                                                version='1.0',
                                                                ref='myfares:1zone'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:B+C',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bravo to Charley'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:B'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:C'
                                                    ),
                                                    structure_factors=GeographicalStructureFactorsRelStructure(
                                                        geographical_structure_factor_ref_or_geographical_structure_factor=[
                                                            GeographicalStructureFactorRef(
                                                                version='1.0',
                                                                ref='myfares:2zone'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:C+C',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Charley to Charley'
                                                    ),
                                                    choice=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:C'
                                                    ),
                                                    choice_1=TariffZoneRefStructure(
                                                        version='any',
                                                        ref='mybus:C'
                                                    ),
                                                    structure_factors=GeographicalStructureFactorsRelStructure(
                                                        geographical_structure_factor_ref_or_geographical_structure_factor=[
                                                            GeographicalStructureFactorRef(
                                                                version='1.0',
                                                                ref='myfares:1zone'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        price_groups=PriceGroupsRelStructure(
                                            price_group_ref_or_price_group=[
                                                PriceGroupRef(
                                                    version='1.0',
                                                    ref='myfares:DTA@Nested_Zone'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_products=FareProductsInFrameRelStructure(
                                fare_product=[
                                    PreassignedFareProduct(
                                        id='myfares:Single_trip',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Zone passes'
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
                                                    id='myfares:Single_trip@travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Single  ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Nested_Zone@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Nested_Zone@conditions_of_travel'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='myfares:Single_trip@travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='First ride'
                                                    ),
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='1.0',
                                                        ref='myfares:Single_trip@travel'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='myfares:DTA@Nested_Zone@prices',
                            version='1.0',
                            name=MultilingualString(
                                value='Prices for unit zone '
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='myfares:DTA@Nested_Zone@products'
                                    ),
                                ]
                            ),
                            pricing_parameter_set=PricingParameterSet(
                                id='myfares:DTA@Nested_Zone@pp',
                                version='any',
                                price_unit_ref=PriceUnitRef(
                                    version='any',
                                    ref='myfares:1Zone'
                                ),
                                price_units=PriceUnitsRelStructure(
                                    price_unit_ref_or_price_unit=[
                                        PriceUnit(
                                            id='myfares:1Zone',
                                            version='any',
                                            name=MultilingualString(
                                                value='Arbitrary Quanitized Unit of Transport Usage -  '
                                            )
                                        ),
                                    ]
                                )
                            ),
                            price_groups=FarePricesInFrameRelStructure(
                                price_group=[
                                    PriceGroup1(
                                        id='myfares:DTA@Nested_Zone',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Unit fare zones'
                                        ),
                                        members=FarePricesRelStructure(
                                            fare_price_ref_or_cell_ref_or_fare_price=[
                                                GeographicalIntervalPrice(
                                                    id='myfares:Nested_Zone@gi_1',
                                                    version='1.0',
                                                    amount=Decimal('1.00'),
                                                    units=Decimal('1'),
                                                    geographical_interval_ref=GeographicalIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:gi_1zone'
                                                    )
                                                ),
                                                GeographicalIntervalPrice(
                                                    id='myfares:Nested_Zone@gi_2',
                                                    version='1.0',
                                                    amount=Decimal('1.50'),
                                                    units=Decimal('2'),
                                                    geographical_interval_ref=GeographicalIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:gi_2zone'
                                                    )
                                                ),
                                                GeographicalIntervalPrice(
                                                    id='myfares:Nested_Zone@gi_3',
                                                    version='1.0',
                                                    amount=Decimal('3.00'),
                                                    units=Decimal('3'),
                                                    geographical_interval_ref=GeographicalIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:gi_3zone'
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
                                                    id='ntx:unit_distance',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Unit distance (count of stops, sections, zones)'
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
                                        id='myfares:Types_of_TravelDocument',
                                        version='any',
                                        name=MultilingualString(
                                            value='Types of concession'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfTravelDocument(
                                                    id='myfares:printed_ticket',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Paper ticket'
                                                    )
                                                ),
                                                TypeOfTravelDocument(
                                                    id='myfares:mobile_app',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Mobile app'
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='TypeOfTravelDocument'
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
