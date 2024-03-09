from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from .discounting_rule_ref import DiscountingRuleRef
from .entity_in_version_structure import DataManagedObjectStructure
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
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    method_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_pricing_rule_ref: Optional[TypeOfPricingRuleRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    discounting_rule_ref_or_pricing_rule_ref: Optional[
        Union[LimitingRuleRef, DiscountingRuleRef, PricingRuleRef]
    ] = field(
        default=None,
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
            ),
        },
    )
    factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Factor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
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
        },
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
