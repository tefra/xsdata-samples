from __future__ import annotations

from dataclasses import dataclass

from .block_ref_structure import BlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlockRefStructure(BlockRefStructure):
    pass
