from __future__ import annotations

from dataclasses import dataclass

from .link_sequence_ref_structure import LinkSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPatternRefStructure(LinkSequenceRefStructure):
    pass
