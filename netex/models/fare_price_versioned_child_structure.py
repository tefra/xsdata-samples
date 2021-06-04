from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.capping_rule_price_ref import CappingRulePriceRef
from netex.models.controllable_element_price_ref import ControllableElementPriceRef
from netex.models.customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from netex.models.discounting_rule import DiscountingRule
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.models.fare_price_ref import FarePriceRef
from netex.models.fare_product_price_ref import FareProductPriceRef
from netex.models.fare_structure_element_price_ref import FareStructureElementPriceRef
from netex.models.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from netex.models.geographical_interval_price_ref import GeographicalIntervalPriceRef
from netex.models.geographical_unit_price_ref import GeographicalUnitPriceRef
from netex.models.limiting_rule import LimitingRule
from netex.models.limiting_rule_in_context import LimitingRuleInContext
from netex.models.limiting_rule_ref import LimitingRuleRef
from netex.models.multilingual_string import MultilingualString
from netex.models.parking_price_ref import ParkingPriceRef
from netex.models.price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from netex.models.price_unit_ref import PriceUnitRef
from netex.models.pricing_rule_1 import PricingRule1
from netex.models.pricing_rule_2 import PricingRule2
from netex.models.pricing_rule_ref import PricingRuleRef
from netex.models.pricing_service_ref import PricingServiceRef
from netex.models.private_code import PrivateCode
from netex.models.quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from netex.models.rounding_ref import RoundingRef
from netex.models.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from netex.models.series_constraint_price_ref import SeriesConstraintPriceRef
from netex.models.time_interval_price_ref import TimeIntervalPriceRef
from netex.models.time_unit_price_ref import TimeUnitPriceRef
from netex.models.usage_parameter_price_ref import UsageParameterPriceRef
from netex.models.validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePriceVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "FarePrice_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
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
    is_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_service_ref: Optional[PricingServiceRef] = field(
        default=None,
        metadata={
            "name": "PricingServiceRef",
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
    limiting_rule_ref: List[LimitingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    discounting_rule_ref: List[DiscountingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "DiscountingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    pricing_rule_ref: Optional[PricingRuleRef] = field(
        default=None,
        metadata={
            "name": "PricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limiting_rule_in_context: List[LimitingRuleInContext] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRuleInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    limiting_rule: List[LimitingRule] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    discounting_rule: List[DiscountingRule] = field(
        default_factory=list,
        metadata={
            "name": "DiscountingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    pricing_rule: List[PricingRule2] = field(
        default_factory=list,
        metadata={
            "name": "PricingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    netex_org_uk_netex_pricing_rule: Optional[PricingRule1] = field(
        default=None,
        metadata={
            "name": "PricingRule_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    can_be_cumulative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanBeCumulative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ranking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
