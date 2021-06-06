from dataclasses import dataclass, field
from typing import List
from .distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from .distance_matrix_element_ref import DistanceMatrixElementRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "distanceMatrixElementRefs_RelStructure"

    distance_matrix_element_ref: List[DistanceMatrixElementRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_inverse_ref: List[DistanceMatrixElementInverseRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementInverseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
