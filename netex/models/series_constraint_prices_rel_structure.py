from dataclasses import dataclass, field
from typing import List
from netex.models.cell_ref_1 import CellRef1
from netex.models.cell_ref_2 import CellRef2
from netex.models.series_constraint_price_ref import SeriesConstraintPriceRef
from netex.models.series_constraint_price_versioned_child_structure import SeriesConstraintPriceVersionedChildStructure
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "seriesConstraintPrices_RelStructure"

    series_constraint_price_ref: List[SeriesConstraintPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraint_price: List[SeriesConstraintPriceVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintPrice",
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
