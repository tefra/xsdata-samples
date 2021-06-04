from dataclasses import dataclass
from netex.models.distance_matrix_element_price_ref_structure import DistanceMatrixElementPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementPriceRef(DistanceMatrixElementPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
