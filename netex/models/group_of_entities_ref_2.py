from dataclasses import dataclass
from netex.models.group_of_entities_ref_structure_2 import GroupOfEntitiesRefStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfEntitiesRef2(GroupOfEntitiesRefStructure2):
    class Meta:
        name = "GroupOfEntitiesRef"
        namespace = "http://www.netex.org.uk/netex"
