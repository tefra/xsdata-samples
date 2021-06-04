from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.models.capping_rule_price_ref import CappingRulePriceRef
from netex.models.controllable_element_price_ref import ControllableElementPriceRef
from netex.models.customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.models.fare_price_ref import FarePriceRef
from netex.models.fare_product_price_ref import FareProductPriceRef
from netex.models.fare_structure_element_price_ref import FareStructureElementPriceRef
from netex.models.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from netex.models.geographical_interval_price_ref import GeographicalIntervalPriceRef
from netex.models.geographical_unit_price_ref import GeographicalUnitPriceRef
from netex.models.limiting_rule_ref import LimitingRuleRef
from netex.models.multilingual_string import MultilingualString
from netex.models.parking_price_ref import ParkingPriceRef
from netex.models.price_unit_ref import PriceUnitRef
from netex.models.pricing_rule_ref import PricingRuleRef
from netex.models.quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from netex.models.rounding_ref import RoundingRef
from netex.models.rounding_step_ref import RoundingStepRef
from netex.models.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from netex.models.series_constraint_price_ref import SeriesConstraintPriceRef
from netex.models.time_interval_price_ref import TimeIntervalPriceRef
from netex.models.time_unit_price_ref import TimeUnitPriceRef
from netex.models.usage_parameter_price_ref import UsageParameterPriceRef
from netex.models.validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceRuleStepResultStructure:
    customer_purchase_package_price_ref: Optional[CustomerPurchasePackagePriceRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_price_ref: Optional[ParkingPriceRef] = field(
        default=None,
        metadata={
            "name": "ParkingPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_interval_price_ref: Optional[TimeIntervalPriceRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit_price_ref: Optional[TimeUnitPriceRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factor_price_ref: Optional[QualityStructureFactorPriceRef] = field(
        default=None,
        metadata={
            "name": "QualityStructureFactorPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_price_ref: Optional[ControllableElementPriceRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element_price_ref: Optional[ValidableElementPriceRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval_price_ref: Optional[GeographicalIntervalPriceRef] = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_price_ref: Optional[GeographicalUnitPriceRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameter_price_ref: Optional[UsageParameterPriceRef] = field(
        default=None,
        metadata={
            "name": "UsageParameterPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_price_ref: Optional[SalesOfferPackagePriceRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_price_ref: Optional[DistanceMatrixElementPriceRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_price_ref: Optional[FareStructureElementPriceRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_method_price_ref: Optional[FulfilmentMethodPriceRef] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraint_price_ref: Optional[SeriesConstraintPriceRef] = field(
        default=None,
        metadata={
            "name": "SeriesConstraintPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capping_rule_price_ref: Optional[CappingRulePriceRef] = field(
        default=None,
        metadata={
            "name": "CappingRulePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_product_price_ref: Optional[FareProductPriceRef] = field(
        default=None,
        metadata={
            "name": "FareProductPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    rate_used: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateUsed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjustment_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AdjustmentAmount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjustment_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AdjustmentUnits",
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
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    discounting_rule_ref: List[DiscountingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "DiscountingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    pricing_rule_ref: Optional[PricingRuleRef] = field(
        default=None,
        metadata={
            "name": "PricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
    rounding_step_ref: Optional[RoundingStepRef] = field(
        default=None,
        metadata={
            "name": "RoundingStepRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    narrative: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Narrative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
