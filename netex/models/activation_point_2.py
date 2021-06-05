from dataclasses import dataclass
from netex.models.point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationPoint2(PointVersionStructure):
    class Meta:
        name = "ActivationPoint_"
        namespace = "http://www.netex.org.uk/netex"
