from dataclasses import dataclass, field
from typing import List
from netex.models.cell_ref_1 import CellRef1
from netex.models.cell_ref_2 import CellRef2
from netex.models.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from netex.models.fulfilment_method_price_versioned_child_structure import FulfilmentMethodPriceVersionedChildStructure
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FulfilmentMethodPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fulfilmentMethodPrices_RelStructure"

    fulfilment_method_price_ref: List[FulfilmentMethodPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_method_price: List[FulfilmentMethodPriceVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cell_ref: List[CellRef2] = field(
        default_factory=list,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_cell_ref: List[CellRef1] = field(
        default_factory=list,
        metadata={
            "name": "CellRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
