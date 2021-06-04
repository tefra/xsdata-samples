from dataclasses import dataclass
from netex.models.distance_matrix_element_version_structure import DistanceMatrixElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElement(DistanceMatrixElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
