from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.distance_matrix_element import DistanceMatrixElement
from netex.models.distance_matrix_element_price import DistanceMatrixElementPrice
from netex.models.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.models.distance_matrix_element_prices_rel_structure import DistanceMatrixElementPricesRelStructure
from netex.models.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.models.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import ValidBetween
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.fare_frame import FareFrame
from netex.models.fare_frame_ref import FareFrameRef
from netex.models.fare_prices_in_frame_rel_structure import FarePricesInFrameRelStructure
from netex.models.fare_product_ref import FareProductRef
from netex.models.fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from netex.models.fare_structure_element import FareStructureElement
from netex.models.fare_structure_element_ref import FareStructureElementRef
from netex.models.fare_structure_element_refs_rel_structure import FareStructureElementRefsRelStructure
from netex.models.fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.generic_parameter_assignments_rel_structure import GenericParameterAssignment
from netex.models.interchanging import Interchanging
from netex.models.line import Line
from netex.models.line_ref import LineRef
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.logical_operation_enumeration import LogicalOperationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.price_group_ref import PriceGroupRef
from netex.models.priceable_object_version_structure import FarePricesRelStructure
from netex.models.priceable_object_version_structure import PriceGroup
from netex.models.priceable_object_version_structure import PriceGroupsRelStructure
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.round_trip import RoundTrip
from netex.models.round_trip_type_enumeration import RoundTripTypeEnumeration
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.tariff import Tariff
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_fare_product import TypeOfFareProduct
from netex.models.type_of_fare_product_ref import TypeOfFareProductRef
from netex.models.type_of_tariff import TypeOfTariff
from netex.models.type_of_tariff_ref import TypeOfTariffRef
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_parameters_rel_structure import UsageParametersRelStructure
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_ref import ValidableElementRef
from netex.models.validable_elements_rel_structure import ValidableElementsRelStructure
from netex.models.validity_parameters_rel_structure import ValidityParametersRelStructure
from netex.models.value_set import ValueSet
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
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
                                id='range',
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
                id='myfares:DTA@Line_1',
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
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='mybus:DTA@Line_1@network',
                            version='1.0',
                            name=MultilingualString(
                                value='Stops for Line 1 Tariff'
                            ),
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_codespace_ref=CodespaceRefStructure(
                                    ref='mybus'
                                )
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@Common_Resources'
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line(
                                        id='mybus:Line_1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 1'
                                        ),
                                        operator_ref=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
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
                                        short_name=MultilingualString(
                                            value='Alpha'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='ALPH'
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
                                            value='Bravo Street'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Bravo'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='BRAV'
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
                                            value='Charley Crescent'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.3000'),
                                            latitude=Decimal('0.3000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Charley'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='CHAS'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='myfares:DTA@Line_1@products',
                            version='1.0',
                            name=MultilingualString(
                                value='Fare Products  for Line 1 '
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ServiceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@Line_1@network'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='myfares:PointToPoint',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Point to pont tariff'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        type_of_tariff_ref=TypeOfTariffRef(
                                            version='ntx:v1.0',
                                            ref='ntx:point_to_point'
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='myfares:PointToPoint@access',
                                                    version='1.0',
                                                    choice_1=DistanceMatrixElementsRelStructure(
                                                        distance_matrix_element_ref_or_distance_matrix_element=[
                                                            DistanceMatrixElementRef(
                                                                version='1.0',
                                                                ref='myfares:SSP_001+SSP_002'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='1.0',
                                                                ref='myfares:SSP_001+SSP_077'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='1.0',
                                                                ref='myfares:SSP_002+SSP_077'
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:PointToPoint@access',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:can_access'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.XOR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            choice=[
                                                                OperatorRef(
                                                                    version='any',
                                                                    ref='mybus:DTA'
                                                                ),
                                                            ],
                                                            line_ref=[
                                                                LineRef(
                                                                    version='any',
                                                                    ref='mybus:Line_1'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:PointToPoint@conditions_of_travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Conditions of Travel '
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:PointToPoint@conditions_of_travel',
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
                                                                    id='myfares:PointToPoint@conditions_of_travel@trip',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='Single Trip'
                                                                    ),
                                                                    trip_type=RoundTripTypeEnumeration.SINGLE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='myfares:PointToPoint@conditions_of_travel@frequency',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='One trip no transfers'
                                                                    ),
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    maximal_frequency=1
                                                                ),
                                                                Interchanging(
                                                                    id='myfares:PointToPoint@conditions_of_travel@interchanging',
                                                                    version='1.0',
                                                                    from_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                                                    to_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                                                    maximum_number_of_interchanges=0,
                                                                    can_break_journey=False
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
                                                    id='myfares:SSP_001+SSP_002',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Alpha to Bravo'
                                                    ),
                                                    choice=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    choice_1=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    prices=DistanceMatrixElementPricesRelStructure(
                                                        distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref=[
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:SSP_001+SSP_002'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:SSP_001+SSP_077',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Alpha to Charley'
                                                    ),
                                                    choice=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    choice_1=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    prices=DistanceMatrixElementPricesRelStructure(
                                                        distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref=[
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:SSP_001+SSP_077'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:SSP_002+SSP_077',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Bravo to Charley'
                                                    ),
                                                    choice=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    choice_1=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    prices=DistanceMatrixElementPricesRelStructure(
                                                        distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref=[
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:SSP_002+SSP_077'
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
                                                    ref='myfares:Line_1'
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
                                            value='Single trip'
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
                                                        value='Single trip'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint@conditions_of_travel'
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
                                                    is_first_in_sequence=True,
                                                    is_last_in_sequence=True,
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
                            ),
                            sales_offer_packages=SalesOfferPackagesInFrameRelStructure(
                                sales_offer_package=[
                                    SalesOfferPackage(
                                        id='myfares:Single_trip-SOP@p-ticket',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Single, Paper Ticket '
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:Single_trip-SOP@p-ticket',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:paper_ticket'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=FareProductRef(
                                                        version='1.0',
                                                        ref='myfares:Single_trip'
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
                            id='myfares:DTA@Line_1@prices',
                            version='1.0',
                            name=MultilingualString(
                                value='Prices for Line 1 '
                            ),
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_currency='EUR'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='myfares:DTA@Line_1@products'
                                    ),
                                ]
                            ),
                            price_groups=FarePricesInFrameRelStructure(
                                price_group=[
                                    PriceGroup(
                                        id='myfares:Line_1',
                                        version='1.0',
                                        members=FarePricesRelStructure(
                                            fare_price_ref_or_cell_ref_or_fare_price=[
                                                DistanceMatrixElementPrice(
                                                    id='myfares:SSP_001+SSP_002',
                                                    version='1.0',
                                                    amount=Decimal('1.00'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='1.0',
                                                        ref='myfares:SSP_001+SSP_002'
                                                    )
                                                ),
                                                DistanceMatrixElementPrice(
                                                    id='myfares:SSP_001+SSP_077',
                                                    version='1.0',
                                                    amount=Decimal('3.00'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='1.0',
                                                        ref='myfares:SSP_001+SSP_077'
                                                    )
                                                ),
                                                DistanceMatrixElementPrice(
                                                    id='myfares:SSP_002+SSP_077',
                                                    version='1.0',
                                                    amount=Decimal('2.00'),
                                                    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                        version='1.0',
                                                        ref='myfares:SSP_002+SSP_077'
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
                                        id='myfares:Types_of_TravelDocument',
                                        version='any',
                                        name=MultilingualString(
                                            value='Types of concession'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfTravelDocument(
                                                    id='myfares:paper_ticket',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Paper ticket'
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
