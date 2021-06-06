from dataclasses import dataclass
from .point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrafficControlPointVersionStructure(PointVersionStructure):
    class Meta:
        name = "TrafficControlPoint_VersionStructure"
