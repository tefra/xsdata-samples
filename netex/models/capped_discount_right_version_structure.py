from __future__ import annotations

from dataclasses import dataclass, field

from .capping_rules_rel_structure import CappingRulesRelStructure
from .sale_discount_right_version_structure import (
    SaleDiscountRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappedDiscountRightVersionStructure(SaleDiscountRightVersionStructure):
    class Meta:
        name = "CappedDiscountRight_VersionStructure"

    capping_rules: None | CappingRulesRelStructure = field(
        default=None,
        metadata={
            "name": "cappingRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
