from dataclasses import dataclass
from netex.models.group_of_entities_ref_structure_1 import GroupOfEntitiesRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfEntitiesRef1(GroupOfEntitiesRefStructure1):
    class Meta:
        name = "GroupOfEntitiesRef"
        namespace = "http://www.netex.org.uk/netex"
