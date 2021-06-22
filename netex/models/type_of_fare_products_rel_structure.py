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

    type_of_fare_product_ref_or_type_of_fare_product: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFareProductRef",
                    "type": TypeOfFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProduct",
                    "type": TypeOfFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
