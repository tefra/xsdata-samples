from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .distance_matrix_element import DistanceMatrixElement
from .distance_matrix_element_ref import DistanceMatrixElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "distanceMatrixElements_RelStructure"

    distance_matrix_element_ref_or_distance_matrix_element: Iterable[
        Union[DistanceMatrixElementRef, DistanceMatrixElement]
    ] = field(
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
                    "name": "DistanceMatrixElement",
                    "type": DistanceMatrixElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
