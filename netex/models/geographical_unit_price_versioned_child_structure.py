from dataclasses import dataclass, field
from typing import List, Optional
from .cell_ref_1 import CellRef1
from .cell_ref_2 import CellRef2
from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .geographical_unit_ref import GeographicalUnitRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalUnitPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "GeographicalUnitPrice_VersionedChildStructure"

    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional["GeographicalUnitPricesRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class GeographicalUnitPricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "geographicalUnitPrices_RelStructure"

    geographical_unit_price_ref: List[GeographicalUnitPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_price: List[GeographicalUnitPriceVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnitPrice",
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
