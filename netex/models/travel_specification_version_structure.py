from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .capping_rule_price_ref import CappingRulePriceRef
from .cell_ref_1 import CellRef1
from .cell_ref_2 import CellRef2
from .controllable_element_price_ref import ControllableElementPriceRef
from .customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from .distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from .fare_contract_entry_version_structure import FareContractEntryVersionStructure
from .fare_price_ref import FarePriceRef
from .fare_product_price_ref import FareProductPriceRef
from .fare_request_ref import FareRequestRef
from .fare_structure_element_price_ref import FareStructureElementPriceRef
from .fulfilment_method_price_ref import FulfilmentMethodPriceRef
from .geographical_interval_price_ref import GeographicalIntervalPriceRef
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .parking_price_ref import ParkingPriceRef
from .passenger_information_request_ref import PassengerInformationRequestRef
from .payment_method_enumeration import PaymentMethodEnumeration
from .price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from .price_unit_ref import PriceUnitRef
from .quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from .repeated_trip_fare_request_ref import RepeatedTripFareRequestRef
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .sales_transaction_ref import SalesTransactionRef
from .schedule_request_ref import ScheduleRequestRef
from .series_constraint_price_ref import SeriesConstraintPriceRef
from .single_trip_fare_request_ref import SingleTripFareRequestRef
from .specific_parameter_assignment_version_structure import SpecificParameterAssignmentsRelStructure
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

    sales_transaction_ref: Optional[SalesTransactionRef] = field(
        default=None,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
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
                {
                    "name": "PassengerInformationRequestRef",
                    "type": PassengerInformationRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
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
                    "type": CellRef1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef_",
                    "type": CellRef2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Amount",
                    "type": Decimal,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Currency",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                    "min_length": 3,
                    "max_length": 3,
                    "pattern": r"[A-Z][A-Z][A-Z]",
                },
                {
                    "name": "PriceUnitRef",
                    "type": PriceUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Units",
                    "type": Decimal,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ruleStepResults",
                    "type": PriceRuleStepResultsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PaymentMethod",
                    "type": PaymentMethodEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPaymentMethodRef",
                    "type": TypeOfPaymentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartOfValidity",
                    "type": XmlDateTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndOfValidity",
                    "type": XmlDateTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecificationSummaryView",
                    "type": TravelSpecificationSummaryView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "specificParameterAssignments",
                    "type": SpecificParameterAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "noticeAssignments",
                    "type": NoticeAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 70,
        }
    )
