from dataclasses import dataclass
from netex.models.road_point_ref_structure import RoadPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoadPointRef(RoadPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
