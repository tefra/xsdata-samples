from dataclasses import dataclass

from .capping_rule_price_ref_structure import CappingRulePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappingRulePriceRef(CappingRulePriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
