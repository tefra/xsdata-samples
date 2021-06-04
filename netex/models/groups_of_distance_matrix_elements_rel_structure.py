from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.group_of_distance_matrix_elements import GroupOfDistanceMatrixElements
from netex.models.group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupsOfDistanceMatrixElementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfDistanceMatrixElements_RelStructure"

    group_of_distance_matrix_elements_ref: List[GroupOfDistanceMatrixElementsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distance_matrix_elements: List[GroupOfDistanceMatrixElements] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
