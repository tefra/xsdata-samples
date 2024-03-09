from dataclasses import dataclass

from .point_projection_version_structure import PointProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointProjection(PointProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
