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

    usage_parameter_price_ref_or_usage_parameter_price_or_cell_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
