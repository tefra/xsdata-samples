from dataclasses import dataclass, field
from typing import List
from netex.models.capping_rule_price import CappingRulePrice
from netex.models.capping_rule_price_ref import CappingRulePriceRef
from netex.models.cell_ref_1 import CellRef1
from netex.models.cell_ref_2 import CellRef2
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappingRulePricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "cappingRulePrices_RelStructure"

    capping_rule_price_ref: List[CappingRulePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "CappingRulePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cell_ref: List[CellRef1] = field(
        default_factory=list,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_cell_ref: List[CellRef2] = field(
        default_factory=list,
        metadata={
            "name": "CellRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capping_rule_price: List[CappingRulePrice] = field(
        default_factory=list,
        metadata={
            "name": "CappingRulePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
