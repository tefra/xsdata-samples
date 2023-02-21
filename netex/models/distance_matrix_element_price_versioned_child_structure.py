from dataclasses import dataclass, field
from typing import List
from .distance_matrix_element_ref import DistanceMatrixElementRef
from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from .group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "DistanceMatrixElementPrice_VersionedChildStructure"

    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElementsRef",
                    "type": GroupOfDistanceMatrixElementsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
