from dataclasses import dataclass
from .alternative_texts_rel_structure import EntityInVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntityInVersion(EntityInVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
