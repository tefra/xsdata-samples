from dataclasses import dataclass
from .distance_matrix_element_ref_structure import DistanceMatrixElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementRef(DistanceMatrixElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
