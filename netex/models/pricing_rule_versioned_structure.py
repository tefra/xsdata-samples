from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.limiting_rule_ref import LimitingRuleRef
from netex.models.multilingual_string import MultilingualString
from netex.models.price_unit_ref import PriceUnitRef
from netex.models.pricing_rule_ref import PricingRuleRef
from netex.models.type_of_pricing_rule_ref import TypeOfPricingRuleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PricingRuleVersionedStructure(DataManagedObjectStructure):
    class Meta:
        name = "PricingRule_VersionedStructure"

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
    method_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_pricing_rule_ref: Optional[TypeOfPricingRuleRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPricingRuleRef",
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
        }
    )
    factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Factor",
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
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
