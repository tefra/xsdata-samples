from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import ValidBetween
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.boolean_operator_enumeration import BooleanOperatorEnumeration
from netex.models.cell_versioned_child_structure import CellsRelStructure
from netex.models.cell_versioned_child_structure import FarePricesRelStructure
from netex.models.cell_versioned_child_structure import FareTable
from netex.models.cell_versioned_child_structure import FareTablesRelStructure
from netex.models.cell_versioned_child_structure import PriceGroup
from netex.models.codespace import Codespace
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.discounting_rule import DiscountingRule
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.effective_from_enumeration import EffectiveFromEnumeration
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
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignment
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignmentsRelStructure
from netex.models.group_of_sales_offer_packages import GroupOfSalesOfferPackages
from netex.models.group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from netex.models.groups_of_sales_offer_packages_in_frame_rel_structure import GroupsOfSalesOfferPackagesInFrameRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.partial_refund_basis_enumeration import PartialRefundBasisEnumeration
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.per_basis_enumeration import PerBasisEnumeration
from netex.models.priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.pricing_rules_rel_structure import PricingRulesRelStructure
from netex.models.proof_of_identity_enumeration import ProofOfIdentityEnumeration
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.models.purchase_when_enumeration import PurchaseWhenEnumeration
from netex.models.purchase_window import PurchaseWindow
from netex.models.refund_policy_enumeration import RefundPolicyEnumeration
from netex.models.refund_type_enumeration import RefundTypeEnumeration
from netex.models.refunding import Refunding
from netex.models.resell_when_enumeration import ResellWhenEnumeration
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.sale_discount_right import SaleDiscountRight
from netex.models.sale_discount_right_ref import SaleDiscountRightRef
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_entitlement_given import SalesOfferPackageEntitlementGiven
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_package_refs_rel_structure import SalesOfferPackageRefsRelStructure
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.subscribing import Subscribing
from netex.models.subscription_term_type_enumeration import SubscriptionTermTypeEnumeration
from netex.models.suspending import Suspending
from netex.models.suspension_policy_enumeration import SuspensionPolicyEnumeration
from netex.models.tariff import Tariff
from netex.models.tariff_ref import TariffRef
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.time_interval import TimeInterval
from netex.models.time_interval_price import TimeIntervalPrice
from netex.models.time_interval_ref import TimeIntervalRef
from netex.models.time_interval_refs_rel_structure import TimeIntervalRefsRelStructure
from netex.models.time_intervals_rel_structure import TimeIntervalsRelStructure
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
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_ref import ValidableElementRef
from netex.models.validable_elements_rel_structure import ValidableElementsRelStructure
from netex.models.validity_parameters_rel_structure import ValidityParametersRelStructure
from netex.models.value_set import ValueSet
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod


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
                                id='mytoc:range',
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
                id='myfares:DTA@RailCards',
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
                            id='mytoc',
                            xmlns='mytoc',
                            xmlns_url='http://www.mytoc.eu/network',
                            description='My train operator'
                        ),
                        Codespace(
                            id='myfares',
                            xmlns='myfares',
                            xmlns_url='http://www.mytoc.eu/fares',
                            description='Fare  data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_currency='EUR'
                ),
                frames=FramesRelStructure(
                    choice=[
                        FareFrame(
                            id='myfares:DTA@RailCards@products',
                            version='1.0',
                            prerequisites=VersionFrameRefsRelStructure(
                                choice=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='myfares:DTA@Common_Resources'
                                    ),
                                ]
                            ),
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='myfares:Railcard_discount',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Railcard Discount  tariff'
                                        ),
                                        choice=OperatorRef(
                                            version='any',
                                            ref='mytoc:DTA'
                                        ),
                                        type_of_tariff_ref=TypeOfTariffRef(
                                            version='ntx:v1.0',
                                            ref='ntx:zonal'
                                        ),
                                        time_intervals=TimeIntervalsRelStructure(
                                            time_interval_ref_or_time_interval=[
                                                TimeInterval(
                                                    id='myfares:Railcard_discount@1year',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='One Year'
                                                    ),
                                                    duration=XmlDuration("P1Y")
                                                ),
                                                TimeInterval(
                                                    id='myfares:Railcard_discount@2year',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Two Years'
                                                    ),
                                                    duration=XmlDuration("P2Y")
                                                ),
                                                TimeInterval(
                                                    id='myfares:payment_installment@3month',
                                                    version='1.0',
                                                    duration=XmlDuration("P3M")
                                                ),
                                                TimeInterval(
                                                    id='myfares:payment_installment@6month',
                                                    version='1.0',
                                                    duration=XmlDuration("P6M")
                                                ),
                                                TimeInterval(
                                                    id='myfares:payment_installment@1year',
                                                    version='1.0',
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
                                                    id='myfares:Railcard_discount@access',
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
                                                                    VehicleModeEnumeration.RAIL,
                                                                ],
                                                            ],
                                                            all_operators_ref_or_operator_ref=[
                                                                OperatorRef(
                                                                    version='any',
                                                                    ref='mytoc:DTA'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Railcard_discount@access_when',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Allowed periods for  use of a  Railcard'
                                                    ),
                                                    time_interval_ref_or_time_intervals_or_time_structure_factors=TimeIntervalsRelStructure(
                                                        time_interval_ref_or_time_interval=[
                                                            TimeIntervalRef(
                                                                version='1.0',
                                                                ref='myfares:Railcard_discount@1year'
                                                            ),
                                                            TimeIntervalRef(
                                                                version='1.0',
                                                                ref='myfares:Railcard_discount@2year'
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Time_interval@access_when',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:can_access_when',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        limitation_grouping_type=BooleanOperatorEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UsageValidityPeriod(
                                                                    id='myfares:Time_interval@access_whes',
                                                                    version='1.0',
                                                                    validity_period_type=UsageValidityTypeEnumeration.SEASON_TICKET,
                                                                    usage_trigger=UsageTriggerEnumeration.SPECIFIED_START_DATE,
                                                                    usage_start_constraint_type=UsageStartConstraintTypeEnumeration.VARIABLE,
                                                                    start_only_on=DayTypesRelStructure(
                                                                        choice=[
                                                                            DayType(
                                                                                id='myfares:Time_interval@access_when',
                                                                                version='1.0',
                                                                                properties=PropertiesOfDayRelStructure(
                                                                                    property_of_day=[
                                                                                        PropertyOfDay(
                                                                                            month_of_year_or_day_of_month_or_day_of_year=DerivedElement(
                                                                                                qname='{http://www.netex.org.uk/netex}DayOfMonth',
                                                                                                value=XmlPeriod("---01")
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
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Railcard_discount@can_purchase',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Allowed periods for payment installationsd'
                                                    ),
                                                    time_interval_ref_or_time_intervals_or_time_structure_factors=TimeIntervalsRelStructure(
                                                        time_interval_ref_or_time_interval=[
                                                            TimeIntervalRef(
                                                                version='1.0',
                                                                ref='myfares:payment_installment@3month'
                                                            ),
                                                            TimeIntervalRef(
                                                                version='1.0',
                                                                ref='myfares:payment_installment@6month'
                                                            ),
                                                            TimeIntervalRef(
                                                                version='1.0',
                                                                ref='myfares:payment_installment@1year'
                                                            ),
                                                        ]
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Time_interval@can_purchase',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:can_purchase',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        validity_parameter_grouping_type=BooleanOperatorEnumeration.XOR
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Railcard_discount@eligibility',
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
                                                                        value='Normal'
                                                                    ),
                                                                    type_of_concession_ref=TypeOfConcessionRef(
                                                                        version='any',
                                                                        ref='myfares:standard'
                                                                    )
                                                                ),
                                                                UserProfile(
                                                                    id='myfares:child',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Child'
                                                                    ),
                                                                    type_of_concession_ref=TypeOfConcessionRef(
                                                                        version='any',
                                                                        ref='myfares:concession'
                                                                    ),
                                                                    maximum_age=16
                                                                ),
                                                                UserProfile(
                                                                    id='myfares:student',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Student'
                                                                    ),
                                                                    type_of_concession_ref=TypeOfConcessionRef(
                                                                        version='any',
                                                                        ref='myfares:concession'
                                                                    ),
                                                                    proof_required=[
                                                                        ProofOfIdentityEnumeration.MEMBERSHIP_CARD,
                                                                    ]
                                                                ),
                                                                UserProfile(
                                                                    id='myfares:senior',
                                                                    version='any',
                                                                    name=MultilingualString(
                                                                        value='Senior'
                                                                    ),
                                                                    type_of_concession_ref=TypeOfConcessionRef(
                                                                        version='any',
                                                                        ref='myfares:concession'
                                                                    ),
                                                                    minimum_age=60,
                                                                    proof_required=[
                                                                        ProofOfIdentityEnumeration.DRIVING_LICENCE,
                                                                        ProofOfIdentityEnumeration.PASSPORT,
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='myfares:Railcard_discount@conditions_of_sale',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Conditions of use'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='myfares:Railcard_discount@conditions_of_sale',
                                                        version='1.0',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            version='ntx:v1.0',
                                                            ref='ntx:condition_of_sale'
                                                        ),
                                                        limitation_grouping_type=BooleanOperatorEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UsageValidityPeriod(
                                                                    id='myfares:duration',
                                                                    version='any',
                                                                    validity_period_type=UsageValidityTypeEnumeration.PROFILE_MEMBERSHIP,
                                                                    usage_trigger=UsageTriggerEnumeration.SPECIFIED_START_DATE,
                                                                    usage_end=UsageEndEnumeration.PRODUCT_EXPIRY
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        ),
                                        fare_tables=FareTablesRelStructure(
                                            choice=[
                                                FareTableRef(
                                                    version='1.0',
                                                    ref='myfares:Railcard@prices'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_products=FareProductsInFrameRelStructure(
                                choice=[
                                    SaleDiscountRight(
                                        id='myfares:Railcard',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Adult  Standard Flat  fare'
                                        ),
                                        type_of_fare_product_ref_or_types_of_fare_product=TypeOfFareProductRef(
                                            version='ntx:v1.0',
                                            ref='ntx:discount_card'
                                        ),
                                        authority_ref_or_operator_ref=OperatorRef(
                                            version='any',
                                            ref='mytoc:DTA'
                                        ),
                                        validable_elements=ValidableElementsRelStructure(
                                            validable_element_ref_or_validable_element=[
                                                ValidableElement(
                                                    id='myfares:Railcard@travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='A metro Trip'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Railcard_discount@access'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Railcard_discount@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1.0',
                                                                ref='myfares:Railcard_discount@conditions_of_sale'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='myfares:Railcard@travel',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='First ride'
                                                    ),
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='1.0',
                                                        ref='myfares:Railcard@travel'
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
                                        id='myfares:Railcard-SOP@standard',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Railcard - standard'
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='myfares:Railcard-SOP@standard@eligible',
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
                                        group_of_sales_offer_packages_ref_or_groups_of_sale_offer_packages=GroupOfSalesOfferPackagesRef(
                                            version='1.0',
                                            ref='myfares:Railcard-GSOP'
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='myfares:Railcard-SOP@student',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Ralcard - student'
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='myfares:Railcard-SOP@student@eligible',
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
                                                                ref='myfares:student'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                GenericParameterAssignment(
                                                    id='myfares:Railcard-SOP@student@access_when',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Student pass only one year'
                                                    ),
                                                    order=1,
                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                        version='ntx:v1.0',
                                                        ref='ntx:can_access_when'
                                                    ),
                                                    time_interval_ref_or_parking_charge_band_ref_or_time_structure_factor_ref=TimeIntervalRef(
                                                        version='1.0',
                                                        ref='myfares:Railcard_discount@1year'
                                                    )
                                                ),
                                            ]
                                        ),
                                        group_of_sales_offer_packages_ref_or_groups_of_sale_offer_packages=GroupOfSalesOfferPackagesRef(
                                            version='1.0',
                                            ref='myfares:Railcard-GSOP'
                                        )
                                    ),
                                    SalesOfferPackage(
                                        id='myfares:Railcard-SOP@senior',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Ralcard - senior'
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='myfares:Railcard-SOP@senior@eligible',
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
                                                                ref='myfares:senior'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                GenericParameterAssignment(
                                                    id='myfares:Railcard-SOP@senior@subscribing',
                                                    version='1.0',
                                                    order=1,
                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                        version='ntx:v1.0',
                                                        ref='ntx:can_purchase'
                                                    ),
                                                    limitation_grouping_type=BooleanOperatorEnumeration.XOR,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            Subscribing(
                                                                id='myfares:ABO_3year_card_on_1year_payment_installment',
                                                                version='1.0',
                                                                subscription_term_type=SubscriptionTermTypeEnumeration.OPEN_ENDED,
                                                                minimum_subscription_period=XmlDuration("P1Y"),
                                                                maximum_subscription_period=XmlDuration("P10Y"),
                                                                possible_installmentt_intervals=TimeIntervalRefsRelStructure(
                                                                    time_interval_ref=[
                                                                        TimeIntervalRef(
                                                                            version='1.0',
                                                                            ref='myfares:payment_installment@3month'
                                                                        ),
                                                                        TimeIntervalRef(
                                                                            version='1.0',
                                                                            ref='myfares:payment_installment@6month'
                                                                        ),
                                                                        TimeIntervalRef(
                                                                            version='1.0',
                                                                            ref='myfares:payment_installment@1year'
                                                                        ),
                                                                    ]
                                                                ),
                                                                installment_payment_methods=[
                                                                    PaymentMethodEnumeration.DEBIT_CARD,
                                                                    PaymentMethodEnumeration.CREDIT_CARD,
                                                                    PaymentMethodEnumeration.DIRECT_DEBIT,
                                                                ]
                                                            ),
                                                            UsageValidityPeriod(
                                                                id='myfares:ABO_validity_conditions',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Refund for subscription'
                                                                ),
                                                                validity_period_type=UsageValidityTypeEnumeration.SUBSCRIPTION,
                                                                usage_trigger=UsageTriggerEnumeration.SPECIFIED_START_DATE,
                                                                usage_start_constraint_type=UsageStartConstraintTypeEnumeration.VARIABLE
                                                            ),
                                                            Suspending(
                                                                id='myfares:ABO_suspending',
                                                                version='1.0',
                                                                suspension_policy=[
                                                                    SuspensionPolicyEnumeration.FOR_CERTIFIED_ILLNESS,
                                                                    SuspensionPolicyEnumeration.FOR_HOLIDAY,
                                                                ],
                                                                qualification_period=XmlDuration("P6M"),
                                                                minimum_suspension_period=XmlDuration("P1M"),
                                                                maximum_suspension_period=XmlDuration("P9M"),
                                                                maximum_number_of_suspensions_per_term=1
                                                            ),
                                                            Refunding(
                                                                id='myfares:ABO_refund_conditions',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Refund for subscription'
                                                                ),
                                                                can_change_class=True,
                                                                unused_tickets_only=False,
                                                                only_at_certain_distribution_points=True,
                                                                resell_when=ResellWhenEnumeration.WITHIN_SPECIFIED_WINDOW,
                                                                exchangable_from_any_time_or_exchangable_from_duration_or_exchangable_from_percent_use=Decimal('0.30'),
                                                                exchangable_until_any_time_or_exchangable_until_duration_or_exchangable_until_percent_use=Decimal('0.90'),
                                                                effective_from=EffectiveFromEnumeration.NEXT_INSTALLMENT,
                                                                notification_period=XmlDuration("P1M"),
                                                                has_fee=True,
                                                                refund_basis=PerBasisEnumeration.PER_OFFER,
                                                                payment_methods=[
                                                                    PaymentMethodEnumeration.CHEQUE,
                                                                    PaymentMethodEnumeration.BANK_TRANSFER,
                                                                    PaymentMethodEnumeration.CREDIT_CARD,
                                                                ],
                                                                refund_type=RefundTypeEnumeration.EARLY_TERMINATION,
                                                                refund_policy=[
                                                                    RefundPolicyEnumeration.ANY,
                                                                ],
                                                                partial_refund_basis=PartialRefundBasisEnumeration.UNUSED_MONTHS
                                                            ),
                                                            PurchaseWindow(
                                                                id='myfares:ABO_purchase Window_conditions',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Purchase window for subscription'
                                                                ),
                                                                purchase_when=PurchaseWhenEnumeration.ADVANCE_ONLY,
                                                                minimum_period_before_departure=XmlDuration("P3D"),
                                                                purchase_moment=[
                                                                    PurchaseMomentEnumeration.IN_ADVANCE_ONLY,
                                                                ]
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        group_of_sales_offer_packages_ref_or_groups_of_sale_offer_packages=GroupOfSalesOfferPackagesRef(
                                            version='1.0',
                                            ref='myfares:Railcard-GSOP'
                                        )
                                    ),
                                ]
                            ),
                            groups_of_sales_offer_packages=GroupsOfSalesOfferPackagesInFrameRelStructure(
                                group_of_sales_offer_packages=[
                                    GroupOfSalesOfferPackages(
                                        id='myfares:Railcard-GSOP',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Common properties of Railcards'
                                        ),
                                        validity_parameter_assignments=GenericParameterAssignmentsRelStructure(
                                            generic_parameter_assignment_or_generic_parameter_assignment_in_context=[
                                                GenericParameterAssignment(
                                                    id='myfares:Season_pass-SOP@entitles',
                                                    version='1.0',
                                                    order=1,
                                                    type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                        version='ntx:v1.0',
                                                        ref='ntx:eligible'
                                                    ),
                                                    limitation_grouping_type=BooleanOperatorEnumeration.XOR,
                                                    limitations=UsageParametersRelStructure(
                                                        choice=[
                                                            SalesOfferPackageEntitlementGiven(
                                                                id='myfares:Railcard-GSOP@trip',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Right to buy rail tickets at a discount'
                                                                ),
                                                                sales_offer_package_ref=SalesOfferPackageRef(
                                                                    ref='myfares:Rail_Trip',
                                                                    version_ref='EXTERNAL'
                                                                )
                                                            ),
                                                            SalesOfferPackageEntitlementGiven(
                                                                id='myfares:Railcard-GSOP@period_pass',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Right to buy rail season passes at a discount'
                                                                ),
                                                                sales_offer_package_ref=SalesOfferPackageRef(
                                                                    ref='myfares:Rail_Pass',
                                                                    version_ref='EXTERNAL'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='myfares:Railcard-GSOP',
                                                    version='1.0',
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        version='any',
                                                        ref='myfares:card'
                                                    ),
                                                    choice=SaleDiscountRightRef(
                                                        version='1.0',
                                                        ref='myfares:Railcard'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        ),
                                        members=SalesOfferPackageRefsRelStructure(
                                            sales_offer_package_ref=[
                                                SalesOfferPackageRef(
                                                    version='1.0',
                                                    ref='myfares:Railcard-SOP@standard'
                                                ),
                                                SalesOfferPackageRef(
                                                    version='1.0',
                                                    ref='myfares:Railcard-SOP@student'
                                                ),
                                                SalesOfferPackageRef(
                                                    version='1.0',
                                                    ref='myfares:Railcard-SOP@senior'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        FareFrame(
                            id='myfares:DTA@RailCards@prices',
                            version='1.0',
                            name=MultilingualString(
                                value='Railcard prices'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                choice=[
                                    FareFrameRef(
                                        version='1.0',
                                        ref='myfares:DTA@RailCards@products'
                                    ),
                                ]
                            ),
                            pricing_parameter_set=PricingParameterSet(
                                id='myfares:RailCards@prices',
                                version='1.0',
                                pricing_rules=PricingRulesRelStructure(
                                    choice=[
                                        DiscountingRule(
                                            id='myfares:normal_discount',
                                            version='1.0',
                                            discount_as_percentage=Decimal('5')
                                        ),
                                        DiscountingRule(
                                            id='myfares:student_discount',
                                            version='1.0',
                                            discount_as_percentage=Decimal('20')
                                        ),
                                        DiscountingRule(
                                            id='myfares:senior_discount',
                                            version='1.0',
                                            discount_as_percentage=Decimal('20')
                                        ),
                                    ]
                                )
                            ),
                            price_groups=FarePricesInFrameRelStructure(
                                price_group=[
                                    PriceGroup(
                                        id='myfares:With_Railcard@discounts',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Discounts for Rail Cards'
                                        ),
                                        members=FarePricesRelStructure(
                                            choice=[
                                                UsageParameterPrice(
                                                    id='myfares:With_Railcard@adult',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Standard discount - all fares'
                                                    ),
                                                    choice_1=DiscountingRuleRef(
                                                        version='1.0',
                                                        ref='myfares:normal_discount'
                                                    ),
                                                    choice_2=UserProfileRef(
                                                        version='any',
                                                        ref='myfares:adult'
                                                    )
                                                ),
                                                UsageParameterPrice(
                                                    id='myfares:With_Railcard@child',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Standard discount - child fares'
                                                    ),
                                                    choice_1=DiscountingRuleRef(
                                                        version='1.0',
                                                        ref='myfares:normal_discount'
                                                    ),
                                                    choice_2=UserProfileRef(
                                                        version='any',
                                                        ref='myfares:child'
                                                    )
                                                ),
                                                UsageParameterPrice(
                                                    id='myfares:With_Railcard@student',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Student  discount - all fares'
                                                    ),
                                                    choice_1=DiscountingRuleRef(
                                                        version='1.0',
                                                        ref='myfares:student_discount'
                                                    ),
                                                    choice_2=UserProfileRef(
                                                        version='any',
                                                        ref='myfares:student'
                                                    )
                                                ),
                                                UsageParameterPrice(
                                                    id='myfares:With_Railcard@senior',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Senior discount - all fares'
                                                    ),
                                                    choice_1=DiscountingRuleRef(
                                                        version='1.0',
                                                        ref='myfares:senior_discount'
                                                    ),
                                                    choice_2=UserProfileRef(
                                                        version='any',
                                                        ref='myfares:senior'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            fare_tables=FareTablesInFrameRelStructure(
                                standard_fare_table_or_fare_table_in_context_or_fare_table=[
                                    FareTable(
                                        id='myfares:Railcard@prices',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Prices to buy Rail Cards'
                                        ),
                                        prices_for=PriceableObjectRefsRelStructure(
                                            choice=[
                                                SaleDiscountRightRef(
                                                    version='1.0',
                                                    ref='myfares:Railcard'
                                                ),
                                            ]
                                        ),
                                        used_in=UsedInRefsRelStructure(
                                            choice=[
                                                TariffRef(
                                                    version='1.0',
                                                    ref='myfares:Railcard_discount'
                                                ),
                                            ]
                                        ),
                                        includes=FareTablesRelStructure(
                                            choice=[
                                                FareTable(
                                                    id='myfares:Railcard@prices@adult',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Prices to buy Rail Cards - adult'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            SalesOfferPackageRef(
                                                                version='1.0',
                                                                ref='myfares:Railcard-SOP@standard'
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
                                                    cells=CellsRelStructure(
                                                        choice=[
                                                            TimeIntervalPrice(
                                                                id='myfares:railcard@adult@1year',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='adult Railcard 1 year'
                                                                ),
                                                                amount=Decimal('80'),
                                                                time_interval_ref=TimeIntervalRef(
                                                                    version='1.0',
                                                                    ref='myfares:Railcard_discount@1year'
                                                                )
                                                            ),
                                                            TimeIntervalPrice(
                                                                id='myfares:railcard@adult@2year',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='adult Railcard 2 years'
                                                                ),
                                                                amount=Decimal('140'),
                                                                time_interval_ref=TimeIntervalRef(
                                                                    version='1.0',
                                                                    ref='myfares:Railcard_discount@2year'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareTable(
                                                    id='myfares:Railcard@prices@child',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Prices to buy Rail Cards - child'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            SalesOfferPackageRef(
                                                                version='1.0',
                                                                ref='myfares:Railcard-SOP@standard'
                                                            ),
                                                        ]
                                                    ),
                                                    limitations=UsageParameterRefsRelStructure(
                                                        choice=[
                                                            UserProfileRef(
                                                                version='any',
                                                                ref='myfares:child'
                                                            ),
                                                        ]
                                                    ),
                                                    cells=CellsRelStructure(
                                                        choice=[
                                                            TimeIntervalPrice(
                                                                id='myfares:railcard@child@1year',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='child Railcard 1 year'
                                                                ),
                                                                amount=Decimal('40'),
                                                                time_interval_ref=TimeIntervalRef(
                                                                    version='1.0',
                                                                    ref='myfares:Railcard_discount@1year'
                                                                )
                                                            ),
                                                            TimeIntervalPrice(
                                                                id='myfares:railcard@child@2year',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='child Railcard 2 years'
                                                                ),
                                                                amount=Decimal('70'),
                                                                time_interval_ref=TimeIntervalRef(
                                                                    version='1.0',
                                                                    ref='myfares:Railcard_discount@2year'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareTable(
                                                    id='myfares:Railcard@prices@student',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Prices to buy Rail Cards - student'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            SalesOfferPackageRef(
                                                                version='1.0',
                                                                ref='myfares:Railcard-SOP@student'
                                                            ),
                                                        ]
                                                    ),
                                                    limitations=UsageParameterRefsRelStructure(
                                                        choice=[
                                                            UserProfileRef(
                                                                version='any',
                                                                ref='myfares:student'
                                                            ),
                                                        ]
                                                    ),
                                                    cells=CellsRelStructure(
                                                        choice=[
                                                            TimeIntervalPrice(
                                                                id='myfares:railcard@student@1year',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='student Railcard 1 year'
                                                                ),
                                                                amount=Decimal('50'),
                                                                time_interval_ref=TimeIntervalRef(
                                                                    version='1.0',
                                                                    ref='myfares:Railcard_discount@1year'
                                                                )
                                                            ),
                                                            TimeIntervalPrice(
                                                                id='myfares:railcard@student@2year',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Student Railcard 2 years'
                                                                ),
                                                                is_allowed=False,
                                                                time_interval_ref=TimeIntervalRef(
                                                                    version='1.0',
                                                                    ref='myfares:Railcard_discount@2year'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareTable(
                                                    id='myfares:Railcard@prices@senior',
                                                    version='1.0',
                                                    name=MultilingualString(
                                                        value='Prices to buy Rail Cards - Senior'
                                                    ),
                                                    prices_for=PriceableObjectRefsRelStructure(
                                                        choice=[
                                                            SalesOfferPackageRef(
                                                                version='1.0',
                                                                ref='myfares:Railcard-SOP@senior'
                                                            ),
                                                        ]
                                                    ),
                                                    limitations=UsageParameterRefsRelStructure(
                                                        choice=[
                                                            UserProfileRef(
                                                                version='any',
                                                                ref='myfares:senior'
                                                            ),
                                                        ]
                                                    ),
                                                    cells=CellsRelStructure(
                                                        choice=[
                                                            TimeIntervalPrice(
                                                                id='myfares:railcard@senior@1year',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Senior Railcard 1 year'
                                                                ),
                                                                amount=Decimal('60'),
                                                                time_interval_ref=TimeIntervalRef(
                                                                    version='1.0',
                                                                    ref='myfares:Railcard_discount@1year'
                                                                )
                                                            ),
                                                            TimeIntervalPrice(
                                                                id='myfares:railcard@senior@2year',
                                                                version='1.0',
                                                                name=MultilingualString(
                                                                    value='Senior Railcard 2 years'
                                                                ),
                                                                amount=Decimal('120'),
                                                                time_interval_ref=TimeIntervalRef(
                                                                    version='1.0',
                                                                    ref='myfares:Railcard_discount@2year'
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
                            id='myfares:DTA@Common_Resources',
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
                                        id='myfares:Types_of_Concession',
                                        version='any',
                                        name=MultilingualString(
                                            value='Types of Concession'
                                        ),
                                        values=TypesOfValueStructure(
                                            choice=[
                                                TypeOfConcession(
                                                    id='myfares:standard',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Full'
                                                    )
                                                ),
                                                TypeOfConcession(
                                                    id='myfares:concession',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Reduced'
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
                                                    id='myfares:card',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Railcard - plastic'
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
                                                        value='Grants access rights to use or travel on'
                                                    )
                                                ),
                                                TypeOfAccessRightAssignment(
                                                    id='ntx:can_access_when',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Grants access rights to use or travel during a specified period'
                                                    )
                                                ),
                                                TypeOfAccessRightAssignment(
                                                    id='ntx:condition_of_use',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Defines a condition or restriction on use'
                                                    )
                                                ),
                                                TypeOfAccessRightAssignment(
                                                    id='ntx:condition_of_sale',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Defines a condition or restriction on sale'
                                                    )
                                                ),
                                                TypeOfAccessRightAssignment(
                                                    id='ntx:can_purchase',
                                                    version='ntx:v1.0',
                                                    name=MultilingualString(
                                                        value='Describes an available purchase or means of purchase'
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
                                        id='mytoc:DTA',
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
