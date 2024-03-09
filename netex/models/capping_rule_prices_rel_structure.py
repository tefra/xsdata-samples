from dataclasses import dataclass, field
from typing import List, Union

from .capping_rule_price import CappingRulePrice
from .capping_rule_price_ref import CappingRulePriceRef
from .cell_ref_1 import CellRef1
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappingRulePricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "cappingRulePrices_RelStructure"

    capping_rule_price_ref_or_cell_ref_or_capping_rule_price: List[
        Union[CappingRulePriceRef, CellRef1, CappingRulePrice]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
