from __future__ import annotations

from dataclasses import dataclass

from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Section2(LinkSequenceVersionStructure):
    class Meta:
        name = "Section_"
        namespace = "http://www.netex.org.uk/netex"
