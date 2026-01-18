from __future__ import annotations

from dataclasses import dataclass

from .wire_link_ref_structure import WireLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireLinkRef(WireLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
