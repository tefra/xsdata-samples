from dataclasses import dataclass, field
from typing import Optional
from .capping_rules_rel_structure import CappingRulesRelStructure
from .sale_discount_right_version_structure import (
    SaleDiscountRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappedDiscountRightVersionStructure(SaleDiscountRightVersionStructure):
    class Meta:
        name = "CappedDiscountRight_VersionStructure"

    capping_rules: Optional[CappingRulesRelStructure] = field(
        default=None,
        metadata={
            "name": "cappingRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
