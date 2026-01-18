from __future__ import annotations

from dataclasses import dataclass

from .block_version_structure import BlockVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Block(BlockVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
