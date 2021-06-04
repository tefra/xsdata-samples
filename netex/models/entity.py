from dataclasses import dataclass
from netex.models.entity_structure import EntityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Entity(EntityStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
