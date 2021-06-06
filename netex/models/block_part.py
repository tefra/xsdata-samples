from dataclasses import dataclass
from .block_part_version_structure import BlockPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlockPart(BlockPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
