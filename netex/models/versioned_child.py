from dataclasses import dataclass
from .alternative_texts_rel_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionedChild(VersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
