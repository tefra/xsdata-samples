from __future__ import annotations

from dataclasses import dataclass

from .link_sequence_projection_ref_structure import (
    LinkSequenceProjectionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkSequenceProjectionRef(LinkSequenceProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
