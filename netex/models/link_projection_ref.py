from __future__ import annotations

from dataclasses import dataclass

from .link_projection_ref_structure import LinkProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkProjectionRef(LinkProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
