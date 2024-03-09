from dataclasses import dataclass

from .point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Point2(PointVersionStructure):
    class Meta:
        name = "Point"
        namespace = "http://www.netex.org.uk/netex"
