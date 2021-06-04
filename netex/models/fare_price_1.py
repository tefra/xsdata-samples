from dataclasses import dataclass
from netex.models.alternative_texts_rel_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePrice1(VersionedChildStructure):
    class Meta:
        name = "FarePrice_"
        namespace = "http://www.netex.org.uk/netex"
