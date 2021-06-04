from dataclasses import dataclass
from netex.models.group_of_points_ref_structure import GroupOfPointsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfPointsRef2(GroupOfPointsRefStructure):
    class Meta:
        name = "GroupOfPointsRef"
        namespace = "http://www.netex.org.uk/netex"
