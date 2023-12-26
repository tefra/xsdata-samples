from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import ValidBetween
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.boolean_operator_enumeration import BooleanOperatorEnumeration
from netex.models.cell_versioned_child_structure import FarePricesRelStructure
from netex.models.cell_versioned_child_structure import PriceGroup
from netex.models.cell_versioned_child_structure import PriceGroupsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.discounting_rule import DiscountingRule
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
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
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignment
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignmentsRelStructure
from netex.models.group_ticket import GroupTicket
from netex.models.group_ticket_ref import GroupTicketRef
from netex.models.interchanging import Interchanging
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.preassigned_fare_product import PreassignedFareProduct
from netex.models.price_group_ref import PriceGroupRef
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.pricing_rules_rel_structure import PricingRulesRelStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.round_trip import RoundTrip
from netex.models.round_trip_type_enumeration import RoundTripTypeEnumeration
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_price import SalesOfferPackagePrice
from netex.models.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.tariff import Tariff
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
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
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
        participant_ref='SYS002',
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        choice=[
                            AvailabilityCondition(
                                id='mybus:range',
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
                id='myfares:DTA@Flat',
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
                    choice=[
                        FareFrame(
                            id='myfares:DTA@Flat@products',
                            version='1.0',
                            prerequisites=VersionFrameRefsRelStructure(
                                choice=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='mybus:DTA@Common_Resources'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='myfares:Flat',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Flat  tariff'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        type_of_tariff_ref=TypeOfTariffRef(
                                            version='ntx:v1.0',
                                            ref='ntx:flat'
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='myfares:Flat@access',
                                                    version='1.0',
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Flat@access',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:can_access'
                                                        ),
                                                        validity_parameter_grouping_type=BooleanOperatorEnumeration.XOR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            vehicle_modes=[
                                                                [
                                                                    VehicleModeEnumeration.METRO,
                                                                ],
                                                            ],
                                                            all_operators_ref_or_operator_ref=[
                                                                OperatorRef(
                                                                    version='any',
                                                                    ref='mybus:DTA'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Flat@eligibility',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Eligible user types'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Flat@eligibility',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:eligible'
                                                        ),
                                                        limitation_grouping_type=BooleanOperatorEnumeration.XOR,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UserProfile(
                                                                    id='myfares:adult',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Child Fare'
                                                                    ),
                                                                    minimum_age=17
                                                                ),
                                                                UserProfile(
                                                                    id='myfares:child',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Child Fare'
                                                                    ),
                                                                    maximum_age=16
                                                                ),
                                                                GroupTicket(
                                                                    id='myfares:group',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Group Fare - 10 or more people'
                                                                    ),
                                                                    minimum_number_of_persons=10
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Flat@conditions_of_travel@single',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Conditions of travel'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Flat@conditions_of_travel@single',
                                                        version='1.0',
                                                        name=MultilingualString(
                                                            value='Conditions of travel'
                                                        ),
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:condition_of_use'
                                                        ),
                                                        limitation_grouping_type=BooleanOperatorEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                RoundTrip(
                                                                    id='myfares:Flat@conditions_of_travel@single@trip',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Single'
                                                                    ),
                                                                    trip_type=RoundTripTypeEnumeration.SINGLE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='myfares:Flat@conditions_of_travel@single@frequency',
                                                                    version='1.0',
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    maximal_frequency=1
                                                                ),
                                                                Interchanging(
                                                                    id='myfares:Flat@conditions_of_travel@single@interchanging',
                                                                    version='1.0',
                                                                    can_interchange=True,
                                                                    from_mode=VehicleModeEnumeration.METRO,
                                                                    to_mode=VehicleModeEnumeration.METRO,
                                                                    can_break_journey=False
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Flat@conditions_of_travel@outbound',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Conditions of travel'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Flat@conditions_of_travel@outbound',
                                                        version='1.0',
                                                        name=MultilingualString(
                                                            value='Conditions of travel'
                                                        ),
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:condition_of_use'
                                                        ),
                                                        limitation_grouping_type=BooleanOperatorEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                RoundTrip(
                                                                    id='myfares:Flat@conditions_of_travel@outbound@trip',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Outbound'
                                                                    ),
                                                                    trip_type=RoundTripTypeEnumeration.SINGLE
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='myfares:Flat@conditions_of_travel@outbound@frequency',
                                                                    version='1.0',
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    maximal_frequency=1
                                                                ),
                                                                Interchanging(
                                                                    id='myfares:Flat@conditions_of_travel@outbound@interchanging',
                                                                    version='1.0',
                                                                    can_interchange=True,
                                                                    can_break_journey=False
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Flat@conditions_of_travel@inbound',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Conditions of travel'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Flat@conditions_of_travel@inbound',
                                                        version='1.0',
                                                        name=MultilingualString(
                                                            value='Conditions of travel'
                                                        ),
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:condition_of_use'
                                                        ),
                                                        limitation_grouping_type=BooleanOperatorEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                RoundTrip(
                                                                    id='myfares:Flat@conditions_of_travel@inbound@trip',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Return'
                                                                    ),
                                                                    trip_type=RoundTripTypeEnumeration.RETURN_ONLY
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='myfares:Flat@conditions_of_travel@inbound@frequency',
                                                                    version='1.0',
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE,
                                                                    maximal_frequency=1
                                                                ),
                                                                Interchanging(
                                                                    id='myfares:Flat@conditions_of_travel@inbound@interchanging',
                                                                    version='1.0',
                                                                    can_interchange=True,
                                                                    can_break_journey=False
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        ),
                                        price_groups=PriceGroupsRelStructure(
                                            price_group_ref_or_price_group=[
                                                PriceGroupRef(
                                                    version='1.0',
                                                    ref='myfares:Flat'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_products=FareProductsInFrameRelStructure(
                                choice=[
                                    PreassignedFareProduct(
                                        id='myfares:Single_trip',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Adult  Standard Flat  fare  - One way '
                                        ),
                                        type_of_fare_product_ref_or_types_of_fare_product=TypeOfFareProductRef(
                                            version='ntx:v1.0',
                                            ref='ntx:trip'
                                        ),
                                        authority_ref_or_operator_ref=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        validable_elements=ValidableElementsRelStructure(
                                            validable_element_ref_or_validable_element=[
                                                ValidableElement(
                                                    id='myfares:Single_trip@travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='A metro Trip'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Flat@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Flat@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Flat@conditions_of_travel@single'
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
                                    PreassignedFareProduct(
                                        id='myfares:Return_trip',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Adult  Standard Flat  fare  - One way '
                                        ),
                                        type_of_fare_product_ref_or_types_of_fare_product=TypeOfFareProductRef(
                                            version='ntx:v1.0',
                                            ref='ntx:trip'
                                        ),
                                        authority_ref_or_operator_ref=OperatorRef(
                                            version='any',
                                            ref='mybus:DTA'
                                        ),
                                        validable_elements=ValidableElementsRelStructure(
                                            validable_element_ref_or_validable_element=[
                                                ValidableElement(
                                                    id='myfares:Return_trip@travel@outbound',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Outbound  metro Trip'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Flat@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Flat@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Flat@conditions_of_travel@outbound'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                ValidableElement(
                                                    id='myfares:Return_trip@travel@inbound',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Return metro Trip'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Flat@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Flat@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Flat@conditions_of_travel@inbound'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='myfares:Return_trip@travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Outbound  trip'
                                                    ),
                                                    is_first_in_sequence=False,
                                                    is_last_in_sequence=True,
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='1.0',
                                                        ref='myfares:Return_trip@travel@outbound'
                                                    )
                                                ),
                                                AccessRightInProduct(
                                                    id='myfares:Return_trip@travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Return tripe'
                                                    ),
                                                    is_first_in_sequence=False,
                                                    is_last_in_sequence=True,
                                                    order=2,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='1.0',
                                                        ref='myfares:Return_trip@travel@inbound'
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
                                        id='myfares:Single_trip-SOP@p-ticket@individual',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Individual Single, Paper Ticket '
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='myfares:Single_trip-SOP@p-ticket@individual',
                                                    version='1.0',
                                                    order=1,
                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                        version='ntx:v1.0',
                                                        ref='ntx:eligible'
                                                    ),
                                                    limitation_grouping_type=BooleanOperatorEnumeration.XOR,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            UserProfileRef(
                                                                version='any',
                                                                ref='myfares:adult'
                                                            ),
                                                            UserProfileRef(
                                                                version='any',
                                                                ref='myfares:child'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:Single_trip-SOP@p-ticket@individual',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:paper_ticket'
                                                    ),
                                                    choice=FareProductRef(
                                                        version='1.0',
                                                        ref='myfares:Single_trip'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='myfares:Return_trip-SOP@p-ticket@individual',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Individual Return, Paper Ticket '
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='myfares:Return_trip-SOP@p-ticket@individual',
                                                    version='1.0',
                                                    order=1,
                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                        version='ntx:v1.0',
                                                        ref='ntx:eligible'
                                                    ),
                                                    limitation_grouping_type=BooleanOperatorEnumeration.XOR,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            UserProfileRef(
                                                                version='any',
                                                                ref='myfares:adult'
                                                            ),
                                                            UserProfileRef(
                                                                version='any',
                                                                ref='myfares:child'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:Return_trip-SOP@p-ticket@individual',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:paper_ticket'
                                                    ),
                                                    choice=FareProductRef(
                                                        version='1.0',
                                                        ref='myfares:Return_trip'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='myfares:Single_trip-SOP@p-ticket@group',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Group Single, Paper Ticket '
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='myfares:Single_trip-SOP@p-ticket@group',
                                                    version='1.0',
                                                    order=1,
                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                        version='ntx:v1.0',
                                                        ref='ntx:eligible'
                                                    ),
                                                    limitation_grouping_type=BooleanOperatorEnumeration.XOR,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            GroupTicketRef(
                                                                version='any',
                                                                ref='myfares:group'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:Single_trip-SOP@p-tickett@group',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:paper_ticket'
                                                    ),
                                                    choice=FareProductRef(
                                                        version='1.0',
                                                        ref='myfares:Single_trip'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='myfares:Return_trip-SOP@p-ticket@group',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Group Return , Paper Ticket '
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='myfares:Return_trip-SOP@p-ticket@group',
                                                    version='1.0',
                                                    order=1,
                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                        version='ntx:v1.0',
                                                        ref='ntx:eligible'
                                                    ),
                                                    limitation_grouping_type=BooleanOperatorEnumeration.XOR,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            GroupTicketRef(
                                                                version='any',
                                                                ref='myfares:group'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:Return_trip-SOP@p-ticket@group',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:paper_ticket'
                                                    ),
                                                    choice=FareProductRef(
                                                        version='1.0',
                                                        ref='myfares:Return_trip'
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
                            id='myfares:DTA@Flat@prices',
                            version='1.0',
                            prerequisites=VersionFrameRefsRelStructure(
                                choice=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='myfares:DTA@Flat@products'
                                    ),
                                ]
                            ),
                            pricing_parameter_set=PricingParameterSet(
                                id='myfares:Flat@prices',
                                version='1.0',
                                pricing_rules=PricingRulesRelStructure(
                                    choice=[
                                        DiscountingRule(
                                            id='myfares:group_discount',
                                            version='any',
                                            discount_as_percentage=Decimal('75')
                                        ),
                                    ]
                                )
                            ),
                            price_groups=FarePricesInFrameRelStructure(
                                price_group=[
                                    PriceGroup(
                                        id='myfares:Flat',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Prices for Flat  Fare Products'
                                        ),
                                        members=FarePricesRelStructure(
                                            choice=[
                                                SalesOfferPackagePrice(
                                                    id='myfares:Single_trip-SOP@p-ticket@individual',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Return fare'
                                                    ),
                                                    amount=Decimal('1.00'),
                                                    currency='EUR',
                                                    sales_offer_package_ref_or_sales_offer_package_element_ref=SalesOfferPackageRef(
                                                        version='1.0',
                                                        ref='myfares:Single_trip-SOP@p-ticket@individual'
                                                    )
                                                ),
                                                SalesOfferPackagePrice(
                                                    id='myfares:Return_trip-SOP@p-ticket@individual',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Single fare'
                                                    ),
                                                    amount=Decimal('1.75'),
                                                    currency='EUR',
                                                    sales_offer_package_ref_or_sales_offer_package_element_ref=SalesOfferPackageRef(
                                                        version='1.0',
                                                        ref='myfares:Return_trip-SOP@p-ticket@individual'
                                                    )
                                                ),
                                                SalesOfferPackagePrice(
                                                    id='Single_trip-SOP@p-ticket@group',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Group discount - all fares'
                                                    ),
                                                    choice=SalesOfferPackagePriceRef(
                                                        version='1.0',
                                                        ref='myfares:Single_trip-SOP@p-ticket@individual'
                                                    ),
                                                    choice_1=DiscountingRuleRef(
                                                        version='any',
                                                        ref='myfares:group_discount'
                                                    ),
                                                    sales_offer_package_ref_or_sales_offer_package_element_ref=SalesOfferPackageRef(
                                                        version='1.0',
                                                        ref='myfares:Single_trip-SOP@p-ticket@group'
                                                    )
                                                ),
                                                SalesOfferPackagePrice(
                                                    id='Return_trip-SOP@p-ticket@group',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Group discount - all fares'
                                                    ),
                                                    choice=SalesOfferPackagePriceRef(
                                                        version='1.0',
                                                        ref='myfares:Return_trip-SOP@p-ticket@individual'
                                                    ),
                                                    choice_1=DiscountingRuleRef(
                                                        version='any',
                                                        ref='myfares:group_discount'
                                                    ),
                                                    sales_offer_package_ref_or_sales_offer_package_element_ref=SalesOfferPackageRef(
                                                        version='1.0',
                                                        ref='myfares:Return_trip-SOP@p-ticket@group'
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
                                value='Common Resources'
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
                                            choice=[
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
                                            choice=[
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
                                            value='Types of Travel document'
                                        ),
                                        values=TypesOfValueStructure(
                                            choice=[
                                                TypeOfTravelDocument(
                                                    id='myfares:mobile_app',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Mobile Electronic'
                                                    )
                                                ),
                                                TypeOfTravelDocument(
                                                    id='myfares:paper_ticket',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Printed ticket'
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
                                            choice=[
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
                                                        value='Grants access rights to use or travel on a network'
                                                    )
                                                ),
                                                TypeOfAccessRightAssignment(
                                                    id='ntx:can_access_when',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Grants access rights to use or travel within a given period'
                                                    )
                                                ),
                                                TypeOfAccessRightAssignment(
                                                    id='ntx:can_purchase_when',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Specified conditiosn on when a product can eb purchased'
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
                                choice=[
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
