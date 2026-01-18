from dataclasses import dataclass, field
from decimal import Decimal

from .discounting_rule_versioned_structure import (
    DiscountingRuleVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LimitingRuleVersionedStructure(DiscountingRuleVersionedStructure):
    class Meta:
        name = "LimitingRule_VersionedStructure"

    minimum_price: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_price_as_percentage: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumPriceAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_price_as_multiple: int | None = field(
        default=None,
        metadata={
            "name": "MinimumPriceAsMultiple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_price: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_price_as_percentage: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumPriceAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_price_as_multiple: int | None = field(
        default=None,
        metadata={
            "name": "MaximumPriceAsMultiple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_limit_price_as_percentage: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumLimitPriceAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_limit_price: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumLimitPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_limit_price_as_percentage: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumLimitPriceAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_limit_price: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumLimitPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
