from dataclasses import dataclass
from netex.models.point_projection_ref_structure import PointProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointProjectionRef(PointProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
