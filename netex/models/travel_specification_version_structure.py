from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDateTime

from .capping_rule_price_ref import CappingRulePriceRef
from .cell_ref import CellRef
from .controllable_element_price_ref import ControllableElementPriceRef
from .customer_purchase_package_price_ref import (
    CustomerPurchasePackagePriceRef,
)
from .distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from .fare_contract_entry_version_structure import (
    FareContractEntryVersionStructure,
)
from .fare_price_ref import FarePriceRef
from .fare_product_price_ref import FareProductPriceRef
from .fare_request_ref import FareRequestRef
from .fare_structure_element_price_ref import FareStructureElementPriceRef
from .fulfilment_method_price_ref import FulfilmentMethodPriceRef
from .geographical_interval_price_ref import GeographicalIntervalPriceRef
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .parking_price_ref import ParkingPriceRef
from .payment_method_enumeration import PaymentMethodEnumeration
from .price_rule_step_results_rel_structure import (
    PriceRuleStepResultsRelStructure,
)
from .price_unit_ref import PriceUnitRef
from .quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from .repeated_trip_fare_request_ref import RepeatedTripFareRequestRef
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .sales_transaction_ref import SalesTransactionRef
from .schedule_request_ref import ScheduleRequestRef
from .series_constraint_price_ref import SeriesConstraintPriceRef
from .single_trip_fare_request_ref import SingleTripFareRequestRef
from .specific_parameter_assignments_rel_structure import (
    SpecificParameterAssignmentsRelStructure,
)
from .stop_event_request_ref import StopEventRequestRef
from .stop_finder_request_ref import StopFinderRequestRef
from .time_interval_price_ref import TimeIntervalPriceRef
from .time_unit_price_ref import TimeUnitPriceRef
from .travel_specification_summary_view import TravelSpecificationSummaryView
from .trip_plan_request_ref import TripPlanRequestRef
from .type_of_payment_method_ref import TypeOfPaymentMethodRef
from .usage_parameter_price_ref import UsageParameterPriceRef
from .validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationVersionStructure(FareContractEntryVersionStructure):
    class Meta:
        name = "TravelSpecification_VersionStructure"

    sales_transaction_ref: SalesTransactionRef | None = field(
        default=None,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_request_ref_or_passenger_information_request_ref: (
        RepeatedTripFareRequestRef
        | SingleTripFareRequestRef
        | FareRequestRef
        | StopFinderRequestRef
        | StopEventRequestRef
        | ScheduleRequestRef
        | TripPlanRequestRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RepeatedTripFareRequestRef",
                    "type": RepeatedTripFareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleTripFareRequestRef",
                    "type": SingleTripFareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareRequestRef",
                    "type": FareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopFinderRequestRef",
                    "type": StopFinderRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopEventRequestRef",
                    "type": StopEventRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduleRequestRef",
                    "type": ScheduleRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TripPlanRequestRef",
                    "type": TripPlanRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    fare_price_ref_or_cell_ref: (
        CustomerPurchasePackagePriceRef
        | ParkingPriceRef
        | TimeIntervalPriceRef
        | TimeUnitPriceRef
        | QualityStructureFactorPriceRef
        | ControllableElementPriceRef
        | ValidableElementPriceRef
        | GeographicalIntervalPriceRef
        | GeographicalUnitPriceRef
        | UsageParameterPriceRef
        | SeriesConstraintPriceRef
        | SalesOfferPackagePriceRef
        | DistanceMatrixElementPriceRef
        | FareStructureElementPriceRef
        | FulfilmentMethodPriceRef
        | CappingRulePriceRef
        | FareProductPriceRef
        | FarePriceRef
        | CellRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    amount: Decimal | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    currency: str | None = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        },
    )
    price_unit_ref: PriceUnitRef | None = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    units: Decimal | None = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rule_step_results: PriceRuleStepResultsRelStructure | None = field(
        default=None,
        metadata={
            "name": "ruleStepResults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_method: PaymentMethodEnumeration | None = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_payment_method_ref: TypeOfPaymentMethodRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_of_validity: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "StartOfValidity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_of_validity: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "EndOfValidity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specification_summary_view: (
        TravelSpecificationSummaryView | None
    ) = field(
        default=None,
        metadata={
            "name": "TravelSpecificationSummaryView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    specific_parameter_assignments: (
        SpecificParameterAssignmentsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "specificParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: NoticeAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
