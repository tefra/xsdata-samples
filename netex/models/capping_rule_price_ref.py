from __future__ import annotations

from dataclasses import dataclass

from .capping_rule_price_ref_structure import CappingRulePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappingRulePriceRef(CappingRulePriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
