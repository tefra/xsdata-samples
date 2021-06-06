from dataclasses import dataclass
from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceGroup2(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "PriceGroup_"
        namespace = "http://www.netex.org.uk/netex"
