from dataclasses import dataclass, field
from typing import List
from netex.models.cell_ref_1 import CellRef1
from netex.models.cell_ref_2 import CellRef2
from netex.models.geographical_interval_price_ref import GeographicalIntervalPriceRef
from netex.models.geographical_interval_price_versioned_child_structure import GeographicalIntervalPriceVersionedChildStructure
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalIntervalPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "geographicalIntervalPrices_RelStructure"

    geographical_interval_price_ref: List[GeographicalIntervalPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval_price: List[GeographicalIntervalPriceVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalPrice",
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
