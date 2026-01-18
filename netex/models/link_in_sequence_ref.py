from __future__ import annotations

from dataclasses import dataclass

from .link_in_sequence_ref_structure import LinkInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkInSequenceRef(LinkInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
