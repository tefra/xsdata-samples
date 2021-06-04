from dataclasses import dataclass
from netex.models.block_part_ref_structure import BlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlockPartRef(BlockPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
