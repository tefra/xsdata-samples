from __future__ import annotations

from dataclasses import dataclass

from .block_part_ref_structure import BlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlockPartRefStructure(BlockPartRefStructure):
    pass
