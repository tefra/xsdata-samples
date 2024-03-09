from dataclasses import dataclass

from .group_of_entities_ref_structure_1 import GroupOfEntitiesRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfPointsRef2(GroupOfEntitiesRefStructure1):
    class Meta:
        name = "GroupOfPointsRef_"
        namespace = "http://www.netex.org.uk/netex"
