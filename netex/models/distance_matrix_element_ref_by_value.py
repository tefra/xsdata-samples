from dataclasses import dataclass
from netex.models.distance_matrix_element_ref_by_value_structure import DistanceMatrixElementRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementRefByValue(DistanceMatrixElementRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
