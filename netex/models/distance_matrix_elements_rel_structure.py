from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.distance_matrix_element import DistanceMatrixElement
from netex.models.distance_matrix_element_ref import DistanceMatrixElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "distanceMatrixElements_RelStructure"

    distance_matrix_element_ref: List[DistanceMatrixElementRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element: List[DistanceMatrixElement] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
