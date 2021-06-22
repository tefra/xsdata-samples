from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .discounting_rule_ref import DiscountingRuleRef
from .limiting_rule_ref import LimitingRuleRef
from .multilingual_string import MultilingualString
from .price_unit_ref import PriceUnitRef
from .pricing_rule_ref import PricingRuleRef
from .type_of_pricing_rule_ref import TypeOfPricingRuleRef

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
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleRef",
                    "type": LimitingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRuleRef",
                    "type": DiscountingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRuleRef",
                    "type": PricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Factor",
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
                    "name": "url",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 10,
        }
    )
