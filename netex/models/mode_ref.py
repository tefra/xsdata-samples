from __future__ import annotations

from dataclasses import dataclass

from .mode_ref_structure import ModeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeRef(ModeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
