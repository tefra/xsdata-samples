from __future__ import annotations

from dataclasses import dataclass

from .capping_rule_price_versioned_child_structure import (
    CappingRulePriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappingRulePrice(CappingRulePriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
