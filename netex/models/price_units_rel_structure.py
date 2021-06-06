from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .price_unit import PriceUnit
from .price_unit_ref import PriceUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceUnitsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "priceUnits_RelStructure"

    price_unit_ref: List[PriceUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_unit: List[PriceUnit] = field(
        default_factory=list,
        metadata={
            "name": "PriceUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
