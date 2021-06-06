from dataclasses import dataclass
from .alternative_texts_rel_structure import TimebandVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Timeband(TimebandVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
