from dataclasses import dataclass
from .alternative_texts_rel_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePrice2(VersionedChildStructure):
    class Meta:
        name = "FarePrice_"
        namespace = "http://www.netex.org.uk/netex"
