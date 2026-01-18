from __future__ import annotations

from dataclasses import dataclass

from .level_ref_structure import LevelRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LevelRef(LevelRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
