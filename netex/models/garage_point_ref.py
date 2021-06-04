from dataclasses import dataclass
from netex.models.garage_point_ref_structure import GaragePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GaragePointRef(GaragePointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
