from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_distance_matrix_elements import GroupOfDistanceMatrixElements
from .group_of_distance_matrix_elements_ref import (
    GroupOfDistanceMatrixElementsRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfDistanceMatrixElementsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "groupsOfDistanceMatrixElements_RelStructure"

    group_of_distance_matrix_elements_ref_or_group_of_distance_matrix_elements: Iterable[
        GroupOfDistanceMatrixElementsRef | GroupOfDistanceMatrixElements
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GroupOfDistanceMatrixElementsRef",
                    "type": GroupOfDistanceMatrixElementsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElements",
                    "type": GroupOfDistanceMatrixElements,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
