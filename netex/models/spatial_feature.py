from dataclasses import dataclass
from .group_of_points_version_structure import GroupOfPointsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SpatialFeature(GroupOfPointsVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
