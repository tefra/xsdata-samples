from __future__ import annotations

from dataclasses import dataclass

from .block_part_ref_structure import BlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlockPartRef(BlockPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
