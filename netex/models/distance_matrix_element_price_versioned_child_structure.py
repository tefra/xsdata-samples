from dataclasses import dataclass, field
from typing import Optional
from netex.models.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.models.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.models.group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "DistanceMatrixElementPrice_VersionedChildStructure"

    distance_matrix_element_ref: Optional[DistanceMatrixElementRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distance_matrix_elements_ref: Optional[GroupOfDistanceMatrixElementsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
