from dataclasses import dataclass
from .compound_block_structure import CompoundBlockStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompoundBlock(CompoundBlockStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
