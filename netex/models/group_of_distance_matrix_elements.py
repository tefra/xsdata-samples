from dataclasses import dataclass
from netex.models.group_of_distance_matrix_elements_version_structure import GroupOfDistanceMatrixElementsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfDistanceMatrixElements(GroupOfDistanceMatrixElementsVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
