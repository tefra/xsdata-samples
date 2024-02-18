from decimal import Decimal
from netex.models.access_right_in_product import AccessRightInProduct
from netex.models.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import FareDayType
from netex.models.alternative_texts_rel_structure import TimebandVersionedChildStructure
from netex.models.alternative_texts_rel_structure import TimebandsRelStructure
from netex.models.alternative_texts_rel_structure import ValidBetween
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.amount_of_price_unit_enumeration import AmountOfPriceUnitEnumeration
from netex.models.amount_of_price_unit_product import AmountOfPriceUnitProduct
from netex.models.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.models.charging_moment_enumeration import ChargingMomentEnumeration
from netex.models.customer import Customer
from netex.models.customer_account import CustomerAccount
from netex.models.customer_account_ref import CustomerAccountRef
from netex.models.customer_accounts_rel_structure import CustomerAccountsRelStructure
from netex.models.customer_purchase_package import CustomerPurchasePackage
from netex.models.customer_purchase_package_element import CustomerPurchasePackageElement
from netex.models.customer_purchase_package_element_access import CustomerPurchasePackageElementAccess
from netex.models.customer_purchase_package_element_accesses_rel_structure import CustomerPurchasePackageElementAccessesRelStructure
from netex.models.customer_purchase_package_elements_rel_structure import CustomerPurchasePackageElementsRelStructure
from netex.models.customer_purchase_package_status_enumeration import CustomerPurchasePackageStatusEnumeration
from netex.models.customer_purchase_packages_rel_structure import CustomerPurchasePackagesRelStructure
from netex.models.customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment
from netex.models.customer_purchase_parameter_assignments_rel_structure import CustomerPurchaseParameterAssignmentsRelStructure
from netex.models.customer_ref import CustomerRef
from netex.models.customers_in_frame_rel_structure import CustomersInFrameRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_assignment import DayTypeAssignment
from netex.models.day_type_assignments_in_frame_rel_structure import DayTypeAssignmentsInFrameRelStructure
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.fare_contract import FareContract
from netex.models.fare_contract_entries_rel_structure import FareContractEntriesRelStructure
from netex.models.fare_contracts_rel_structure import FareContractsRelStructure
from netex.models.fare_demand_factor import FareDemandFactor
from netex.models.fare_demand_factor_ref import FareDemandFactorRef
from netex.models.fare_frame import FareFrame
from netex.models.fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from netex.models.fare_structure_element import FareStructureElement
from netex.models.fare_structure_element_ref import FareStructureElementRef
from netex.models.fare_structure_element_refs_rel_structure import FareStructureElementRefsRelStructure
from netex.models.fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from netex.models.fare_zone_ref import FareZoneRef
from netex.models.frequency_of_use import FrequencyOfUse
from netex.models.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignment
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.interchanging import Interchanging
from netex.models.logical_operation_enumeration import LogicalOperationEnumeration
from netex.models.marked_as_enumeration import MarkedAsEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.operating_periods_in_frame_rel_structure import OperatingPeriodsInFrameRelStructure
from netex.models.operator_ref import OperatorRef
from netex.models.partial_refund_basis_enumeration import PartialRefundBasisEnumeration
from netex.models.participant_ref import ParticipantRef
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.proof_of_identity_enumeration import ProofOfIdentityEnumeration
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.purchase_action_enumeration import PurchaseActionEnumeration
from netex.models.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.models.purchase_window import PurchaseWindow
from netex.models.quality_structure_factor_1 import QualityStructureFactor1
from netex.models.quality_structure_factor_ref import QualityStructureFactorRef
from netex.models.quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from netex.models.refund_policy_enumeration import RefundPolicyEnumeration
from netex.models.refund_type_enumeration import RefundTypeEnumeration
from netex.models.refunding import Refunding
from netex.models.replacing import Replacing
from netex.models.resell_type_enumeration import ResellTypeEnumeration
from netex.models.sales_offer_package import SalesOfferPackage
from netex.models.sales_offer_package_element import SalesOfferPackageElement
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.sales_transaction import SalesTransaction
from netex.models.sales_transaction_frame import SalesTransactionFrame
from netex.models.sales_transaction_ref import SalesTransactionRef
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_journey_ref import ServiceJourneyRef
from netex.models.smartcard_ref import SmartcardRef
from netex.models.specific_parameter_assignment_version_structure import SpecificParameterAssignment
from netex.models.specific_parameter_assignment_version_structure import SpecificParameterAssignmentsRelStructure
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.tariff import Tariff
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.time_interval import TimeInterval
from netex.models.time_interval_ref import TimeIntervalRef
from netex.models.time_intervals_rel_structure import TimeIntervalsRelStructure
from netex.models.transferability import Transferability
from netex.models.travel_specification_1 import TravelSpecification1
from netex.models.travel_specifications_rel_structure import TravelSpecificationsRelStructure
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.models.type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from netex.models.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.models.uic_operating_period import UicOperatingPeriod
from netex.models.uic_operating_period_ref import UicOperatingPeriodRef
from netex.models.usage_end_enumeration import UsageEndEnumeration
from netex.models.usage_parameters_rel_structure import UsageParametersRelStructure
from netex.models.usage_trigger_enumeration import UsageTriggerEnumeration
from netex.models.usage_validity_period import UsageValidityPeriod
from netex.models.usage_validity_period_ref import UsageValidityPeriodRef
from netex.models.user_profile import UserProfile
from netex.models.validable_element import ValidableElement
from netex.models.validable_element_ref import ValidableElementRef
from netex.models.validable_elements_rel_structure import ValidableElementsRelStructure
from netex.models.validity_parameters_rel_structure import ValidityParametersRelStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2017, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example of simple zonal pass fares.'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='ENT:school_carnet:38',
                data_source_ref_attribute='ENT:fare_data',
                version='1',
                frames=FramesRelStructure(
                    common_frame=[
                        FareFrame(
                            id='ENT:1',
                            version='1',
                            tariffs=TariffsInFrameRelStructure(
                                tariff=[
                                    Tariff(
                                        id='ENT:school_carnet:380',
                                        version='1',
                                        time_intervals=TimeIntervalsRelStructure(
                                            time_interval_ref_or_time_interval=[
                                                TimeInterval(
                                                    id='ENT:school_carnet@academic_year',
                                                    version='1'
                                                ),
                                            ]
                                        ),
                                        quality_structure_factors=QualityStructureFactorsRelStructure(
                                            quality_structure_factor_ref_or_quality_structure_factor=[
                                                QualityStructureFactor1(
                                                    id='ENT:school_carnet@380',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='380 activations'
                                                    ),
                                                    factor='activation',
                                                    value='380'
                                                ),
                                                FareDemandFactor(
                                                    id='ENT:school_carnet@school_day@morning',
                                                    validity_conditions_or_valid_between=[
                                                        ValidityConditionsRelStructure(
                                                            choice=[
                                                                AvailabilityCondition(
                                                                    id='ENT:school_carnet@school_day@morning',
                                                                    version='1',
                                                                    day_types=DayTypesRelStructure(
                                                                        day_type_ref_or_day_type=[
                                                                            DayTypeRef(
                                                                                ref='ENT:school_day'
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    timebands=TimebandsRelStructure(
                                                                        timeband_ref_or_timeband=[
                                                                            TimebandVersionedChildStructure(
                                                                                id='ENT:school_carnet@morning',
                                                                                version='1',
                                                                                start_time_or_start_event=XmlTime(7, 0, 0, 0),
                                                                                choice=[
                                                                                    XmlTime(9, 0, 0, 0),
                                                                                ]
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                    version='1'
                                                ),
                                                FareDemandFactor(
                                                    id='ENT:school_carnet@school_day@afternoon',
                                                    validity_conditions_or_valid_between=[
                                                        ValidityConditionsRelStructure(
                                                            choice=[
                                                                AvailabilityCondition(
                                                                    id='ENT:school_carnet@school_day@afternoon',
                                                                    version='1',
                                                                    day_types=DayTypesRelStructure(
                                                                        day_type_ref_or_day_type=[
                                                                            DayTypeRef(
                                                                                ref='ENT:school_day'
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    timebands=TimebandsRelStructure(
                                                                        timeband_ref_or_timeband=[
                                                                            TimebandVersionedChildStructure(
                                                                                id='ENT:school_carnet@afternoon',
                                                                                version='1',
                                                                                start_time_or_start_event=XmlTime(12, 0, 0, 0),
                                                                                choice=[
                                                                                    XmlTime(16, 0, 0, 0),
                                                                                ]
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                    version='1'
                                                ),
                                            ]
                                        ),
                                        fare_structure_elements=FareStructureElementsRelStructure(
                                            fare_structure_element_ref_or_fare_structure_element=[
                                                FareStructureElement(
                                                    id='ENT:school_carnet@access_zones',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Available zones'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access',
                                                        version_ref='fxc:v1.0'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ENT:school_carnet@access_zones',
                                                        version='1',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:can_access',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        validity_parameter_grouping_type=LogicalOperationEnumeration.XOR,
                                                        validity_parameters=ValidityParametersRelStructure(
                                                            fare_zone_ref=[
                                                                FareZoneRef(
                                                                    ref='ENT:Bergen@X',
                                                                    version_ref='1'
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ENT:school_carnet@access_when@morning',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Access time restrictions'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access_when',
                                                        version_ref='fxc:v1.0'
                                                    ),
                                                    choice=FareDemandFactorRef(
                                                        ref='ENT:school_carnet@school_day@morning',
                                                        version_ref='1'
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ENT:school_carnet@access_when@afternoon',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Access time restrictions'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:access_whenn',
                                                        version_ref='fxc:v1.0'
                                                    ),
                                                    choice=FareDemandFactorRef(
                                                        ref='ENT:school_carnet@school_day@afternoon',
                                                        version_ref='1'
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ENT:school_carnet@eligibility',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Eligible user types'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:eligibility',
                                                        version_ref='fxc:v1.0'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ENT:school_carnet@eligibility',
                                                        version='1',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:eligible',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.XOR,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UserProfile(
                                                                    id='ENT:school_carnet@Pupil',
                                                                    version='1',
                                                                    name=MultilingualString(
                                                                        value='Pupil',
                                                                        lang='no'
                                                                    ),
                                                                    proof_required=[
                                                                        ProofOfIdentityEnumeration.IDENTITY_DOCUMENT,
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ENT:school_carnet@usage_limit',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Usage limit  restrictions'
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:usage_limit',
                                                        version_ref='fxc:v1.0'
                                                    ),
                                                    choice=QualityStructureFactorRef(
                                                        ref='ENT:school_carnet@380',
                                                        version_ref='1'
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ENT:school_carnet@durations',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Available durations NOTE WE DONT REALLY NEED THIS FOR A CARNET - WOULD NEED IT FOR A PASS  '
                                                    ),
                                                    type_of_fare_structure_element_ref=TypeOfFareStructureElementRef(
                                                        ref='fxc:durations',
                                                        version_ref='fxc:v1.0'
                                                    ),
                                                    time_interval_ref_or_time_intervals_or_time_structure_factors=TimeIntervalsRelStructure(
                                                        time_interval_ref_or_time_interval=[
                                                            TimeIntervalRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@academic_year'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ENT:school_carnet@conditions_of_travel@carnet',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Conditions of travel - overall carnet'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ENT:school_carnet@conditions_of_travel',
                                                        version='1',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:condition_of_use',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UsageValidityPeriod(
                                                                    id='ENT:school_carnet@carnet_validity',
                                                                    version='1',
                                                                    name=MultilingualString(
                                                                        value='Valid from start of school year'
                                                                    ),
                                                                    usage_trigger=UsageTriggerEnumeration.START_OF_PERIOD,
                                                                    usage_end=UsageEndEnumeration.PRODUCT_EXPIRY
                                                                ),
                                                                Transferability(
                                                                    id='ENT:school_carnet@ransferability',
                                                                    version='1',
                                                                    name=MultilingualString(
                                                                        value='Carnet is not transferable'
                                                                    ),
                                                                    can_transfer=False
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='ENT:school_carnet@frequency',
                                                                    version='1',
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.TWICE_ADAY
                                                                ),
                                                                Interchanging(
                                                                    id='ENT:school_carnet@interchanging',
                                                                    version='1',
                                                                    can_interchange=True
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ENT:school_carnet@conditions_of_travel@trip',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Conditions of travel - overall carnet'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ENT:school_carnet@conditions_of_travel@trip',
                                                        version='1',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:condition_of_use',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UsageValidityPeriod(
                                                                    id='ENT:school_carnet@trip@validity',
                                                                    version='1',
                                                                    name=MultilingualString(
                                                                        value='Trip is valid for 70 minutes'
                                                                    ),
                                                                    usage_trigger=UsageTriggerEnumeration.ACTIVATION,
                                                                    usage_end=UsageEndEnumeration.STANDARD_DURATION,
                                                                    standard_duration=XmlDuration("PT70M")
                                                                ),
                                                                Transferability(
                                                                    id='ENT:school_carnet@trip@ransferability',
                                                                    version='1',
                                                                    name=MultilingualString(
                                                                        value='Ticket is not transferable'
                                                                    ),
                                                                    can_transfer=False
                                                                ),
                                                                FrequencyOfUse(
                                                                    id='ENT:school_carnet@trip@frequency',
                                                                    version='1',
                                                                    frequency_of_use_type=FrequencyOfUseTypeEnumeration.SINGLE
                                                                ),
                                                                Interchanging(
                                                                    id='ENT:school_carnet@trip@interchanging',
                                                                    version='1',
                                                                    can_interchange=True
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ),
                                                FareStructureElement(
                                                    id='ENT:school_carnet@conditions_of_sale',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Conditions of sale - overall carnet'
                                                    ),
                                                    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                                        id='ENT:school_carnet@conditions_of_sale',
                                                        version='1',
                                                        order=1,
                                                        type_of_access_right_assignment_ref=TypeOfAccessRightAssignmentRef(
                                                            ref='fxc:condition_of_salee',
                                                            version_ref='fxc:v1.0'
                                                        ),
                                                        limitation_grouping_type=LogicalOperationEnumeration.AND,
                                                        limitations=UsageParametersRelStructure(
                                                            choice=[
                                                                UsageValidityPeriod(
                                                                    id='ENT:school_carnet@validity',
                                                                    version='1',
                                                                    name=MultilingualString(
                                                                        value='Carnet is valid till end of year'
                                                                    ),
                                                                    usage_trigger=UsageTriggerEnumeration.START_OF_PERIOD,
                                                                    usage_end=UsageEndEnumeration.PRODUCT_EXPIRY
                                                                ),
                                                                PurchaseWindow(
                                                                    id='ENT:school_carnet@purchase_window',
                                                                    version='1',
                                                                    name=MultilingualString(
                                                                        value='Must be bought  at least one day beforehand'
                                                                    ),
                                                                    purchase_action=PurchaseActionEnumeration.PURCHASE,
                                                                    minimum_period_before_departure=XmlDuration("P1D"),
                                                                    purchase_moment=[
                                                                        PurchaseMomentEnumeration.IN_ADVANCE_ONLY,
                                                                    ]
                                                                ),
                                                                Refunding(
                                                                    id='ENT:school_carnet@refunding',
                                                                    version='1',
                                                                    name=MultilingualString(
                                                                        value='Refund allowed for certain reasons'
                                                                    ),
                                                                    allowed=ResellTypeEnumeration.PARTIAL,
                                                                    only_at_certain_distribution_points=True,
                                                                    exchangable_until_any_time_or_exchangable_until_duration_or_exchangable_until_percent_use=Decimal('80'),
                                                                    has_fee=True,
                                                                    refund_type=RefundTypeEnumeration.CANCELLATION,
                                                                    refund_policy=[
                                                                        RefundPolicyEnumeration.CHANGE_OF_RESIDENCE,
                                                                    ],
                                                                    partial_refund_basis=PartialRefundBasisEnumeration.UNUSED_DAYS,
                                                                    payment_method=[
                                                                        PaymentMethodEnumeration.BANK_TRANSFER,
                                                                    ]
                                                                ),
                                                                Replacing(
                                                                    id='ENT:school_carnet@replacing',
                                                                    version='1',
                                                                    name=MultilingualString(
                                                                        value='Replacement allowed for a fee'
                                                                    ),
                                                                    allowed=ResellTypeEnumeration.PARTIAL,
                                                                    has_fee=True
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
                                    AmountOfPriceUnitProduct(
                                        id='ENT:school_carnet',
                                        version='1',
                                        name=MultilingualString(
                                            value='School transport with limited number of rides',
                                            lang='no'
                                        ),
                                        charging_moment_type=ChargingMomentEnumeration.BEFORE_TRAVEL,
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            ref='ENT:bergen_muni',
                                            version_ref='1.0'
                                        ),
                                        validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context=GenericParameterAssignment(
                                            id='ENT:school_carnet',
                                            version='1',
                                            order=1,
                                            fare_structure_element_ref=FareStructureElementRef(
                                                version='1',
                                                ref='ENT:school_carnet@conditions_of_sale'
                                            )
                                        ),
                                        validable_elements=ValidableElementsRelStructure(
                                            validable_element_ref_or_validable_element=[
                                                ValidableElement(
                                                    id='ENT:school_carnet@morning_trip',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Enkelttur Entur'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@access_zones'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@usage_limit'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@access_when@morning'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@durations'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@conditions_of_travel@trip'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                ValidableElement(
                                                    id='ENT:school_carnet@afternoon_trip',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Enkelttur Entur'
                                                    ),
                                                    fare_structure_elements=FareStructureElementRefsRelStructure(
                                                        fare_structure_element_ref=[
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@access_zones'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@usage_limit'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@access_when@afternoon'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@eligibility'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@durations'
                                                            ),
                                                            FareStructureElementRef(
                                                                version='1',
                                                                ref='ENT:school_carnet@conditions_of_travel@trip'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        access_rights_in_product=AccessRightsInProductRelStructure(
                                            access_right_in_product_ref_or_access_right_in_product=[
                                                AccessRightInProduct(
                                                    id='ENT:school_carnet@morning_trip',
                                                    version='1',
                                                    maximum_access=1,
                                                    order=1,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='1',
                                                        ref='ENT:school_carnet@morning_trip'
                                                    )
                                                ),
                                                AccessRightInProduct(
                                                    id='ENT:school_carnet@evening_trip',
                                                    version='1',
                                                    maximum_access=1,
                                                    order=2,
                                                    validable_element_ref=ValidableElementRef(
                                                        version='1',
                                                        ref='ENT:school_carnet@afternoon_trip'
                                                    )
                                                ),
                                            ]
                                        ),
                                        product_type=AmountOfPriceUnitEnumeration.TRIP_CARNET
                                    ),
                                ]
                            ),
                            sales_offer_packages=SalesOfferPackagesInFrameRelStructure(
                                sales_offer_package=[
                                    SalesOfferPackage(
                                        id='ENT:school_carnet',
                                        version='1',
                                        name=MultilingualString(
                                            value='School transport Municipality X',
                                            lang='no'
                                        ),
                                        sales_offer_package_elements=SalesOfferPackageElementsRelStructure(
                                            sales_offer_package_element_ref_or_sales_offer_package_element=[
                                                SalesOfferPackageElement(
                                                    id='ENT:school_carnet',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='School transport Municipality X',
                                                        lang='no'
                                                    ),
                                                    type_of_travel_document_ref=TypeOfTravelDocumentRef(
                                                        ref='ENT:smartcard',
                                                        version_ref='1.0'
                                                    ),
                                                    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref=AmountOfPriceUnitProductRef(
                                                        version='1',
                                                        ref='ENT:school_carnet'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='ENT:Bergen2020',
                            version='1',
                            name=MultilingualString(
                                value='SchoolYear calendar'
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    FareDayType(
                                        id='ENT:school_day',
                                        version='1',
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.WEEKDAYS,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.SCHOOL_DAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            operating_periods=OperatingPeriodsInFrameRelStructure(
                                operating_period_or_uic_operating_period=[
                                    UicOperatingPeriod(
                                        id='ENT:Bergen2020',
                                        version='1',
                                        from_operating_day_ref_or_from_date=XmlDateTime(2020, 8, 17, 0, 0, 0),
                                        to_operating_day_ref_or_to_date=XmlDateTime(2020, 12, 31, 0, 0, 0),
                                        valid_day_bits='\n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111100 \n                                1111 \n\t\t\t\t\t\t\t'
                                    ),
                                ]
                            ),
                            day_type_assignments=DayTypeAssignmentsInFrameRelStructure(
                                day_type_assignment=[
                                    DayTypeAssignment(
                                        id='ENT:Calendar',
                                        version='1',
                                        order=1,
                                        choice=UicOperatingPeriodRef(
                                            version='1',
                                            ref='ENT:Bergen2020'
                                        ),
                                        day_type_ref=DayTypeRef(
                                            version='1',
                                            ref='ENT:school_day'
                                        )
                                    ),
                                ]
                            )
                        ),
                        SalesTransactionFrame(
                            id='ENX:school_Card_examples',
                            version='1',
                            customers=CustomersInFrameRelStructure(
                                customer=[
                                    Customer(
                                        id='ENX:1234',
                                        version='1',
                                        first_name='Loki',
                                        email='loki@troll.no',
                                        customer_accounts=CustomerAccountsRelStructure(
                                            customer_account_ref_or_customer_account=[
                                                CustomerAccount(
                                                    id='ENX:1234-T',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='School Travel Travel'
                                                    )
                                                ),
                                            ]
                                        ),
                                        fare_contracts=FareContractsRelStructure(
                                            fare_contract_ref_or_fare_contract=[
                                                FareContract(
                                                    id='ENX:1234@school_card',
                                                    version='1',
                                                    name=MultilingualString(
                                                        value='Skolekort Municipality X'
                                                    ),
                                                    start_date=XmlDateTime(2020, 9, 6, 1, 7, 0),
                                                    end_date=XmlDateTime(2021, 9, 7, 1, 7, 0),
                                                    fare_contract_entries=FareContractEntriesRelStructure(
                                                        choice=[
                                                            SalesTransaction(
                                                                id='ENX:5781234501',
                                                                version='1',
                                                                name=MultilingualString(
                                                                    value='Kjøp Skoleskyss'
                                                                ),
                                                                description=MultilingualString(
                                                                    value='Initial purchase of carnet'
                                                                ),
                                                                date=XmlDateTime(2020, 9, 6, 1, 7, 0),
                                                                amount=Decimal('10000'),
                                                                currency='NOK',
                                                                payment_method=PaymentMethodEnumeration.DEBIT_CARD,
                                                                travel_specifications=TravelSpecificationsRelStructure(
                                                                    travel_specification_ref_or_travel_specification=[
                                                                        TravelSpecification1(
                                                                            id='ENT:5781234501',
                                                                            version='1',
                                                                            units=Decimal('380'),
                                                                            start_of_validity=XmlDateTime(2020, 1, 1, 7, 5, 0),
                                                                            end_of_validity=XmlDateTime(2020, 12, 31, 16, 0, 0),
                                                                            specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                specific_parameter_assignment=[
                                                                                    SpecificParameterAssignment(
                                                                                        id='ENT:5781234501',
                                                                                        version='1',
                                                                                        order=1,
                                                                                        sales_offer_package_ref=SalesOfferPackageRef(
                                                                                            version='1',
                                                                                            ref='ENT:school_carnet'
                                                                                        ),
                                                                                        validity_parameters=ValidityParametersRelStructure(
                                                                                            fare_zone_ref=[
                                                                                                FareZoneRef(
                                                                                                    ref='ENT:Bergen@X',
                                                                                                    version_ref='1'
                                                                                                ),
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                customer_purchase_packages=CustomerPurchasePackagesRelStructure(
                                                                    customer_purchase_package_or_customer_purchase_package_ref=[
                                                                        CustomerPurchasePackage(
                                                                            id='ENX:1234@school_transport',
                                                                            version='1',
                                                                            customer_ref=CustomerRef(
                                                                                version='1',
                                                                                ref='ENX:1234'
                                                                            ),
                                                                            customer_account_ref=CustomerAccountRef(
                                                                                version='1',
                                                                                ref='ENX:1234-T'
                                                                            ),
                                                                            customer_purchase_package_status=CustomerPurchasePackageStatusEnumeration.PARTIALLY_USED,
                                                                            travel_specifications=TravelSpecificationsRelStructure(
                                                                                travel_specification_ref_or_travel_specification=[
                                                                                    TravelSpecification1(
                                                                                        id='ENX:1234@school_transport',
                                                                                        version='1',
                                                                                        units=Decimal('380'),
                                                                                        start_of_validity=XmlDateTime(2020, 1, 1, 7, 5, 0),
                                                                                        end_of_validity=XmlDateTime(2020, 12, 31, 16, 0, 0),
                                                                                        specific_parameter_assignments=SpecificParameterAssignmentsRelStructure(
                                                                                            specific_parameter_assignment=[
                                                                                                SpecificParameterAssignment(
                                                                                                    id='ENX:1234@school_transport',
                                                                                                    version='1',
                                                                                                    order=1,
                                                                                                    sales_offer_package_ref=SalesOfferPackageRef(
                                                                                                        version='1',
                                                                                                        ref='ENT:school_carnet'
                                                                                                    ),
                                                                                                    validity_parameters=ValidityParametersRelStructure(
                                                                                                        fare_zone_ref=[
                                                                                                            FareZoneRef(
                                                                                                                ref='ENT:Bergen@X',
                                                                                                                version_ref='1'
                                                                                                            ),
                                                                                                        ]
                                                                                                    )
                                                                                                ),
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                            customer_purchase_package_elements=CustomerPurchasePackageElementsRelStructure(
                                                                                customer_purchase_package_element=[
                                                                                    CustomerPurchasePackageElement(
                                                                                        id='ENT:school_transport@morning_trip',
                                                                                        validity_conditions_or_valid_between=[
                                                                                            ValidBetween(
                                                                                                from_date=XmlDateTime(2020, 1, 1, 7, 0, 0),
                                                                                                to_date=XmlDateTime(2020, 12, 31, 16, 0, 0)
                                                                                            ),
                                                                                        ],
                                                                                        version='1',
                                                                                        element_accesses=CustomerPurchasePackageElementAccessesRelStructure(
                                                                                            customer_purchase_package_element_access=[
                                                                                                CustomerPurchasePackageElementAccess(
                                                                                                    id='ENT:school_transport@morning_trip@1',
                                                                                                    changed=XmlDateTime(2020, 1, 5, 7, 5, 0),
                                                                                                    version='1',
                                                                                                    marked_as=MarkedAsEnumeration.USED,
                                                                                                    validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                                                                        customer_purchase_parameter_assignment=[
                                                                                                            CustomerPurchaseParameterAssignment(
                                                                                                                id='ENT:school_transport@morning_trip@1',
                                                                                                                version='1',
                                                                                                                order=1,
                                                                                                                limitations=UsageParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        UsageValidityPeriodRef(
                                                                                                                            version='1',
                                                                                                                            ref='ENT:school_carnet@trip@validity'
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                ),
                                                                                                                validity_parameters=ValidityParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        OperatorRef(
                                                                                                                            ref='ENT:bergen_muni',
                                                                                                                            version_ref='EXTERNAl'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    choice_1=[
                                                                                                                        StopPlaceRef(
                                                                                                                            ref='NSR:123',
                                                                                                                            version_ref='EXTERNAl'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    service_journey_ref=[
                                                                                                                        ServiceJourneyRef(
                                                                                                                            ref='ENT:ServiceJourney:1234578',
                                                                                                                            version_ref='EXTERNAl'
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                )
                                                                                                            ),
                                                                                                        ]
                                                                                                    )
                                                                                                ),
                                                                                                CustomerPurchasePackageElementAccess(
                                                                                                    id='ENT:school_transport@morning_trip@2',
                                                                                                    created=XmlDateTime(2020, 1, 6, 7, 15, 0),
                                                                                                    version='1',
                                                                                                    marked_as=MarkedAsEnumeration.USED,
                                                                                                    validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                                                                        customer_purchase_parameter_assignment=[
                                                                                                            CustomerPurchaseParameterAssignment(
                                                                                                                id='ENT:school_transport@morning_trip@2',
                                                                                                                version='1',
                                                                                                                order=1,
                                                                                                                limitations=UsageParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        UsageValidityPeriodRef(
                                                                                                                            version='1',
                                                                                                                            ref='ENT:school_carnet@trip@validity'
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                ),
                                                                                                                validity_parameters=ValidityParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        OperatorRef(
                                                                                                                            ref='ENT:bergen_muni',
                                                                                                                            version_ref='1.0'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    choice_1=[
                                                                                                                        StopPlaceRef(
                                                                                                                            ref='NSR:123',
                                                                                                                            version_ref='EXTERNAl'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    service_journey_ref=[
                                                                                                                        ServiceJourneyRef(
                                                                                                                            ref='ENT:ServiceJourney:12348',
                                                                                                                            version_ref='EXTERNAl'
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                )
                                                                                                            ),
                                                                                                        ]
                                                                                                    )
                                                                                                ),
                                                                                                CustomerPurchasePackageElementAccess(
                                                                                                    id='ENT:school_transport@morning_trip@3',
                                                                                                    created=XmlDateTime(2020, 1, 7, 7, 16, 0),
                                                                                                    version='1',
                                                                                                    marked_as=MarkedAsEnumeration.USED,
                                                                                                    validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                                                                        customer_purchase_parameter_assignment=[
                                                                                                            CustomerPurchaseParameterAssignment(
                                                                                                                id='ENT:school_transport@morning_trip@3',
                                                                                                                version='1',
                                                                                                                order=1,
                                                                                                                limitations=UsageParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        UsageValidityPeriodRef(
                                                                                                                            version='1',
                                                                                                                            ref='ENT:school_carnet@trip@validity'
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                ),
                                                                                                                validity_parameters=ValidityParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        OperatorRef(
                                                                                                                            ref='ENT:bergen_muni',
                                                                                                                            version_ref='1.0'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    choice_1=[
                                                                                                                        StopPlaceRef(
                                                                                                                            ref='NSR:123',
                                                                                                                            version_ref='EXTERNAl'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    service_journey_ref=[
                                                                                                                        ServiceJourneyRef(
                                                                                                                            ref='ENT:ServiceJourney:12347',
                                                                                                                            version_ref='EXTERNAl'
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
                                                                                                    id='ENT:school_transport@morning_trip@2020-01-01@07:05:00',
                                                                                                    version='1',
                                                                                                    order=1,
                                                                                                    validable_element_ref=ValidableElementRef(
                                                                                                        version='1',
                                                                                                        ref='ENT:school_carnet@morning_trip'
                                                                                                    )
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                        order=1
                                                                                    ),
                                                                                    CustomerPurchasePackageElement(
                                                                                        id='ENT:school_transport@afternoon_trip',
                                                                                        validity_conditions_or_valid_between=[
                                                                                            ValidBetween(
                                                                                                from_date=XmlDateTime(2020, 1, 1, 12, 0, 0),
                                                                                                to_date=XmlDateTime(2020, 12, 31, 16, 0, 0)
                                                                                            ),
                                                                                        ],
                                                                                        version='1',
                                                                                        element_accesses=CustomerPurchasePackageElementAccessesRelStructure(
                                                                                            customer_purchase_package_element_access=[
                                                                                                CustomerPurchasePackageElementAccess(
                                                                                                    id='ENT:school_transport@afternoon_trip@1',
                                                                                                    created=XmlDateTime(2020, 1, 5, 16, 20, 0),
                                                                                                    version='1',
                                                                                                    marked_as=MarkedAsEnumeration.USED,
                                                                                                    validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                                                                        customer_purchase_parameter_assignment=[
                                                                                                            CustomerPurchaseParameterAssignment(
                                                                                                                id='ENT:school_transport@afternoon_trip@1',
                                                                                                                version='1',
                                                                                                                order=1,
                                                                                                                limitations=UsageParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        UsageValidityPeriodRef(
                                                                                                                            version='1',
                                                                                                                            ref='ENT:school_carnet@trip@validity'
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                ),
                                                                                                                validity_parameters=ValidityParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        OperatorRef(
                                                                                                                            ref='ENT:bergen_muni',
                                                                                                                            version_ref='1.0'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    choice_1=[
                                                                                                                        StopPlaceRef(
                                                                                                                            ref='NSR:891',
                                                                                                                            version_ref='EXTERNAl'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    service_journey_ref=[
                                                                                                                        ServiceJourneyRef(
                                                                                                                            ref='ENT:ServiceJourney:123455438',
                                                                                                                            version_ref='EXTERNAl'
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                )
                                                                                                            ),
                                                                                                        ]
                                                                                                    )
                                                                                                ),
                                                                                                CustomerPurchasePackageElementAccess(
                                                                                                    id='ENT:school_transport@afternoon_trip@2',
                                                                                                    created=XmlDateTime(2020, 1, 6, 16, 25, 0),
                                                                                                    version='1',
                                                                                                    marked_as=MarkedAsEnumeration.USED,
                                                                                                    validity_parameter_assignments=CustomerPurchaseParameterAssignmentsRelStructure(
                                                                                                        customer_purchase_parameter_assignment=[
                                                                                                            CustomerPurchaseParameterAssignment(
                                                                                                                id='ENT:school_transport@afternoon_trip@2',
                                                                                                                version='1',
                                                                                                                order=1,
                                                                                                                limitations=UsageParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        UsageValidityPeriodRef(
                                                                                                                            version='1',
                                                                                                                            ref='ENT:school_carnet@trip@validity'
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                ),
                                                                                                                validity_parameters=ValidityParametersRelStructure(
                                                                                                                    choice=[
                                                                                                                        OperatorRef(
                                                                                                                            ref='ENT:bergen_muni',
                                                                                                                            version_ref='1.0'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    choice_1=[
                                                                                                                        StopPlaceRef(
                                                                                                                            ref='NSR:891',
                                                                                                                            version_ref='EXTERNAl'
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    service_journey_ref=[
                                                                                                                        ServiceJourneyRef(
                                                                                                                            ref='ENT:ServiceJourney:123455438',
                                                                                                                            version_ref='EXTERNAl'
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
                                                                                                    id='ENT:school_transport@afternoon_trip@2020-01-01@07:05:00',
                                                                                                    version='1',
                                                                                                    order=1,
                                                                                                    validable_element_ref=ValidableElementRef(
                                                                                                        version='1',
                                                                                                        ref='ENT:school_carnet@afternoon_trip'
                                                                                                    )
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                        order=1
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                            sales_transaction_ref=SalesTransactionRef(
                                                                                version='1',
                                                                                ref='ENX:5781234501'
                                                                            ),
                                                                            medium_access_device_ref=SmartcardRef(
                                                                                ref='ENX:87654',
                                                                                version_ref='1'
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
        ]
    ),
    version='1.1'
)
