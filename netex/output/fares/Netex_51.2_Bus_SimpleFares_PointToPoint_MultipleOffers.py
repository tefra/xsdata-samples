from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import ValidBetween
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.cell_versioned_child_structure import CellsRelStructure
from netex.models.cell_versioned_child_structure import FarePricesRelStructure
from netex.models.cell_versioned_child_structure import FareTable1
from netex.models.cell_versioned_child_structure import FareTablesRelStructure
from netex.models.cell_versioned_child_structure import PriceGroup1
from netex.models.cell_versioned_child_structure import PriceGroupsRelStructure
from netex.models.class_of_use import ClassOfUse
from netex.models.class_of_use_ref import ClassOfUseRef
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
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
from netex.models.fare_table_specifics_structure import FareTableSpecificsStructure
from netex.models.fare_tables_in_frame_rel_structure import FareTablesInFrameRelStructure
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.models.fulfilment_method_ref import FulfilmentMethodRef
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignment
from netex.models.group_of_lines import GroupOfLines
from netex.models.group_of_lines_ref import GroupOfLinesRef
from netex.models.groups_of_lines_in_frame_rel_structure import GroupsOfLinesInFrameRelStructure
from netex.models.interchanging import Interchanging
from netex.models.line_1 import Line1
from netex.models.line_ref import LineRef
from netex.models.line_refs_rel_structure import LineRefsRelStructure
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.logical_operation_enumeration import LogicalOperationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
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
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.round_trip import RoundTrip
from netex.models.round_trip_type_enumeration import RoundTripTypeEnumeration
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.tariff import Tariff
from netex.models.tariff_ref import TariffRef
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.ticketing_service_facility_list import TicketingServiceFacilityList
from netex.models.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_concession import TypeOfConcession
from netex.models.type_of_concession_ref import TypeOfConcessionRef
from netex.models.type_of_fare_product import TypeOfFareProduct
from netex.models.type_of_fare_product_ref import TypeOfFareProductRef
from netex.models.type_of_tariff import TypeOfTariff
from netex.models.type_of_tariff_ref import TypeOfTariffRef
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.usage_parameter_price import UsageParameterPrice
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
                id='myfares:DTA@Line24',
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
                    ),
                    default_currency='EUR'
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='mybus:DTA@Line24@network',
                            version='1.0',
                            name=MultilingualString(
                                value='Stops for Winter timetable for route 24 '
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@Common_resources'
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line1(
                                        id='mybus:LN_24',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 24 Alpha to Charley'
                                        ),
                                        public_code='24',
                                        authority_ref_or_operator_ref=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        )
                                    ),
                                ]
                            ),
                            groups_of_lines=GroupsOfLinesInFrameRelStructure(
                                group_of_lines=[
                                    GroupOfLines(
                                        id='mybus:my_lines',
                                        version='any',
                                        name=MultilingualString(
                                            value='Express routes'
                                        ),
                                        members=LineRefsRelStructure(
                                            line_ref=[
                                                LineRef(
                                                    version='any',
                                                    ref='mybus:LN_24'
                                                ),
                                            ]
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
                                        short_name=MultilingualString(
                                            value='Alpha'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='ALPH'
                                        )
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
                                        short_name=MultilingualString(
                                            value='Bravo'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='BRAV'
                                        )
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
                                        short_name=MultilingualString(
                                            value='Charley'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='CHAS'
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='myfares:DTA@Line24@products',
                            version='1.0',
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ServiceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@Line24@network'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='myfares:PointToPoint_01',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Point to Point   Tariff'
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
                                                    id='myfares:PointToPoint_01@access',
                                                    version='1.0',
                                                    choice_1=DistanceMatrixElementsRelStructure(
                                                        distance_matrix_element_ref_or_distance_matrix_element=[
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:SSP_001+SSP_002'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:SSP_001+SSP_077'
                                                            ),
                                                            DistanceMatrixElementRef(
                                                                version='any',
                                                                ref='myfares:SSP_002+SSP_077'
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:PointToPoint_01@access',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:can_access'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.XOR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            group_of_lines_ref=[
                                                                GroupOfLinesRef(
                                                                    version='any',
                                                                    ref='mybus:my_lines'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:PointToPoint_01@eligibility',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Eligible user types'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:PointToPoint_01@eligibility',
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
                                                    id='myfares:PointToPoint_01@classes_of_use',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Available classes of use'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:PointToPoint_01@classes_of_use',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:can_access'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.XOR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            class_of_use_ref=[
                                                                ClassOfUseRef(
                                                                    version='any',
                                                                    ref='myfares:standard'
                                                                ),
                                                                ClassOfUseRef(
                                                                    version='any',
                                                                    ref='myfares:first'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:PointToPoint_01@conditions_of_travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Conditions of travel'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:PointToPoint_01@conditions_of_travel',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:condition_of_use'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                RoundTrip(
                                                                    id='myfares:PointToPoint_01@conditions_of_travel@trip',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='Single Trip'
                                                                    ),
                                                                    trip_type=RoundTripTypeEnumeration.SINGLE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='myfares:PointToPoint_01@conditions_of_travel@frequency',
                                                                    version='1.0',
                                                                    name=MultilingualString(
                                                                        value='One trip no transfers'
                                                                    ),
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    maximal_frequency=1
                                                                ),
                                                                Interchanging(
                                                                    id='myfares:PointToPoint_01@conditions_of_travel@interchanging',
                                                                    version='1.0',
                                                                    from_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                                                    to_mode=AllVehicleModesOfTransportEnumeration.BUS,
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
                                                    id='myfares:SSP_001+SSP_002',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='A to B'
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
                                                                ref='myfares:PointToPoint_01@p-ticket@SSP_001+SSP_002@standard'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@p-ticket@SSP_001+SSP_002@first'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@m-ticket@SSP_001+SSP_002@standard'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@m-ticket@SSP_001+SSP_002@first'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:SSP_001+SSP_077',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='A to C'
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
                                                                ref='myfares:PointToPoint_01@p-ticket@SSP_001+SSP_077@standard'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@p-ticket@SSP_001+SSP_077@first'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@m-ticket@SSP_001+SSP_077@standard'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@m-ticket@SSP_001+SSP_077@first'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                DistanceMatrixElement(
                                                    id='myfares:SSP_002+SSP_077',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='B to C'
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
                                                                ref='myfares:PointToPoint_01@p-ticket@SSP_002+SSP_077@standard'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@p-ticket@SSP_002+SSP_077@first'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@m-ticket@SSP_002+SSP_077@standard'
                                                            ),
                                                            DistanceMatrixElementPriceRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@m-ticket@SSP_002+SSP_077@first'
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
                                                    ref='myfares:Line24@discounts'
                                                ),
                                            ]
                                        ),
                                        fare_tables=FareTablesRelStructure(
                                            fare_table_ref_or_fare_table=[
                                                FareTableRef(
                                                    version='1.0',
                                                    ref='myfares:Line24'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_products=FareProductsInFrameRelStructure(
                                fare_product=[
                                    PreassignedFareProduct(
                                        id='myfares:Trip',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Standard Point To Point Trip  fare   '
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
                                                    id='myfares:Trip@travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Single  ride'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@classes_of_use'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:PointToPoint_01@conditions_of_travel'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='myfares:Trip',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='First ride'
                                                    ),
                                                    is_first_in_sequence=True,
                                                    is_last_in_sequence=True,
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='1.0',
                                                        ref='myfares:Trip@travel'
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
                                        id='myfares:Trip-SOP@p-ticket',
                                        version='1.0',
                                        name=MultilingualString(

                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='myfares:Trip-SOP@p-ticket@atStop',
                                                    version='10',
                                                    name=MultilingualString(
                                                        value='Onboard'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Pay for ticket onboard'
                                                    ),
                                                    order=1,
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
                                                    id='myfares:Trip-SOP@p-ticket@onBoard',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Onboard'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Pay for ticket onboard'
                                                    ),
                                                    order=2,
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
                                                    id='myfares:Trip-SOP@p-ticket',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:printed_ticket'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='1.0',
                                                        ref='myfares:Trip'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='myfares:Trip-SOP@m-ticket',
                                        version='1.0',
                                        name=MultilingualString(

                                        ),
                                        distribution_assignments=DistributionAssignmentsRelStructure(
                                            distribution_assignment_ref_or_distribution_assignment=[
                                                DistributionAssignment(
                                                    id='myfares:Trip-SOP@m-ticket@online',
                                                    version='10',
                                                    name=MultilingualString(
                                                        value='Online'
                                                    ),
                                                    order=1,
                                                    distribution_channel_type=DistributionChannelTypeEnumeration.MOBILE_DEVICE,
                                                    payment_methods=[
                                                        PaymentMethodEnumeration.CARDS_ONLY,
                                                    ],
                                                    fulfilment_method_ref=FulfilmentMethodRef(
                                                        ref='ntx:mobile_app',
                                                        version_ref='ntx:v1.0'
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:Trip-SOP@m-ticket',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:mobile_app'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=PreassignedFareProductRef(
                                                        version='1.0',
                                                        ref='myfares:Trip'
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
                            id='myfares:DTA@Line24@prices',
                            version='1.0',
                            name=MultilingualString(
                                value='Prices for Line 24'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='myfares:DTA@Line24@products'
                                    ),
                                ]
                            ),
                            pricing_parameter_set=PricingParameterSet(
                                id='myfares:Line24',
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
                                        id='myfares:Line24@discounts',
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
                                        id='myfares:Line24',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Prices for Point to Point  Trip Product'
                                        ),
                                        prices_for=PriceableObjectRefsRelStructure(
                                            choice=[
                                                PreassignedFareProductRef(
                                                    version='1.0',
                                                    ref='myfares:Trip'
                                                ),
                                            ]
                                        ),
                                        used_in=UsedInRefsRelStructure(
                                            choice=[
                                                TariffRef(
                                                    version='1.0',
                                                    ref='myfares:PointToPoint_01'
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
                                                FareTable1(
                                                    id='myfares:Line24@p-ticket',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Prices for Point to Point  Trip Product - paper ticket'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            SalesOfferPackageRef(
                                                                version='1.0',
                                                                ref='myfares:Trip-SOP@p-ticket'
                                                            ),
                                                        ]
                                                    ),
                                                    includes=FareTablesRelStructure(
                                                        fare_table_ref_or_fare_table=[
                                                            FareTable1(
                                                                id='myfares:PointToPoint_01@p-ticket@standard',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Prices for Point to Point Trip Product  - Standard'
                                                                ),
                                                                specifics=FareTableSpecificsStructure(
                                                                    class_of_use_ref=ClassOfUseRef(
                                                                        version='any',
                                                                        ref='myfares:standard'
                                                                    )
                                                                ),
                                                                cells=CellsRelStructure(
                                                                    choice=[
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@p-ticket@SSP_001+SSP_002@standard',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Alpha to Beta - Price'
                                                                            ),
                                                                            amount=Decimal('1.00'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_001+SSP_002'
                                                                            )
                                                                        ),
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@p-ticket@SSP_001+SSP_077@standard',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Alpha  to Charley - Price'
                                                                            ),
                                                                            amount=Decimal('3.00'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_001+SSP_077'
                                                                            )
                                                                        ),
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@p-ticket@SSP_002+SSP_077@standard',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Beta  to Charley - Price'
                                                                            ),
                                                                            amount=Decimal('2.00'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_002+SSP_077'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            FareTable1(
                                                                id='myfares:PointToPoint_01@p-ticket@first',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Prices for  Point to Point Fare Product  - First Class'
                                                                ),
                                                                specifics=FareTableSpecificsStructure(
                                                                    class_of_use_ref=ClassOfUseRef(
                                                                        version='any',
                                                                        ref='myfares:first'
                                                                    )
                                                                ),
                                                                cells=CellsRelStructure(
                                                                    choice=[
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@p-ticket@SSP_001+SSP_002@first',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Alpha to Beta - Price'
                                                                            ),
                                                                            amount=Decimal('1.50'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_001+SSP_002'
                                                                            )
                                                                        ),
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@p-ticket@SSP_001+SSP_077@first',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Alpha  to Charley - Price'
                                                                            ),
                                                                            amount=Decimal('5.00'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_001+SSP_077'
                                                                            )
                                                                        ),
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@p-ticket@SSP_002+SSP_077@first',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Beta  to Charley - Price'
                                                                            ),
                                                                            amount=Decimal('3.00'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_002+SSP_077'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareTable1(
                                                    id='myfares:Line24@m-ticket',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Prices for Point to Point  Trip Product - Mobile app'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            SalesOfferPackageRef(
                                                                version='1.0',
                                                                ref='myfares:Trip-SOP@m-ticket'
                                                            ),
                                                        ]
                                                    ),
                                                    includes=FareTablesRelStructure(
                                                        fare_table_ref_or_fare_table=[
                                                            FareTable1(
                                                                id='myfares:PointToPoint_01@m-ticket@standard',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Prices for Point to Point Trip Product  - Mobile app - Standard'
                                                                ),
                                                                specifics=FareTableSpecificsStructure(
                                                                    class_of_use_ref=ClassOfUseRef(
                                                                        version='any',
                                                                        ref='myfares:standard'
                                                                    )
                                                                ),
                                                                cells=CellsRelStructure(
                                                                    choice=[
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@m-ticket@SSP_001+SSP_002@standard',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Alpha to Beta - Price'
                                                                            ),
                                                                            amount=Decimal('0.90'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_001+SSP_002'
                                                                            )
                                                                        ),
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@m-ticket@SSP_001+SSP_077@standard',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Alpha  to Charley - Price'
                                                                            ),
                                                                            amount=Decimal('2.70'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_001+SSP_077'
                                                                            )
                                                                        ),
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@m-ticket@SSP_002+SSP_077@standard',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Beta  to Charley - Price'
                                                                            ),
                                                                            amount=Decimal('1.90'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_002+SSP_077'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            FareTable1(
                                                                id='myfares:PointToPoint_01@m-ticket@first',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Prices for  Point to Point Fare Product  - Mobile app - First Class'
                                                                ),
                                                                specifics=FareTableSpecificsStructure(
                                                                    class_of_use_ref=ClassOfUseRef(
                                                                        version='any',
                                                                        ref='myfares:first'
                                                                    )
                                                                ),
                                                                cells=CellsRelStructure(
                                                                    choice=[
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@m-ticket@SSP_001+SSP_002@first',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Alpha to Beta - Price'
                                                                            ),
                                                                            amount=Decimal('1.40'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_001+SSP_002'
                                                                            )
                                                                        ),
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@m-ticket@SSP_001+SSP_077@first',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Alpha  to Charley - Price'
                                                                            ),
                                                                            amount=Decimal('4.80'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_001+SSP_077'
                                                                            )
                                                                        ),
                                                                        DistanceMatrixElementPrice(
                                                                            id='myfares:PointToPoint_01@m-ticket@SSP_002+SSP_077@first',
                                                                            version='1.0',
                                                                            name=MultilingualString(
                                                                                value='Beta  to Charley - Price'
                                                                            ),
                                                                            amount=Decimal('2.80'),
                                                                            distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref=DistanceMatrixElementRef(
                                                                                version='any',
                                                                                ref='myfares:SSP_002+SSP_077'
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
                        ResourceFrame(
                            id='mybus:DTA@Common_resources',
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
                                        id='myfares:Classes_of_Use',
                                        version='any',
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                ClassOfUse(
                                                    id='myfares:first',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='First'
                                                    )
                                                ),
                                                ClassOfUse(
                                                    id='myfares:standard',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Standard'
                                                    )
                                                ),
                                            ]
                                        ),
                                        class_of_values='ClassOfUse'
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
