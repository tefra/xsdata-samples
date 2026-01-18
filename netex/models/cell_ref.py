from __future__ import annotations

from dataclasses import dataclass

from .cell_ref_structure import CellRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CellRef(CellRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
