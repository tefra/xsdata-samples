from dataclasses import dataclass, field
from typing import List
from .cell_ref_1 import CellRef1
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .usage_parameter_price import UsageParameterPrice
from .usage_parameter_price_ref import UsageParameterPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParameterPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "usageParameterPrices_RelStructure"

    usage_parameter_price_ref: List[UsageParameterPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameter_price: List[UsageParameterPrice] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterPrice",
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
