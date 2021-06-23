from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .capping_rule_price_ref import CappingRulePriceRef
from .controllable_element_price_ref import ControllableElementPriceRef
from .customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from .discounting_rule_ref import DiscountingRuleRef
from .distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from .fare_price_ref import FarePriceRef
from .fare_product_price_ref import FareProductPriceRef
from .fare_structure_element_price_ref import FareStructureElementPriceRef
from .fulfilment_method_price_ref import FulfilmentMethodPriceRef
from .geographical_interval_price_ref import GeographicalIntervalPriceRef
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .limiting_rule_ref import LimitingRuleRef
from .multilingual_string import MultilingualString
from .parking_price_ref import ParkingPriceRef
from .price_unit_ref import PriceUnitRef
from .pricing_rule_ref import PricingRuleRef
from .quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from .rounding_ref import RoundingRef
from .rounding_step_ref import RoundingStepRef
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .series_constraint_price_ref import SeriesConstraintPriceRef
from .time_interval_price_ref import TimeIntervalPriceRef
from .time_unit_price_ref import TimeUnitPriceRef
from .usage_parameter_price_ref import UsageParameterPriceRef
from .validable_element_price_ref import ValidableElementPriceRef

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
    limiting_rule_ref: Optional[LimitingRuleRef] = field(
        default=None,
        metadata={
            "name": "LimitingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    discounting_rule_ref: Optional[DiscountingRuleRef] = field(
        default=None,
        metadata={
            "name": "DiscountingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
