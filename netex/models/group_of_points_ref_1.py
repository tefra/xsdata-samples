from dataclasses import dataclass

from .group_of_points_ref_structure import GroupOfPointsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfPointsRef1(GroupOfPointsRefStructure):
    class Meta:
        name = "GroupOfPointsRef"
        namespace = "http://www.netex.org.uk/netex"
