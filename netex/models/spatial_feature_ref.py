from dataclasses import dataclass
from netex.models.group_of_points_ref_structure import GroupOfPointsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SpatialFeatureRef(GroupOfPointsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
