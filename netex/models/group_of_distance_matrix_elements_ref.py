from dataclasses import dataclass
from netex.models.group_of_distance_matrix_elements_ref_structure_element import GroupOfDistanceMatrixElementsRefStructureElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfDistanceMatrixElementsRef(GroupOfDistanceMatrixElementsRefStructureElement):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
