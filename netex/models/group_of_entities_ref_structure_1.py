from dataclasses import dataclass
from .group_of_entities_ref_structure_2 import GroupOfEntitiesRefStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfEntitiesRefStructure1(GroupOfEntitiesRefStructure2):
    class Meta:
        name = "GroupOfEntitiesRefStructure"
