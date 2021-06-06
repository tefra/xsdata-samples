from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_fare_product import TypeOfFareProduct
from .type_of_fare_product_ref import TypeOfFareProductRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareProductsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typeOfFareProducts_RelStructure"

    type_of_fare_product_ref: List[TypeOfFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_product: List[TypeOfFareProduct] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
