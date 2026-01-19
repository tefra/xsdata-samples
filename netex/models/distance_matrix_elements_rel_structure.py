from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .distance_matrix_element import DistanceMatrixElement
from .distance_matrix_element_ref import DistanceMatrixElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "distanceMatrixElements_RelStructure"

    distance_matrix_element_ref_or_distance_matrix_element: Sequence[
        DistanceMatrixElementRef | DistanceMatrixElement
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
