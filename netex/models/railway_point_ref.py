from dataclasses import dataclass
from netex.models.railway_point_ref_structure import RailwayPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RailwayPointRef(RailwayPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
