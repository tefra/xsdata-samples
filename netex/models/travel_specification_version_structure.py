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
    repeated_trip_fare_request_ref: List[RepeatedTripFareRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "RepeatedTripFareRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    single_trip_fare_request_ref: List[SingleTripFareRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "SingleTripFareRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_request_ref: List[FareRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "FareRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    stop_finder_request_ref: List[StopFinderRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "StopFinderRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    stop_event_request_ref: List[StopEventRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "StopEventRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    schedule_request_ref: List[ScheduleRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "ScheduleRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    trip_plan_request_ref: List[TripPlanRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "TripPlanRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    passenger_information_request_ref: Optional[PassengerInformationRequestRef] = field(
        default=None,
        metadata={
            "name": "PassengerInformationRequestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_price_ref: List[CustomerPurchasePackagePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    parking_price_ref: List[ParkingPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    time_interval_price_ref: List[TimeIntervalPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    time_unit_price_ref: List[TimeUnitPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    quality_structure_factor_price_ref: List[QualityStructureFactorPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactorPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    controllable_element_price_ref: List[ControllableElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    validable_element_price_ref: List[ValidableElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    geographical_interval_price_ref: List[GeographicalIntervalPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    geographical_unit_price_ref: List[GeographicalUnitPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    usage_parameter_price_ref: List[UsageParameterPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    sales_offer_package_price_ref: List[SalesOfferPackagePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    distance_matrix_element_price_ref: List[DistanceMatrixElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_structure_element_price_ref: List[FareStructureElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fulfilment_method_price_ref: List[FulfilmentMethodPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    series_constraint_price_ref: List[SeriesConstraintPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    capping_rule_price_ref: List[CappingRulePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "CappingRulePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_product_price_ref: List[FareProductPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareProductPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_price_ref: Optional[FarePriceRef] = field(
        default=None,
        metadata={
            "name": "FarePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cell_ref: List[CellRef1] = field(
        default_factory=list,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
        }
    )
    netex_org_uk_netex_cell_ref: Optional[CellRef2] = field(
        default=None,
        metadata={
            "name": "CellRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        }
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rule_step_results: Optional[PriceRuleStepResultsRelStructure] = field(
        default=None,
        metadata={
            "name": "ruleStepResults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_payment_method_ref: Optional[TypeOfPaymentMethodRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_of_validity: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartOfValidity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_of_validity: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndOfValidity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specification_summary_view: Optional[TravelSpecificationSummaryView] = field(
        default=None,
        metadata={
            "name": "TravelSpecificationSummaryView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    specific_parameter_assignments: Optional[SpecificParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "specificParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
